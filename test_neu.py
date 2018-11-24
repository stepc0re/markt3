# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_neu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from otherwindow import  Ui_otherwindow
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

class Ui_MainWindow(object):

    def openwindow(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_otherwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.setStyleSheet()
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 140, 171, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.setStyleSheet("background-color: red")
        # self.pushButton.setStyleSheet('border-width: 5px')
        # self.pushButton.setStyleSheet('border-radius: 20px')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLog_in = QtGui.QMenu(self.menubar)
        self.menuLog_in.setObjectName(_fromUtf8("menuLog_in"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin_window = QtGui.QAction(MainWindow)
        self.actionLogin_window.setObjectName(_fromUtf8("actionLogin_window"))
        self.menuLog_in.addAction(self.actionLogin_window)
        self.menubar.addAction(self.menuLog_in.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionLogin_window, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Neuen Kunden anlegen", None))
        self.menuLog_in.setTitle(_translate("MainWindow", "Log in", None))
        self.actionLogin_window.setText(_translate("MainWindow", "login_window", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: gray;border: 3px solid red;}')
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

