
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


lst = [u"D", u"E", u"EF", u"F", u"FG", u"G", u"H", u"JS", u"J", u"K", u"M", u"P", u"R", u"S", u"T", u"U", u"V", u"X", u"Y", u"Z"]


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        window_width = 1200
        window_height = 600
        self.setFixedSize(window_width, window_height)
    
        groupbox = QGroupBox("".format(), self)
        groupbox.setGeometry(10, 10, 120, 60)

        layout_groupbox = QHBoxLayout(groupbox)

        #groupBox.setGeometry(QtCore.QRect(10, 70, 371, 51))
        #groupBox.setObjectName(_fromUtf8("groupBox"))
        #btn_search = QtGui.QPushButton(self.groupBox)
        #self.btn_search.setGeometry(QtCore.QRect(290, 20, 75, 23))

        self.btn_search.setObjectName(_fromUtf8("btn_search"))
        self.search_txt = QtGui.QLineEdit(self.groupBox)
        self.search_txt.setGeometry(QtCore.QRect(60, 20, 221, 21))
        self.search_txt.setObjectName(_fromUtf8("search_txt"))
        self.lb_search = QtGui.QLabel(self.groupBox)
        self.lb_search.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.lb_search.setObjectName(_fromUtf8("lb_search"))
        self.groupbox.layout().addLayout(self.groupbox)
        layout_groupbox.addStretch(1)
        self.initUI()

    def createLayout_group(self, number):
        sgroupbox = QGroupBox("Kunden_List{}:".format(number), self)
        sgroupbox.setGeometry(10, 10, 1200, 600)

        layout_groupbox = QVBoxLayout(sgroupbox)

        for i in range(len(lst)):
            row = QtGui.QHBoxLayout()
            row.addWidget(QtGui.QLineEdit(lst[i]))
            row.addWidget(QtGui.QPushButton('Push Button'))
            row.addWidget(QtGui.QPushButton('Push Button_1'))
            row.addWidget(QtGui.QPushButton('Push Button_2'))
            sgroupbox.layout().addLayout(row)

        layout_groupbox.addStretch(1)


        return sgroupbox

    def createLayout_Container(self):
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedWidth(1200)
        self.scrollarea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollarea.setWidget(widget)
        self.layout_SArea = QVBoxLayout(widget)

        for i in range(5):
            self.layout_SArea.addWidget(self.createLayout_group(i))
        self.layout_SArea.addStretch(1)

    def initUI(self):
        self.createLayout_Container()
        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.scrollarea)
        self.layout_All.addWidget(self.groupBox)
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())