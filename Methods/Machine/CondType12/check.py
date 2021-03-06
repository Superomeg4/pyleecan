# -*- coding: utf-8 -*-
"""@package Methods.Machine.CondType12.check
Check that the Conductor is correct
@date Created on Thu Jan 22 17:38:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi, power

from pyleecan.Methods.Machine.Conductor.check import CondCheckError


def check(self):
    """Check that the Conductor object is correct

    Parameters
    ----------
    self : CondType12
        A CondType12 object

    Returns
    -------
    None

    Raises
    _______
    C12_WireDontFit
        The wire is too big to fit in the conductor
    C12_WireDontFit
        The wires are too big to fit in the conductor
    """

    Swire = power((self.Wwire + 2 * self.Wins_wire) / 2.0, 2) * pi * self.Nwppc
    Scond = self.comp_surface()

    if Swire > Scond:
        if self.Nwppc == 1:
            raise C12_WireDontFit("The wire is too big to fit in the conductor")
        else:
            raise C12_WireDontFit("The wires are too big to fit in the conductor")


class Cond12CheckError(CondCheckError):
    """ """

    pass


class C12_WireDontFit(Cond12CheckError):
    """ """
