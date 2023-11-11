from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

import sys


class AppWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        '''Uygulama penceresi ayarları'''
        super(AppWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(QtCore.QSize(960, 540))
        self.setMaximumSize(QtCore.QSize(1920, 1080))

        self.cameras = QCameraInfo.availableCameras()
        if not self.cameras:
            pass

        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder)

        self.selectCam(0)
        self.show()

    def selectCam(self, i):
        '''Kamera cihazı seçimi'''
        self.cam = QCamera(self.cameras[i])
        self.cam.setViewfinder(self.viewfinder)
        # self.configView ()
        self.cam.error.connect(lambda: self.alert(self.camera.errorString()))
        self.cam.start()

    def configView(self):
        '''Görüntü ayarları'''
        self.viewfinder.setContrast(64)
        self.viewfinder.setBrightness(128)
        self.viewfinder.setHue(14)
        self.viewfinder.setSaturation(64)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Mask Detection")
    window = AppWindow()
    app.exec_()
