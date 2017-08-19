# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unipyFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

<<<<<<< HEAD
=======

>>>>>>> master
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from qtpy.compat import from_qvariant, to_qvariant
import pandas as pd
import unipy.dataset.api as dm
from pandasql import sqldf

#from spyder.widgets.variableexplorer.dataframeeditor import DataFrameModel, DataFrameView

<<<<<<< HEAD
class aPandasModel(QtCore.QAbstractTableModel):
=======
__all__ = ['tv']


class PandasModel(QtCore.QAbstractTableModel):
>>>>>>> master
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._df = pd.DataFrame(data)
        self._df_header = self._df.columns.tolist()
        self._df_index = self._df.index.tolist()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df_header[section]
            except (IndexError,):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df_index[section]
            except (IndexError,):
                return QtCore.QVariant()

    def rowCount(self, parent=None):
        return self._df.shape[0]

    def columnCount(self, parent=None):
        return self._df.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                column = index.column()
                row = index.row()
                return Qt.QVariant(str(self._df.iloc[index.row(), index.column()]))
        return None

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        row = index.row()
        col = index.columns()
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def get_value(self, row, column):
        """Returns the value of the DataFrame"""
        # To increase the performance iat is used but that requires error
        # handling, so fallback uses iloc
        try:
            value = self._df.iat[row, column]
        except:
            value = self._df.iloc[row, column]
        return value

    def sort(self, column, order=QtCore.Qt.AscendingOrder):
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(self._df.columns[column-1], ascending= order == QtCore.Qt.AscendingOrder, inplace=True, kind='mergesort')
        #self._df.sort_index(inplace=True)
        #self._df_index = self._df.index.tolist()
        #self._df.set_index(self._df.columns[0], drop=False, inplace=True)
        #self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

    def update_df_index(self):
        """"Update the DataFrame index"""
        self._df_index = self._df.index.tolist()


class columnListWidget(QtWidgets.QListWidget):
    def __init__(self, type, parent=None):
        super(columnListWidget, self).__init__(parent)
        #self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(columnListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            super(columnListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        print('dropEvent', event)
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.PYQT_SIGNAL("dropped"), links)
        else:
            event.setDropAction(QtCore.Qt.MoveAction)
            super(columnListWidget, self).dropEvent(event)


# -*- coding: utf-8 -*-
"""
Created on 24/07/17 23:23

@author: pydemia
"""



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

#MyTableModel
class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)

        self.df = pd.DataFrame(data)
        self.df_header = self.df.columns.tolist()
        self.df_index = self.df.index.tolist()
        self._format = format
        self.complex_intran = None


    def rowCount(self, parent):
        return len(self.df)

    def columnCount(self, parent):
        return len(self.df_header)

    def get_value(self, index):
        i = index.row()
        j = index.column()
        return self.df[i][j]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                column = index.column()
                row = index.row()
                return Qt.QVariant(str(self.df.iloc[index.row(), index.column()]))
        return None

    def setData(self, index, value, role):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.df[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            header = self.df_header[section]
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


    def update_df_index(self):
        """"Update the DataFrame index"""
        self.df_index = self.df.index.tolist()


    def sort(self, column, order=QtCore.Qt.AscendingOrder):
        """Overriding sort method"""
        if self.complex_intran is not None:
            if self.complex_intran.any(axis=0).iloc[column-1]:
                QMessageBox.critical(self.dialog, "Error",
                                     "TypeError error: no ordering "
                                     "relation is defined for complex numbers")
                return False
        try:
            ascending = order == QtCore.Qt.AscendingOrder
            if column > 0:
                try:
                    self.df.sort_values(by=self.df.columns[column-1],
                                        ascending=ascending, inplace=True,
                                        kind='mergesort')
                except AttributeError:
                    # for pandas version < 0.17
                    self.df.sort(columns=self.df.columns[column-1],
                                 ascending=ascending, inplace=True,
                                 kind='mergesort')
                self.update_df_index()
            else:
                self.df.sort_index(inplace=True, ascending=ascending)
                self.update_df_index()
        except TypeError as e:
            QMessageBox.critical(self.dialog, "Error",
                                 "TypeError error: %s" % str(e))
            return False

        self.reset()
        return True


    def reset(self):
        self.beginResetModel()
        self.endResetModel()

class errorMsg(Qt.QErrorMessage):
    pass





class Ui_unipyFrameViewerWindow(object):
    def setupUi(self, unipyFrameViewerWindow):
        unipyFrameViewerWindow.setObjectName("unipyFrameViewerWindow")
        unipyFrameViewerWindow.resize(1300, 857)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(unipyFrameViewerWindow.sizePolicy().hasHeightForWidth())
        unipyFrameViewerWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(unipyFrameViewerWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.main_indicator_frame_rowcol_number = QtWidgets.QLabel(self.centralwidget)
        self.main_indicator_frame_rowcol_number.setGeometry(QtCore.QRect(210, 30, 251, 17))
        self.main_indicator_frame_rowcol_number.setObjectName("main_indicator_frame_rowcol_number")
        self.tabMenu_vertical_line = QtWidgets.QFrame(self.centralwidget)
        self.tabMenu_vertical_line.setGeometry(QtCore.QRect(190, 80, 20, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMenu_vertical_line.sizePolicy().hasHeightForWidth())
        self.tabMenu_vertical_line.setSizePolicy(sizePolicy)
        self.tabMenu_vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.tabMenu_vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tabMenu_vertical_line.setObjectName("tabMenu_vertical_line")
        self.main_toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.main_toolBox.setGeometry(QtCore.QRect(10, 70, 181, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_toolBox.sizePolicy().hasHeightForWidth())
        self.main_toolBox.setSizePolicy(sizePolicy)
        self.main_toolBox.setObjectName("main_toolBox")
        self.columns_page = QtWidgets.QWidget()
        self.columns_page.setGeometry(QtCore.QRect(0, 0, 181, 628))
        self.columns_page.setObjectName("columns_page")
        self.columns_select_col_listView = QtWidgets.QListWidget(self.columns_page)
        self.columns_select_col_listView.setGeometry(QtCore.QRect(0, 10, 181, 261))
        self.columns_select_col_listView.setDragEnabled(True)
        self.columns_select_col_listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.columns_select_col_listView.setObjectName("columns_select_col_listView")
        self.columns_remain_col_listView = QtWidgets.QListWidget(self.columns_page)
        self.columns_remain_col_listView.setGeometry(QtCore.QRect(0, 354, 181, 231))
        self.columns_remain_col_listView.setDragEnabled(True)
        self.columns_remain_col_listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.columns_remain_col_listView.setObjectName("columns_remain_col_listView")
        self.columns_to_select_button = QtWidgets.QPushButton(self.columns_page)
        self.columns_to_select_button.setGeometry(QtCore.QRect(26, 316, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.columns_to_select_button.setFont(font)
        self.columns_to_select_button.setObjectName("columns_to_select_button")
        self.columns_indicator_select_col_number = QtWidgets.QLabel(self.columns_page)
        self.columns_indicator_select_col_number.setGeometry(QtCore.QRect(3, 272, 171, 17))
        self.columns_indicator_select_col_number.setObjectName("columns_indicator_select_col_number")
        self.columns_indicator_remain_col_number = QtWidgets.QLabel(self.columns_page)
        self.columns_indicator_remain_col_number.setGeometry(QtCore.QRect(3, 590, 171, 16))
        self.columns_indicator_remain_col_number.setObjectName("columns_indicator_remain_col_number")
        self.columns_to_remain_button = QtWidgets.QPushButton(self.columns_page)
        self.columns_to_remain_button.setGeometry(QtCore.QRect(88, 316, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.columns_to_remain_button.setFont(font)
        self.columns_to_remain_button.setObjectName("columns_to_remain_button")
        self.main_toolBox.addItem(self.columns_page, "")
        self.groupby_page = QtWidgets.QWidget()
        self.groupby_page.setObjectName("groupby_page")
        self.groupby_groupkey_listView = QtWidgets.QListWidget(self.groupby_page)
        self.groupby_groupkey_listView.setGeometry(QtCore.QRect(0, 30, 181, 151))
        self.groupby_groupkey_listView.setObjectName("groupby_groupkey_listView")
        self.groupby_targetkey_listView = QtWidgets.QListWidget(self.groupby_page)
        self.groupby_targetkey_listView.setGeometry(QtCore.QRect(0, 250, 181, 101))
        self.groupby_targetkey_listView.setObjectName("groupby_targetkey_listView")
        self.groupby_groupkey_label = QtWidgets.QLabel(self.groupby_page)
        self.groupby_groupkey_label.setGeometry(QtCore.QRect(0, 10, 101, 17))
        self.groupby_groupkey_label.setObjectName("groupby_groupkey_label")
        self.groupby_aggfunc_label = QtWidgets.QLabel(self.groupby_page)
        self.groupby_aggfunc_label.setGeometry(QtCore.QRect(13, 200, 61, 17))
        self.groupby_aggfunc_label.setObjectName("groupby_aggfunc_label")
        self.groupby_aggfunc_comboBox = QtWidgets.QComboBox(self.groupby_page)
        self.groupby_aggfunc_comboBox.setGeometry(QtCore.QRect(79, 196, 85, 27))
        self.groupby_aggfunc_comboBox.setObjectName("groupby_aggfunc_comboBox")
        self.groupby_targetkey_label = QtWidgets.QLabel(self.groupby_page)
        self.groupby_targetkey_label.setGeometry(QtCore.QRect(0, 230, 101, 17))
        self.groupby_targetkey_label.setObjectName("groupby_targetkey_label")
        self.groupby_remains_listView = QtWidgets.QListWidget(self.groupby_page)
        self.groupby_remains_listView.setGeometry(QtCore.QRect(0, 390, 181, 181))
        self.groupby_remains_listView.setObjectName("groupby_remains_listView")
        self.groupby_remains_label = QtWidgets.QLabel(self.groupby_page)
        self.groupby_remains_label.setGeometry(QtCore.QRect(0, 370, 101, 17))
        self.groupby_remains_label.setObjectName("groupby_remains_label")
        self.groupby_run_button = QtWidgets.QPushButton(self.groupby_page)
        self.groupby_run_button.setGeometry(QtCore.QRect(37, 580, 99, 27))
        self.groupby_run_button.setObjectName("groupby_run_button")
        self.main_toolBox.addItem(self.groupby_page, "")
        self.sql_page = QtWidgets.QWidget()
        self.sql_page.setGeometry(QtCore.QRect(0, 0, 181, 628))
        self.sql_page.setObjectName("sql_page")
        self.sql_run_button = QtWidgets.QPushButton(self.sql_page)
        self.sql_run_button.setGeometry(QtCore.QRect(30, 610, 99, 27))
        self.sql_run_button.setObjectName("sql_run_button")
        self.sql_plainTextEdit = QtWidgets.QPlainTextEdit(self.sql_page)
        self.sql_plainTextEdit.setGeometry(QtCore.QRect(0, 0, 181, 591))
        self.sql_plainTextEdit.setObjectName("sql_plainTextEdit")
        self.main_toolBox.addItem(self.sql_page, "")
        self.main_tableView = QtWidgets.QTableView(self.centralwidget)
        self.main_tableView.setGeometry(QtCore.QRect(210, 70, 1081, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_tableView.sizePolicy().hasHeightForWidth())
        self.main_tableView.setSizePolicy(sizePolicy)
        self.main_tableView.setProperty("showDropIndicator", True)
        self.main_tableView.setDragEnabled(True)
        self.main_tableView.setTextElideMode(QtCore.Qt.ElideLeft)
        self.main_tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.main_tableView.setSortingEnabled(True)
        self.main_tableView.setObjectName("main_tableView")
        self.main_tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.main_tableView.horizontalHeader().setDefaultSectionSize(110)
        self.main_tableView.horizontalHeader().setSortIndicatorShown(True)
        self.main_tableView.horizontalHeader().setStretchLastSection(False)
        self.main_tableView.verticalHeader().setCascadingSectionResizes(True)
        self.main_tableView.verticalHeader().setHighlightSections(False)
        self.main_tableView.verticalHeader().setSortIndicatorShown(False)
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setGeometry(QtCore.QRect(105, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.apply_button.setFont(font)
        self.apply_button.setObjectName("apply_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(15, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        unipyFrameViewerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(unipyFrameViewerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 25))
        self.menubar.setObjectName("menubar")
        unipyFrameViewerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(unipyFrameViewerWindow)
        self.statusbar.setObjectName("statusbar")
        unipyFrameViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(unipyFrameViewerWindow)
        self.main_toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(unipyFrameViewerWindow)


        self.columns_select_col_listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.columns_select_col_listView.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.columns_select_col_listView.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.columns_select_col_listView.setDragEnabled(True)
        self.columns_select_col_listView.setAcceptDrops(True)


        self.columns_remain_col_listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.columns_remain_col_listView.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.columns_remain_col_listView.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.columns_remain_col_listView.setDragEnabled(True)
        self.columns_remain_col_listView.setAcceptDrops(True)

        self.groupby_groupkey_listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.groupby_groupkey_listView.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.groupby_groupkey_listView.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.groupby_groupkey_listView.setDragEnabled(True)
        self.groupby_groupkey_listView.setAcceptDrops(True)

        self.groupby_targetkey_listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.groupby_targetkey_listView.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.groupby_targetkey_listView.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.groupby_targetkey_listView.setDragEnabled(True)
        self.groupby_targetkey_listView.setAcceptDrops(True)

        self.groupby_remains_listView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.groupby_remains_listView.setDragDropMode(Qt.QAbstractItemView.DragDrop)
        self.groupby_remains_listView.setSelectionMode(Qt.QAbstractItemView.ExtendedSelection)
        self.groupby_remains_listView.setDragEnabled(True)
        self.groupby_remains_listView.setAcceptDrops(True)

        #self.main_tableView.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)


        self.columns_select_col_listView.itemChanged.connect(self._recount_settext_colnums_listWidget)
        self.columns_remain_col_listView.itemChanged.connect(self._recount_settext_colnums_listWidget)
        #self.columns_remain_col_listView.itemChanged.connect(self._sendto_remain_columns)
        # self.columns_select_col_listView.itemEntered.connect(self._sendto_remain_columns)
        # self.columns_remain_col_listView.itemEntered.connect(self._sendto_select_columns)
        # Custom

        # Auto Calculation
        #self.END_DT_inputText.editingFinished.connect(self.auto_calculate_start_dt)
        #self.TM_WINDOW_inputText.editingFinished.connect(self.auto_calculate_start_dt)

        # Button Operation
        self.columns_to_select_button.clicked.connect(self._sendto_select_columns)
        self.columns_to_remain_button.clicked.connect(self._sendto_remain_columns)

        self.reset_button.clicked.connect(self._reload_datamodel)
        self.groupby_run_button.clicked.connect(self._groupby_run)
        self.sql_run_button.clicked.connect(self._pandasql_run)
        #self.pushButton_CONFIRM.clicked.connect(self.generate_filename)
        #self.pushButton_GETDATA.clicked.connect(self.get_data)
        #self.pushButton_CANCEL.clicked.connect(MainWindow.close)



        self.main_tableView.setSortingEnabled(True)
        #self.main_tableView.resize(self.main_tableView.maximumWidth(), self.main_tableView.maximumHeight())
        #self.main_tableView.setResizeMode(self.main_tableView.ResizeToContents)
        #self.main_tableView.setSizeAdjustPolicy(self.main_tableView.)
        self.main_tableView.resizeColumnsToContents()
        self.main_tableView.horizontalHeader().setSectionResizeMode(3)

        #data = dm.load('titanic')
        self.original_data = dm.load('adult')
        self.data = self.original_data
        self.dataModel = PandasModel(self.data)
        self.main_tableView.setModel(self.dataModel)

        self.select_colList = self.data.columns.tolist()
        self.remain_colList = []
        self.columns_select_col_listView.addItems(self.select_colList)
        self.columns_remain_col_listView.addItems(self.remain_colList)
        self.groupby_remains_listView.addItems(self.select_colList)

        self.main_indicator_frame_rowcol_number.setText(
            'row:  {rownum},  col: {colnum}'.format(rownum=self.data.shape[0], colnum=self.data.shape[1]))


        self._recount_settext_colnums_listWidget()




    def retranslateUi(self, unipyFrameViewerWindow):
        _translate = QtCore.QCoreApplication.translate
        unipyFrameViewerWindow.setWindowTitle(_translate("unipyFrameViewerWindow", "unipy DataFrame Viewer"))
        self.main_indicator_frame_rowcol_number.setText(_translate("unipyFrameViewerWindow", "row:  {rownum},  col: {colnum}"))
        self.main_toolBox.setToolTip(_translate("unipyFrameViewerWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.columns_to_select_button.setText(_translate("unipyFrameViewerWindow", "▲"))
        self.columns_indicator_select_col_number.setText(_translate("unipyFrameViewerWindow", "{select_colnum} selected"))
        self.columns_indicator_remain_col_number.setText(_translate("unipyFrameViewerWindow", "{remain_colnum} remains"))
        self.columns_to_remain_button.setText(_translate("unipyFrameViewerWindow", "▼"))
        self.main_toolBox.setItemText(self.main_toolBox.indexOf(self.columns_page), _translate("unipyFrameViewerWindow", "Columns"))
        self.groupby_groupkey_label.setText(_translate("unipyFrameViewerWindow", "GroupKey"))
        self.groupby_aggfunc_label.setText(_translate("unipyFrameViewerWindow", "AggFunc"))
        self.groupby_targetkey_label.setText(_translate("unipyFrameViewerWindow", "TargetKey"))
        self.groupby_remains_label.setText(_translate("unipyFrameViewerWindow", "Remains"))
        self.groupby_run_button.setText(_translate("unipyFrameViewerWindow", "Run"))
        self.main_toolBox.setItemText(self.main_toolBox.indexOf(self.groupby_page), _translate("unipyFrameViewerWindow", "Groupby"))
        self.sql_run_button.setText(_translate("unipyFrameViewerWindow", "Run"))
        self.sql_plainTextEdit.setPlainText(_translate("unipyFrameViewerWindow", "SELECT *\n"
"FROM data\n"
"WHERE 1=1\n"
"AND ROWNUM <= 10"))
        self.main_toolBox.setItemText(self.main_toolBox.indexOf(self.sql_page), _translate("unipyFrameViewerWindow", "SQL"))
        self.apply_button.setText(_translate("unipyFrameViewerWindow", "Apply"))
        self.reset_button.setText(_translate("unipyFrameViewerWindow", "Reset"))




    def _reload_datamodel(self):
        self.data = self.original_data
        self.dataModel = PandasModel(self.data)
        self.main_tableView.setModel(self.dataModel)

        self.select_colList = self.data.columns.tolist()
        self.remain_colList = []

        self.columns_select_col_listView.clear()
        self.columns_remain_col_listView.clear()
        self.groupby_groupkey_listView.clear()
        self.groupby_targetkey_listView.clear()
        self.groupby_remains_listView.clear()
        self.columns_select_col_listView.addItems(self.select_colList)
        self.columns_remain_col_listView.addItems(self.remain_colList)
        self.groupby_remains_listView.addItems(self.select_colList)

        self.main_indicator_frame_rowcol_number.setText(
            'row:  {rownum},  col: {colnum}'.format(rownum=self.data.shape[0], colnum=self.data.shape[1]))


    def _show_grouped_res(self):
        self.grouped_dataModel = PandasModel(self.grouped_res)
        self.main_tableView.setModel(self.grouped_dataModel)

        self.main_indicator_frame_rowcol_number.setText(
            'row:  {rownum},  col: {colnum}'.format(rownum=self.grouped_res.shape[0], colnum=self.grouped_res.shape[1]))


    def _show_sqled_res(self):
        self.sqled_dataModel = PandasModel(self.sqled_res)
        self.main_tableView.setModel(self.sqled_dataModel)

        self.main_indicator_frame_rowcol_number.setText(
            'row:  {rownum},  col: {colnum}'.format(rownum=self.sqled_res.shape[0], colnum=self.sqled_res.shape[1]))

    def _apply_condition(self):

        # Check which tab is activated
        pass


    def _drag_columns(self):
        self._recount_settext_colnums_listWidget()
        self._subset_columns()

    def _dragto_remain_columns(self):
        self._recount_settext_colnums_listWidget()
        self._subset_columns()


    def _sendto_select_columns(self):
        selectedItem = self.columns_remain_col_listView.selectedItems()


        for item in selectedItem:
            self.columns_select_col_listView.addItem(item.text())
            self.columns_remain_col_listView.takeItem(self.columns_remain_col_listView.row(item))

        self._recount_settext_colnums_listWidget()
        self._subset_columns()


    def _sendto_remain_columns(self):
        selectedItem = self.columns_select_col_listView.selectedItems()

        for item in selectedItem:
            self.columns_remain_col_listView.addItem(item.text())
            self.columns_select_col_listView.takeItem(self.columns_select_col_listView.row(item))

        self._recount_settext_colnums_listWidget()
        self._subset_columns()


    def _reset_columns_lists(self):
        self.select_colList = [self.columns_select_col_listView.item(idx).text()
                               for idx in range(self.columns_select_col_listView.count())]
        self.remain_colList = [self.columns_remain_col_listView.item(idx).text()
                               for idx in range(self.columns_remain_col_listView.count())]

        self.columns_select_col_listView.clear()
        self.columns_select_col_listView.addItems(self.select_colList)
        self.columns_remain_col_listView.clear()
        self.columns_remain_col_listView.addItems(self.remain_colList)


    def _recount_settext_colnums_listWidget(self):
        self.select_colList = [self.columns_select_col_listView.item(idx).text()
                               for idx in range(self.columns_select_col_listView.count())]
        self.remain_colList = [self.columns_remain_col_listView.item(idx).text()
                               for idx in range(self.columns_remain_col_listView.count())]

        #self.columns_select_col_listView.clear()
        #self.columns_select_col_listView.addItems(self.select_colList)
        self.columns_select_col_listView.repaint()
        #self.columns_remain_col_listView.clear()
        #self.columns_remain_col_listView.addItems(self.remain_colList)
        self.columns_select_col_listView.repaint()

        select_col_str = '{select_colnum} selected'.format(select_colnum=len(self.select_colList))
        remain_col_str = '{remain_colnum} remains'.format(remain_colnum=len(self.remain_colList))
        self.columns_indicator_select_col_number.setText(select_col_str)
        self.columns_indicator_remain_col_number.setText(remain_col_str)


    def _subset_columns(self):

        self.res_data = self.original_data[self.select_colList]
        self.subset_dataModel = PandasModel(self.res_data)
        self.main_tableView.setModel(self.subset_dataModel)

        self.main_indicator_frame_rowcol_number.setText(
            'row:  {rownum},  col: {colnum}'.format(rownum=self.res_data.shape[0], colnum=self.res_data.shape[1]))


    def _recount_settext_groupby_listWidget(self):
        self.groupby_groupkey_list = [self.groupby_groupkey_listView.item(idx).text()
                               for idx in range(self.groupby_groupkey_listView.count())]
        self.groupby_targetkey_list = [self.groupby_targetkey_listView.item(idx).text()
                               for idx in range(self.groupby_targetkey_listView.count())]


    def _groupby_run(self):
        self._recount_settext_groupby_listWidget()
        groupkey  = self.groupby_groupkey_list
        targetkey = self.groupby_targetkey_list
        self.grouped_res = self.data.groupby(groupkey)[targetkey].nunique()
        self._show_grouped_res()


    def _pandasql_run(self):
        try:
            data = self.data
            #pysqldf = lambda query: sqldf(query, globals())
            query_str = self.sql_plainTextEdit.toPlainText()
            self.sqled_res = sqldf(query_str)
            self._show_sqled_res()
        except:
            error = Qt.QErrorMessage()
            error.showMessage("Something's wrong!\nPlease re-try.")
            error.exec_()


def tv(dataFrame):
    app = QtWidgets.QApplication(sys.argv)
    unipyFrameViewerWindow = QtWidgets.QMainWindow()
    ui = Ui_unipyFrameViewerWindow()
    ui.setupUi(unipyFrameViewerWindow)
    unipyFrameViewerWindow.show()


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 70, 1111, 561))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "unipy DataFrame Viewer"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    unipyFrameViewerWindow = QtWidgets.QMainWindow()
    ui = Ui_unipyFrameViewerWindow()
    ui.setupUi(unipyFrameViewerWindow)
    unipyFrameViewerWindow.show()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

