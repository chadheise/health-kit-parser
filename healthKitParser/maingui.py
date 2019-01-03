import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class MainGui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initWindow()
        self.initMenu()
        self.initSelectionPanel()

        self.central_widget = CentralWidget(self) 
        self.setCentralWidget(self.central_widget)

    def initWindow(self):
        self.setWindowTitle("Apple HealthKit Analyzer")
        self.setGeometry(300, 300, 300, 150)
        self.resize(1500, 750)

    def initMenu(self):
        self.menuBar().setNativeMenuBar(False)

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit, Qt.CTRL + Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.help_menu.addAction('&About', self.about)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
                
    def fileQuit(self):
        self.close()

    def about(self):
        QMessageBox.about(self, "About",
            """Apple HealthKit data analyzer. \n\nManor, LLC""")

class CentralWidget(QWidget):

    def __init__(self, parent):        
        super(CentralWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.selection_panel = SelectionPanel(self)
        self.layout.addWidget(self.selection_panel)

        self.graph_panel = SelectionPanel(self)
        self.layout.addWidget(self.graph_panel)

        self.setLayout(self.layout)

class SelectionPanel(QWidget):

    def __init__(self, parent):
        super(SelectionPanel, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.setLayout(self.layout)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)
