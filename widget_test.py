
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import os
import json



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
        self.resize(window_width, window_height)

        self.initUI()

    def load_data(self):
        self.data = []
        self.Firma = []

        # Extract the directory of this file...
        base_dir = os.path.dirname(os.path.realpath(__file__))
        # Concatenate the directory with the file name...
        data_file = os.path.join(base_dir, "C:\\Users\\Steph\\Desktop\\BoaVista\\json_file.json")
        # Open the file so we can read the data...
        with open(data_file, 'r') as f:
            # For each line in the file...
            d = json.load(f)
            for i, entry in enumerate(d):
                # Append to the list of data...
                #print(entry['txtKontaktperson'])
                self.data.append(entry['txtKontaktperson'])
                self.Firma.append(entry['txtFirmenname'])
            return self.data, self.Firma

    def creatgroup_new(self):

        groupbox = QGroupBox("", self)
        groupbox.setGeometry(10, 10, 120, 60)
        filter = QHBoxLayout(groupbox)
        lbl_search = QLabel(text="search: ")
        self.txt_filter = QLineEdit()
        btn_search = QPushButton()
        btn_search.setText("Search")
        # Add the created widgets to the layout
        filter.addWidget(lbl_search)
        filter.addWidget(self.txt_filter)
        filter.addWidget(btn_search)

        groupbox.layout().addLayout(filter)
        return groupbox

    def createLayout_group(self, number):
        sgroupbox = QGroupBox("Kunden_List:".format(number), self)
        sgroupbox.setGeometry(10, 150, 1200, 600)

        layout_groupbox = QVBoxLayout(sgroupbox)
        layout_groupbox.totalSizeHint()
        data, Firma = self.load_data()
        for i in (range(len(data))):
            row = QtGui.QHBoxLayout()

            rechnung_btn = QPushButton()
            rechnung_btn.setText('Rechnung erstellen')
            rechnung_btn.setChecked(True)

            self.space = QLineEdit()
            self.space.setFixedSize(400, 20)
            self.space.setStyleSheet("border: 0px; background-color:Light Steel Blue;")


            self.Kontaktperson = QCheckBox()
            self.Kontaktperson.setText(Firma[i])
            self.Kontaktperson.setFixedSize(200, 20)
            row.addWidget(self.Kontaktperson)

            self.FirmenName = QPushButton()
            self.FirmenName.setFixedSize(200, 20)
            self.FirmenName.setText(data[i])
            row.addWidget(self.FirmenName)

            row.addWidget(self.space)
            row.setSpacing(100)
            row.addWidget(rechnung_btn)
            row.setSpacing(20)
            row.addWidget(QtGui.QPushButton('Mahnung erstellen'))
            row.addWidget(QtGui.QPushButton('Email'))
            row.addWidget(QtGui.QPushButton('To Black-List'))
            sgroupbox.layout().addLayout(row)

        layout_groupbox.addStretch(1)


        return sgroupbox

    def createLayout_Container(self):
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedWidth(1170)
        self.scrollarea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollarea.setWidget(widget)
        self.layout_SArea = QVBoxLayout(widget)
        self.layout_SArea.addWidget(self.creatgroup_new())

        for i in range(1):
            self.layout_SArea.addWidget(self.createLayout_group(i))
        self.layout_SArea.addStretch(1)

    def initUI(self):
        self.createLayout_Container()
        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.scrollarea)

        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())