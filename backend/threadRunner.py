
from PySide6.QtCore import QDateTime as sQDateTime
from PySide6.QtCore import QObject 
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal



from PySide6.QtCore import QObject
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal
import cv2
import time

class threadRunner(QObject):
    finished = Signal()

    def __init__(self, func):
        super(threadRunner,self).__init__()
        self.set_func(func)
        self._thread = QThread
    
    def __starter__(self,):
            while True:
                self.func()
            print('dddd33333333333')
            self.finished.emit()
        # while True:
        #     try:
        #         self.func()
        #         time.sleep(0.01)

        #     except:
        #         print('camera Error happend in thread while !')
            
    def set_func(self, func):
        self.func = func
    
    def start_thread(self,):
        self._thread = QThread()
        self.moveToThread( self._thread )
        self._thread.started.connect( self.__starter__ )
        #self.finished.connect(self._thread.quit)
        #self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()


# class cameraThreadHandler:

#     def __init__(self):


#     def start(self,):
#         cth = cameraThread(cam)
#         thread = QThread()
#         cth.moveToThread(thread)
#         cth.success_grab_signal.connect(test)
#         thread.start()


# class threadRunner(QObject):
#     #rig_signal = Signal()
#     finished = Signal()

#     def __init__(self, func) -> None:
#         super(threadRunner,self).__init__()
#         print('a'*800)
#         self.set_func(func)

#     def set_func(self, func):
#         self.func = func

#     def __run_func__(self,):
#         self.func()
#         #self.finished.emit()

#     def run_thread(self, ):
#             self.thread = QThread()
#             self.moveToThread(self.thread)
#             self.thread.started.connect(self.__run_func__)
#             # self.finished.connect(self._thread.deleteLater)
#             print('befooooooooooor')
#             self.thread.start()
#             print('afterrrrrrrrrrr')