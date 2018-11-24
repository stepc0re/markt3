# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from new_frame_weiter import Ui_BoaWista
from weiter import Ui_Frame


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_otherwindow(object):
    def setupUi(self, otherwindow):
        otherwindow.setObjectName(_fromUtf8("otherwindow"))
        otherwindow.resize(775, 568)
        self.centralwidget = QtGui.QWidget(otherwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.DB_Edit = QtGui.QPushButton(self.centralwidget)
        self.DB_Edit.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.DB_Edit.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.DB_Edit.setObjectName(_fromUtf8("DB_Edit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 281, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.neue_kunde = QtGui.QToolButton(self.centralwidget)
        self.neue_kunde.setGeometry(QtCore.QRect(30, 250, 191, 41))
        self.neue_kunde.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.neue_kunde.setObjectName(_fromUtf8("Rechnung"))
        self.Statictik = QtGui.QPushButton(self.centralwidget)
        self.Statictik.setGeometry(QtCore.QRect(30, 310, 191, 41))
        self.Statictik.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.Statictik.setObjectName(_fromUtf8("Statistik"))
        # self.Black_list = QtGui.QPushButton(self.centralwidget)
        # self.Black_list.setGeometry(QtCore.QRect(30, 370, 191, 41))
        # self.Black_list.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        # self.Black_list.setObjectName(_fromUtf8("Black_list"))
        self.neuen_Markt = QtGui.QPushButton(self.centralwidget)
        self.neuen_Markt.setGeometry(QtCore.QRect(30, 130, 191, 41))
        self.neuen_Markt.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.neuen_Markt.setObjectName(_fromUtf8("neuen_Markt"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 511, 481))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/Street_Food.jpg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        otherwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(otherwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        otherwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(otherwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        otherwindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(otherwindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(otherwindow)
        QtCore.QObject.connect(self.DB_Edit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.open_new_frame_weiter)
        QtCore.QObject.connect(self.DB_Edit, QtCore.SIGNAL(_fromUtf8("clicked()")), otherwindow.close)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def open_new_frame_weiter(self):
        self.window = QtGui.QFrame()
        self.ui = Ui_BoaWista()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, otherwindow):
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow", None))
        self.DB_Edit.setText(_translate("otherwindow", "DB_bearbeiten", None))
        self.label.setText(_translate("otherwindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#00007f;\">Willkommen bei Boa Vista</span></p></body></html>", None))
        self.neue_kunde.setText(_translate("otherwindow", "neuen Kunden anlegen", None))
        self.Statictik.setText(_translate("otherwindow", "Statistik", None))
        #self.Black_list.setText(_translate("otherwindow", "Black-List", None))
        #self.neuen_Markt.setText(_translate("otherwindow", "Neuen Markt anlegen", None))
        self.menuFIle.setTitle(_translate("otherwindow", "File", None))
        self.actionExit.setText(_translate("otherwindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    otherwindow = QtGui.QMainWindow()
    ui = Ui_otherwindow()
    ui.setupUi(otherwindow)
    otherwindow.show()
    sys.exit(app.exec_())

