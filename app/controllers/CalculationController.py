from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from ..models.Calculation import CalculationModel
from .DataController import DataController
import time

class CalculationController(QObject):
    def __init__(self):
        super().__init__()
        self.model = CalculationModel()
    
    def importData(self, projectId):
        #TODO each time the parameter is changed, we have to import again? 
        if not self.checkFirstImport(projectId):
            self.uploadCalculation()
            # call to Calculation Controller to set the firsts values
        else:
            print('Its imported')

    def checkFirstImport(self, projectId):
        print('Checking if is imported')
        imported = 0
        #TODO bind value is not working
        query = QSqlQuery("SELECT count(*)>0 FROM calculations WHERE project_id = "+str(projectId))
        while query.next():
            imported = query.value(0)
        return bool(imported)
    
    def uploadCalculation(self):
        print('uploading..')
        start_time = time.time()
        #TODO put the progress dialog into the Data Controller
        data = DataController().getJsonData()
        for row in data:
            self.model.select()
            rec = self.model.record()
            rec.setValue('project_id',1)
            rec.setValue('initial_segment',row['AUX_TRM_I'])
            rec.setValue('initial segment',row['AUX_TRM_I'])
            rec.setValue('final_segment',row['AUX_TRM_F'])
            rec.setValue('collector_number',row['ID_COL'])
            rec.setValue('col_seg',row['ID_TRM_(N)'])
            rec.setValue('extension',row['L'])
            rec.setValue('previous_col_seg_id',row['TRM_(N-1)_A'])
            rec.setValue('m1_col_id',row['TRM_(N-1)_B'])
            rec.setValue('m2_col_id',row['TRM_(N-1)_C'])
            if not row['ID_UC'] == 'NULL':
                rec.setValue('block_others_id',row['ID_UC'])
            rec.setValue('qty_final_qe',row['QE_FP']) if 'QE_FP' in row else rec.setValue('qty_final_qe',row['QEF'])
            rec.setValue('qty_initial_qe',row['QE_IP']) if 'QE_IP' in row else rec.setValue('qty_final_qe',row['QEI'])
            if not row['AUX_POS'] == 'NULL':
                rec.setValue('col_pipe_position',row['AUX_POS'])
            if not row['AUX_PROF_I'] == 'NULL':
                rec.setValue('aux_prof_i',row['AUX_PROF_I'])
            rec.setValue('el_terr_up',row['COTA_I'])
            rec.setValue('el_terr_down',row['COTA_F'])
            rec.setValue('inspection_id_up',row['NODO_I'])
            rec.setValue('inspection_id_down',row['NODO_F'])
            rec.setValue('downstream_seg_id',row['TRM_(N+1)'])
            row = self.model.rowCount()
            self.model.insertRecord(row, rec)
        print("Total time execution to upload: --- %s seconds ---" % (time.time() - start_time))
        #calculate with the parameters

