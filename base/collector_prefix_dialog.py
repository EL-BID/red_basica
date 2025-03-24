import os
from PyQt5.QtWidgets import QDialog, QMessageBox, QProgressBar
from PyQt5 import uic
from qgis.core import QgsSpatialIndex, QgsField, QgsMapLayerProxyModel, Qgis
from PyQt5.QtCore import QTimer, QVariant, Qt, QCoreApplication
from qgis.utils import iface

translate = QCoreApplication.translate

class CollectorPrefixDialog(QDialog):
    def __init__(self):
        super().__init__()
        uiFile = os.path.join(os.path.dirname(__file__), 'resources', 'collector_prefix_dialog.ui')
        uic.loadUi(uiFile, self)
        self.layer_combo.setFilters(QgsMapLayerProxyModel.LineLayer)

        self.increment_type_combo.addItem(translate("CollectorPrefixDialog", "Alphabetic"), 'A')
        self.increment_type_combo.addItem(translate("CollectorPrefixDialog", "Numeric"), 'N')

        self.buttons.button(self.buttons.Ok).clicked.connect(self.main)
        self.buttons.button(self.buttons.Cancel).clicked.connect(self.reject)

        # Data structures initialization
        self.segment_name_attr = "ID_TRM_(N)"
        self.selected_layer = None
        self.segment_dict = {}
        self.spatial_index = None
        self.named_segments = set()

        self.message_bar = iface.messageBar()
        self.progress_message = QProgressBar()
        self.progress_message.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.message_bar.pushWidget(self.progress_message, Qgis.Info)

    def get_collector_prefix_and_increment_type_and_layer_and_selection(self):
        """
        Retrieves the user-defined prefix, increment type, selected layer, and selection mode.
        """
        self.selected_layer = self.layer_combo.currentLayer()
        return (
            self.prefix_edit.text(),
            self.increment_type_combo.currentData() == 'A',
            self.only_selected_check.isChecked()
        )

    def find_connected_segments(self, segment, upstream=True):
        """
        Finds segments that are connected to the given segment at one of its endpoints.
        Returns:
            list: A list of QgsFeature objects representing the connected segments.
        """
        connected_segments = []
        geom = segment.geometry()
        polyline = geom.asMultiPolyline()[0] if geom.isMultipart() else geom.asPolyline()
        point_to_match = polyline[0] if upstream else polyline[-1]

        candidate_ids = self.spatial_index.nearestNeighbor(point_to_match, 2)
        candidate_ids.remove(segment.id())
        
        for candidate_id in candidate_ids:
            candidate_segment = self.segment_dict[candidate_id]
            candidate_geom = candidate_segment.geometry()
            candidate_polyline = candidate_geom.asMultiPolyline()[0] if candidate_geom.isMultipart() else candidate_geom.asPolyline()
        
            if (upstream and candidate_polyline[-1] == point_to_match) or (not upstream and candidate_polyline[0] == point_to_match):
                connected_segments.append(candidate_segment)

        return connected_segments

    def get_initial_segments(self):
        """
        Identifies the initial segments in the network, i.e., segments that have no upstream connections.

        Returns:
            list: A list of QgsFeature objects representing the initial segments.
        """
        initial_segments = []

        for segment in self.segment_dict.values():
            connected_upstream_segments = self.find_connected_segments(segment, upstream=True)
            if not connected_upstream_segments:
                initial_segments.append(segment)
        return initial_segments

    def get_final_segment(self):
        """
        Identifies the final segment in the network, i.e., the segment that has no downstream connections.
        """
        for segment in self.segment_dict.values():
            connected_downstream_segments = self.find_connected_segments(segment, upstream=False)

            if not connected_downstream_segments:
                return segment  

        return None

    def name_segments(self, segment, collector_name, segment_number):
        """
        Recursively names the segments starting from the given segment. Each segment is named with
        the collector's name followed by a segment number. The naming process continues downstream.
        """
        if segment.id() in self.named_segments:
            return

        segment_name = f"{collector_name}-{segment_number:03d}"
        self.selected_layer.changeAttributeValue(segment.id(), self.selected_layer.fields().lookupField(self.segment_name_attr), segment_name)
        self.selected_layer.changeAttributeValue(segment.id(), self.selected_layer.fields().lookupField("ID_COL"), collector_name)

        self.named_segments.add(segment.id())

        connected_downstream_segments = self.find_connected_segments(segment, upstream=False)

        if not connected_downstream_segments:
            return

        for connected_segment in connected_downstream_segments:
            self.name_segments(connected_segment, collector_name, segment_number + 1)

    def increment_collector_name(self, collector_prefix, current_name, is_alphabetic):
        """
        Function to increment the collector name alphabetically
        """
        if is_alphabetic:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            base_name = current_name.split('_')[-1]
            new_name = ""

            carry = True
            for char in reversed(base_name):
                if carry:
                    index = (alphabet.index(char) + 1) % len(alphabet)
                    carry = index == 0
                    new_name = alphabet[index] + new_name
                else:
                    new_name = char + new_name

            if carry:
                new_name = "A" + new_name

        else:
            try:
                current_number = int(current_name.split('_')[-1])
            except ValueError:
                current_number = 0

            new_name = f"{current_number + 1:03d}"

        return f"{collector_prefix}_{new_name}"


    # Function to name all collectors
    def name_all_collectors(self, initial_segments, collector_prefix, is_alphabetic, progress_bar):
        collector_name = f"{collector_prefix}_A" if is_alphabetic else f"{collector_prefix}_001"

        for i, initial_segment in enumerate(initial_segments):
            self.name_segments(initial_segment, collector_name, 1)
            collector_name = self.increment_collector_name(collector_prefix, collector_name, is_alphabetic)
            progress_bar.setValue(int((i + 1) / len(initial_segments) * 100))
    
    def build_segment_dict_and_spatial_index(self, selected_layer, only_selected):
        """Helper function to build the segment dictionary and spatial index."""
        self.segment_dict = {f.id(): f for f in (selected_layer.selectedFeatures() if only_selected else selected_layer.getFeatures())}
        spatial_index = QgsSpatialIndex()
        for feat in self.segment_dict.values():
            spatial_index.addFeature(feat)
        return self.segment_dict, spatial_index
    
    def create_field_if_not_exists(self, field_name):
        """Helper function to add a field if it doesn't exist."""
        if self.selected_layer.fields().indexFromName(field_name) == -1:
            self.selected_layer.dataProvider().addAttributes([QgsField(field_name, QVariant.String)])
            self.selected_layer.updateFields()

    def main(self):
        collector_prefix, is_alphabetic, only_selected = self.get_collector_prefix_and_increment_type_and_layer_and_selection()

        segments_already_named = any(
            feature[self.segment_name_attr] for feature in (self.selected_layer.selectedFeatures() if only_selected else self.selected_layer.getFeatures())
        )
        if segments_already_named:
            reply = QMessageBox.question(None, translate("CollectorPrefixDialog", "Segments already named"),
                                        translate("CollectorPrefixDialog", "There are segments that are already named. Would you like to rename them?"),
                                        QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                raise Exception(translate("CollectorPrefixDialog", "User canceled the operation."))
            else:
                # Clear values for the 'ID_TRM_(N)' and 'ID_COL' fields
                for feature in (self.selected_layer.selectedFeatures() if only_selected else self.selected_layer.getFeatures()):
                    self.selected_layer.changeAttributeValue(feature.id(), self.selected_layer.fields().lookupField(self.segment_name_attr), None)
                    self.selected_layer.changeAttributeValue(feature.id(), self.selected_layer.fields().lookupField("ID_COL"), None)

        self.create_field_if_not_exists(self.segment_name_attr)
        self.create_field_if_not_exists("ID_COL")

        self.selected_layer.startEditing()

        self.segment_dict, self.spatial_index = self.build_segment_dict_and_spatial_index(self.selected_layer, only_selected)

        initial_segments = self.get_initial_segments()
        final_segment = self.get_final_segment()

        if not final_segment:
            QMessageBox.critical(self, "Error", translate("CollectorPrefixDialog", "The sewer network does not have a final segment (outlet/root)."))
            return

        self.named_segments = set()

        self.name_all_collectors(initial_segments, collector_prefix, is_alphabetic, self.progress_message)
        self.selected_layer.commitChanges()

        def remove_progress_bar():
            self.message_bar.clearWidgets()
            self.close()

        QTimer.singleShot(2500, remove_progress_bar)
