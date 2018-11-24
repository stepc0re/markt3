# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scroll_test.ui'
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

class Ui_ScrollArea(object):
    def setupUi(self, ScrollArea):
        ScrollArea.setObjectName(_fromUtf8("ScrollArea"))
        ScrollArea.resize(733, 393)
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 391))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(170, 0, 391, 341))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 90, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 60, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 90, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 140, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 190, 75, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 310, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 280, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_13 = QtGui.QPushButton(self.groupBox)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 280, 75, 23))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(450, 50, 75, 23))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(220, 50, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_15 = QtGui.QPushButton(self.groupBox)
        self.pushButton_15.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(180, 310, 75, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)

    def retranslateUi(self, ScrollArea):
        ScrollArea.setWindowTitle(_translate("ScrollArea", "ScrollArea", None))
        self.groupBox.setTitle(_translate("ScrollArea", "GroupBox", None))
        self.pushButton.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_2.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_3.setText(_translate("ScrollArea", "PushButton", None))
        self.label.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_4.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_5.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_6.setText(_translate("ScrollArea", "PushButton", None))
        self.label_2.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_7.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_8.setText(_translate("ScrollArea", "PushButton", None))
        self.label_3.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_9.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_10.setText(_translate("ScrollArea", "PushButton", None))
        self.label_4.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_11.setText(_translate("ScrollArea", "PushButton", None))
        self.label_5.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_13.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_14.setText(_translate("ScrollArea", "PushButton", None))
        self.label_6.setText(_translate("ScrollArea", "nahid", None))
        self.pushButton_15.setText(_translate("ScrollArea", "PushButton", None))
        self.pushButton_12.setText(_translate("ScrollArea", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScrollArea = QtGui.QScrollArea()
    ui = Ui_ScrollArea()
    ui.setupUi(ScrollArea)
    ScrollArea.show()
    sys.exit(app.exec_())

