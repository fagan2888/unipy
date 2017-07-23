# -*- coding: utf-8 -*-
"""
Created on 22/07/17 02:32

@author: pydemia
"""


def __init__(self, model, view):
    QAbstractTableModel.__init__(self)
    self.model = model
    self.view = view
    self.view.setModel(self)
    self._lastClickedColumn = 0
    self.columnMenu = QMenu()
    for index, fieldId in enumerate(FIELD_ORDER):
        fieldName = FIELD_NAMES[fieldId]
        action = self.columnMenu.addAction(fieldName)
        action.setData(index)
        action.triggered.connect(self.columnMenuItemClicked)
    self.view.horizontalHeader().sectionClicked.connect(self.tableSectionClicked)
