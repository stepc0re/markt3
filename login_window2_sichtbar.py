# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window2_sichtbar.ui'
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

class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName(_fromUtf8("Login_Window"))
        Login_Window.resize(762, 390)
        Login_Window.setFrameShape(QtGui.QFrame.StyledPanel)
        Login_Window.setFrameShadow(QtGui.QFrame.Raised)
        self.user_btn = QtGui.QLabel(Login_Window)
        self.user_btn.setGeometry(QtCore.QRect(30, 150, 71, 20))
        self.user_btn.setObjectName(_fromUtf8("user_btn"))
        self.pass_btn = QtGui.QLabel(Login_Window)
        self.pass_btn.setGeometry(QtCore.QRect(30, 180, 81, 20))
        self.pass_btn.setObjectName(_fromUtf8("pass_btn"))
        self.Foto = QtGui.QLabel(Login_Window)
        self.Foto.setGeometry(QtCore.QRect(380, 0, 381, 391))
        self.Foto.setText(_fromUtf8(""))
        self.Foto.setPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/BoaVista/Brand.png")))
        self.Foto.setObjectName(_fromUtf8("Foto"))
        self.user_text = QtGui.QLineEdit(Login_Window)
        self.user_text.setGeometry(QtCore.QRect(130, 150, 181, 20))
        self.user_text.setObjectName(_fromUtf8("user_text"))
        self.pass_text = QtGui.QLineEdit(Login_Window)
        self.pass_text.setGeometry(QtCore.QRect(130, 180, 181, 21))
        self.pass_text.setObjectName(_fromUtf8("pass_text"))
        self.willkommen_btn = QtGui.QLabel(Login_Window)
        self.willkommen_btn.setGeometry(QtCore.QRect(10, 30, 341, 81))
        self.willkommen_btn.setObjectName(_fromUtf8("willkommen_btn"))
        self.Login_btn = QtGui.QPushButton(Login_Window)
        self.Login_btn.setGeometry(QtCore.QRect(150, 260, 131, 31))
        self.Login_btn.setObjectName(_fromUtf8("Login_btn"))
        self.passwort_sichtbar_btn = QtGui.QPushButton(Login_Window)
        self.passwort_sichtbar_btn.setGeometry(QtCore.QRect(150, 220, 131, 31))
        self.passwort_sichtbar_btn.setObjectName(_fromUtf8("passwort_sichtbar_btn"))

        self.retranslateUi(Login_Window)
        QtCore.QObject.connect(self.passwort_sichtbar_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Login_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        Login_Window.setWindowTitle(_translate("Login_Window", "Frame", None))
        self.user_btn.setText(_translate("Login_Window", "<html><head/><body><p><span style=\" font-size:11pt;\">Username</span></p></body></html>", None))
        self.pass_btn.setText(_translate("Login_Window", "<html><head/><body><p><span style=\" font-size:11pt;\">Password</span></p></body></html>", None))
        self.willkommen_btn.setText(_translate("Login_Window", "<html><head/><body><p><span style=\" font-size:22pt; color:#00007f;\">Willkommen bei Boa Vista</span></p></body></html>", None))
        self.Login_btn.setText(_translate("Login_Window", "anmelden", None))
        self.passwort_sichtbar_btn.setText(_translate("Login_Window", "Passwort sichbar machen", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login_Window = QtGui.QFrame()
    ui = Ui_Login_Window()
    ui.setupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec_())

