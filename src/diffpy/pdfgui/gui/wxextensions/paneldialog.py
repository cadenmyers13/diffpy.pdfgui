#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Wed Mar 29 15:15:14 2006
##############################################################################
#
# wxextensions      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

"""This module contains the PanelDialog class, a simple class that turns any
panel into a dialog.
"""


import wx


class PanelDialog(wx.Dialog):
    """This class will turn any panel into a dialog.  Using this makes for
    quicker development and encourages the developer to design a gui as a
    collection of panels, instead of a monolithic mega-panel.
    """

    def __init__(self, *args, **kwds):
        """Initialize the PanelDialog.

        This takes the same args and kwds as wxDialog. See the wxDialog
        documentation for more information.

        Unless specified, style is automatically set as
        wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER

        Creating a PanelDialog requires three steps.
        1) Create the PanelDialog.
        2) Create the Panel, with the new PanelDialog as the parent.
        3) Call the setPanel method of the PanelDialog with the new Panel as the
           the argument.
        """
        if not hasattr(kwds, "style"):
            kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        return

    def setPanel(self, panel):
        """Call this method to add the panel to the dialog."""
        self.panel = panel
        self.__set_properties()
        self.__do_layout()
        return

    def __set_properties(self):
        return

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        return


# End of class PanelDialog