# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weiter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import new_frame_weiter

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(729, 411)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.txtStrom = QtGui.QLabel(Frame)
        self.txtStrom.setGeometry(QtCore.QRect(380, 70, 101, 21))
        self.txtStrom.setObjectName(_fromUtf8("txtStrom"))
        self.Schuko_text = QtGui.QLineEdit(Frame)
        self.Schuko_text.setGeometry(QtCore.QRect(530, 110, 181, 20))
        self.Schuko_text.setObjectName(_fromUtf8("Schuko_text"))
        self.txtWasser = QtGui.QLabel(Frame)
        self.txtWasser.setGeometry(QtCore.QRect(380, 280, 71, 20))
        self.txtWasser.setObjectName(_fromUtf8("txtWasser"))
        self.CEE_32_text = QtGui.QLineEdit(Frame)
        self.CEE_32_text.setGeometry(QtCore.QRect(530, 190, 181, 20))
        self.CEE_32_text.setObjectName(_fromUtf8("CEE_32_text"))
        self.save_btn = QtGui.QPushButton(Frame)
        self.save_btn.setGeometry(QtCore.QRect(510, 360, 75, 23))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.Breite_text = QtGui.QLineEdit(Frame)
        self.Breite_text.setGeometry(QtCore.QRect(110, 150, 181, 20))
        self.Breite_text.setObjectName(_fromUtf8("Breite_text"))
        self.CEE_16_text = QtGui.QLineEdit(Frame)
        self.CEE_16_text.setGeometry(QtCore.QRect(530, 150, 181, 20))
        self.CEE_16_text.setObjectName(_fromUtf8("CEE_16_text"))
        self.laenge_text = QtGui.QLineEdit(Frame)
        self.laenge_text.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.laenge_text.setObjectName(_fromUtf8("laenge_text"))
        self.txtBreite = QtGui.QLabel(Frame)
        self.txtBreite.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.txtBreite.setObjectName(_fromUtf8("txtBreite"))
        self.Groesse_text = QtGui.QLineEdit(Frame)
        self.Groesse_text.setGeometry(QtCore.QRect(110, 230, 181, 20))
        self.Groesse_text.setObjectName(_fromUtf8("Groesse_text"))
        self.txtGas = QtGui.QLabel(Frame)
        self.txtGas.setGeometry(QtCore.QRect(10, 280, 41, 21))
        self.txtGas.setObjectName(_fromUtf8("txtGas"))
        self.txtHoehe = QtGui.QLabel(Frame)
        self.txtHoehe.setGeometry(QtCore.QRect(10, 190, 71, 21))
        self.txtHoehe.setObjectName(_fromUtf8("txtHoehe"))
        self.Type_text = QtGui.QComboBox(Frame)
        self.Type_text.setGeometry(QtCore.QRect(110, 70, 181, 20))
        self.Type_text.setObjectName(_fromUtf8("Type_text"))
        self.Type_text.addItem(_fromUtf8(""))
        self.Type_text.addItem(_fromUtf8(""))
        self.Type_text.addItem(_fromUtf8(""))
        self.txtSchuko = QtGui.QLabel(Frame)
        self.txtSchuko.setGeometry(QtCore.QRect(380, 110, 71, 21))
        self.txtSchuko.setObjectName(_fromUtf8("txtSchuko"))
        self.txtCEE_16 = QtGui.QLabel(Frame)
        self.txtCEE_16.setGeometry(QtCore.QRect(380, 150, 91, 21))
        self.txtCEE_16.setObjectName(_fromUtf8("txtCEE_16"))
        self.txtLaenge = QtGui.QLabel(Frame)
        self.txtLaenge.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.txtLaenge.setObjectName(_fromUtf8("txtLaenge"))
        self.Wasser_text = QtGui.QComboBox(Frame)
        self.Wasser_text.setGeometry(QtCore.QRect(530, 280, 181, 20))
        self.Wasser_text.setObjectName(_fromUtf8("Wasser_text"))
        self.Wasser_text.addItem(_fromUtf8(""))
        self.Wasser_text.addItem(_fromUtf8(""))
        self.CEE_32 = QtGui.QLabel(Frame)
        self.CEE_32.setGeometry(QtCore.QRect(380, 190, 81, 21))
        self.CEE_32.setObjectName(_fromUtf8("CEE_32"))
        self.txtGesamtleistung = QtGui.QLabel(Frame)
        self.txtGesamtleistung.setGeometry(QtCore.QRect(380, 230, 161, 21))
        self.txtGesamtleistung.setObjectName(_fromUtf8("txtGesamtleistung"))
        self.Gas_text = QtGui.QComboBox(Frame)
        self.Gas_text.setGeometry(QtCore.QRect(110, 280, 181, 20))
        self.Gas_text.setObjectName(_fromUtf8("Gas_text"))
        self.Gas_text.addItem(_fromUtf8(""))
        self.Gas_text.addItem(_fromUtf8(""))
        self.txtType = QtGui.QLabel(Frame)
        self.txtType.setGeometry(QtCore.QRect(8, 70, 71, 21))
        self.txtType.setObjectName(_fromUtf8("txtType"))
        self.abbrechen_btn = QtGui.QPushButton(Frame)
        self.abbrechen_btn.setGeometry(QtCore.QRect(590, 360, 75, 23))
        self.abbrechen_btn.setObjectName(_fromUtf8("abbrechen_btn"))
        self.Strombedarf_text = QtGui.QComboBox(Frame)
        self.Strombedarf_text.setGeometry(QtCore.QRect(530, 70, 181, 20))
        self.Strombedarf_text.setObjectName(_fromUtf8("Strombedarf_text"))
        self.Strombedarf_text.addItem(_fromUtf8(""))
        self.Strombedarf_text.addItem(_fromUtf8(""))
        self.Gesamtleistung_text = QtGui.QLineEdit(Frame)
        self.Gesamtleistung_text.setGeometry(QtCore.QRect(530, 230, 181, 20))
        self.Gesamtleistung_text.setObjectName(_fromUtf8("Gesamtleistung_text"))
        self.Hoehe_text = QtGui.QLineEdit(Frame)
        self.Hoehe_text.setGeometry(QtCore.QRect(110, 190, 181, 20))
        self.Hoehe_text.setObjectName(_fromUtf8("Hoehe_text"))
        self.txtGroesse = QtGui.QLabel(Frame)
        self.txtGroesse.setGeometry(QtCore.QRect(10, 230, 71, 21))
        self.txtGroesse.setObjectName(_fromUtf8("txtGroesse"))
        self.zurück_btn = QtGui.QPushButton(Frame)
        self.zurück_btn.setGeometry(QtCore.QRect(430, 360, 75, 23))
        self.zurück_btn.setObjectName(_fromUtf8("abbrechen_btn"))

        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.save_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Frame.close)
        QtCore.QObject.connect(self.abbrechen_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Frame.close)
        QtCore.QObject.connect(self.zurück_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.back_to_last_page)
        QtCore.QObject.connect(self.zurück_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def back_to_last_page(self):

        self.window = QtGui.QFrame()
        self.ui = new_frame_weiter.Ui_BoaWista()
        self.ui.setupUi(self.window)
        self.window.show()

    def save_Data(self):
        self.data = []

        self.data.append(self.txtType.objectName())
        self.data.append(self.Type_text.text())
        self.data.append(self.txtLaenge.objectName())
        self.data.append(self.laenge_text.text())
        self.data.append(self.txtBreite.objectName())
        self.data.append(self.Breite_text.text())
        self.data.append(self.txtHoehe.objectName())
        self.data.append(self.Hoehe_text_text.text())
        self.data.append(self.txtStrom.objectName())
        self.data.append(self.Strombedarf_text_text.text())
        self.data.append(self.txtSchuko.objectName())
        self.data.append(self.Schuko_text_text.text())
        self.data.append(self.txtCEE_16.objectName())
        self.data.append(self.CEE_16_text_text.text())
        self.data.append(self.CEE_32.objectName())
        self.data.append(self.CEE_32_text.text())
        self.data.append(self.txtGesamtleistung.objectName())
        self.data.append(self.Gesamtleistung_text.text())
        self.data.append(self.txtGas.objectName())
        self.data.append(self.Gas_text.text())
        self.data.append(self.txtWasser.objectName())
        self.data.append(self.Wasser_text.currentText())

        self.sub_dict = {}
        for i in range(0, len(self.data), 2):
            self.sub_dict[self.data[i]] = self.data[i + 1]  # key-value pair defined

        # self.open_new_window()

        print('output=', self.sub_dict)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.txtStrom.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Strombedarf</span></p></body></html>", None))
        self.txtWasser.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Wasser</span></p></body></html>", None))
        self.save_btn.setText(_translate("Frame", "Speichern", None))
        self.txtBreite.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Breite</span></p></body></html>", None))
        self.txtGas.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Gas</span></p></body></html>", None))
        self.txtHoehe.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Höhe</span></p></body></html>", None))
        self.Type_text.setItemText(0, _translate("Frame", "Food_Truck", None))
        self.Type_text.setItemText(1, _translate("Frame", "Anhänger", None))
        self.Type_text.setItemText(2, _translate("Frame", "Pavillions", None))
        self.txtSchuko.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Schuko</span></p></body></html>", None))
        self.txtCEE_16.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">CEE 16 5p</span></p></body></html>", None))
        self.txtLaenge.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Länge</span></p></body></html>", None))
        self.Wasser_text.setItemText(0, _translate("Frame", "Ja", None))
        self.Wasser_text.setItemText(1, _translate("Frame", "Nein", None))
        self.CEE_32.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">CEE 32 5p</span></p></body></html>", None))
        self.txtGesamtleistung.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Gesamtleistung(KW)</span></p></body></html>", None))
        self.Gas_text.setItemText(0, _translate("Frame", "Ja", None))
        self.Gas_text.setItemText(1, _translate("Frame", "Nein", None))
        self.txtType.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Type of </span></p></body></html>", None))
        self.abbrechen_btn.setText(_translate("Frame", "Abbrechen", None))
        self.zurück_btn.setText(_translate("Frame", "Zurück", None))
        self.Strombedarf_text.setItemText(0, _translate("Frame", "Ja", None))
        self.Strombedarf_text.setItemText(1, _translate("Frame", "Nein", None))
        self.txtGroesse.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Größe</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

