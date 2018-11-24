# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_frame_weiter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import weiter
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
        BoaWista.resize(831, 594)
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
        self.txtKontaktperson = QtGui.QLabel(BoaWista)
        self.txtKontaktperson.setGeometry(QtCore.QRect(30, 110, 111, 21))
        self.txtKontaktperson.setObjectName(_fromUtf8("txtKontaktperson"))
        self.Email_text = QtGui.QLineEdit(BoaWista)
        self.Email_text.setGeometry(QtCore.QRect(542, 70, 181, 20))
        self.Email_text.setObjectName(_fromUtf8("Email_text"))
        self.lngWarengruppen = QtGui.QLabel(BoaWista)
        self.lngWarengruppen.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.lngWarengruppen.setObjectName(_fromUtf8("lngWarengruppen"))
        self.txtEmail = QtGui.QLabel(BoaWista)
        self.txtEmail.setGeometry(QtCore.QRect(402, 70, 51, 20))
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
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
        self.txtAnschrift = QtGui.QLabel(BoaWista)
        self.txtAnschrift.setGeometry(QtCore.QRect(30, 190, 81, 21))
        self.txtAnschrift.setObjectName(_fromUtf8("txtAnschrift"))
        self.kundennummer_txt = QtGui.QLineEdit(BoaWista)
        self.kundennummer_txt.setGeometry(QtCore.QRect(542, 180, 181, 20))
        self.kundennummer_txt.setObjectName(_fromUtf8("kundennummer_txt"))
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
        self.txtHndelKategorie = QtGui.QLabel(BoaWista)
        self.txtHndelKategorie.setGeometry(QtCore.QRect(402, 220, 121, 21))
        self.txtHndelKategorie.setObjectName(_fromUtf8("txtHndelKategorie"))
        self.txtOrt = QtGui.QLabel(BoaWista)
        self.txtOrt.setGeometry(QtCore.QRect(30, 270, 51, 20))
        self.txtOrt.setObjectName(_fromUtf8("txtOrt"))
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
        self.Weiter_btn = QtGui.QPushButton(BoaWista)
        self.Weiter_btn.setGeometry(QtCore.QRect(620, 550, 75, 23))
        self.Weiter_btn.setObjectName(_fromUtf8("Weiter_btn"))
        self.Abbruch_btn = QtGui.QPushButton(BoaWista)
        self.Abbruch_btn.setGeometry(QtCore.QRect(710, 550, 75, 23))
        self.Abbruch_btn.setObjectName(_fromUtf8("Abbruch_btn"))



        self.retranslateUi(BoaWista)
        QtCore.QObject.connect(self.Weiter_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QObject.connect(self.Weiter_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), BoaWista.close)
        QtCore.QObject.connect(self.Abbruch_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), BoaWista.close)

        QtCore.QMetaObject.connectSlotsByName(BoaWista)

    def retranslateUi(self, BoaWista):
        BoaWista.setWindowTitle(_translate("BoaWista", "Frame", None))
        self.txtTelefonnummer.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Telefonnummer</span></p></body></html>", None))
        self.Haendlerkategorie_text.setItemText(0, _translate("BoaWista", "Neuekunde", None))
        self.Haendlerkategorie_text.setItemText(1, _translate("BoaWista", "Premium", None))
        self.Haendlerkategorie_text.setItemText(2, _translate("BoaWista", "Bestandskunde", None))
        self.Haendlerkategorie_text.setItemText(3, _translate("BoaWista", "Blacklist", None))
        self.txtBezeichungSpeise.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Speisen</span></p></body></html>", None))
        self.IDKundennummer.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Kundennummer</span></p></body></html>", None))
        self.Warengruppe_text.setItemText(0, _translate("BoaWista", "Speisen", None))
        self.Warengruppe_text.setItemText(1, _translate("BoaWista", "Sonstige", None))
        self.Warengruppe_text.setItemText(2, _translate("BoaWista", "Getränke", None))
        self.Warengruppe_text.setItemText(3, _translate("BoaWista", "Non-Food", None))
        self.txtKontaktperson.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Kontaktperson</span></p></body></html>", None))
        self.lngWarengruppen.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Warengruppe</span></p></body></html>", None))
        self.txtEmail.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Email</span></p></body></html>", None))
        self.txtPLZ.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">PLZ</span></p></body></html>", None))
        self.txtFirmenname.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Firma</span></p></body></html>", None))
        self.txtAnschrift.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Straße Nr.</span></p></body></html>", None))
        self.txtHndelKategorie.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Händlerkategorie</span></p></body></html>", None))
        self.txtOrt.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Ort</span></p></body></html>", None))
        self.txtAlias.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Alias</span></p></body></html>", None))
        self.txtLand.setText(_translate("BoaWista", "<html><head/><body><p><span style=\" font-size:11pt; color:#0055ff;\">Land</span></p></body></html>", None))
        self.Weiter_btn.setText(_translate("BoaWista", "Weiter", None))
        self.Abbruch_btn.setText(_translate("BoaWista", "Abbrechen", None))

    def save(self):
        #BoaWista.close()
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

        output = self.sub_dict
        #self.open_new_window()

        print('output=', self.sub_dict)

    #def open_new_window(self):
        self.window = QtGui.QFrame()
        self.ui = weiter.Ui_Frame()
        self.ui.setupUi(self.window)
        self.window.show()
        return output


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BoaWista = QtGui.QFrame()
    ui = Ui_BoaWista()
    ui.setupUi(BoaWista)
    BoaWista.show()
    sys.exit(app.exec_())
    

