# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/star/PycharmProjects/datascience/ara.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.setWindowModality(QtCore.Qt.ApplicationModal)
        Home.resize(762, 660)
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 40, 641, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.content = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.content.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.content.setObjectName("content")
        self.gridLayout.addWidget(self.content, 0, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 270, 141, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.read = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.read.setObjectName("read")
        self.gridLayout_2.addWidget(self.read, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(380, 270, 160, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.save = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setObjectName("save")
        self.gridLayout_3.addWidget(self.save, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 5, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 600, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(100, 600, 651, 16))
        self.status.setText("")
        self.status.setObjectName("status")
        Home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(Home)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Home)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent = QtWidgets.QAction(Home)
        self.actionRecent.setObjectName("actionRecent")
        self.actionCut = QtWidgets.QAction(Home)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(Home)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(Home)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind = QtWidgets.QAction(Home)
        self.actionFind.setObjectName("actionFind")
        self.actionSelect = QtWidgets.QAction(Home)
        self.actionSelect.setObjectName("actionSelect")
        self.actionSelect_All = QtWidgets.QAction(Home)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRecent)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionSelect)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Arabic TTS Synthesizer"))
        self.read.setText(_translate("Home", "Read"))
        self.save.setText(_translate("Home", "Save"))
        self.label.setText(_translate("Home", "ARABIC TEXT TO SPEECH SYNTHESIS"))
        self.label_2.setText(_translate("Home", "Status:"))
        self.menuFile.setTitle(_translate("Home", "File"))
        self.menuEdit.setTitle(_translate("Home", "Edit"))
        self.menuHelp.setTitle(_translate("Home", "Help"))
        self.actionNew.setText(_translate("Home", "New"))
        self.actionOpen.setText(_translate("Home", "Open"))
        self.actionRecent.setText(_translate("Home", "Recent"))
        self.actionCut.setText(_translate("Home", "Cut"))
        self.actionCopy.setText(_translate("Home", "Copy"))
        self.actionPaste.setText(_translate("Home", "Paste"))
        self.actionFind.setText(_translate("Home", "Find"))
        self.actionSelect.setText(_translate("Home", "Select"))
        self.actionSelect_All.setText(_translate("Home", "Select All"))