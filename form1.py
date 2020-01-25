# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets

import form2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.autoFillBackground()
        MainWindow.setStyleSheet("background-image: url(nn.jpg);")
        layout = QtWidgets.QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")






        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 80, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("IT",["ICICI","ITC","WIPRO"])
        self.comboBox.addItem("PHARMA",["CIPLA","REDDYS","SUN"])
        self.comboBox.addItem("REAL ESTATE",["INDIA HOME LOANS","INDIABULLS","LIC"])
        self.comboBox.currentIndexChanged.connect(self.indexChanged)
        layout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")

        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 190, 181, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 310, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openform2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.indexChanged(self.comboBox.currentIndex())
        layout.addWidget(self.comboBox_2)

        MainWindow.show()
    def indexChanged(self, index):
        self.comboBox_2.clear()
        data = self.comboBox.itemData(index)
        if data is not None:
            self.comboBox_2.addItems(data)
    def openform2(self):
        self.stck=self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        #self.modelcall()

        self.form2window = QtWidgets.QMainWindow()
        self.ui = form2.Ui_form2window()
        self.ui.stck=self.stck
        self.ui.setupUi(self.form2window)
        self.form2window.show()
        #self.modelcall()
        #self.ui.but.clicked.connect()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STOCK PREDICTION"))
        self.label.setText(_translate("MainWindow", "Select Sector :"))
        self.label_2.setText(_translate("MainWindow", "Select Company :"))



        self.pushButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    sys.exit(app.exec_())





