# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import SVMModel
import table
class Ui_form2window(object):
    def setupUi(self, form2window):
        #self.stck=stck
        form2window.setObjectName("form2window")
        form2window.resize(640, 480)
        form2window.autoFillBackground()
        form2window.setStyleSheet("background-image: url(nn.jpg);")
        self.centralwidget = QtWidgets.QWidget(form2window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.r1 = QtWidgets.QRadioButton(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(140, 130, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.r1.setFont(font)
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QRadioButton(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(140, 220, 381, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.r2.setFont(font)
        self.r2.setObjectName("r2")
        self.but = QtWidgets.QPushButton(self.centralwidget)
        self.but.setGeometry(QtCore.QRect(250, 350, 91, 41))
        self.but.setObjectName("but")
        form2window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form2window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        form2window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form2window)
        self.statusbar.setObjectName("statusbar")
        form2window.setStatusBar(self.statusbar)
        self.but.clicked.connect(self.onclick)

        self.retranslateUi(form2window)
        QtCore.QMetaObject.connectSlotsByName(form2window)

    def retranslateUi(self, form2window):
        _translate = QtCore.QCoreApplication.translate
        form2window.setWindowTitle(_translate("form2window", "MainWindow"))
        self.label.setText(_translate("form2window", "Select the option"))
        self.r1.setText(_translate("form2window", "Show Graph of Forecast"))
        self.r2.setText(_translate("form2window", "Show Predicted Closing Prices"))
        self.but.setText(_translate("form2window", "OK"))

    def modelcall(self):

        self.o = SVMModel.SVMModel()
        stck=self.stck+".csv"
        print(stck)
        self.o.input(stck)
        self.o.train_test()
        self.o.SVM()
        self.forcast=self.o.forecast_set
        print(self.o.forecast_set)

    def onclick(self):
        self.modelcall()
        if self.r1.isChecked():
            self.o.displayGraph()
        if self.r2.isChecked():
            self.tablewindow = QtWidgets.QMainWindow()
            self.uii = table.Ui_MainWindow()
            self.uii.forcast= self.forcast
            self.uii.setupUi(self.tablewindow)
            self.tablewindow.show()





