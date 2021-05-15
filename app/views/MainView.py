from PyQt5.QtWidgets import (
    QMainWindow,
    QDialog,
    QAbstractItemView,
    QMessageBox,
    QFileDialog,
)
from PyQt5.QtCore import QThread, Qt, QModelIndex, QCoreApplication
from PyQt5 import uic, QtGui, QtWidgets
from qgis.utils import iface, Qgis, QgsMessageLog
from .ui.MainWindowUi import Ui_MainWindow
from ..controllers.CalculationController import CalculationController
from ..controllers.DataController import DataController
from ..controllers.ApiController import ApiController
from ..controllers.XlsController import XlsController
from ..controllers.SwmmController import SwmmController
from ..models.Calculation import Calculation
from ..models.Contribution import Contribution
from ..models.WaterLevelAdj import WaterLevelAdj
from ..models.delegates.CalculationDelegate import (
    CalculationDelegate,
    NumberFormatDelegate,
)
from ..lib.ProgressThread import ProgressThread
from ...helper_functions import HelperFunctions
import json

translate = QCoreApplication.translate


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, dialogs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.selected = {}
        self.h = HelperFunctions(iface)

        # Main window
        self._dialogs = dialogs
        self.currentProjectId = self._dialogs["newProject"].model.getActiveId()
        self.calculationController = CalculationController()

        # Hide progress bar
        self.progressBar.hide()
        self.progressMsg.hide()
        self.messageLabel.hide()

        # Models
        self.calcModel = Calculation()
        self.contribModel = Contribution()
        self.wlaModel = WaterLevelAdj()

        # Red Basica Table
        self.calcTable.setModel(self.calcModel)
        self.calcTable.setItemDelegate(CalculationDelegate(self.calcTable))
        self.calcTable.setItemDelegateForColumn(
            self.calcModel.fieldIndex("slopes_min_accepted_col"), NumberFormatDelegate()
        )
        self.calcTable.model().dataChanged.connect(self.onDataChanged)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("project_id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("layer_name"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("created_at"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("updated_at"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("x_initial"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("y_initial"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("x_final"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("y_final"), True)
        self.calcTable.setColumnHidden(
            self.calcModel.fieldIndex("slopes_min_modified"), True
        )

        # Set header data
        schd = self.calcModel.setHeaderData
        cidx = self.calcModel.fieldIndex
        qth = Qt.Horizontal
        schd(cidx("id"), qth, translate("CalcTbl", "id"))
        schd(cidx("project_id"), qth, translate("CalcTbl", "project_id"))
        schd(cidx("layer_name"), qth, translate("CalcTbl", "layer_name"))
        schd(cidx("initial_segment"), qth, translate("CalcTbl", "initial_segment"))
        schd(cidx("final_segment"), qth, translate("CalcTbl", "final_segment"))
        schd(cidx("collector_number"), qth, translate("CalcTbl", "collector_number"))
        schd(cidx("col_seg"), qth, translate("CalcTbl", "col_seg"))
        schd(cidx("extension"), qth, translate("CalcTbl", "extension"))
        schd(
            cidx("previous_col_seg_id"),
            qth,
            translate("CalcTbl", "previous_col_seg_id"),
        )
        schd(cidx("m1_col_id"), qth, translate("CalcTbl", "m1_col_id"))
        schd(cidx("m2_col_id"), qth, translate("CalcTbl", "m2_col_id"))
        schd(cidx("block_others_id"), qth, translate("CalcTbl", "block_others_id"))
        schd(cidx("qty_final_qe"), qth, translate("CalcTbl", "qty_final_qe"))
        schd(cidx("qty_initial_qe"), qth, translate("CalcTbl", "qty_initial_qe"))
        schd(cidx("intake_in_seg"), qth, translate("CalcTbl", "intake_in_seg"))
        schd(
            cidx("total_flow_rate_end"),
            qth,
            translate("CalcTbl", "total_flow_rate_end"),
        )
        schd(
            cidx("total_flow_rate_start"),
            qth,
            translate("CalcTbl", "total_flow_rate_start"),
        )
        schd(cidx("col_pipe_position"), qth, translate("CalcTbl", "col_pipe_position"))
        schd(cidx("aux_prof_i"), qth, translate("CalcTbl", "aux_prof_i"))
        schd(cidx("force_depth_up"), qth, translate("CalcTbl", "force_depth_up"))
        schd(
            cidx("aux_depth_adjustment"),
            qth,
            translate("CalcTbl", "aux_depth_adjustment"),
        )
        schd(cidx("covering_up"), qth, translate("CalcTbl", "covering_up"))
        schd(cidx("covering_down"), qth, translate("CalcTbl", "covering_down"))
        schd(cidx("depth_up"), qth, translate("CalcTbl", "depth_up"))
        schd(cidx("depth_down"), qth, translate("CalcTbl", "depth_down"))
        schd(cidx("force_depth_down"), qth, translate("CalcTbl", "force_depth_down"))
        schd(cidx("el_terr_up"), qth, translate("CalcTbl", "el_terr_up"))
        schd(cidx("el_terr_down"), qth, translate("CalcTbl", "el_terr_down"))
        schd(cidx("el_col_up"), qth, translate("CalcTbl", "el_col_up"))
        schd(cidx("el_col_down"), qth, translate("CalcTbl", "el_col_down"))
        schd(cidx("el_top_gen_up"), qth, translate("CalcTbl", "el_top_gen_up"))
        schd(cidx("el_top_gen_down"), qth, translate("CalcTbl", "el_top_gen_down"))
        schd(cidx("slopes_terr"), qth, translate("CalcTbl", "slopes_terr"))
        schd(
            cidx("slopes_min_accepted_col"),
            qth,
            translate("CalcTbl", "slopes_min_accepted_col"),
        )
        schd(
            cidx("slopes_adopted_col"), qth, translate("CalcTbl", "slopes_adopted_col")
        )
        schd(
            cidx("suggested_diameter"), qth, translate("CalcTbl", "suggested_diameter")
        )
        schd(cidx("adopted_diameter"), qth, translate("CalcTbl", "adopted_diameter"))
        schd(cidx("c_manning"), qth, translate("CalcTbl", "c_manning"))
        schd(
            cidx("prj_flow_rate_qgmax"),
            qth,
            translate("CalcTbl", "prj_flow_rate_qgmax"),
        )
        schd(cidx("water_level_y"), qth, translate("CalcTbl", "water_level_y"))
        schd(
            cidx("water_level_pipe_end"),
            qth,
            translate("CalcTbl", "water_level_pipe_end"),
        )
        schd(cidx("tractive_force"), qth, translate("CalcTbl", "tractive_force"))
        schd(cidx("critical_velocity"), qth, translate("CalcTbl", "critical_velocity"))
        schd(cidx("velocity"), qth, translate("CalcTbl", "velocity"))
        schd(
            cidx("initial_flow_rate_qi"),
            qth,
            translate("CalcTbl", "initial_flow_rate_qi"),
        )
        schd(
            cidx("water_level_y_start"),
            qth,
            translate("CalcTbl", "water_level_y_start"),
        )
        schd(
            cidx("water_level_pipe_start"),
            qth,
            translate("CalcTbl", "water_level_pipe_start"),
        )
        schd(
            cidx("tractive_force_start"),
            qth,
            translate("CalcTbl", "tractive_force_start"),
        )
        schd(cidx("inspection_id_up"), qth, translate("CalcTbl", "inspection_id_up"))
        schd(
            cidx("inspection_type_up"), qth, translate("CalcTbl", "inspection_type_up")
        )
        schd(
            cidx("inspection_id_down"), qth, translate("CalcTbl", "inspection_id_down")
        )
        schd(
            cidx("inspection_type_down"),
            qth,
            translate("CalcTbl", "inspection_type_down"),
        )
        schd(cidx("downstream_seg_id"), qth, translate("CalcTbl", "downstream_seg_id"))
        schd(cidx("observations"), qth, translate("CalcTbl", "observations"))

        # set filters
        self.set_table_filters()

        # layer features selection
        self.calcTable.verticalHeader().sectionClicked.connect(self.onRowSelected)

        # Contributions Table
        self.contribTable.setModel(self.contribModel)
        self.contribTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("id"), True)
        self.contribTable.setColumnHidden(
            self.contribModel.fieldIndex("calculation_id"), True
        )
        self.contribTable.setColumnHidden(
            self.contribModel.fieldIndex("created_at"), True
        )
        self.contribTable.setColumnHidden(
            self.contribModel.fieldIndex("updated_at"), True
        )
        self.contribTable.setColumnHidden(
            self.contribModel.fieldIndex("initial_segment"), True
        )
        self.contribTable.horizontalHeader().setSectionResizeMode(True)

        sconhd = self.contribModel.setHeaderData
        conidx = self.contribModel.fieldIndex

        sconhd(conidx("col_seg"), qth, translate("ContTbl", "col_seg"))
        sconhd(
            conidx("previous_col_seg_end"),
            qth,
            translate("ContTbl", "previous_col_seg_end"),
        )
        sconhd(conidx("col_pipe_m1_end"), qth, translate("ContTbl", "col_pipe_m1_end"))
        sconhd(conidx("col_pipe_m2_end"), qth, translate("ContTbl", "col_pipe_m2_end"))
        sconhd(
            conidx("subtotal_up_seg_end"),
            qth,
            translate("ContTbl", "subtotal_up_seg_end"),
        )
        sconhd(
            conidx("condominial_lines_end"),
            qth,
            translate("ContTbl", "condominial_lines_end"),
        )
        sconhd(
            conidx("linear_contr_seg_end"),
            qth,
            translate("ContTbl", "linear_contr_seg_end"),
        )
        sconhd(
            conidx("previous_col_seg_start"),
            qth,
            translate("ContTbl", "previous_col_seg_start"),
        )
        sconhd(
            conidx("col_pipe_m1_start"), qth, translate("ContTbl", "col_pipe_m1_start")
        )
        sconhd(
            conidx("col_pipe_m2_start"), qth, translate("ContTbl", "col_pipe_m2_start")
        )
        sconhd(
            conidx("subtotal_up_seg_start"),
            qth,
            translate("ContTbl", "subtotal_up_seg_start"),
        )
        sconhd(
            conidx("condominial_lines_start"),
            qth,
            translate("ContTbl", "condominial_lines_start"),
        )
        sconhd(
            conidx("linear_contr_seg_start"),
            qth,
            translate("ContTbl", "linear_contr_seg_start"),
        )

        # WaterLevelAdj Table
        self.wlaTable.setModel(self.wlaModel)
        self.wlaTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("calculation_id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("created_at"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("updated_at"), True)

        # menu actions
        self.actionProject.triggered.connect(self.checkProjectAction)
        self.actionParameters.triggered.connect(self.openParametersDialog)
        self.actionCalculara_DN.triggered.connect(self.calculateDN)
        self.actionCalcular_DN_Creciente.triggered.connect(self.calculateGrowingDN)
        self.actionMin_Excav.triggered.connect(self.calculateMinExc)
        self.actionMin_Desnivel.triggered.connect(self.calculateMinSlope)
        self.actionAjuste_NA.triggered.connect(self.setIterations)
        self.actionImportData.triggered.connect(self.startImport)
        self.actionExportToXls.triggered.connect(self.downloadXls)
        self.actionResetear_Ajuste_NA.triggered.connect(self.resetWaterLevelAdj)
        self.actionReiniciar_DN.triggered.connect(self.clearDiameters)
        self.actionCreateResultsLayer.triggered.connect(self.showCreateLayerDialog)
        self.actionCreateQiSwmmFile.triggered.connect(lambda: self.writeInpFile("q_i"))
        self.actionCreateQfSwmmFile.triggered.connect(lambda: self.writeInpFile("q_f"))
        self.actionPublishProject.triggered.connect(self.showLogin)

        # triggered actions
        self._dialogs["newProject"].buttonBox.accepted.connect(self.saveNewProject)
        self._dialogs["project"].newProjectButton.clicked.connect(
            self.openNewProjectDialog
        )
        self._dialogs["project"].dialogButtonBox.accepted.connect(self.updateProject)
        self._dialogs["project"].deleteProjectButton.clicked.connect(self.refreshTables)
        self._dialogs["project"].dialogButtonBox.rejected.connect(self.updateMainWindow)
        self._dialogs["parameters"].buttonBox.accepted.connect(self.saveParameters)
        self._dialogs["editValues"].accepted.connect(
            lambda: self.editAction(self._dialogs["editValues"].editValueEdit.value())
        )
        self._dialogs["iterations"].accepted.connect(
            lambda: self.adjustNA(self._dialogs["iterations"].iterationsEdit.value())
        )
        self._dialogs["login"].accepted.connect(
            lambda: self.publish(
                self._dialogs["login"].userText.text(),
                self._dialogs["login"].passText.text(),
            )
        )
        self._dialogs["export"].accepted.connect(self.createResultLayer)

    def updateMainWindow(self):
        """updates main window content"""
        self.changeMainTitle()
        self.currentProjectId = self._dialogs["project"].model.getActiveId()
        self.set_table_filters()

    def set_table_filters(self):
        """applies filters to calculations, contributions and wla_adjustments tables"""
        if self.currentProjectId:
            self.calcModel.setFilter("project_id = {}".format(self.currentProjectId))
            self.contribModel.setFilter(
                "calculation_id in (select id from calculations where project_id = {})".format(
                    self.currentProjectId
                )
            )
            self.wlaModel.setFilter(
                "calculation_id in (select id from calculations where project_id = {})".format(
                    self.currentProjectId
                )
            )
        self.refreshTables()

    def newProject(self):
        self.closeProjectDialog()
        self.openNewProjectDialog()

    def saveNewProject(self):
        self.updateMainWindow()
        self.closeProjectDialog()
        self.openParametersDialog()

    def updateProject(self):
        self._dialogs["project"].saveRecord()
        self.updateMainWindow()

    def checkProjectAction(self):
        if self._dialogs["project"].model.getActiveProject():
            self.openProjectDialog()
        else:
            self.openNewProjectDialog()

    def openProjectDialog(self):
        self._dialogs["project"].show()

    def closeProjectDialog(self):
        self._dialogs["project"].hide()

    def openNewProjectDialog(self):
        self.closeProjectDialog()
        self._dialogs["newProject"].addRecord()
        self._dialogs["newProject"].show()

    def changeMainTitle(self):
        name = self._dialogs["newProject"].model.getNameActiveProject()
        title = "SANIBIDapp [{}]".format(name) if name is not None else "SANIBIDapp"
        self.setWindowTitle(title)

    def closeNewProjectDialog(self):
        self._dialogs["newProject"].hide()

    def openParametersDialog(self):
        self._dialogs["parameters"].show()

    def closeParametersDialog(self):
        self._dialogs["parameters"].hide()

    def saveParameters(self):
        """action triggered when saving parameters dialog"""
        valid = self._dialogs["parameters"].saveParameters()
        if valid:
            self.closeParametersDialog()
            self.startImport(validate=True)

    def onDataChanged(self, index, index2, roles):
        # this is fired twice and index is the row after database change
        # TODO: find a better way to do this
        val = index.data()
        colName = self.calcModel.record(index.row()).fieldName(index.column())
        if colName == "slopes_min_accepted_col":
            id = self.calcModel.record(index.row()).value("id")
            self.calcModel.updateColById(1, "slopes_min_modified", id)
        if type(val) in [int]:
            row = index.row()
            record = self.calcModel.record(row)
            colSeg = record.value("col_seg")
            controller = CalculationController()
            ProgressThread(
                self,
                controller,
                (lambda: controller.updateVal(self.currentProjectId, colSeg)),
            )

    def onRowSelected(self, logicalIndex):
        selectedRows = self.calcTable.selectionModel().selectedRows()
        colsegs = []
        for index in selectedRows:
            row = index.row()
            rec = self.calcModel.record(row)
            colseg = rec.value("col_seg")
            colsegs.append(colseg)
        self.h.selectByColSeg(colsegs)

    def refreshTables(self):
        """Refresh table views, its called from ProgressThread instances"""
        self.calcModel.select()  # TODO order by col_seg
        self.contribModel.select()
        self.wlaModel.select()

    def startImport(self, validate=False):
        checked = validate and self._dialogs["parameters"].is_valid_form()
        if not validate or checked:
            has_records = self.calcModel.rowCount() > 0
            if has_records > 0:
                if (
                    QMessageBox.question(
                        self,
                        "Import Data",
                        translate("CalcTbl", "This action will replace loaded and calculated data, do you want to continue?"),
                        QMessageBox.Yes | QMessageBox.No,
                    )
                    == QMessageBox.No
                ):
                    self.progressBar.hide()
                    self.progressMsg.setText("Data import aborted by user")
                    return
            self.closeParametersDialog()
            checksCtrl = DataController()
            ProgressThread(
                self, checksCtrl, checksCtrl.runVerifications, callback=self.uploadData
            )

    def uploadData(self, verifications):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController(projectId)

        if verifications["success"]:
            ProgressThread(self, controller, controller.importData)
        else:
            if verifications["fix"]:
                if (
                    QMessageBox.question(
                        self,
                        "Fix Segments",
                        "some segments dont have previous segment and are neither beginning nor ending , do you want automatic correction?",
                        QMessageBox.Yes | QMessageBox.No,
                    )
                    == QMessageBox.No
                ):
                    self.progressBar.hide()
                    self.progressMsg.setText(
                        "Process aborted by user, fix errors and try again later"
                    )
                    return
                ProgressThread(self, controller, controller.importData)
            else:
                self.progressBar.hide()
                self.progressMsg.setText(verifications["info"])
                self.iface.messageBar().pushMessage(
                    verifications["info"], level=Qgis.Critical, duration=3
                )

    def calculateDN(self):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController()
        ProgressThread(self, controller, (lambda: controller.calculateDN(projectId)))

    def calculateGrowingDN(self):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController()
        ProgressThread(
            self, controller, (lambda: controller.calculateGrowDN(projectId))
        )

    def calculateMinExc(self):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController()
        ProgressThread(
            self, controller, (lambda: controller.calculateMinExc(projectId))
        )

    def calculateMinSlope(self):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController()
        ProgressThread(
            self, controller, (lambda: controller.calculateMinSlope(projectId))
        )

    def setIterations(self):
        iterationsDialog = self._dialogs["iterations"]
        iterationsDialog.show()
        iterationsDialog.iterationsEdit.setValue(12)

    def adjustNA(self, iteration):
        projectId = self._dialogs["newProject"].model.getActiveId()
        controller = CalculationController()
        ProgressThread(
            self, controller, (lambda: controller.adjustNA(projectId, iteration))
        )

    def contextMenuEvent(self, pos):
        if self.calcTable.selectionModel().selection().indexes():
            selected = {}
            for i in self.calcTable.selectionModel().selection().indexes():
                if i.column() not in selected:
                    selected[i.column()] = []
                selected[i.column()].append(i.row())
            self.menu = QtWidgets.QMenu()
            self.selected = selected
            editValuesAction = QtWidgets.QAction("Edit Values", self)
            editValuesAction.triggered.connect(
                lambda: self.editValuesAction(self.selected)
            )
            deleteAction = QtWidgets.QAction("Delete Value", self)
            deleteAction.triggered.connect(lambda: self.deleteAction(self.selected))
            self.menu.addAction(editValuesAction)
            self.menu.addAction(deleteAction)
            self.menu.popup(QtGui.QCursor.pos())

    def editValuesAction(self, selected):
        editDialog = self._dialogs["editValues"]
        editDialog.show()
        editDialog.editValueEdit.setValue(0)

    def editAction(self, value):
        selected = self.selected
        column = next(iter(selected))
        calcModel = self.calcModel
        colSegs = []
        oldColNumber = None
        for item in selected.values():
            for row in item:
                index = calcModel.index(row, column)
                colName = calcModel.record(row).fieldName(column)
                id = calcModel.record(row).value("id")
                collectorNumber = calcModel.record(row).value("collector_number")
                if collectorNumber != oldColNumber:
                    colSegs.append(calcModel.record(row).value("col_seg"))
                calcModel.updateColById(value, colName, id)
                if colName == "slopes_min_accepted_col":
                    calcModel.updateColById(1, "slopes_min_modified", id)
                oldColNumber = collectorNumber
        self.calcModel.select()
        controller = CalculationController()
        ProgressThread(
            self,
            controller,
            (lambda: controller.updateValues(self.currentProjectId, colSegs)),
        )

    def deleteAction(self, selected):
        column = next(iter(selected))
        calcModel = self.calcModel
        colSegs = []
        oldColNumber = None
        for item in selected.values():
            for row in item:
                index = calcModel.index(row, column)
                colName = calcModel.record(row).fieldName(column)
                id = calcModel.record(row).value("id")
                collectorNumber = calcModel.record(row).value("collector_number")
                if collectorNumber != oldColNumber:
                    colSegs.append(calcModel.record(row).value("col_seg"))
                calcModel.updateColById(None, colName, id)
                if colName == "slopes_min_accepted_col":
                    calcModel.updateColById(None, "slopes_min_modified", id)
                oldColNumber = collectorNumber
        self.calcModel.select()
        controller = CalculationController()
        ProgressThread(
            self,
            controller,
            (lambda: controller.updateValues(self.currentProjectId, colSegs)),
        )

    def downloadXls(self):
        controller = XlsController()
        output = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "{}.xls".format(self.windowTitle()),
            "Excel 97-2003 (*.xls)",
        )
        if output:
            controller.createFile(output[0])

    def resetWaterLevelAdj(self):
        controller = CalculationController()
        ProgressThread(
            self,
            controller,
            (lambda: controller.resetWaterLevel(self.currentProjectId)),
        )

    def clearDiameters(self):
        controller = CalculationController()
        ProgressThread(
            self, controller, (lambda: controller.clearDiameters(self.currentProjectId))
        )

    def createResultLayer(self):
        """Merge data from calculations to layer"""
        seg_layer = self.h.GetLayer()
        node_layer = self.h.GetNodeLayer()

        override = self._dialogs["export"].overrideRadioButton.isChecked()
        if seg_layer and node_layer:
            data = CalculationController().exportData(self.currentProjectId)
            if data:
                controller = DataController()
                nodes_layername = self._dialogs["export"].nodesEdit.text()
                segments_layername = self._dialogs["export"].segmentsEdit.text()
                ProgressThread(
                    self,
                    controller,
                    (
                        lambda: controller.writeToLayers(
                            data,
                            override=override,
                            nodes_layername=nodes_layername,
                            segments_layername=segments_layername,
                        )
                    ),
                )
            else:
                self.iface.messageBar().pushMessage(
                    "No data to import", level=Qgis.Info, duration=3
                )
        else:
            self.iface.messageBar().pushMessage(
                "Node layer not found", level=Qgis.Critical, duration=3
            )

    def writeInpFile(self, flowType):
        """Write INP file"""

        if flowType in ["q_i", "q_f"]:
            project = self._dialogs["newProject"].model.getNameActiveProject()
            f, __ = QFileDialog.getSaveFileName(
                self,
                "INP file",
                "{}_{}_{}.inp".format(
                    "sanibid", project, "QI" if flowType == "q_i" else "QF"
                ),
                "EPANET INP file (*.inp)",
            )

            if 0 < len(f):
                writer = SwmmController(self.iface, self.currentProjectId, flowType)
                try:
                    writer.writeInp(f)
                except Exception as e:
                    print("Saving INP file failed: " + str(e))
                    return False
                return True
            return False
        else:
            self.iface.messageBar().pushMessage(
                "Export Error: Invalid flowType value {}".format(flowType),
                level=Qgis.Critical,
                duration=3,
            )
        return False

    def showLogin(self):
        loginDialog = self._dialogs["login"]
        loginDialog.show()
        loginDialog.passText.setText("")

    def publish(self, user, password):
        if user != "" and password != "":
            projectId = self._dialogs["newProject"].model.getActiveId()
            controller = ApiController()
            ProgressThread(
                self,
                controller,
                (lambda: controller.publishProject(projectId, user, password)),
            )
        else:
            self.showLogin()

    def showCreateLayerDialog(self):
        dg = self._dialogs["export"]
        seg_layer = self.h.GetLayer()
        node_layer = self.h.GetNodeLayer()

        dg.nodesEdit.setText("{}_copy".format(node_layer.name()))
        dg.segmentsEdit.setText("{}_copy".format(seg_layer.name()))
        dg.show()
