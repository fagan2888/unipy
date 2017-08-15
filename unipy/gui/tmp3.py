import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class MyWindow(Qt.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.table = Qt.QTableWidget(5,5)
        self.table.setHorizontalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.setVerticalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)

        layout = Qt.QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def changeHorizontalHeader(self, index):
        oldHeader = self.table.horizontalHeaderItem(index).text()
        newHeader, ok = Qt.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       Qt.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.table.horizontalHeaderItem(index).setText(newHeader)


class MetaHeaderView(Qt.QHeaderView):
    def __init__(self, orientation, parent=None):
        super(MetaHeaderView, self).__init__(orientation, parent)
        self.setMovable(True)
        self.setClickable(True)
        # This block sets up the edit line by making setting the parent
        # to the Headers Viewport.
        self.line = Qt.QLineEdit(parent=self.viewport())  # Create
        self.line.setAlignment(QtCore.Qt.AlignTop)  # Set the Alignmnet
        self.line.setHidden(True)  # Hide it till its needed
        # This is needed because I am having a werid issue that I believe has
        # to do with it losing focus after editing is done.
        self.line.blockSignals(True)
        self.sectionedit = 0
        # Connects to double click
        self.sectionDoubleClicked.connect(self.editHeader)
        self.line.editingFinished.connect(self.doneEditing)

    def doneEditing(self):
        # This block signals needs to happen first otherwise I have lose focus
        # problems again when there are no rows
        self.line.blockSignals(True)
        self.line.setHidden(True)
        oldname = self.model().dataset.field(self.sectionedit)
        newname = str(self.line.text())
        self.model().dataset.changeFieldName(oldname, newname)
        self.line.setText('')
        self.setCurrentIndex(QtCore.QModelIndex())

    def editHeader(self, section):
        # This block sets up the geometry for the line edit
        edit_geometry = self.line.geometry()
        edit_geometry.setWidth(self.sectionSize(section))
        edit_geometry.moveLeft(self.sectionViewportPosition(section))
        self.line.setGeometry(edit_geometry)

        self.line.setText(self.model().dataset.field(section).name)
        self.line.setHidden(False)  # Make it visiable
        self.line.blockSignals(False)  # Let it send signals
        self.line.setFocus()
        self.line.selectAll()
        self.sectionedit = section


if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    main = MyWindow()
    main.show()

    sys.exit(app.exec_())