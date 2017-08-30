# *****************************************************************
# IonControl:  Copyright 2016 Sandia Corporation
# This Software is released under the GPL license detailed
# in the file "license.txt" in the top-level IonControl directory
# *****************************************************************
from PyQt5 import QtCore, QtGui
from modules.firstNotNone import firstNotNone
from functools import partial

class MemsPositionsTableModel(QtCore.QAbstractTableModel):
    headerDataLookup = ['x1', 'cal. x1', 'y1', 'cal. y1','x2', 'cal. x2', 'y2', 'cal. y2'] #['On', 'Name', 'Frequency', 'Phase', 'Amplitude', 'Square' ]

    # x1Changed = QtCore.pyqtSignal(object, object)
    # x1cChanged = QtCore.pyqtSignal(object, object)
    # y1Changed = QtCore.pyqtSignal(object, object)
    # y1cChanged = QtCore.pyqtSignal(object, object)
    # x2Changed = QtCore.pyqtSignal(object, object)
    # x2cChanged = QtCore.pyqtSignal(object, object)
    # y2Changed = QtCore.pyqtSignal(object, object)
    # y2cChanged = QtCore.pyqtSignal(object, object)

    def __init__(self, nIons, globalDict, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        # scanNames are given as a SortedDict
        #self.ddsChannels = ddsChannels
        self.nIons = nIons
        self.defaultBG = QtGui.QColor(QtCore.Qt.white)
        self.textBG = QtGui.QColor(QtCore.Qt.green).lighter(175)
        self.dataLookup = {  #(QtCore.Qt.CheckStateRole, 0): lambda row: QtCore.Qt.Checked if self.ddsChannels[row].enabled else QtCore.Qt.Unchecked,
                             #(QtCore.Qt.DisplayRole, 1): lambda row: self.nIons[row].name,
                             (QtCore.Qt.DisplayRole, 0): lambda row: str(self.nIons[row].x1),
                             (QtCore.Qt.DisplayRole, 1): lambda row: str(self.nIons[row].x1c),
                             (QtCore.Qt.DisplayRole, 2): lambda row: str(self.nIons[row].y1),
                             (QtCore.Qt.DisplayRole, 3): lambda row: str(self.nIons[row].y1c),
                             (QtCore.Qt.DisplayRole, 4): lambda row: str(self.nIons[row].x2),
                             (QtCore.Qt.DisplayRole, 5): lambda row: str(self.nIons[row].x2c),
                             (QtCore.Qt.DisplayRole, 6): lambda row: str(self.nIons[row].y2),
                             (QtCore.Qt.DisplayRole, 7): lambda row: str(self.nIons[row].y2c),

                             #(QtCore.Qt.EditRole, 1): lambda row: self.nIons[row].name,
                             (QtCore.Qt.EditRole, 0): lambda row: firstNotNone( self.nIons[row].x1Text, str(self.nIons[row].x1)),
                             (QtCore.Qt.EditRole, 1): lambda row: firstNotNone( self.nIons[row].x1cText, str(self.nIons[row].x1c)),
                             (QtCore.Qt.EditRole, 2): lambda row: firstNotNone(self.nIons[row].y1Text, str(self.nIons[row].y1)),
                             (QtCore.Qt.EditRole, 3): lambda row: firstNotNone(self.nIons[row].y1cText, str(self.nIons[row].y1c)),
                             (QtCore.Qt.EditRole, 4): lambda row: firstNotNone(self.nIons[row].x2Text, str(self.nIons[row].x2)),
                             (QtCore.Qt.EditRole, 5): lambda row: firstNotNone(self.nIons[row].x2cText, str(self.nIons[row].x2c)),
                             (QtCore.Qt.EditRole, 6): lambda row: firstNotNone(self.nIons[row].y2Text, str(self.nIons[row].y2)),
                             (QtCore.Qt.EditRole, 7): lambda row: firstNotNone(self.nIons[row].y2cText, str(self.nIons[row].y2c)),

                             (QtCore.Qt.BackgroundColorRole, 0): lambda row: self.defaultBG if self.nIons[row].x1Test is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 1): lambda row: self.defaultBG if self.nIons[row].x1cText is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 2): lambda row: self.defaultBG if self.nIons[row].y1Text is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 3): lambda row: self.defaultBG if self.nIons[row].y1cText is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 4): lambda row: self.defaultBG if self.nIons[row].x2Text is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 5): lambda row: self.defaultBG if self.nIons[row].x2cText is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 6): lambda row: self.defaultBG if self.nIons[row].y2Text is None else self.textBG,
                             (QtCore.Qt.BackgroundColorRole, 7): lambda row: self.defaultBG if self.nIons[row].y2cText is None else self.textBG,
                             }

        self.setDataLookup = { (QtCore.Qt.EditRole, 0): self.setx1,
                               (QtCore.Qt.EditRole, 1): self.setx1c,
                               (QtCore.Qt.EditRole, 2): self.sety1,
                               (QtCore.Qt.EditRole, 3): self.sety1c,
                               (QtCore.Qt.EditRole, 4): self.setx2,
                               (QtCore.Qt.EditRole, 5): self.setx2c,
                               (QtCore.Qt.EditRole, 6): self.sety2,
                               (QtCore.Qt.EditRole, 7): self.sety2c,
                               (QtCore.Qt.UserRole, 0): partial( self.setx1Text, 'x1Text'),
                               (QtCore.Qt.UserRole, 1): partial( self.setx1cText, 'x1cText'),
                               (QtCore.Qt.UserRole, 2): partial( self.sety1Text, 'y1Text'),
                               (QtCore.Qt.UserRole, 3): partial( self.sety1cText, 'y1cText'),
                               (QtCore.Qt.UserRole, 4): partial( self.setx2Text, 'x2Text'),
                               (QtCore.Qt.UserRole, 5): partial( self.setx2cText, 'x2cText'),
                               (QtCore.Qt.UserRole, 6): partial( self.sety2Text, 'y2Text'),
                               (QtCore.Qt.UserRole, 7): partial( self.sety2cText, 'y2cText'),


                               }

        self.globalDict = globalDict

    # def setValue(self, index, value):
    #     self.setData( index, value, QtCore.Qt.EditRole)

    def setx1(self, index, value):
        self.nIons[index.row()].x1 = value
        self.x1Changed.emit( index.row(), value)
        return True
    
    def setx1c(self, index, value):
        self.nIons[index.row()].x1c = value
        self.x1cChanged.emit( index.row(), value)
        return True

    def sety1(self, index, value):
        self.nIons[index.row()].y1 = value
        self.y1Changed.emit(index.row(), value)
        return True

    def sety1c(self, index, value):
        self.nIons[index.row()].y1c = value
        self.y1cChanged.emit(index.row(), value)
        return True

    def setx2(self, index, value):
        self.nIons[index.row()].x2 = value
        self.x2Changed.emit(index.row(), value)
        return True

    def setx2c(self, index, value):
        self.nIons[index.row()].x2c = value
        self.x2cChanged.emit(index.row(), value)
        return True

    def sety2(self, index, value):
        self.nIons[index.row()].y2 = value
        self.y2Changed.emit(index.row(), value)
        return True

    def sety2c(self, index, value):
        self.nIons[index.row()].y2c = value
        self.y2cChanged.emit(index.row(), value)
        return True

    # def setFieldText(self, fieldname, index, value):
    #     setattr( self.nIons[index.row()], fieldname, value )
    #     return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.nIons)
        
    def columnCount(self, parent=QtCore.QModelIndex()): 
        return 8
 
    def data(self, index, role): 
        if index.isValid():
            return self.dataLookup.get((role, index.column()), lambda row: None)(index.row())
        return None
    
    def setData(self, index, value, role):
        return self.setDataLookup.get((role, index.column()), lambda index, value: False )(index, value)
        
    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable if index.column() in [0, 5] else QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        if (role == QtCore.Qt.DisplayRole):
            if (orientation == QtCore.Qt.Horizontal): 
                return self.headerDataLookup[section]
            elif (orientation == QtCore.Qt.Vertical):
                return str(section)
        return None  # QtCore.QVariant()