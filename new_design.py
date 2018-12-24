# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import json

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

class Ui_BoaVista(object):
    def setupUi(self, BoaVista):
        BoaVista.setObjectName(_fromUtf8("BoaVista"))
        BoaVista.resize(676, 612)



        self.DB_Edit = QtGui.QWidget()

        self.DB_Edit.setObjectName(_fromUtf8("DB_Edit"))
        self.groupBox = QtGui.QGroupBox(self.DB_Edit)
        #self.groupBox.adjustSize()
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 381, 430))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))


        self.tableWidget = QtGui.QTableWidget(self.groupBox)

        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 401))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setHorizontalHeaderLabels(('Firma Name', 'Kntakt Person'))


        self.groupBox_2 = QtGui.QGroupBox(self.DB_Edit)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 641, 40))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        #self.groupBox_2.setSizeIncrement(200, 200)

        self.txt_search = QtGui.QLineEdit(self.groupBox_2)
       # self.txt_search.adjustSize()
        self.txt_search.setGeometry(QtCore.QRect(239, 8, 311, 24))
        self.txt_search.setObjectName(_fromUtf8("txt_search"))
        self.suche_lbl = QtGui.QLabel(self.groupBox_2)
        self.suche_lbl.setGeometry(QtCore.QRect(10, 9, 211, 20))
        self.suche_lbl.setObjectName(_fromUtf8("suche_lbl"))
        self.Search_btn = QtGui.QPushButton(self.groupBox_2)
        self.Search_btn.setGeometry(QtCore.QRect(560, 8, 71, 24))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.groupBox_3 = QtGui.QGroupBox(self.DB_Edit)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 140, 251, 430))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Edit_Daten = QtGui.QPushButton(self.groupBox_3)
        self.Edit_Daten.setGeometry(QtCore.QRect(75, 50, 100, 24))
        self.Edit_Daten.setObjectName(_fromUtf8("Edit_Daten"))
        self.Rechnung_erstellen = QtGui.QPushButton(self.groupBox_3)
        self.Rechnung_erstellen.setGeometry(QtCore.QRect(75, 130, 100, 24))
        self.Rechnung_erstellen.setObjectName(_fromUtf8("Rechnung_erstellen"))
        self.Mahnung_erstellen = QtGui.QPushButton(self.groupBox_3)
        self.Mahnung_erstellen.setGeometry(QtCore.QRect(75, 170, 100, 24))
        self.Mahnung_erstellen.setObjectName(_fromUtf8("Mahnung_erstellen"))
        self.Black_List = QtGui.QPushButton(self.groupBox_3)
        self.Black_List.setGeometry(QtCore.QRect(75, 210, 100, 24))
        self.Black_List.setObjectName(_fromUtf8("Black_List"))
        self.Email_to_All = QtGui.QPushButton(self.groupBox_3)
        self.Email_to_All.setGeometry(QtCore.QRect(75, 250, 100, 24))
        self.Email_to_All.setObjectName(_fromUtf8("Email_to_All"))
        self.Rechnung_All = QtGui.QPushButton(self.groupBox_3)
        self.Rechnung_All.setGeometry(QtCore.QRect(75, 290, 100, 24))
        self.Rechnung_All.setObjectName(_fromUtf8("Rechnung_All"))
        self.Mahnung_All = QtGui.QPushButton(self.groupBox_3)
        self.Mahnung_All.setGeometry(QtCore.QRect(75, 330, 100, 24))
        self.Mahnung_All.setObjectName(_fromUtf8("Mahnung_All"))
        self.Send_Email = QtGui.QPushButton(self.groupBox_3)
        self.Send_Email.setGeometry(QtCore.QRect(75, 90, 100, 24))
        self.Send_Email.setObjectName(_fromUtf8("Send_Email"))
        self.Markte = QtGui.QComboBox(self.DB_Edit)
        self.Markte.setGeometry(QtCore.QRect(140, 30, 81, 24))
        self.Markte.setObjectName(_fromUtf8("Markte"))
        self.Markte.addItem(_fromUtf8(""))
        self.Markte.addItem(_fromUtf8(""))
        self.Markt_Auswahl = QtGui.QLabel(self.DB_Edit)
        self.Markt_Auswahl.setGeometry(QtCore.QRect(30, 30, 101, 24))
        self.Markt_Auswahl.setObjectName(_fromUtf8("Markt_Auswahl"))
        self.Update = QtGui.QPushButton(self.DB_Edit)
        self.Update.setGeometry(QtCore.QRect(450, 30, 191, 24))
        self.Update.setObjectName(_fromUtf8("Update"))
        BoaVista.addTab(self.DB_Edit, _fromUtf8(""))
        self.Neue_Kunde = QtGui.QWidget()
        self.Neue_Kunde.setObjectName(_fromUtf8("Neue_Kunde"))
        self.dockWidget = QtGui.QDockWidget(self.Neue_Kunde)
        self.dockWidget.setGeometry(QtCore.QRect(130, 110, 120, 80))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.Test_tab2 = QtGui.QLabel(self.Neue_Kunde)
        self.Test_tab2.setGeometry(QtCore.QRect(190, 240, 71, 16))
        self.Test_tab2.setObjectName(_fromUtf8("Test_tab2"))
        BoaVista.addTab(self.Neue_Kunde, _fromUtf8(""))
        self.Statistik = QtGui.QWidget()
        self.Statistik.setObjectName(_fromUtf8("Statistik"))
        BoaVista.addTab(self.Statistik, _fromUtf8(""))
        self.neuer_Markt = QtGui.QWidget()
        self.neuer_Markt.setObjectName(_fromUtf8("neuer_Markt"))
        BoaVista.addTab(self.neuer_Markt, _fromUtf8(""))

        self.retranslateUi(BoaVista)
        BoaVista.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BoaVista)


        data, firma = self.load_data()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            newitem = QtGui.QTableWidgetItem(data[i])
            self.tableWidget.setItem(i, 1, (newitem))
            newitem = QtGui.QTableWidgetItem(firma[i])
            self.tableWidget.setItem(i, 0, (newitem))
            self.tableWidget.resizeColumnsToContents()

        #self.tableWidget.isItemSelected(QtGui.QTableWidgetItem)
    def load_data(self):
        self.data = []
        self.Firma = []

        # Extract the directory of this file...
        base_dir = os.path.dirname(os.path.realpath(__file__))
        # Concatenate the directory with the file name...
        data_file = os.path.join(base_dir, "C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json")
        # Open the file so we can read the data...
        with open(data_file, 'r') as f:
            # For each line in the file...
            d = json.load(f)
            for i, entry in enumerate(d):

                # Append to the list of data...
                # print(entry['txtKontaktperson'])
                self.data.append(entry['txtKontaktperson'])
                self.Firma.append(entry['txtFirmenname'])
            return self.data, self.Firma

    def retranslateUi(self, BoaVista):
        BoaVista.setWindowTitle(_translate("BoaVista", "Boa Vista", None))
        self.suche_lbl.setText(_translate("BoaVista", "Suche nach FirmenName or KontaktPerson", None))
        self.Search_btn.setText(_translate("BoaVista", "Suchen", None))
        self.Edit_Daten.setText(_translate("BoaVista", "Edit", None))
        self.Rechnung_erstellen.setText(_translate("BoaVista", "Rechnung", None))
        self.Mahnung_erstellen.setText(_translate("BoaVista", "Mahnung", None))
        self.Black_List.setText(_translate("BoaVista", "To Black List", None))
        self.Email_to_All.setText(_translate("BoaVista", "Email to All", None))
        self.Rechnung_All.setText(_translate("BoaVista", "Rechnung für allle", None))
        self.Mahnung_All.setText(_translate("BoaVista", "Mahnung für alle", None))
        self.Send_Email.setText(_translate("BoaVista", "Email", None))
        self.Markte.setItemText(0, _translate("BoaVista", "Markt 2018", None))
        self.Markte.setItemText(1, _translate("BoaVista", "Memmingen Markt", None))
        self.Markt_Auswahl.setText(_translate("BoaVista", "Markt auswählen", None))
        self.Update.setText(_translate("BoaVista", "DB_Update", None))
        BoaVista.setTabText(BoaVista.indexOf(self.DB_Edit), _translate("BoaVista", "DB_bearbeiten", None))
        self.Test_tab2.setText(_translate("BoaVista", "Lable", None))
        BoaVista.setTabText(BoaVista.indexOf(self.Neue_Kunde), _translate("BoaVista", "Neun Kunde anlegen", None))
        BoaVista.setTabText(BoaVista.indexOf(self.Statistik), _translate("BoaVista", "Statistische Analyse", None))
        BoaVista.setTabText(BoaVista.indexOf(self.neuer_Markt), _translate("BoaVista", "Neuen Markt anlegen", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BoaVista = QtGui.QTabWidget()
    ui = Ui_BoaVista()
    ui.setupUi(BoaVista)
    BoaVista.show()
    sys.exit(app.exec_())

