# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Raphael\Desktop\Git\PyManatee\pyleecan\GUI\Dialog\DMachineSetup\SWindCond\PCondType11\PCondType11.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCondType11(object):
    def setupUi(self, PCondType11):
        PCondType11.setObjectName("PCondType11")
        PCondType11.resize(1154, 544)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PCondType11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_cond = QtWidgets.QLabel(PCondType11)
        self.img_cond.setMinimumSize(QtCore.QSize(0, 0))
        self.img_cond.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_cond.setText("")
        self.img_cond.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WindParam/Cond_1_1.PNG")
        )
        self.img_cond.setScaledContents(True)
        self.img_cond.setObjectName("img_cond")
        self.horizontalLayout.addWidget(self.img_cond)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.si_Nwpc1_tan = QtWidgets.QSpinBox(PCondType11)
        self.si_Nwpc1_tan.setMinimumSize(QtCore.QSize(70, 0))
        self.si_Nwpc1_tan.setProperty("value", 99)
        self.si_Nwpc1_tan.setObjectName("si_Nwpc1_tan")
        self.gridLayout.addWidget(self.si_Nwpc1_tan, 0, 1, 1, 1)
        self.lf_Wwire = FloatEdit(PCondType11)
        self.lf_Wwire.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Wwire.setMaximumSize(QtCore.QSize(100, 100))
        self.lf_Wwire.setObjectName("lf_Wwire")
        self.gridLayout.addWidget(self.lf_Wwire, 2, 1, 1, 1)
        self.in_Nwpc1_tan = QtWidgets.QLabel(PCondType11)
        self.in_Nwpc1_tan.setMinimumSize(QtCore.QSize(60, 0))
        self.in_Nwpc1_tan.setObjectName("in_Nwpc1_tan")
        self.gridLayout.addWidget(self.in_Nwpc1_tan, 0, 0, 1, 1)
        self.si_Nwpc1_rad = QtWidgets.QSpinBox(PCondType11)
        self.si_Nwpc1_rad.setProperty("value", 99)
        self.si_Nwpc1_rad.setObjectName("si_Nwpc1_rad")
        self.gridLayout.addWidget(self.si_Nwpc1_rad, 1, 1, 1, 1)
        self.lf_Hwire = FloatEdit(PCondType11)
        self.lf_Hwire.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Hwire.setMaximumSize(QtCore.QSize(100, 100))
        self.lf_Hwire.setObjectName("lf_Hwire")
        self.gridLayout.addWidget(self.lf_Hwire, 3, 1, 1, 1)
        self.unit_Wwire = QtWidgets.QLabel(PCondType11)
        self.unit_Wwire.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Wwire.setObjectName("unit_Wwire")
        self.gridLayout.addWidget(self.unit_Wwire, 2, 2, 1, 1)
        self.unit_Wins_wire = QtWidgets.QLabel(PCondType11)
        self.unit_Wins_wire.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Wins_wire.setObjectName("unit_Wins_wire")
        self.gridLayout.addWidget(self.unit_Wins_wire, 4, 2, 1, 1)
        self.unit_Hwire = QtWidgets.QLabel(PCondType11)
        self.unit_Hwire.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Hwire.setObjectName("unit_Hwire")
        self.gridLayout.addWidget(self.unit_Hwire, 3, 2, 1, 1)
        self.in_Wwire = QtWidgets.QLabel(PCondType11)
        self.in_Wwire.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Wwire.setObjectName("in_Wwire")
        self.gridLayout.addWidget(self.in_Wwire, 2, 0, 1, 1)
        self.in_Nwpc1_rad = QtWidgets.QLabel(PCondType11)
        self.in_Nwpc1_rad.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Nwpc1_rad.setObjectName("in_Nwpc1_rad")
        self.gridLayout.addWidget(self.in_Nwpc1_rad, 1, 0, 1, 1)
        self.lf_Wins_wire = FloatEdit(PCondType11)
        self.lf_Wins_wire.setMinimumSize(QtCore.QSize(50, 0))
        self.lf_Wins_wire.setMaximumSize(QtCore.QSize(100, 100))
        self.lf_Wins_wire.setObjectName("lf_Wins_wire")
        self.gridLayout.addWidget(self.lf_Wins_wire, 4, 1, 1, 1)
        self.in_Wins_wire = QtWidgets.QLabel(PCondType11)
        self.in_Wins_wire.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Wins_wire.setObjectName("in_Wins_wire")
        self.gridLayout.addWidget(self.in_Wins_wire, 4, 0, 1, 1)
        self.in_Hwire = QtWidgets.QLabel(PCondType11)
        self.in_Hwire.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Hwire.setObjectName("in_Hwire")
        self.gridLayout.addWidget(self.in_Hwire, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.w_out = WCondOut(PCondType11)
        self.w_out.setObjectName("w_out")
        self.verticalLayout_2.addWidget(self.w_out)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(PCondType11)
        QtCore.QMetaObject.connectSlotsByName(PCondType11)
        PCondType11.setTabOrder(self.si_Nwpc1_tan, self.si_Nwpc1_rad)
        PCondType11.setTabOrder(self.si_Nwpc1_rad, self.lf_Wwire)
        PCondType11.setTabOrder(self.lf_Wwire, self.lf_Hwire)
        PCondType11.setTabOrder(self.lf_Hwire, self.lf_Wins_wire)

    def retranslateUi(self, PCondType11):
        _translate = QtCore.QCoreApplication.translate
        PCondType11.setWindowTitle(_translate("PCondType11", "Form"))
        self.in_Nwpc1_tan.setText(_translate("PCondType11", "Nwpc1_tan :"))
        self.unit_Wwire.setText(_translate("PCondType11", "m"))
        self.unit_Wins_wire.setText(_translate("PCondType11", "m"))
        self.unit_Hwire.setText(_translate("PCondType11", "m"))
        self.in_Wwire.setText(_translate("PCondType11", "Wwire :"))
        self.in_Nwpc1_rad.setText(_translate("PCondType11", "Nwpc1_rad :"))
        self.in_Wins_wire.setText(_translate("PCondType11", "Wins_wire :"))
        self.in_Hwire.setText(_translate("PCondType11", "Hwire :"))


from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.WCondOut.WCondOut import WCondOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
