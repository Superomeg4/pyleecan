# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.PWSlot28
SlotW28 Setup Page
@date Created on Wed Jul 15 14:30:54 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

import PyQt5.QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.GUI import gui_option
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot28.Gen_PWSlot28 import Gen_PWSlot28
from pyleecan.Methods.Slot.Slot.check import SlotCheckError

translate = PyQt5.QtCore.QCoreApplication.translate


class PWSlot28(Gen_PWSlot28, QWidget):
    """Page to set the Slot Type 28
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for Slot combobox
    slot_name = "Slot Type 28"
    slot_type = SlotW28

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot18
            A PWSlot18 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H3.unit = "m"
        self.lf_R1.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W3,
            self.unit_H0,
            self.unit_H3,
            self.unit_R1,
        ]
        for wid in wid_list:
            wid.setText(gui_option.unit.get_m_name())

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W3.setValue(self.slot.W3)
        self.lf_R1.setValue(self.slot.R1)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H3.setValue(self.slot.H3)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal/slot
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H3.editingFinished.connect(self.set_H3)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot28
            A PWSlot28 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot28
            A PWSlot28 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PWSlot28
            A PWSlot28 object
        """
        self.slot.R1 = self.lf_R1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot28
            A PWSlot28 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H3(self):
        """Signal to update the value of H3 according to the line edit

        Parameters
        ----------
        self : PWSlot28
            A PWSlot28 object
        """
        self.slot.H3 = self.lf_H3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return translate("You must set W0 !", "PWSlot28 check")
        elif lam.slot.W3 is None:
            return translate("You must set W3 !", "PWSlot28 check")
        elif lam.slot.R1 is None:
            return translate("You must set R1 !", "PWSlot28 check")
        elif lam.slot.H0 is None:
            return translate("You must set H0 !", "PWSlot28 check")
        elif lam.slot.H3 is None:
            return translate("You must set H3 !", "PWSlot28 check")

        # Check that everything is set right
        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PWSlot28 check") + str(
                error
            )

        if yoke_height <= 0:
            return translate(
                "The slot height is greater than the lamination !", "PWSlot28 check"
            )
