# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 691, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.StartdateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.StartdateEdit.setObjectName("StartdateEdit")
        self.horizontalLayout.addWidget(self.StartdateEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.EnddateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget)
        self.EnddateEdit.setObjectName("EnddateEdit")
        self.horizontalLayout.addWidget(self.EnddateEdit)
        self.SelectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SelectButton.setObjectName("SelectButton")
        self.horizontalLayout.addWidget(self.SelectButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.AddButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        self.OrderMenu = QtWidgets.QMenu(self.menubar)
        self.OrderMenu.setObjectName("OrderMenu")
        self.CustomMenu = QtWidgets.QMenu(self.menubar)
        self.CustomMenu.setObjectName("CustomMenu")
        self.AboutMenu = QtWidgets.QMenu(self.menubar)
        self.AboutMenu.setObjectName("AboutMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.OrderMenu.menuAction())
        self.menubar.addAction(self.CustomMenu.menuAction())
        self.menubar.addAction(self.AboutMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MrWang"))
        self.label.setText(_translate("MainWindow", "开始时间："))
        self.label_2.setText(_translate("MainWindow", "结束时间："))
        self.SelectButton.setText(_translate("MainWindow", "查询"))
        self.AddButton.setText(_translate("MainWindow", "添加订单"))
        self.OrderMenu.setTitle(_translate("MainWindow", "订单"))
        self.CustomMenu.setTitle(_translate("MainWindow", "客户管理"))
        self.AboutMenu.setTitle(_translate("MainWindow", "关于"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

