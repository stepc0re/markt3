import sys
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
import PyQt4

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from new_frame_weiter import Ui_BoaWista
import os
import json

import StephansMongoFunctions


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class App(QtGui.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'BoaVista'
        self.left = 0
        self.top = 0
        self.width = 676
        self.height = 612
        self.resize(800, 680)
        self.setWindowTitle(self.title)

        #self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def onResize(event):
        print(event)

class MyTableWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(QtGui.QWidget, self).__init__(parent)
        self.layout = QtGui.QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QtGui.QTabWidget()


        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        # self.tabs.resize(900, 700)
        # self.tabs. tabBar().hide()
        self.tab1.setStyleSheet("font :11px;")
        # Add tabs
        self.tabs.addTab(self.tab1, "DB_Edit")
        self.tabs.addTab(self.tab2, "Neuen Kunde anlegen")
        self.tabs.addTab(self.tab3, "neue")
        self.tabs.addTab(self.tab4, "Statistic")
        #self.tabs.addTab(self.tab5, "Edit")

        self.tabs.removeTab(2)
        #self.tabs.removeTab(4)



        # self.tabs.insertTab(3, self.tabs, "Stat")

        # tab2 einrichten
        self.tab2_layout = QtGui.QGridLayout()

        self.Firma_led = QtGui.QLineEdit()
        self.Firma_led.setStyleSheet("font: 14px;")
        self.Firma_lbl = QtGui.QLabel()
        self.Firma_lbl.setText("Firma")
        self.Firma_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Kontaktperson_led = QtGui.QLineEdit()
        self.Kontaktperson_led.setStyleSheet("font: 14px;")
        self.Kontaktperson_lbl = QtGui.QLabel()
        self.Kontaktperson_lbl.setText("KontaktPerson")
        self.Kontaktperson_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Alias_led = QtGui.QLineEdit()
        self.Alias_led.setStyleSheet("font: 14px;")
        self.Alias_lbl = QtGui.QLabel()
        self.Alias_lbl.setText("Alias")
        self.Alias_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Strasse_led = QtGui.QLineEdit()
        self.Strasse_led.setStyleSheet("font: 14px;")
        self.Strasse_lbl = QtGui.QLabel()
        self.Strasse_lbl.setText("Straße Nr.")
        self.Strasse_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.PLZ_led = QtGui.QLineEdit()
        self.PLZ_led.setStyleSheet("font: 14px;")
        self.PLZ_lbl = QtGui.QLabel()
        self.PLZ_lbl.setText("PLZ")
        self.PLZ_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Ort_led = QtGui.QLineEdit()
        self.Ort_led.setStyleSheet("font: 14px;")
        self.Ort_lbl = QtGui.QLabel()
        self.Ort_lbl.setText("Ort")
        self.Ort_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Land_led = QtGui.QLineEdit()
        self.Land_led.setStyleSheet("font: 14px;")
        self.Land_lbl = QtGui.QLabel()
        self.Land_lbl.setText("Land")
        self.Land_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Warengruppen_lbl = QtGui.QLabel()
        self.Warengruppen_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Warengruppen_lbl.setText("WarenGruppe")
        self.Warengruppe_CB = QtGui.QComboBox()
        self.Warengruppe_CB.setStyleSheet("font-size:12pt")
        self.Warengruppe_CB.addItem(_fromUtf8("1"))
        self.Warengruppe_CB.addItem(_fromUtf8("2"))
        self.Warengruppe_CB.addItem(_fromUtf8("3"))
        self.Warengruppe_CB.addItem(_fromUtf8("4"))

        self.Email_lbl = QtGui.QLabel()
        self.Email_lbl.setText("Email")
        self.Email_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Email_led = QtGui.QLineEdit()
        self.Email_led.setStyleSheet("font: 14px;")

        self.Telefonnummer_led = QtGui.QLineEdit()
        self.Telefonnummer_led.setStyleSheet("font: 14px;")
        self.Telefonnummer_lbl = QtGui.QLabel()
        self.Telefonnummer_lbl.setText("TelefonNummer")
        self.Telefonnummer_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.Kundennnummer_led = QtGui.QLineEdit()
        self.Kundennnummer_led.setStyleSheet("font: 14px;")
        self.Kundennnummer_lbl = QtGui.QLabel()
        self.Kundennnummer_lbl.setText("KundennNummer")
        self.Kundennnummer_lbl.setStyleSheet("font-size:11pt; color:#0055ff")

        self.HndelKategorie_lbl = QtGui.QLabel()
        self.HndelKategorie_lbl.setText("HändelKategorie")
        self.HndelKategorie_lbl.setStyleSheet("font-size:12pt; color:#0055ff")
        self.Haendlerkategorie_CB = QtGui.QComboBox()
        self.Haendlerkategorie_CB.setStyleSheet("font-size:11pt")
        self.Haendlerkategorie_CB.addItem(_fromUtf8("1"))
        self.Haendlerkategorie_CB.addItem(_fromUtf8("2"))
        self.Haendlerkategorie_CB.addItem(_fromUtf8("3"))
        self.Haendlerkategorie_CB.addItem(_fromUtf8("4"))

        self.BezeichungSpeise_lbl = QtGui.QLabel()
        self.BezeichungSpeise_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.BezeichungSpeise_lbl.setText("Speise")
        self.BezeichungSpeise_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Speise_led = QtGui.QLineEdit()
        self.Speise_led.setStyleSheet("font: 16px;")
        self.ignor_lbl = QtGui.QLabel()
        self.ignor_lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.Weiter_btn = QtGui.QPushButton()
        self.Weiter_btn.setStyleSheet("font-size:11pt;")
        self.Weiter_btn.setText("Weiter")
        self.Abbruch_btn = QtGui.QPushButton()
        self.Abbruch_btn.setStyleSheet("font-size:11pt;")
        self.Abbruch_btn.setText("Abbrechen")
        self.back_btn = QtGui.QPushButton()
        self.back_btn.setStyleSheet("font-size:11pt;")
        self.back_btn.setText("zurück")


        self.tab2_layout.setHorizontalSpacing(40)
        self.tab2_layout.setContentsMargins(80, 80, 80, 80)
        self.tab2_layout.setVerticalSpacing(30)
        self.tab2_layout.setColumnStretch(500, 500)

        self.tab2_layout.addWidget(self.Firma_lbl, 0, 0)
        self.tab2_layout.addWidget(self.Firma_led, 0, 1, 1, 6)
        self.tab2_layout.addWidget(self.Kontaktperson_lbl, 1, 0)
        self.tab2_layout.addWidget(self.Kontaktperson_led, 1, 1, 1, 6)
        self.tab2_layout.addWidget(self.Alias_lbl, 2, 0)
        self.tab2_layout.addWidget(self.Alias_led, 2, 1, 1, 6)
        self.tab2_layout.addWidget(self.Strasse_lbl, 3, 0)
        self.tab2_layout.addWidget(self.Strasse_led, 3, 1, 1, 6)
        self.tab2_layout.addWidget(self.PLZ_lbl, 4, 0)
        self.tab2_layout.addWidget(self.PLZ_led, 4, 1, 1, 6)
        self.tab2_layout.addWidget(self.Ort_lbl, 5, 0)
        self.tab2_layout.addWidget(self.Ort_led, 5, 1, 1, 6)
        self.tab2_layout.addWidget(self.Land_lbl, 6, 0)
        self.tab2_layout.addWidget(self.Land_led, 6, 1, 1, 6)
        self.tab2_layout.addWidget(self.Warengruppen_lbl, 7, 0)
        self.tab2_layout.addWidget(self.Warengruppe_CB, 7, 1, 1, 6)

        self.tab2_layout.addWidget(self.Email_lbl, 0, 9)
        self.tab2_layout.addWidget(self.Email_led, 0, 10, 1, 6)
        self.tab2_layout.addWidget(self.Telefonnummer_lbl, 1, 9)
        self.tab2_layout.addWidget(self.Telefonnummer_led, 1, 10, 1, 6)
        self.tab2_layout.addWidget(self.ignor_lbl, 2, 9)
        self.tab2_layout.addWidget(self.Kundennnummer_lbl, 3, 9)
        self.tab2_layout.addWidget(self.Kundennnummer_led, 3, 10, 1, 6)
        self.tab2_layout.addWidget(self.ignor_lbl, 3, 7)

        self.tab2_layout.addWidget(self.HndelKategorie_lbl, 4, 9)
        self.tab2_layout.addWidget(self.Haendlerkategorie_CB, 4, 10, 1, 6)
        self.tab2_layout.addWidget(self.BezeichungSpeise_lbl, 8, 0)
        self.tab2_layout.addWidget(self.Speise_led, 8, 1, 1, 16)
        self.tab2_layout.addWidget(self.Weiter_btn, 20, 20, 1, 3)
        self.tab2_layout.addWidget(self.Abbruch_btn, 20, 18, 1, 3)
        self.tab2_layout.addWidget(self.back_btn, 20, 16, 1, 3)

        self.tab2.setLayout(self.tab2_layout)

        # tab3 einrichten

        self.tab3_layout = QtGui.QGridLayout()

        self.Type_lbl = QtGui.QLabel()
        self.Type_lbl.setText("Type")
        self.Type_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Type_cb = QtGui.QComboBox()
        self.Type_cb.addItem(_fromUtf8(""))
        self.Type_cb.addItem(_fromUtf8(""))
        self.Type_cb.addItem(_fromUtf8(""))

        self.Laenge_lbl = QtGui.QLabel()
        self.Laenge_lbl.setText("Länge")
        self.Laenge_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Laenge_led = QtGui.QLineEdit()

        self.Breite_lbl = QtGui.QLabel()
        self.Breite_lbl.setText("Bereite")
        self.Breite_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Breite_led = QtGui.QLineEdit()

        self.Hoehe_lbl = QtGui.QLabel()
        self.Hoehe_lbl.setText("Höhe")
        self.Hoehe_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Hoehe_led = QtGui.QLineEdit()

        self.Groesse_lbl = QtGui.QLabel()
        self.Groesse_lbl.setText("Größe")
        self.Groesse_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Groesse_led = QtGui.QLineEdit()

        self.Strom_lbl = QtGui.QLabel()
        self.Strom_lbl.setText("Strom")
        self.Strom_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Strom_cb = QtGui.QComboBox()
        self.Strom_cb.addItem(_fromUtf8("Ja"))
        self.Strom_cb.addItem(_fromUtf8("Nein"))

        self.Wasser_lbl = QtGui.QLabel()
        self.Wasser_lbl.setText("Wasser")
        self.Wasser_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Wasser_cb = QtGui.QComboBox()
        self.Wasser_cb.addItem(_fromUtf8("Ja"))
        self.Wasser_cb.addItem(_fromUtf8("Nein"))

        self.Gas_lbl = QtGui.QLabel()
        self.Gas_lbl.setText("Gas")
        self.Gas_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Gas_cb = QtGui.QComboBox()
        self.Gas_cb.addItem(_fromUtf8("Ja"))
        self.Gas_cb.addItem(_fromUtf8("Nein"))

        self.Schuko_lbl = QtGui.QLabel()
        self.Schuko_lbl.setText("Schuko")
        self.Schuko_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Schuko_led = QtGui.QLineEdit()

        self.CEE_16_lbl = QtGui.QLabel()
        self.CEE_16_lbl.setText("CEE 16")
        self.CEE_16_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.CEE_16_led = QtGui.QLineEdit()

        self.CEE_32_lbl = QtGui.QLabel()
        self.CEE_32_lbl.setText("CEE 32")
        self.CEE_32_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.CEE_32_led = QtGui.QLineEdit()

        self.Gesamtleistung_lbl = QtGui.QLabel()
        self.Gesamtleistung_lbl.setText("Gesamtleistung(KW)")
        self.Gesamtleistung_lbl.setStyleSheet("font-size:11pt; color:#0055ff")
        self.Gesamtleistung_led = QtGui.QLineEdit()

        self.abbrechen_btn = QtGui.QPushButton()
        self.abbrechen_btn.setText("Abbrechen")
        self.abbrechen_btn.setStyleSheet("font-size:11pt;")
        self.zurueck_btn = QtGui.QPushButton()
        self.zurueck_btn.setText("Zurück")
        self.zurueck_btn.setStyleSheet("font-size:11pt;")
        self.save_btn = QtGui.QPushButton()
        self.save_btn.setStyleSheet("font-size:11pt;")
        self.save_btn.setText("Speichern")

        self.tab3_layout.setHorizontalSpacing(40)
        self.tab3_layout.setContentsMargins(80, 80, 80, 80)
        self.tab3_layout.setVerticalSpacing(30)
        self.tab3_layout.setColumnStretch(500, 500)

        self.tab3_layout.addWidget(self.Type_lbl, 0, 0)
        self.tab3_layout.addWidget(self.Type_cb, 0, 1, 1, 6)
        self.tab3_layout.addWidget(self.Laenge_lbl, 1, 0)
        self.tab3_layout.addWidget(self.Laenge_led, 1, 1, 1, 6)
        self.tab3_layout.addWidget(self.Breite_lbl, 2, 0)
        self.tab3_layout.addWidget(self.Breite_led, 2, 1, 1, 6)
        self.tab3_layout.addWidget(self.Hoehe_lbl, 3, 0)
        self.tab3_layout.addWidget(self.Hoehe_led, 3, 1, 1, 6)
        self.tab3_layout.addWidget(self.Groesse_lbl, 4, 0)
        self.tab3_layout.addWidget(self.Groesse_led, 4, 1, 1, 6)

        self.tab3_layout.addWidget(self.Gas_lbl, 6, 0)
        self.tab3_layout.addWidget(self.Gas_cb, 6, 1, 1, 6)

        self.tab3_layout.addWidget(self.Strom_lbl, 0, 9)
        self.tab3_layout.addWidget(self.Strom_cb, 0, 10, 1, 6)
        self.tab3_layout.addWidget(self.Schuko_lbl, 1, 9)
        self.tab3_layout.addWidget(self.Schuko_led, 1, 10, 1, 6)
        self.tab3_layout.addWidget(self.CEE_16_lbl, 2, 9)
        self.tab3_layout.addWidget(self.CEE_16_led, 2, 10, 1, 6)
        self.tab3_layout.addWidget(self.CEE_32_lbl, 3, 9)
        self.tab3_layout.addWidget(self.CEE_32_led, 3, 10, 1, 6)
        self.tab3_layout.addWidget(self.Gesamtleistung_lbl, 4, 9)
        self.tab3_layout.addWidget(self.Gesamtleistung_led, 4, 10, 1, 6)

        self.tab3_layout.addWidget(self.ignor_lbl, 0, 7)
        self.tab3_layout.addWidget(self.Wasser_lbl, 6, 9)
        self.tab3_layout.addWidget(self.Wasser_cb, 6, 10, 1, 6)
        
        self.tab3_layout.addWidget(self.zurueck_btn, 20, 20, 1, 3)
        self.tab3_layout.addWidget(self.abbrechen_btn, 20, 18, 1, 3)
        self.tab3_layout.addWidget(self.save_btn, 20, 22, 1, 3)

        self.tab3.setLayout(self.tab3_layout)

        # Groupbox1 einrichten
        # Create first tab1
        self.tab1.layout = QVBoxLayout(self)

        self.Update_btn = QtGui.QPushButton("Update DB")
        self.Update_btn.setStyleSheet("font: 14px;")
        self.Update_btn.setMinimumWidth(200)
        self.markt_wahl = QtGui.QPushButton("Markt auswählen")
        self.markt_wahl.setMinimumWidth(200)
        self.markt_wahl.setStyleSheet("font: 14px;")
        self.groupbox1 = QtGui.QGroupBox()
        self.groupbox1.setStyleSheet("border-color: (0, 0, 0)")
        self.groupbox1.setMaximumHeight(50)
        self.groupbox1.setMaximumWidth(900)
        self.groupbox1.setSizeIncrement(30, 30)
        groupbox1_layout = QtGui.QHBoxLayout(self.groupbox1)
        groupbox1_layout.setAlignment(Qt.AlignLeft)
        groupbox1_layout.addWidget(self.Update_btn)
        groupbox1_layout.addWidget(self.markt_wahl)

        # Groupbox2
        self.groupbox2 = QtGui.QGroupBox()
        self.groupbox2.setMaximumHeight(50)
        self.groupbox2.setMaximumWidth(900)
        self.lbl_search = QtGui.QLabel("search FirmenName: ")
        self.lbl_search.setStyleSheet("font: 13px;")

        kunden_nummer, data, firma = self.load_data_from_mongodb()

        self.test_search = QtGui.QLineEdit()
        self.completer = QtGui.QCompleter(firma)
        self.completer.dumpObjectInfo()
        self.test_search.setCompleter(self.completer)

        self.btn_search = QtGui.QPushButton()
        self.btn_search.setText("Search")
        self.btn_search.setStyleSheet("font: 14px;")
        self.btn_search.setMaximumWidth(100)
        groupbox2_layout = QtGui.QHBoxLayout(self.groupbox2)
        groupbox2_layout.addWidget(self.lbl_search)
        groupbox2_layout.addWidget(self.test_search)
        groupbox2_layout.addWidget(self.btn_search)

        # Groubox3
        self.groupbox3 = QtGui.QGroupBox()
        self.groupbox3.setMinimumWidth(400)
        self.groupbox3.setMaximumWidth(900)
        self.tableWidget = QtGui.QTableWidget()
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setStyleSheet("background-color: rgb(224, 224, 200);"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-radius: 15px;"
                                       "border-color: beige;"
                                       "font: 16px;"
                                       "min-width: 1em;"
                                       "padding: 2px;")

        # self.tableWidget.cellClicked.connect(self.tabSelected)
        # items = self.tableWidget.findItems(self.test_search.text(), QtCore.Qt.MatchContains)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(('Firma Name ', 'Kontakt Person'))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.tableWidget.doubleClicked.connect(self.cell_double_clicked)
        groupbox3_layout = QtGui.QHBoxLayout(self.groupbox3)
        groupbox3_layout.addWidget(self.tableWidget)

        # Groupbox4 einrichten
        self.groupbox4 = QtGui.QGroupBox()
        self.groupbox4.setMinimumWidth(200)
        self.groupbox4.setMaximumWidth(640)
        self.groupbox4.setObjectName('groupbox4')
        self.btn_Edit = QtGui.QPushButton()
        self.btn_Edit.setObjectName("EDIT")
        self.btn_Edit.setText("Edit")
        self.btn_Edit.setStyleSheet("background-color: rgb(224, 224, 200);"
                               "border-style: outset;"
                               "border-width: 2px;"
                               "border-radius: 10px;"
                               "border-color: beige;"
                               "font: 16px;"
                               "min-width: 10em;"
                               "padding: 6px;")

        btn_email = QtGui.QPushButton()
        btn_email.setObjectName("email")
        btn_email.setMinimumWidth(200)
        btn_email.setText("Send Email")
        btn_email.setStyleSheet("background-color: rgb(224, 224, 200);"
                                "border-style: outset;"
                                "border-width: 2px;"
                                "border-radius: 10px;"
                                "border-color: beige;"
                                "font: 16px;"
                                "min-width: 10em;"
                                "padding: 6px;")

        btn_rechnung = QtGui.QPushButton()
        btn_rechnung.setText("Rechnung erstellen")
        btn_rechnung.setStyleSheet("background-color: rgb(224, 224, 200);"
                                   "border-style: outset;"
                                   "border-width: 2px;"
                                   "border-radius: 10px;"
                                   "border-color: beige;"
                                   "font: 16px;"
                                   "min-width: 10em;"
                                   "padding: 6px;")

        btn_mahnung = QtGui.QPushButton()
        btn_mahnung.setText("Mahnung erstellen")
        btn_mahnung.setStyleSheet("background-color: rgb(224, 224, 200);"
                                  "border-style: outset;"
                                  "border-width: 2px;"
                                  "border-radius: 10px;"
                                  "border-color: beige;"
                                  "font: 16px;"
                                  "min-width: 10em;"
                                  "padding: 6px;")

        btn_blackList = QtGui.QPushButton()
        btn_blackList.setText("to Black List")
        btn_blackList.setStyleSheet("background-color: rgb(224, 224, 200);"
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    "font: 16px;"
                                    "min-width: 10em;"
                                    "padding: 6px;")

        groupbox4_layout = QtGui.QVBoxLayout(self.groupbox4)
        groupbox4_layout.setSpacing(30)
        groupbox4_layout.setAlignment(Qt.AlignCenter)
        groupbox4_layout.addWidget(self.btn_Edit)
        groupbox4_layout.addWidget(btn_email)
        groupbox4_layout.addWidget(btn_rechnung)
        groupbox4_layout.addWidget(btn_mahnung)
        groupbox4_layout.addWidget(btn_blackList)

        self.gridLayout = QHBoxLayout(self)

        self.tab1.layout.addWidget(self.groupbox1)
        self.tab1.layout.addWidget(self.groupbox2)
        self.gridLayout.addWidget(self.groupbox3)
        self.gridLayout.addWidget(self.groupbox4)

        self.tab1.layout.addLayout(self.gridLayout)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            newitem = QtGui.QTableWidgetItem(kunden_nummer[i])
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # make cell not editable
            self.tableWidget.setItem(i, 0, newitem)
            newitem = QtGui.QTableWidgetItem(data[i])
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # make cell not editable
            self.tableWidget.setItem(i, 1, newitem)
            newitem = QtGui.QTableWidgetItem(firma[i])
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # make cell not editable
            self.tableWidget.setItem(i, 0, newitem)
            self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortItems(0)

        self.btn_Edit.clicked.connect(self.tab_edit)
        # self.btn_search.clicked.connect(self.search)
        self.test_search.textChanged.connect(self.search)

        self.Weiter_btn.clicked.connect(self.next_page_neuen_kunde)

        self.save_btn.clicked.connect(self.save_to_DB)
        self.zurueck_btn.clicked.connect(self.back_to_page)
        self.abbrechen_btn.clicked.connect(self.cancel)
        self.Abbruch_btn.clicked.connect(self.cancel)
        self.back_btn.clicked.connect(self.back_to_first_page)

    def save_to_DB(self):
        print(1)

    def back_to_first_page(self):
        self.tabs.setCurrentIndex(0)

    def next_page_edit(self):

        self.tabs.removeTab(1)
        self.tabs.insertTab(1, self.tab3, "Edit")
        self.tabs.setCurrentIndex(1)

    def cancel(self):
        self.tabs.setCurrentIndex(0)
        self.tabs.insertTab(1, self.tab2, "neuen Kunden anlegen")
        self.Firma_led.clear()
        self.Kontaktperson_led.clear()
        self.Alias_led.clear()
        self.Strasse_led.clear()
        self.Ort_led.clear()
        self.Land_led.clear()
        self.Email_led.clear()
        self.Telefonnummer_led.clear()
        self.Kundennnummer_led.clear()
        self.Speise_led.clear()
        self.PLZ_led.clear()
        self.Warengruppe_CB.setCurrentIndex(0)
        self.Haendlerkategorie_CB.setCurrentIndex(0)
        self.tabs.removeTab(3)

    def back_to_page(self):
        self.tabs.removeTab(1)
        self.tabs.insertTab(1, self.tab2, "Edit")
        self.tabs.setCurrentIndex(1)

    def next_page_neuen_kunde(self):
        self.tabs.removeTab(1)
        self.tabs.insertTab(1, self.tab3, "neuen Kunden anlegen")
        self.tabs.setCurrentIndex(1)

    def tab_edit(self):

        self.Weiter_btn.clicked.connect(self.next_page_edit)
        self.tabs.insertTab(1, self.tab2, "Edit")
        self.tabs.setCurrentIndex(1)

    def search(self):
        such_text = self.test_search.text()
        # print("such =", such_person)
        print(such_text)
        items = self.tableWidget.findItems(such_text,  QtCore.Qt.MatchRegExp)

        for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 0)
                if item not in items:
                    self.tableWidget.removeRow(row)



        #brush = QtGui.QBrush(QtGui.QColor("green"))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        # for i, item in enumerate(items):
        #
        #     index = self.tableWidget.indexFromItem(item)
        #     print(index)

            #item.setForeground(brush)
        # for i in range(170):
        #     if self.tableWidget.item(i, 0).text() == such_person:
        #         self.tableWidget.selectRow(i)


    def tabSelected(self, arg=None):

            self.window = QtGui.QFrame()
            self.ui = Ui_BoaWista()
            self.ui.setupUi(self.window)
            self.window.show()

    def cell_was_clicked(self, row, col):

        person = (self.tableWidget.item(row, col + 1)).text()
        data_file = os.path.join("C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json")
        # self.window = QtGui.QFrame()
        # self.ui = Ui_BoaWista()
        # self.ui.setupUi(self.window)
        # self.window.show()
        with open(data_file, 'r') as f:
            # For each line in the file...
            d = json.load(f)

        # for i in range(len(d)):
        #
        #     if d[i]["txtKontaktperson"] == person:
        #
        #         self.ui.Telefonnummer_text.setText(d[i]["txtEmail"])
        #

        for i in range(len(d)):
            if d[i]["txtKontaktperson"] == person:
                self.Firma_led.setText(d[i]["txtFirmenname"])
                self.Kontaktperson_led.setText(d[i]["txtKontaktperson"])
                self.Alias_led.setText(d[i]["txtAlias"])
                self.Strasse_led.setText(d[i]["txtAnschrift"])
                self.PLZ_led.setText(d[i]["txtPLZ"])
                self.Ort_led.setText(d[i]["txtOrt"])
                self.Land_led.setText(d[i]["txtLand"])
                self.Email_led.setText(d[i]["txtEmail"])
                self.Telefonnummer_led.setText(d[i]["txtTelefonnummer"])
                self.Kundennnummer_led.setText(str(d[i]["IDKundennummer"]))
                self.Speise_led.setText(d[i]["txtBezeichungSpeise"])
                # print("hier", d[i]["lngH\\u00e4ndlergruppe"])
                for id in range(5):
                    if d[i]["lngWarengruppen"] == id:
                        self.Warengruppe_CB.setCurrentIndex(id)
                    if d[i]["lngH\u00e4ndlergruppe"] == id:
                        self.Haendlerkategorie_CB.setCurrentIndex(id)

    def cell_double_clicked(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            selected_row_text = currentQTableWidgetItem.text()

        self.Weiter_btn.clicked.connect(self.next_page_edit)
        data_file = os.path.join("C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json")
        with open(data_file, 'r') as f:
            d = json.load(f)
        self.tabs.insertTab(1, self.tab2, "Edit")
        self.tabs.setCurrentIndex(1)

        for i in range(len(d)):
            if d[i]["txtKontaktperson"] == selected_row_text:
                self.Firma_led.setText(d[i]["txtFirmenname"])
                self.Kontaktperson_led.setText(d[i]["txtKontaktperson"])
                self.Alias_led.setText(d[i]["txtAlias"])
                self.Strasse_led.setText(d[i]["txtAnschrift"])
                self.PLZ_led.setText(d[i]["txtPLZ"])
                self.Ort_led.setText(d[i]["txtOrt"])
                self.Land_led.setText(d[i]["txtLand"])
                self.Email_led.setText(d[i]["txtEmail"])
                self.Telefonnummer_led.setText(d[i]["txtTelefonnummer"])
                self.Kundennnummer_led.setText(str(d[i]["IDKundennummer"]))
                self.Speise_led.setText(d[i]["txtBezeichungSpeise"])
                # print("hier", d[i]["lngH\\u00e4ndlergruppe"])
                for id in range(5):
                    if d[i]["lngWarengruppen"] == id:
                        self.Warengruppe_CB.setCurrentIndex(id)
                    if d[i]["lngH\u00e4ndlergruppe"] == id:
                        self.Haendlerkategorie_CB.setCurrentIndex(id)

    def load_data_from_file(self):
        self.data = []
        self.Firma = []
        self.id = []

        # Extract the directory of this file...
        base_dir = os.path.dirname(os.path.realpath(__file__))
        # Concatenate the directory with the file name...
        data_file = os.path.join(base_dir, "C:\\Users\\Stephan\\Google Drive\\BoaVista\\json_file.json")
        # Open the file so we can read the data...
        with open(data_file, 'r') as f:
            # For each line in the file...
            print(f)
            d = json.load(f)
            for i, entry in enumerate(d):
                # Append to the list of data...
                # print(entry['txtKontaktperson'])
                self.data.append(entry['txtKontaktperson'])
                self.Firma.append(entry['txtFirmenname'])
                self.id.append(entry['IDKundennummer'])
            return self.id, self.data, self.Firma

    def load_data_from_mongodb(self):
        self.data = []
        self.Firma = []
        self.id = []

        mongodata = StephansMongoFunctions.loadmongotojson("test", "Kunden1")
        #print(mongodata)
        #d = json.(mongodata)
        for i, entry in enumerate(mongodata):
            # Append to the list of data...
            # print(entry['txtKontaktperson'])
            self.data.append(entry['txtKontaktperson'])
            self.Firma.append(entry['txtFirmenname'])
            self.id.append(entry['IDKundennummer'])
        return self.id, self.data, self.Firma


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
