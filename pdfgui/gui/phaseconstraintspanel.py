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

# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Thu Nov  2 11:29:31 2006
__id__ = "$Id$"

import re
import wx
import wx.grid
from pdfpanel import PDFPanel
import phasepanelutils
from wxExtensions.autowidthlabelsgrid import AutoWidthLabelsGrid
from pdfgui.control.constraint import Constraint
from pdfgui.control.controlerrors import *
from sgconstraindialog import SGConstrainDialog

class PhaseConstraintsPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PhaseConstraintsPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizerLatticeParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAdditionalParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAtoms_staticbox = wx.StaticBox(self, -1, "")
        self.sizerPanelName_staticbox = wx.StaticBox(self, -1, "")
        self.labelPanelName = wx.StaticText(self, -1, "Phase Constraints")
        self.labelA = wx.StaticText(self, -1, "a")
        self.textCtrlA = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelB = wx.StaticText(self, -1, "b")
        self.textCtrlB = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelC = wx.StaticText(self, -1, "c")
        self.textCtrlC = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelAlpha = wx.StaticText(self, -1, "alpha")
        self.textCtrlAlpha = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelBeta = wx.StaticText(self, -1, "beta")
        self.textCtrlBeta = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelGamma = wx.StaticText(self, -1, "gamma")
        self.textCtrlGamma = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelScaleFactor = wx.StaticText(self, -1, "Scale Factor")
        self.textCtrlScaleFactor = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelCorrelationLimit = wx.StaticText(self, -1, "Correlation limit")
        self.textCtrlCorrelationLimit = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelDelta1 = wx.StaticText(self, -1, "delta1")
        self.textCtrlDelta1 = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelDelta2 = wx.StaticText(self, -1, "delta2")
        self.textCtrlDelta2 = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelSrat = wx.StaticText(self, -1, "srat")
        self.textCtrlSrat = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelRcut = wx.StaticText(self, -1, "rcut")
        self.textCtrlRcut = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.gridAtoms = AutoWidthLabelsGrid(self, -1, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.onCellRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_EDITOR_SHOWN, self.onEditorShown, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_LABEL_RIGHT_CLICK, self.onLabelRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_CHANGE, self.onCellChange, self.gridAtoms)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: PhaseConstraintsPanel.__set_properties
        self.labelPanelName.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelA.SetToolTipString("lat(1)")
        self.textCtrlA.SetToolTipString("lat(1)")
        self.labelB.SetToolTipString("lat(2)")
        self.textCtrlB.SetToolTipString("lat(2)")
        self.labelC.SetToolTipString("lat(3)")
        self.textCtrlC.SetToolTipString("lat(3)")
        self.labelAlpha.SetToolTipString("lat(4)")
        self.textCtrlAlpha.SetToolTipString("lat(4)")
        self.labelBeta.SetToolTipString("lat(5)")
        self.textCtrlBeta.SetToolTipString("lat(5)")
        self.labelGamma.SetToolTipString("lat(6)")
        self.textCtrlGamma.SetToolTipString("lat(6)")
        self.labelScaleFactor.SetToolTipString("phase scale factor")
        self.textCtrlScaleFactor.SetToolTipString("phase scale")
        self.labelCorrelationLimit.Hide()
        self.textCtrlCorrelationLimit.Hide()
        self.labelDelta1.SetToolTipString("linear atomic correlation factor")
        self.textCtrlDelta1.SetToolTipString("linear atomic correlation factor")
        self.labelDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.textCtrlDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.labelSrat.SetToolTipString("low r peak sharpening")
        self.textCtrlSrat.SetToolTipString("low r peak sharpening")
        self.labelRcut.SetToolTipString("peak sharpening cutoff")
        self.textCtrlRcut.SetToolTipString("peak sharpening cutoff")
        self.gridAtoms.CreateGrid(0, 11)
        self.gridAtoms.EnableDragRowSize(0)
        self.gridAtoms.SetColLabelValue(0, "elem")
        self.gridAtoms.SetColLabelValue(1, "x")
        self.gridAtoms.SetColLabelValue(2, "y")
        self.gridAtoms.SetColLabelValue(3, "z")
        self.gridAtoms.SetColLabelValue(4, "u11")
        self.gridAtoms.SetColLabelValue(5, "u22")
        self.gridAtoms.SetColLabelValue(6, "u33")
        self.gridAtoms.SetColLabelValue(7, "u12")
        self.gridAtoms.SetColLabelValue(8, "u13")
        self.gridAtoms.SetColLabelValue(9, "u23")
        self.gridAtoms.SetColLabelValue(10, "occ")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PhaseConstraintsPanel.__do_layout
        sizerMain = wx.BoxSizer(wx.VERTICAL)
        sizerAtoms = wx.StaticBoxSizer(self.sizerAtoms_staticbox, wx.VERTICAL)
        sizerAdditionalParameters = wx.StaticBoxSizer(self.sizerAdditionalParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_4 = wx.FlexGridSizer(3, 4, 0, 0)
        sizerLatticeParameters = wx.StaticBoxSizer(self.sizerLatticeParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_3 = wx.FlexGridSizer(2, 6, 0, 0)
        sizerPanelName = wx.StaticBoxSizer(self.sizerPanelName_staticbox, wx.HORIZONTAL)
        sizerPanelName.Add(self.labelPanelName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizerMain.Add(sizerPanelName, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_3.Add(self.labelA, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelB, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelC, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelAlpha, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlAlpha, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelBeta, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlBeta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelGamma, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlGamma, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizerLatticeParameters.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerLatticeParameters, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.labelScaleFactor, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlScaleFactor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelCorrelationLimit, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlCorrelationLimit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelDelta1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlDelta1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelDelta2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlDelta2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelSrat, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlSrat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelRcut, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlRcut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizerAdditionalParameters.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAdditionalParameters, 0, wx.ALL|wx.EXPAND, 5)
        sizerAtoms.Add(self.gridAtoms, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAtoms, 1, wx.ALL|wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizerMain)
        sizerMain.Fit(self)
        sizerMain.SetSizeHints(self)
        # end wxGlade

    ##########################################################################
    # Misc Methods

    def __customProperties(self):
        """Custom properties for the panel."""
        self.structure = None
        self.constraints = None
        self._textctrls = ['textCtrlA', 'textCtrlB', 'textCtrlC',
                'textCtrlAlpha', 'textCtrlBeta', 'textCtrlGamma',
                'textCtrlScaleFactor', 'textCtrlDelta1', 'textCtrlDelta2',
                'textCtrlSrat', 'textCtrlRcut']
        self._row = 0
        self._col = 0
        self._focusedText = None
        self._selectedCells = []
        # bind onSetFocus onKillFocus events to text controls
        for widget in self._textctrls:
            self.__dict__[widget].Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            self.__dict__[widget].Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)

        # set up grid
        self.lAtomConstraints = ['x','y','z',
                                 'u11','u22','u33','u12','u13','u23','occ']
        # pdffit internal naming
        self.lConstraints = \
            ['lat(1)','lat(2)','lat(3)','lat(4)','lat(5)','lat(6)',
            'pscale','delta1','delta2','srat','rcut']
        textCtrlIds = [getattr(self, n).GetId() for n in self._textctrls]
        self._id2varname = dict(zip(textCtrlIds, self.lConstraints))

        # set 'elem' abd 'name' columns to read-only
        attr = wx.grid.GridCellAttr()
        attr.SetReadOnly(True)
        self.gridAtoms.SetColAttr(0, attr)
        self.gridAtoms.SetColAttr(11, attr)

        # catch key events and apply them to the grid
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        return
    
    def refresh(self):
        """Refresh wigets on the panel."""
        if self.structure == None:
            raise ValueError, "structure is not defined."

        constraints = self.constraints.copy()
        ### update textctrls ###
        for widget, var in zip(self._textctrls, self.lConstraints):
            wobj = getattr(self, widget)
            if var in self.constraints: s = self.constraints[var].formula
            else:                       s = ""
            wobj.SetValue(s)
        
        ### update the grid ###
        nAtoms = len(self.structure)
        nRows = self.gridAtoms.GetNumberRows()
        self.gridAtoms.BeginBatch()
        # make sure grid has correct number of rows
        if nAtoms > nRows:
            self.gridAtoms.InsertRows(numRows = nAtoms - nRows)
        elif nAtoms < nRows:
            self.gridAtoms.DeleteRows(numRows = nRows - nAtoms)

        # start with clean grid
        self.gridAtoms.ClearGrid()
        
        # fill the first 'elem' column with element symbols
        for row, atom in zip(range(nAtoms), self.structure):
            self.gridAtoms.SetCellValue(row, 0, atom.element)
        
        # update constraints
        bareAtomVarColumn = dict( zip(self.lAtomConstraints,
            range(1, 1 + len(self.lAtomConstraints))) )
        avpat = re.compile(r'(\w+)\((\d+)\)$')
        for var, con in self.constraints.iteritems():
            m = avpat.match(var)
            if not m:   continue
            barevar = m.group(1)
            if not barevar in bareAtomVarColumn:    continue
            column = bareAtomVarColumn[barevar]
            row = int(m.group(2)) - 1
            if not 0 <= row < nAtoms:
                raise ControlValueError, "Invalid variable index for %r" % var
            self.gridAtoms.SetCellValue(row, column, con.formula)
            barevar = re.sub(r'\(\d+\)$', '', var)
            if not barevar in bareAtomVarColumn:    continue

        self.gridAtoms.AutosizeLabels()
        self.gridAtoms.AutoSizeColumns()
        self.gridAtoms.EndBatch()
        
        self.gridAtoms.AdjustScrollbars()
        self.gridAtoms.ForceRefresh()
        return

    def applyTextCtrlChange(self, id, value):
        """Update a structure according to a change in a TextCtrl.
        
        id      --  textctrl id
        value   --  new value  
        """
        self.mainPanel.needsSave()
        var = self._id2varname[id]
        formula = value.strip()
        if formula != "":
            self.constraints[var] = Constraint(formula)
        else:
            self.constraints.pop(var)
        return

    def applyCellChange(self, i, j, value):
        """Update an atom according to a change in a cell.
        
        i       --  cell position
        j       --  cell position
        value   --  new value  
        """
        self.mainPanel.needsSave()        
        key = self.lAtomConstraints[j-1] + '('+`i+1`+')'
        formula = value.strip()
        if formula != "":
            self.constraints[key] = Constraint(formula)
        else:
            self.constraints.pop(key)
        return


    ##########################################################################
    # Event Handlers

    # TextCtrl Events
    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be compared in onKillFocuse later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return
        
    def onKillFocus(self, event):
        """Check value of TextCtrl and update structure if necessary."""
        textctrl = event.GetEventObject()
        value = textctrl.GetValue()

        if self._focusedText != value:
            self.applyTextCtrlChange(textctrl.GetId(), value)
            self.refresh()
                
        self._focusedText = ""
        event.Skip()
        return

    # Grid Events
    def onLabelRightClick(self, event): # wxGlade: PhaseConstraintsPanel.<event_handler>
        """Bring up right-click menu."""
        if self.structure != None:
            dx = dy = 0
            if event.GetRow() == -1:
                dy = self.gridAtoms.GetGridCornerLabelWindow().GetSize().y
            if event.GetCol() == -1:
                dx = self.gridAtoms.GetGridCornerLabelWindow().GetSize().x
    
            # do not popup menu if the whole grid is set to read only
            if len(self.structure) == 0:
                self.popupMenu(self.gridAtoms, event.GetPosition().x-dx, 
                        event.GetPosition().y-dy)
        event.Skip()
        return

    def onCellRightClick(self, event): # wxGlade: PhaseConstraintsPanel.<event_handler>
        """Bring up right-click menu."""
        self._row = event.GetRow()
        self._col = event.GetCol()

        # If the right-clicked node is not part of a group, then make sure that
        # it is the only selected cell.
        append = False
        r = self._row
        c = self._col
        if self.gridAtoms.IsInSelection(r,c):
            append = True
        self.gridAtoms.SelectBlock(r,c,r,c,append)

        self.popupMenu(self.gridAtoms, event.GetPosition().x, event.GetPosition().y)
        event.Skip()
        return

    def onEditorShown(self, event): # wxGlade: PhaseConstraintsPanel.<event_handler>
        """Capture the focused text when the grid editor is shown."""
        i = event.GetRow()
        j = event.GetCol()
        self._focusedText = self.gridAtoms.GetCellValue(i,j)
        self._selectedCells = self.getSelectedCells()
        event.Skip()
        return

    def onCellChange(self, event): # wxGlade: PhaseConstraintsPanel.<event_handler>
        """Update focused text when a cell changes."""
        # NOTE: be careful with refresh() => recursion! operations on grid will
        # call onCellChange
        i = event.GetRow()
        j = event.GetCol()

        # This keeps us out of recursion
        if self._focusedText is None: return
        self._focusedText = None

        value = self.gridAtoms.GetCellValue(i,j)
        # Verify the equation. This is done here since if it is allowed to be
        # done in fillCells, then an error dialog will be thrown for each
        # point in the loop.
        try:
            if value != "":
                Constraint(value)
            if (i,j) not in self._selectedCells:
                self._selectedCells.append((i,j))
            self.fillCells(self._selectedCells, value)
        finally:
            self.refresh()
            event.Skip()
        return

    def onKey(self, event):
        """Catch key events in the panel."""
        key = event.GetKeyCode()

        # Select All - Ctrl+A
        if event.ControlDown() and key == 65:
            rows = self.gridAtoms.GetNumberRows()
            cols = self.gridAtoms.GetNumberCols()
            self.gridAtoms.SelectBlock(0,0,rows,cols)

        # Delete
        elif key == 127:
            indices = self.getSelectedCells()
            self.fillCells(indices, "")
            self.refresh()
            self.mainPanel.needsSave()

        else:
            event.Skip()
        return

    ##########################################################################
    # Grid popup menu and handlers

    def popupMenu(self, window, x, y):
        """Creates the popup menu
        
        window  --  window, where to popup a menu
        x       --  x coordinate
        y       --  y coordinate
        """
        # only do this part the first time so the events are only bound once
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()

            #self.Bind(wx.EVT_MENU, self.onPopupFill, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.onPopupSpaceGroup, id=self.popupID2)

        # make a menu
        menu = wx.Menu()

        # add some other items
        #menu.Append(self.popupID1, "Fill...")
        #menu.AppendSeparator()
        menu.Append(self.popupID2, "Symmetry constraints...")

        # Disable some items if there are no atoms selected
        indices = self.getSelectedAtoms()
        if not indices:
            #menu.Enable(self.popupID1, False);
            menu.Enable(self.popupID2, False);


        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        window.PopupMenu(menu, wx.Point(x,y))
        menu.Destroy()        
        return

    def onPopupFill(self, event):
        """Fills cells selected in the grid with a new value."""
        if self.structure != None:
            if self.gridAtoms.IsSelection():
                dlg = wx.TextEntryDialog(self, 
                        'New value:','Fill Selected Cells', '')
        
                if dlg.ShowModal() == wx.ID_OK:
                    value = dlg.GetValue()
                    
                    indicies = self.getSelectedCells()
                    self.fillCells(indicies, value)
                    self.refresh()
                    self.mainPanel.needsSave()
                dlg.Destroy()
        return

    def onPopupSpaceGroup(self, event):
        """Create a supercell with the supercell dialog."""
        if self.structure != None:

            indices = self.getSelectedAtoms()
            dlg = SGConstrainDialog(self)
            dlg.mainPanel = self.mainPanel
            dlg.indices = indices
            dlg.setStructure(self.structure)
            dlg.updateWidgets()
            if dlg.ShowModal() == wx.ID_OK:
                spcgrp = dlg.getSpaceGroup()
                offset = dlg.getOffset()
                posflag = dlg.getPosFlag()
                tempflag = dlg.getTempFlag()
                self.structure.applySymmetryConstraints(spcgrp, 
                        indices, posflag, tempflag, offset)
                self.refresh()
            dlg.Destroy()
            self.mainPanel.needsSave()
        return

    # Required by event handlers

    def getSelectedAtoms(self):
        """Get list of indices of selected atoms."""
        rows = self.gridAtoms.GetNumberRows()
        cols = self.gridAtoms.GetNumberCols()
        selection = []
        
        for i in xrange(rows):
            for j in xrange(cols):
                if self.gridAtoms.IsInSelection(i,j):
                    selection.append(i)
                    break

        return selection

    def getSelectedCells(self):
        """Get list of (row,col) pairs of selected cells."""
        rows = self.gridAtoms.GetNumberRows()
        cols = self.gridAtoms.GetNumberCols()
        selection = []
        
        for i in xrange(rows):
            for j in xrange(cols):
                if self.gridAtoms.IsInSelection(i,j):
                    selection.append((i,j))

        return selection

    def fillCells(self, indices, value):
        """Fill cells with a given value.

        indices    --  list of (i,j) tuples representing cell coordinates
        value       --  string value to place into cells
        """
        for (i,j) in indices:
            if not self.gridAtoms.IsReadOnly(i,j):
                self.applyCellChange(i,j, value)
        return

# end of class PhaseConstraintsPanel