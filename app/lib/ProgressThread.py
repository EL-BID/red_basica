from PyQt5.QtCore import QThread
from qgis.core import Qgis
from qgis.utils import QgsMessageLog

class ProgressThread(QThread):

    def __init__(self, mainView, controller, run, callback=None):
        super().__init__(mainView)     
        self.bar = mainView.progressBar
        self.msg = mainView.progressMsg        
        self.iface = mainView.iface
        self.refreshTables = mainView.refreshTables
        self.callback = callback

        #show progress bar
        self.bar.show()
        self.msg.show() 
        
        #attach worker
        worker = controller
        self.started.connect(run)        
        worker.moveToThread(self)        
        worker.finished.connect(self.threadFinished)        
        worker.error.connect(self.threadError)
        worker.progress.connect(self.bar.setValue)
        worker.info.connect(self.msg.setText)
        self.worker = worker
        self.start()


    def threadFinished(self, success):               
        # clean up the worker and thread
        self.worker.deleteLater()
        self.quit()
        self.wait()
        self.deleteLater()        

        if self.callback:
            return self.callback(success)       
                        
        if success:
            self.bar.hide()
            self.msg.hide()
            self.refreshTables()            
            self.iface.messageBar().pushMessage('the process ended successfully!')
        else:
            self.bar.hide()
            #let msg open to display last error
            self.iface.messageBar().pushMessage('Something went wrong! See the message log for more information.', level=Qgis.Critical, duration=3)

    def threadError(self, e, trace):        
        QgsMessageLog.logMessage('ProgressBar thread raised an exception:\n {}'.format(trace), level=Qgis.Critical)         