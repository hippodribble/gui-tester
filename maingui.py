from PyQt5.Qt import *
from PyQt5.uic import loadUi
import sys


class maingui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui()


    def gui(self):
        loadUi('maingui.ui', self)
        self.bFile.clicked.connect(self.loadFile)
        self.show()


    def loadFile(self):
        a = QFileDialog()
        f = a.getOpenFileName(self, 'Open a file!', filter='All image files (*.png *.jpg *.wav);;All sound files (*.mp3 *.aac)')
        self.statusBar().showMessage(f[0], 2000)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    m=maingui()
    sys.exit(app.exec_())



