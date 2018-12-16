import sys
from PyQt4.QtGui import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
                         QGridLayout)
from PyQt4.QtCore import (Qt)

class AddressBook(QWidget): # subclass QWidget

    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)   # initialise the base class

        # create input labels and fields
        nameLabel = QLabel(self.tr("Name:"))
        nameLine = QLineEdit(self)

        addrLabel = QLabel(self.tr("Address:"))
        addrText = QTextEdit(self)

        # create and populate layout
        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLine, 0, 1)
        mainLayout.addWidget(addrLabel, 1, 0, Qt.AlignTop)
        mainLayout.addWidget(addrText, 1, 1)

        # set this objects layout and window title
        self.setLayout(mainLayout)
        self.setWindowTitle(self.tr("Simple Address Book"))


def main():
    app = QApplication(sys.argv)    # required for all GUI applications

    ab = AddressBook()
    ab.show()                       # make me visible

    sys.exit(app.exec_())           # start main event thread

if __name__ == '__main__':
    main()