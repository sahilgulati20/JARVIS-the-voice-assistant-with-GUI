# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActivityGUI(object):
    def setupUi(self, ActivityGUI):
        ActivityGUI.setObjectName("ActivityGUI")
        ActivityGUI.resize(1375, 886)
        self.centralwidget = QtWidgets.QWidget(ActivityGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-150, -30, 1531, 891))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../project jarvis/maxresdefault.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 291, 431))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../project jarvis/jarvis 4.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 240, 441, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../project jarvis/jarvis.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 190, 391, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../project jarvis/jarvis 3.gif"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 520, 441, 131))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../project jarvis/634aeafde3993421dbdf337d49f425dc.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(820, 240, 311, 411))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../project jarvis/jarvis 2.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(78, 255, 25);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1120, 780, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 52, 12);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 760, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border-radius: none;\n"
"colour:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1090, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"border-radius: none;\n"
"colour:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        ActivityGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActivityGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 21))
        self.menubar.setObjectName("menubar")
        ActivityGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActivityGUI)
        self.statusbar.setObjectName("statusbar")
        ActivityGUI.setStatusBar(self.statusbar)

        self.retranslateUi(ActivityGUI)
        QtCore.QMetaObject.connectSlotsByName(ActivityGUI)

    def retranslateUi(self, ActivityGUI):
        _translate = QtCore.QCoreApplication.translate
        ActivityGUI.setWindowTitle(_translate("ActivityGUI", "MainWindow"))
        self.pushButton.setText(_translate("ActivityGUI", "RUN"))
        self.pushButton_2.setText(_translate("ActivityGUI", "TERMINATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActivityGUI = QtWidgets.QMainWindow()
    ui = Ui_ActivityGUI()
    ui.setupUi(ActivityGUI)
    ActivityGUI.show()
    sys.exit(app.exec_())
