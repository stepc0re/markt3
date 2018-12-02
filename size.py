import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'BoaVista'
        self.left = 0
        self.top = 0
        self.width = 676
        self.height = 612
        self.resize(670, 680)
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "DB_Edit")
        self.tabs.addTab(self.tab2, "neuer_Markt")
        self.tabs.addTab(self.tab3, "Statistic")

        # Create first tab
        self.tab1.layout = QHBoxLayout(self)
        self.new_layot = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton1.adjustSize()

        self.groupbox = QGroupBox()
        self.groupbox.adjustSize()
        self.suche_lbl = QPushButton(self.groupbox)
        self.suche_lbl.adjustSize()
        self.suche_lbl.setObjectName(("suche_lbl"))

        self.groupbox1 = QGroupBox()


        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.groupbox)
        self.tab1.layout.addWidget(self.groupbox1)
        self.tab1.layout.addWidget(self.suche_lbl)

        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())