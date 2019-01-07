# gui-tester

Just to test __PyCharm__ with __PyQt5__
A basic _MainWindow_ dialog opens.
Press the button, and then select one or more audio or image files.
The names of the files appear in the window. The total number of files appears to the right.
The status bar flashes the number of files for 2 seconds.

## Why

The typical way of creating a PyQt5 GUI is demonstrated:

### Imports

```
from PyQt5.Qt import *         - easiest way to import PyQt
from PyQt5.uic import loadUi   - this loads a Qt Designer .ui file
import sys
import os
```

### Remarks on Code

**Class Definition**
- we are subclassing a MainWindow object
```
class maingui(QMainWindow):
```
**Starting the application**
- There's a check after all of the definitions to see if we are in the main module. If we are, then we:
- create a QApplication object (the ```sys.argv``` argument allows us to enter parameters at the command line, if we want to
- get an instance of our MainWindow class
- ```sys.exit(app.exec_)``` starts things off

```
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m=maingui()
    sys.exit(app.exec_())
```
**Make the GUI**
```
    def __init__(self):
        super().__init__()
        self.gui()


    def gui(self):
        loadUi('maingui.ui', self)
        self.bFile.clicked.connect(self.loadFile)
        self.show()
```
- we initialise by calling the superclass's constructor
- the ```loadUi('maingui.ui, self)``` call loads the .ui XML file
- ```self.bFile.clicked.connect(self.loadFile)``` is used to connect the PushButton to some code
- ```self.show()``` displays the GUI on the screen

**Handle the PushButton***
- Our PushButton uses the following code. It starts off by instamntiating a file opening dialog (part of PyQt)
- next, we get the names of the files that were selected into a tuple
- the first element of the tuple has an array of the fgiles we have selected
- we loop through the list of files, adding the name to a PlainTextEdit (the window in the middle)
- we update a little label at the top right with the number of files that we opened
- we also put the same information on the MainWindow's StatusBar
```
    def loadFile(self):
        a = QFileDialog()
        f = a.getOpenFileNames(self, 'Open a file!', filter='All image files (*.png *.jpg *.wav);;All sound files (*.mp3 *.aac)')
        for item in f[0]:
            # print(type(item), item)
            self.text.appendPlainText(item)
            nFiles=len(f[0])
        self.lblFileCount.setText(str(nFiles))
        self.statusBar().showMessage('Opened {} files'.format(nFiles), 2000)
```
