# -*- coding: utf-8 -*-
"""
Created on 24/07/17 23:23

@author: pydemia
"""

# !python3
# http://python.su/forum/viewtopic.php?id=7346
import sys
from PyQt5 import QtGui, QtCore, Qt


class MyWindow(Qt.QWidget):
    def __init__(self, *args):
        Qt.QWidget.__init__(self, *args)

        # create table
        table = FreezeTableWidget(self)

        # layout
        layout = Qt.QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)


class FreezeTableWidget(Qt.QTableView):
    def __init__(self, parent=None, *args):
        Qt.QTableView.__init__(self, parent, *args)

        self.setMinimumSize(800, 600)

        tm = MyTableModel(self)

        # set the proxy model
        pm = Qt.QSortFilterProxyModel(self)
        pm.setSourceModel(tm)

        self.setModel(pm)

        self.frozenTableView = Qt.QTableView(self)
        self.frozenTableView.setModel(pm)
        self.frozenTableView.verticalHeader().hide()
        self.frozenTableView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frozenTableView.horizontalHeader().setSectionResizeMode(Qt.QHeaderView.Fixed)
        self.frozenTableView.setStyleSheet('''border: none; background-color: #8EDE21; 
                                       selection-background-color: #999''')
        self.frozenTableView.setSelectionModel(Qt.QAbstractItemView.selectionModel(self))
        self.frozenTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.frozenTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.viewport().stackUnder(self.frozenTableView)

        self.setEditTriggers(Qt.QAbstractItemView.SelectedClicked)

        # hide gridnt()
        #        self.setShowGrid(False)
        self.setStyleSheet('font: 10pt "Courier New"')

        hh = self.horizontalHeader()
        hh.setDefaultAlignment(QtCore.Qt.AlignCenter)
        hh.setStretchLastSection(True)

        #        self.resizeColumnsToContents()

        ncol = tm.columnCount(self)
        for col in range(ncol):
            if col == 0:
                self.horizontalHeader().resizeSection(col, 60)
                self.horizontalHeader().setSectionResizeMode(col, Qt.QHeaderView.Fixed)
                self.frozenTableView.setColumnWidth(col, self.columnWidth(col))
            elif col == 1:
                self.horizontalHeader().resizeSection(col, 150)
                self.horizontalHeader().setSectionResizeMode(col, Qt.QHeaderView.Fixed)
                self.frozenTableView.setColumnWidth(col, self.columnWidth(col))
            else:
                self.horizontalHeader().resizeSection(col, 100)
                self.frozenTableView.setColumnHidden(col, True)

        self.frozenTableView.setSortingEnabled(True)
        self.frozenTableView.sortByColumn(0, QtCore.Qt.AscendingOrder)

        self.setAlternatingRowColors(True)

        vh = self.verticalHeader()
        vh.setDefaultSectionSize(25)
        vh.setDefaultAlignment(QtCore.Qt.AlignCenter)
        vh.setVisible(True)
        self.frozenTableView.verticalHeader().setDefaultSectionSize(vh.defaultSectionSize())

        #        nrows = tm.rowCount(self)
        #        for row in xrange(nrows):
        #            self.setRowHeight(row, 25)

        self.frozenTableView.show()
        self.updateFrozenTableGeometry()

        self.setHorizontalScrollMode(Qt.QAbstractItemView.ScrollPerPixel)
        self.setVerticalScrollMode(Qt.QAbstractItemView.ScrollPerPixel)
        self.frozenTableView.setVerticalScrollMode(Qt.QAbstractItemView.ScrollPerPixel)

        tm.dataChanged.connect(self.test)
        # connect the headers and scrollbars of both tableviews together
        self.horizontalHeader().sectionResized.connect(self.updateSectionWidth)
        self.verticalHeader().sectionResized.connect(self.updateSectionHeight)
        self.frozenTableView.verticalScrollBar().valueChanged.connect(self.verticalScrollBar().setValue)
        self.verticalScrollBar().valueChanged.connect(self.frozenTableView.verticalScrollBar().setValue)

    def test(self, index):
        print(index.row(), index.column())

    def updateSectionWidth(self, logicalIndex, oldSize, newSize):
        if logicalIndex == 0 or logicalIndex == 1:
            self.frozenTableView.setColumnWidth(logicalIndex, newSize)
            self.updateFrozenTableGeometry()

    def updateSectionHeight(self, logicalIndex, oldSize, newSize):
        self.frozenTableView.setRowHeight(logicalIndex, newSize)

    def resizeEvent(self, event):
        Qt.QTableView.resizeEvent(self, event)
        self.updateFrozenTableGeometry()

    def scrollTo(self, index, hint):
        if index.column() > 1:
            Qt.QTableView.scrollTo(self, index, hint)

    def updateFrozenTableGeometry(self):
        if self.verticalHeader().isVisible():
            self.frozenTableView.setGeometry(self.verticalHeader().width() + self.frameWidth(),
                                             self.frameWidth(), self.columnWidth(0) + self.columnWidth(1),
                                             self.viewport().height() + self.horizontalHeader().height())
        else:
            self.frozenTableView.setGeometry(self.frameWidth(),
                                             self.frameWidth(), self.columnWidth(0) + self.columnWidth(1),
                                             self.viewport().height() + self.horizontalHeader().height())

    def moveCursor(self, cursorAction, modifiers):
        current = Qt.QTableView.moveCursor(self, cursorAction, modifiers)
        if cursorAction == self.MoveLeft and current.column() > 1 and self.visualRect(current).topLeft().x() < (
            self.frozenTableView.columnWidth(0) + self.frozenTableView.columnWidth(1)):
            newValue = self.horizontalScrollBar().value() + self.visualRect(current).topLeft().x() - (
            self.frozenTableView.columnWidth(0) + self.frozenTableView.columnWidth(1))
            self.horizontalScrollBar().setValue(newValue)
        return current


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.colLabels = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6',
                          'Col7', 'Col8', 'Col9', 'Col10']
        self.dataCached = [
            [111, 'cell12', 'cell13', 'cell14', 'cell15', 'cell12', 'cell13', 'cell14', 'cell15', 'cell16'],
            [112, 'cell22', 'cell23', 'cell24', 'cell25', 'cell26', 'cell27', 'cell28', 'cell29', 'cell30'],
            [113, 'cell32', 'cell33', 'cell34', 'cell35', 'cell36', 'cell37', 'cell38', 'cell39', 'cell40'],
            [114, 'cell42', 'cell43', 'cell44', 'cell45', 'cell46', 'cell47', 'cell48', 'cell49', 'cell50'],
            [115, 'cell52', 'cell53', 'cell54', 'cell55', 'cell56', 'cell57', 'cell58', 'cell59', 'cell60'],
            [116, 'cell62', 'cell63', 'cell64', 'cell65', 'cell66', 'cell67', 'cell68', 'cell69', 'cell70'],
            [117, 'cell72', 'cell73', 'cell74', 'cell75', 'cell76', 'cell77', 'cell78', 'cell79', 'cell80'],
            [118, 'cell82', 'cell83', 'cell84', 'cell85', 'cell86', 'cell87', 'cell88', 'cell89', 'cell90'],
            [119, 'cell12', 'cell13', 'cell14', 'cell15', 'cell12', 'cell13', 'cell14', 'cell15', 'cell16'],
            [120, 'cell22', 'cell23', 'cell24', 'cell25', 'cell26', 'cell27', 'cell28', 'cell29', 'cell30'],
            [121, 'cell32', 'cell33', 'cell34', 'cell35', 'cell36', 'cell37', 'cell38', 'cell39', 'cell40'],
            [122, 'cell42', 'cell43', 'cell44', 'cell45', 'cell46', 'cell47', 'cell48', 'cell49', 'cell50'],
            [123, 'cell52', 'cell53', 'cell54', 'cell55', 'cell56', 'cell57', 'cell58', 'cell59', 'cell60'],
            [124, 'cell62', 'cell63', 'cell64', 'cell65', 'cell66', 'cell67', 'cell68', 'cell69', 'cell70'],
            [125, 'cell72', 'cell73', 'cell74', 'cell75', 'cell76', 'cell77', 'cell78', 'cell79', 'cell80'],
            [126, 'cell82', 'cell83', 'cell84', 'cell85', 'cell86', 'cell87', 'cell88', 'cell89', 'cell90'],
            [127, 'cell12', 'cell13', 'cell14', 'cell15', 'cell12', 'cell13', 'cell14', 'cell15', 'cell16'],
            [128, 'cell22', 'cell23', 'cell24', 'cell25', 'cell26', 'cell27', 'cell28', 'cell29', 'cell30'],
            [129, 'cell32', 'cell33', 'cell34', 'cell35', 'cell36', 'cell37', 'cell38', 'cell39', 'cell40'],
            [130, 'cell42', 'cell43', 'cell44', 'cell45', 'cell46', 'cell47', 'cell48', 'cell49', 'cell50'],
            [131, 'cell52', 'cell53', 'cell54', 'cell55', 'cell56', 'cell57', 'cell58', 'cell59', 'cell60'],
            [132, 'cell62', 'cell63', 'cell64', 'cell65', 'cell66', 'cell67', 'cell68', 'cell69', 'cell70'],
            [133, 'cell72', 'cell73', 'cell74', 'cell75', 'cell76', 'cell77', 'cell78', 'cell79', 'cell80'],
            [134, 'cell82', 'cell83', 'cell84', 'cell85', 'cell86', 'cell87', 'cell88', 'cell89', 'cell90'],
            [135, 'cell82', 'cell83', 'cell84', 'cell85', 'cell86', 'cell87', 'cell88', 'cell89', 'cell90'],
            [136, 'cell82', 'cell83', 'cell84', 'cell85', 'cell86', 'cell87', 'cell88', 'cell89', 'cell90']
        ]

    def rowCount(self, parent):
        return len(self.dataCached)

    def columnCount(self, parent):
        return len(self.colLabels)

    def get_value(self, index):
        i = index.row()
        j = index.column()
        return self.dataCached[i][j]

    def data(self, index, role):
        if not index.isValid():
            return None
        value = self.get_value(index)
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return value
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
        return None

    def setData(self, index, value, role):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.dataCached[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            header = self.colLabels[section]
            return header
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return str(section + 1)

        return None

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        elif index.column() > 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())