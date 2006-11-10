#!/usr/bin/env python
########################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Tue Feb 21 12:00:30 2006

import sys
import wx
from mainpanel import MainPanel

class PDFGuiFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = MainPanel(self, -1)
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        # This is now done in the main panel so that the filename of the current
        # file can be displayed correctly.
        #self.SetTitle("PDFGui")
        pass

    def __do_layout(self):
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        sizer_3.SetSizeHints(self)
        self.Layout()
        self.SetSize((700, 120))

# end of class PDFGuiFrame


class PDFGuiApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.frame_1 = PDFGuiFrame(None, -1, "")
        self.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        return 1

# end of class PDFGuiApp

def main():
    """PDFGui main kick starter.
    Command line options and arguments can be passed via
    cmdopts and cmdargs variables in pdfguiglobals module.
    """
    # Command line options and arguments can be passed via
    # cmdopts and cmdargs variables in pdfguiglobals
    app = PDFGuiApp(0)
    app.MainLoop()
    return

if __name__ == "__main__":
    main()

# version
__id__ = "$Id$"