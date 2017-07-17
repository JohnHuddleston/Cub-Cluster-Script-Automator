#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstDraftGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.param1 = 0
        self.param2 = 0
        self.param3 = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(800, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 40, 121, 31))
        self.label.setObjectName("label")

        ########################
        ### Project Selector ###
        #############################################

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 40, 103, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self._changeStackPage)

        #############################################



        #############################
        ### Project Parameter Box ###
        #############################################

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(19, 120, 761, 171))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(265, 40, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 63, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setToolTip("Altitude is distance from the ground.\nWe use meters to measure this.")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 63, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setToolTip("Latitude is the distance a location is from\nthe equator, from 180° north to 180°\nsouth.  For this program we say negative\nnumbers are south, and positive numbers\n are north.")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(330, 100, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setToolTip("Longitude is the distance a location is from\nthe Prime Meridian, from 180° west to 180°\neast.  For this program we say negative\nnumbers are west, and positive numbers\n are east.")

        #############################################



        #################################
        ###  Project 1 Param Sliders  ###
        #############################################

        # Slider 1
        self.horizontalSlider = QtWidgets.QSlider(self.page_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(400, 40, 281, 24))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(5000)
        self.horizontalSlider.setTickInterval(500)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self._updateParams)

        #Slider 2
        self.horizontalSlider_2 = QtWidgets.QSlider(self.page_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(400, 70, 281, 24))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(-180)
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setTickInterval(45)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.valueChanged.connect(self._updateParams)

        # Slider 3
        self.horizontalSlider_3 = QtWidgets.QSlider(self.page_2)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(400, 100, 281, 24))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setMinimum(-180)
        self.horizontalSlider_3.setMaximum(180)
        self.horizontalSlider_3.setTickInterval(45)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_3.valueChanged.connect(self._updateParams)

        #############################################




        ######################################
        ### Parameter  Slider Value Labels ###
        #############################################

        ## Placeholder Project 1 Params ##

        # Altitude Value
        self.param1Label = QtWidgets.QLabel(self.page_2)
        self.param1Label.setObjectName("parameter1Label")
        self.param1Label.setGeometry(QtCore.QRect(690, 38, 30, 20))

        # Latitude Value
        self.param2Label = QtWidgets.QLabel(self.page_2)
        self.param2Label.setObjectName("parameter3Label")
        self.param2Label.setGeometry(QtCore.QRect(690, 68, 30, 20))

        # Longitude Value
        self.param3Label = QtWidgets.QLabel(self.page_2)
        self.param3Label.setObjectName("parameter3Label")
        self.param3Label.setGeometry(QtCore.QRect(690, 98, 30, 20))

        #############################################





        ############################
        ### Project Descriptions ###
        #############################################

        ## Placeholder Project 1 Description ##

        # Title
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.proj1Title = QtWidgets.QLabel(self.page_2)
        self.proj1Title.setFont(font)
        self.proj1Title.setObjectName("proj1Title")
        self.proj1Title.setGeometry(QtCore.QRect(55,10,100,30))

        # Description
        self.proj1Desc = QtWidgets.QLabel(self.page_2)
        self.proj1Desc.setObjectName("proj1Desc")
        self.proj1Desc.setGeometry(QtCore.QRect(55,10,250,150))



        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(255, 40, 461, 71))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_5")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 350, 92, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self._run)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 90, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 300, 781, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.triggered.connect(self._reset)
        self.actionReset.setShortcut("Ctrl+R")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionExit.setShortcut("Ctrl+X")
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile_2 = QtWidgets.QMenu(self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self._about)
        self.actionAbout.setShortcut("Ctrl+A")
        self.menuFile_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cub Cluster Script Automator"))
        self.label.setText(_translate("MainWindow", "Select the project:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Project 1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Project 2"))
        self.label_5.setText(_translate("MainWindow", "(NO PROJECT SELECTED)"))
        self.label_2.setText(_translate("MainWindow", "Altitude"))
        self.label_3.setText(_translate("MainWindow", "Latitude"))
        self.label_4.setText(_translate("MainWindow", "Longitude"))
        self.label_6.setText(_translate("MainWindow", "(NOT YET IMPLEMENTED)"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.menuFile_2.setTitle(_translate("MainWindow", "Info..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.param1Label.setText(_translate("MainWindow", "0"))
        self.param2Label.setText(_translate("MainWindow", "0"))
        self.param3Label.setText(_translate("MainWindow", "0"))
        self.proj1Title.setText(_translate("MainWindow", "Project 1"))
        self.proj1Desc.setText(_translate("MainWindow", "This is where we can include a basic over- \nview of the project, and descriptions of \nthe variables involved.  As it stands this \nformatting is done manually, I may add in \na way to automatically wrap and for-\nmat the text."))

    def _run(self):
        if self.comboBox.currentIndex() == 0:
            print("INVALID RUN OPTION, PLEASE SELECT A PROJECT")
            self.statusbar.showMessage("Error: No Project Selected")
        elif self.comboBox.currentIndex() == 1:
            self.statusbar.showMessage("Preparing command...")
            print("Slider 1: " + str(self.param1) + ", Slider 2: " + str(self.param2) + ", Slider 3: " + str(self.param3))
            time.sleep(1)
            print("ncl " + self.label_2.text() + "=" + str(self.param1) + " " + self.label_3.text() + "=" + str(self.param2) + " " + self.label_4.text() + "=" + str(self.param3) + " <scriptname>.ncl")
            self.statusbar.showMessage("Running script...")
            time.sleep(5)
            self.statusbar.showMessage("Script finished.")
        else:
            print("THIS PROJECT NOT YET IMPLEMENTED")
            self.statusbar.showMessage("Error: Invalid Project Selected")

    def _updateParams(self):
        self.param1 = self.horizontalSlider.value()
        self.param1Label.setText(str(self.horizontalSlider.value()))
        self.param2 = self.horizontalSlider_2.value()
        self.param2Label.setText(str(self.horizontalSlider_2.value()))
        self.param3 = self.horizontalSlider_3.value()
        self.param3Label.setText(str(self.horizontalSlider_3.value()))

    def _changeStackPage(self):
        if self.comboBox.currentIndex() == 0:
            self.stackedWidget.setCurrentIndex(0)
        elif self.comboBox.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(2)

    def _reset(self):
        self.comboBox.setCurrentIndex(0)
        self.statusbar.showMessage("GUI Reset.")
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_3.setValue(0)

    def _about(self):
        self.testBox = QtWidgets.QMessageBox(MainWindow)
        self.testBox.setWindowTitle("License Information")
        self.testBox.setText("Cub-Cluster Script Automator\nCopyright (C) 2017  John David Benjamin Huddleston\n\nThis program comes with ABSOLUTELY NO WARRANTY;\nThis is free software, and you are welcome to redis-\ntribute it under certain conditions.")
        self.testBox.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
