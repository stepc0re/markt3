# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'today.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 371, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btn_search = QtGui.QPushButton(self.groupBox)
        self.btn_search.setGeometry(QtCore.QRect(290, 20, 75, 23))

        self.btn_search.setObjectName(_fromUtf8("btn_search"))
        self.search_txt = QtGui.QLineEdit(self.groupBox)
        self.search_txt.setGeometry(QtCore.QRect(60, 20, 221, 21))
        self.search_txt.setObjectName(_fromUtf8("search_txt"))
        self.lb_search = QtGui.QLabel(self.groupBox)
        self.lb_search.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.lb_search.setObjectName(_fromUtf8("lb_search"))
        self.DB_bearbeiten = QtGui.QPushButton(Form)
        self.DB_bearbeiten.setGeometry(QtCore.QRect(20, 30, 91, 23))
        self.DB_bearbeiten.setObjectName(_fromUtf8("DB_bearbeiten"))

        #self.DB_bearbeiten.setStyleSheet("QPushButton{ border-radius: 6px; border-color: black}")


        self.neue_kunde = QtGui.QPushButton(Form)
        self.neue_kunde.setGeometry(QtCore.QRect(120, 30, 161, 23))
        self.neue_kunde.setObjectName(_fromUtf8("neue_kunde"))
        #self.neue_kunde.setStyleSheet("QPushButton{ background-color: yellow; border-radius: 6px; border-width: 4px}")

        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 130, 381, 161))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "GroupBox", None))
        self.btn_search.setText(_translate("Form", "search", None))
        self.lb_search.setText(_translate("Form", "search", None))
        self.DB_bearbeiten.setText(_translate("Form", "DB_bearbeiten", None))
        self.neue_kunde.setText(_translate("Form", "neuen kunden anlegen", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

