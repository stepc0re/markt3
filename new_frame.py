# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_frame.ui'
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

class Ui_BoaWista(object):
    def setupUi(self, BoaWista):
        BoaWista.setObjectName(_fromUtf8("BoaWista"))
        BoaWista.setWindowModality(QtCore.Qt.ApplicationModal)
        BoaWista.resize(848, 886)
        BoaWista.setFrameShape(QtGui.QFrame.StyledPanel)
        BoaWista.setFrameShadow(QtGui.QFrame.Raised)
        self.txtTelefonnummer = QtGui.QLabel(BoaWista)
        self.txtTelefonnummer.setGeometry(QtCore.QRect(402, 110, 111, 21))
        self.txtTelefonnummer.setObjectName(_fromUtf8("txtTelefonnummer"))
        self.Haendlerkategorie_text = QtGui.QComboBox(BoaWista)
        self.Haendlerkategorie_text.setGeometry(QtCore.QRect(542, 220, 181, 20))
        self.Haendlerkategorie_text.setObjectName(_fromUtf8("Haendlerkategorie_text"))
        self.Haendlerkategorie_text.addItem(_fromUtf8(""))
        self.Haendlerkategorie_text.addItem(_fromUtf8(""))
        self.Haendlerkategorie_text.addItem(_fromUtf8(""))
        self.Haendlerkategorie_text.addItem(_fromUtf8(""))
        self.txtBezeichungSpeise = QtGui.QLabel(BoaWista)
        self.txtBezeichungSpeise.setGeometry(QtCore.QRect(32, 410, 51, 20))
        self.txtBezeichungSpeise.setObjectName(_fromUtf8("txtBezeichungSpeise"))
        self.CEE_16_text = QtGui.QLineEdit(BoaWista)
        self.CEE_16_text.setGeometry(QtCore.QRect(552, 610, 181, 20))
        self.CEE_16_text.setObjectName(_fromUtf8("CEE_16_text"))
        self.txtType = QtGui.QLabel(BoaWista)
        self.txtType.setGeometry(QtCore.QRect(30, 530, 71, 21))
        self.txtType.setObjectName(_fromUtf8("txtType"))
        self.Strasse_text = QtGui.QLineEdit(BoaWista)
        self.Strasse_text.setGeometry(QtCore.QRect(132, 190, 181, 20))
        self.Strasse_text.setObjectName(_fromUtf8("Strasse_text"))
        self.IDKundennummer = QtGui.QLabel(BoaWista)
        self.IDKundennummer.setGeometry(QtCore.QRect(402, 180, 121, 21))
        self.IDKundennummer.setObjectName(_fromUtf8("IDKundennummer"))
        self.Warengruppe_text = QtGui.QComboBox(BoaWista)
        self.Warengruppe_text.setGeometry(QtCore.QRect(132, 360, 181, 20))
        self.Warengruppe_text.setObjectName(_fromUtf8("Warengruppe_text"))
        self.Warengruppe_text.addItem(_fromUtf8(""))
        self.Warengruppe_text.addItem(_fromUtf8(""))
        self.Warengruppe_text.addItem(_fromUtf8(""))
        self.Warengruppe_text.addItem(_fromUtf8(""))
        self.CEE_32_text = QtGui.QLineEdit(BoaWista)
        self.CEE_32_text.setGeometry(QtCore.QRect(552, 650, 181, 20))
        self.CEE_32_text.setObjectName(_fromUtf8("CEE_32_text"))
        self.txtGesamtleistung = QtGui.QLabel(BoaWista)
        self.txtGesamtleistung.setGeometry(QtCore.QRect(402, 690, 161, 21))
        self.txtGesamtleistung.setObjectName(_fromUtf8("txtGesamtleistung"))
        self.txtKontaktperson = QtGui.QLabel(BoaWista)
        self.txtKontaktperson.setGeometry(QtCore.QRect(30, 110, 111, 21))
        self.txtKontaktperson.setObjectName(_fromUtf8("txtKontaktperson"))
        self.txtHoehe = QtGui.QLabel(BoaWista)
        self.txtHoehe.setGeometry(QtCore.QRect(32, 650, 71, 21))
        self.txtHoehe.setObjectName(_fromUtf8("txtHoehe"))
        self.Email_text = QtGui.QLineEdit(BoaWista)
        self.Email_text.setGeometry(QtCore.QRect(542, 70, 181, 20))
        self.Email_text.setObjectName(_fromUtf8("Email_text"))
        self.lngWarengruppen = QtGui.QLabel(BoaWista)
        self.lngWarengruppen.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.lngWarengruppen.setObjectName(_fromUtf8("lngWarengruppen"))
        self.laenge_text = QtGui.QLineEdit(BoaWista)
        self.laenge_text.setGeometry(QtCore.QRect(132, 570, 181, 20))
        self.laenge_text.setObjectName(_fromUtf8("laenge_text"))
        self.txtGroesse = QtGui.QLabel(BoaWista)
        self.txtGroesse.setGeometry(QtCore.QRect(32, 690, 71, 21))
        self.txtGroesse.setObjectName(_fromUtf8("txtGroesse"))
        self.txtEmail = QtGui.QLabel(BoaWista)
        self.txtEmail.setGeometry(QtCore.QRect(402, 70, 51, 20))
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.txtStrom = QtGui.QLabel(BoaWista)
        self.txtStrom.setGeometry(QtCore.QRect(402, 530, 101, 21))
        self.txtStrom.setObjectName(_fromUtf8("txtStrom"))
        self.Ort_text = QtGui.QLineEdit(BoaWista)
        self.Ort_text.setGeometry(QtCore.QRect(132, 270, 181, 20))
        self.Ort_text.setObjectName(_fromUtf8("Ort_text"))
        self.PLZ_text = QtGui.QLineEdit(BoaWista)
        self.PLZ_text.setGeometry(QtCore.QRect(132, 230, 181, 20))
        self.PLZ_text.setObjectName(_fromUtf8("PLZ_text"))
        self.Alias_txt = QtGui.QLineEdit(BoaWista)
        self.Alias_txt.setGeometry(QtCore.QRect(133, 150, 181, 20))
        self.Alias_txt.setObjectName(_fromUtf8("Alias_txt"))
        self.txtPLZ = QtGui.QLabel(BoaWista)
        self.txtPLZ.setGeometry(QtCore.QRect(30, 230, 71, 21))
        self.txtPLZ.setObjectName(_fromUtf8("txtPLZ"))
        self.Telefonnummer_text = QtGui.QLineEdit(BoaWista)
        self.Telefonnummer_text.setGeometry(QtCore.QRect(542, 110, 181, 20))
        self.Telefonnummer_text.setObjectName(_fromUtf8("Telefonnummer_text"))
        self.Speise_text = QtGui.QLineEdit(BoaWista)
        self.Speise_text.setGeometry(QtCore.QRect(132, 410, 601, 81))
        self.Speise_text.setObjectName(_fromUtf8("Speise_text"))
        self.txtFirmenname = QtGui.QLabel(BoaWista)
        self.txtFirmenname.setGeometry(QtCore.QRect(30, 70, 51, 21))
        self.txtFirmenname.setObjectName(_fromUtf8("txtFirmenname"))
        self.Strombedarf_text = QtGui.QComboBox(BoaWista)
        self.Strombedarf_text.setGeometry(QtCore.QRect(552, 530, 181, 20))
        self.Strombedarf_text.setObjectName(_fromUtf8("Strombedarf_text"))
        self.Strombedarf_text.addItem(_fromUtf8(""))
        self.Strombedarf_text.addItem(_fromUtf8(""))
        self.txtAnschrift = QtGui.QLabel(BoaWista)
        self.txtAnschrift.setGeometry(QtCore.QRect(30, 190, 81, 21))
        self.txtAnschrift.setObjectName(_fromUtf8("txtAnschrift"))
        self.Wasser_text = QtGui.QComboBox(BoaWista)
        self.Wasser_text.setGeometry(QtCore.QRect(560, 750, 181, 20))
        self.Wasser_text.setObjectName(_fromUtf8("Wasser_text"))
        self.Wasser_text.addItem(_fromUtf8(""))
        self.Wasser_text.addItem(_fromUtf8(""))
        self.kundennummer_txt = QtGui.QLineEdit(BoaWista)
        self.kundennummer_txt.setGeometry(QtCore.QRect(542, 180, 181, 20))
        self.kundennummer_txt.setObjectName(_fromUtf8("kundennummer_txt"))
        self.txtCEE_16 = QtGui.QLabel(BoaWista)
        self.txtCEE_16.setGeometry(QtCore.QRect(402, 610, 91, 21))
        self.txtCEE_16.setObjectName(_fromUtf8("txtCEE_16"))
        self.Type_text = QtGui.QComboBox(BoaWista)
        self.Type_text.setGeometry(QtCore.QRect(132, 530, 181, 20))
        self.Type_text.setObjectName(_fromUtf8("Type_text"))
        self.Type_text.addItem(_fromUtf8(""))
        self.Type_text.addItem(_fromUtf8(""))
        self.Type_text.addItem(_fromUtf8(""))
        self.txtWasser = QtGui.QLabel(BoaWista)
        self.txtWasser.setGeometry(QtCore.QRect(402, 750, 71, 20))
        self.txtWasser.setObjectName(_fromUtf8("txtWasser"))
        self.txtSchuko = QtGui.QLabel(BoaWista)
        self.txtSchuko.setGeometry(QtCore.QRect(402, 570, 71, 21))
        self.txtSchuko.setObjectName(_fromUtf8("txtSchuko"))
        self.txtBreite = QtGui.QLabel(BoaWista)
        self.txtBreite.setGeometry(QtCore.QRect(32, 610, 71, 21))
        self.txtBreite.setObjectName(_fromUtf8("txtBreite"))
        self.Kontaktperson_text = QtGui.QLineEdit(BoaWista)
        self.Kontaktperson_text.setGeometry(QtCore.QRect(132, 110, 181, 20))
        self.Kontaktperson_text.setObjectName(_fromUtf8("Kontaktperson_text"))
        self.Firma_text = QtGui.QLineEdit(BoaWista)
        self.Firma_text.setGeometry(QtCore.QRect(132, 70, 181, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(45)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.Firma_text.sizePolicy().hasHeightForWidth())
        self.Firma_text.setSizePolicy(sizePolicy)
        self.Firma_text.setObjectName(_fromUtf8("Firma_text"))
        self.Schuko_text = QtGui.QLineEdit(BoaWista)
        self.Schuko_text.setGeometry(QtCore.QRect(552, 570, 181, 20))
        self.Schuko_text.setObjectName(_fromUtf8("Schuko_text"))
        self.Gas_text = QtGui.QComboBox(BoaWista)
        self.Gas_text.setGeometry(QtCore.QRect(132, 750, 181, 20))
        self.Gas_text.setObjectName(_fromUtf8("Gas_text"))
        self.Gas_text.addItem(_fromUtf8(""))
        self.Gas_text.addItem(_fromUtf8(""))
        self.Groesse_text = QtGui.QLineEdit(BoaWista)
        self.Groesse_text.setGeometry(QtCore.QRect(132, 690, 181, 20))
        self.Groesse_text.setObjectName(_fromUtf8("Groesse_text"))
        self.Gesamtleistung_text = QtGui.QLineEdit(BoaWista)
        self.Gesamtleistung_text.setGeometry(QtCore.QRect(552, 690, 181, 20))
        self.Gesamtleistung_text.setObjectName(_fromUtf8("Gesamtleistung_text"))
        self.CEE_32 = QtGui.QLabel(BoaWista)
        self.CEE_32.setGeometry(QtCore.QRect(402, 650, 81, 21))
        self.CEE_32.setObjectName(_fromUtf8("CEE_32"))
        self.txtLaenge = QtGui.QLabel(BoaWista)
        self.txtLaenge.setGeometry(QtCore.QRect(32, 570, 71, 21))
        self.txtLaenge.setObjectName(_fromUtf8("txtLaenge"))
        self.Hoehe_text = QtGui.QLineEdit(BoaWista)
        self.Hoehe_text.setGeometry(QtCore.QRect(132, 650, 181, 20))
        self.Hoehe_text.setObjectName(_fromUtf8("Hoehe_text"))
        self.txtHndelKategorie = QtGui.QLabel(BoaWista)
        self.txtHndelKategorie.setGeometry(QtCore.QRect(402, 220, 121, 21))
        self.txtHndelKategorie.setObjectName(_fromUtf8("txtHndelKategorie"))
        self.Breite_text = QtGui.QLineEdit(BoaWista)
        self.Breite_text.setGeometry(QtCore.QRect(132, 610, 181, 20))
        self.Breite_text.setObjectName(_fromUtf8("Breite_text"))
        self.txtOrt = QtGui.QLabel(BoaWista)
        self.txtOrt.setGeometry(QtCore.QRect(30, 270, 51, 20))
        self.txtOrt.setObjectName(_fromUtf8("txtOrt"))
        self.txtGas = QtGui.QLabel(BoaWista)
        self.txtGas.setGeometry(QtCore.QRect(32, 750, 41, 21))
        self.txtGas.setObjectName(_fromUtf8("txtGas"))
        self.txtAlias = QtGui.QLabel(BoaWista)
        self.txtAlias.setGeometry(QtCore.QRect(30, 150, 51, 21))
        self.txtAlias.setObjectName(_fromUtf8("txtAlias"))
        self.verticalScrollBar = QtGui.QScrollBar(BoaWista)
        self.verticalScrollBar.setGeometry(QtCore.QRect(970, -1, 20, 821))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.Land_text = QtGui.QLineEdit(BoaWista)
        self.Land_text.setGeometry(QtCore.QRect(132, 310, 181, 20))
        self.Land_text.setObjectName(_fromUtf8("Land_text"))
        self.txtLand = QtGui.QLabel(BoaWista)
        self.txtLand.setGeometry(QtCore.QRect(30, 310, 51, 20))
        self.txtLand.setObjectName(_fromUtf8("txtLand"))
        self.pushButton = QtGui.QPushButton(BoaWista)
        self.pushButton.setGeometry(QtCore.QRect(620, 830, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(BoaWista)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 830, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(BoaWista)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QMetaObject.connectSlotsByName(BoaWista)

    def retranslateUi(self, BoaWista):
        BoaWista.setWindowTitle(_translate("BoaWista", "Frame", None))
        self.txtTelefonnummer.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Telefonnummer</span></p></body></html>", None))
        self.Haendlerkategorie_text.setItemText(0, _translate("BoaWista", "Neuekunde", None))
        self.Haendlerkategorie_text.setItemText(1, _translate("BoaWista", "Premium", None))
        self.Haendlerkategorie_text.setItemText(2, _translate("BoaWista", "Bestandskunde", None))
        self.Haendlerkategorie_text.setItemText(3, _translate("BoaWista", "Blacklist", None))
        self.txtBezeichungSpeise.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Speisen</span></p></body></html>", None))
        self.txtType.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Type of </span></p></body></html>", None))
        self.IDKundennummer.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Kundennummer</span></p></body></html>", None))
        self.Warengruppe_text.setItemText(0, _translate("BoaWista", "Speisen", None))
        self.Warengruppe_text.setItemText(1, _translate("BoaWista", "Sonstige", None))
        self.Warengruppe_text.setItemText(2, _translate("BoaWista", "Getränke", None))
        self.Warengruppe_text.setItemText(3, _translate("BoaWista", "Non-Food", None))
        self.txtGesamtleistung.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Gesamtleistung(KW)</span></p></body></html>", None))
        self.txtKontaktperson.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Kontaktperson</span></p></body></html>", None))
        self.txtHoehe.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Höhe</span></p></body></html>", None))
        self.lngWarengruppen.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Warengruppe</span></p></body></html>", None))
        self.txtGroesse.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Größe</span></p></body></html>", None))
        self.txtEmail.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Email</span></p></body></html>", None))
        self.txtStrom.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Strombedarf</span></p></body></html>", None))
        self.txtPLZ.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">PLZ</span></p></body></html>", None))
        self.txtFirmenname.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Firma</span></p></body></html>", None))
        self.Strombedarf_text.setItemText(0, _translate("BoaWista", "Ja", None))
        self.Strombedarf_text.setItemText(1, _translate("BoaWista", "Nein", None))
        self.txtAnschrift.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Straße Nr.</span></p></body></html>", None))
        self.Wasser_text.setItemText(0, _translate("BoaWista", "Ja", None))
        self.Wasser_text.setItemText(1, _translate("BoaWista", "Nein", None))
        self.txtCEE_16.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">CEE 16 5p</span></p></body></html>", None))
        self.Type_text.setItemText(0, _translate("BoaWista", "Food_Truck", None))
        self.Type_text.setItemText(1, _translate("BoaWista", "Anhänger", None))
        self.Type_text.setItemText(2, _translate("BoaWista", "Pavillions", None))
        self.txtWasser.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Wasser</span></p></body></html>", None))
        self.txtSchuko.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Schuko</span></p></body></html>", None))
        self.txtBreite.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Breite</span></p></body></html>", None))
        self.Gas_text.setItemText(0, _translate("BoaWista", "Ja", None))
        self.Gas_text.setItemText(1, _translate("BoaWista", "Nein", None))
        self.CEE_32.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">CEE 32 5p</span></p></body></html>", None))
        self.txtLaenge.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Länge</span></p></body></html>", None))
        self.txtHndelKategorie.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Händlerkategorie</span></p></body></html>", None))
        self.txtOrt.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Ort</span></p></body></html>", None))
        self.txtGas.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Gas</span></p></body></html>", None))
        self.txtAlias.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Alias</span></p></body></html>", None))
        self.txtLand.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Land</span></p></body></html>", None))
        self.pushButton.setText(_translate("BoaWista", "Speichern", None))
        self.pushButton_2.setText(_translate("BoaWista", "Abbrechen", None))

    def save(self):
        BoaWista.close()
        self.data = []

        self.data.append(self.IDKundennummer.objectName())
        self.data.append(self.kundennummer_txt.dumpObjectInfo())
        self.data.append(self.txtFirmenname.objectName())
        self.data.append(self.Firma_text.text())
        self.data.append(self.txtAlias.objectName())
        self.data.append(self.Alias_txt.text())
        self.data.append(self.txtAnschrift.objectName())
        self.data.append(self.Strasse_text.text())
        self.data.append(self.txtPLZ.objectName())
        self.data.append(self.PLZ_text.text())
        self.data.append(self.txtOrt.objectName())
        self.data.append(self.Ort_text.text())
        self.data.append(self.txtLand.objectName())
        self.data.append(self.Land_text.text())
        self.data.append(self.txtEmail.objectName())
        self.data.append(self.Email_text.text())
        self.data.append(self.txtKontaktperson.objectName())
        self.data.append(self.Kontaktperson_text.text())
        self.data.append(self.txtTelefonnummer.objectName())
        self.data.append(self.Telefonnummer_text.text())
        self.data.append(self.lngWarengruppen.objectName())
        self.data.append(self.Warengruppe_text.currentText())

        self.sub_dict = {}
        for i in range(0, len(self.data), 2):
            self.sub_dict[self.data[i]] = self.data[i + 1]  # key-value pair defined

        print('output=', self.sub_dict)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BoaWista = QtGui.QFrame()
    ui = Ui_BoaWista()
    ui.setupUi(BoaWista)
    BoaWista.show()
    sys.exit(app.exec_())

