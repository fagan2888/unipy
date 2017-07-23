# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataQueryTool_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import datetime as dt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        self.menuPopup = QtWidgets.QMenu(self.menubar)
        self.menuPopup.setObjectName("menuPopup")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMenu1 = QtWidgets.QAction(MainWindow)
        self.actionMenu1.setObjectName("actionMenu1")
        self.actionSetting1 = QtWidgets.QAction(MainWindow)
        self.actionSetting1.setObjectName("actionSetting1")
        self.menuPopup.addAction(self.actionMenu1)
        self.menuSetting.addAction(self.actionSetting1)
        self.menubar.addAction(self.menuPopup.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        # Main Label Font Size
        font = QtGui.QFont()
        font.setPointSize(16)

        # Base Layout
        self.vertical_line_01 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_01.setGeometry(QtCore.QRect(360, 24, 20, 271))
        self.vertical_line_01.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_01.setObjectName("vertical_line_01")

        self.vertical_line_02 = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line_02.setGeometry(QtCore.QRect(710, 22, 20, 151))
        self.vertical_line_02.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_02.setObjectName("vertical_line_02")

        self.horizontal_line = QtWidgets.QFrame(self.centralwidget)
        self.horizontal_line.setGeometry(QtCore.QRect(370, 166, 691, 16))
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line.setObjectName("horizontal_line")

        # Button : Confirm
        self.pushButton_CONFIRM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CONFIRM.setGeometry(QtCore.QRect(730, 260, 99, 27))
        self.pushButton_CONFIRM.setObjectName("pushButton_CONFIRM")

        # Button : Get Data
        self.pushButton_GETDATA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GETDATA.setGeometry(QtCore.QRect(840, 260, 99, 27))
        self.pushButton_GETDATA.setObjectName("pushButton_CONFIRM")

        # Button: Cancel
        self.pushButton_CANCEL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CANCEL.setGeometry(QtCore.QRect(950, 260, 99, 27))
        self.pushButton_CANCEL.setObjectName("pushButton_CANCEL")

        # X Value
        self.X_label = QtWidgets.QLabel(self.centralwidget)
        self.X_label.setGeometry(QtCore.QRect(120, 16, 101, 21))
        self.X_label.setFont(font)
        self.X_label.setAlignment(QtCore.Qt.AlignCenter)
        self.X_label.setObjectName("X_label")

        self.FAB_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.FAB_ID_label.setGeometry(QtCore.QRect(22, 60, 101, 17))
        self.FAB_ID_label.setObjectName("FAC_ID_label")
        self.FAB_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.FAB_ID_inputText.setGeometry(QtCore.QRect(140, 56, 211, 27))
        self.FAB_ID_inputText.setObjectName("FAC_ID_inputText")

        self.AREA_CD_label = QtWidgets.QLabel(self.centralwidget)
        self.AREA_CD_label.setGeometry(QtCore.QRect(22, 90, 101, 17))
        self.AREA_CD_label.setObjectName("AREA_CD_label")
        self.AREA_CD_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.AREA_CD_inputText.setGeometry(QtCore.QRect(140, 86, 211, 27))
        self.AREA_CD_inputText.setObjectName("AREA_CD_inputText")

        self.EQP_MODEL_label = QtWidgets.QLabel(self.centralwidget)
        self.EQP_MODEL_label.setGeometry(QtCore.QRect(22, 120, 101, 17))
        self.EQP_MODEL_label.setObjectName("EQP_MODEL_label")
        self.EQP_MODEL_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.EQP_MODEL_inputText.setGeometry(QtCore.QRect(140, 116, 211, 27))
        self.EQP_MODEL_inputText.setObjectName("EQP_MODEL_inputText")

        self.EQP_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.EQP_ID_label.setGeometry(QtCore.QRect(22, 150, 101, 17))
        self.EQP_ID_label.setObjectName("EQP_ID_label")
        self.EQP_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.EQP_ID_inputText.setGeometry(QtCore.QRect(140, 146, 211, 27))
        self.EQP_ID_inputText.setObjectName("EQP_ID_inputText")

        self.RECIPE_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.RECIPE_ID_label.setGeometry(QtCore.QRect(22, 180, 101, 17))
        self.RECIPE_ID_label.setObjectName("RECIPE_ID_label")
        self.RECIPE_ID_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.RECIPE_ID_inputText.setGeometry(QtCore.QRect(140, 176, 211, 27))
        self.RECIPE_ID_inputText.setObjectName("RECIPE_ID_inputText")

        self.END_DT_label = QtWidgets.QLabel(self.centralwidget)
        self.END_DT_label.setGeometry(QtCore.QRect(22, 210, 101, 17))
        self.END_DT_label.setObjectName("END_DT_label")
        self.END_DT_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.END_DT_inputText.setGeometry(QtCore.QRect(140, 206, 121, 27))
        self.END_DT_inputText.setObjectName("END_DT_inputText")

        self.END_TM_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.END_TM_Text.setGeometry(QtCore.QRect(270, 206, 81, 27))
        self.END_TM_Text.setReadOnly(True)
        self.END_TM_Text.setObjectName("END_TM_Text")

        self.TM_WINDOW_label = QtWidgets.QLabel(self.centralwidget)
        self.TM_WINDOW_label.setGeometry(QtCore.QRect(22, 239, 101, 17))
        self.TM_WINDOW_label.setObjectName("TM_WINDOW_label")
        self.TM_WINDOW_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.TM_WINDOW_inputText.setGeometry(QtCore.QRect(140, 236, 51, 27))
        self.TM_WINDOW_inputText.setObjectName("TM_WINDOW_inputText")

        self.START_DT_label = QtWidgets.QLabel(self.centralwidget)
        self.START_DT_label.setGeometry(QtCore.QRect(20, 270, 101, 17))
        self.START_DT_label.setObjectName("START_DT_label")
        self.START_DT_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.START_DT_inputText.setGeometry(QtCore.QRect(140, 266, 121, 27))
        self.START_DT_inputText.setText("")
        self.START_DT_inputText.setReadOnly(True)
        self.START_DT_inputText.setObjectName("START_DT_inputText")

        self.START_TM_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.START_TM_Text.setGeometry(QtCore.QRect(270, 266, 81, 27))
        self.START_TM_Text.setReadOnly(True)
        self.START_TM_Text.setObjectName("START_TM_Text")

        # R Value
        self.R_label = QtWidgets.QLabel(self.centralwidget)
        self.R_label.setGeometry(QtCore.QRect(470, 16, 141, 21))
        self.R_label.setFont(font)
        self.R_label.setAlignment(QtCore.Qt.AlignCenter)
        self.R_label.setObjectName("R_label")

        self.ROPER_label = QtWidgets.QLabel(self.centralwidget)
        self.ROPER_label.setGeometry(QtCore.QRect(390, 60, 101, 17))
        self.ROPER_label.setObjectName("ROPER_label")
        self.ROPER_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.ROPER_inputText.setGeometry(QtCore.QRect(490, 56, 211, 27))
        self.ROPER_inputText.setObjectName("ROPER_inputText")

        self.RPRMT_NM_label = QtWidgets.QLabel(self.centralwidget)
        self.RPRMT_NM_label.setGeometry(QtCore.QRect(390, 120, 101, 17))
        self.RPRMT_NM_label.setObjectName("RPRMT_NM_label")
        self.RPRMT_NM_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.RPRMT_NM_inputText.setGeometry(QtCore.QRect(490, 116, 211, 27))
        self.RPRMT_NM_inputText.setObjectName("RPRMT_NM_inputText")

        # Y Value
        self.Y_label = QtWidgets.QLabel(self.centralwidget)
        self.Y_label.setGeometry(QtCore.QRect(840, 16, 101, 21))
        self.Y_label.setFont(font)
        self.Y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_label.setObjectName("Y_label")

        self.YTYPE_label = QtWidgets.QLabel(self.centralwidget)
        self.YTYPE_label.setGeometry(QtCore.QRect(740, 90, 101, 17))
        self.YTYPE_label.setObjectName("YTYPE_label")
        self.YTYPE_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YTYPE_inputText.setGeometry(QtCore.QRect(840, 86, 211, 27))
        self.YTYPE_inputText.setObjectName("YTYPE_inputText")

        self.YPRMT_NM_label = QtWidgets.QLabel(self.centralwidget)
        self.YPRMT_NM_label.setGeometry(QtCore.QRect(740, 120, 101, 17))
        self.YPRMT_NM_label.setObjectName("YPRMT_NM_label")
        self.YPRMT_NM_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YPRMT_NM_inputText.setGeometry(QtCore.QRect(840, 116, 211, 27))
        self.YPRMT_NM_inputText.setObjectName("YPRMT_NM_inputText")

        self.YOPER_label = QtWidgets.QLabel(self.centralwidget)
        self.YOPER_label.setGeometry(QtCore.QRect(740, 60, 101, 17))
        self.YOPER_label.setObjectName("YOPER_label")
        self.YOPER_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.YOPER_inputText.setGeometry(QtCore.QRect(840, 56, 211, 27))
        self.YOPER_inputText.setObjectName("YOPER_inputText")

        # Save Arguments
        self.FILENAME_label = QtWidgets.QLabel(self.centralwidget)
        self.FILENAME_label.setGeometry(QtCore.QRect(400, 199, 101, 17))
        self.FILENAME_label.setObjectName("FILENAME_label")
        self.FILENAME_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.FILENAME_inputText.setGeometry(QtCore.QRect(500, 194, 551, 27))
        self.FILENAME_inputText.setReadOnly(True)
        self.FILENAME_inputText.setObjectName("FILENAME_inputText")

        self.DIRECTORY_label = QtWidgets.QLabel(self.centralwidget)
        self.DIRECTORY_label.setGeometry(QtCore.QRect(400, 230, 101, 17))
        self.DIRECTORY_label.setObjectName("DIRECTORY_label")
        self.DIRECTORY_inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.DIRECTORY_inputText.setGeometry(QtCore.QRect(500, 225, 551, 27))
        self.DIRECTORY_inputText.setReadOnly(True)
        self.DIRECTORY_inputText.setObjectName("DIRECTORY_inputText")

        self.retranslateUi(MainWindow)

        # Auto Calculation
        self.END_DT_inputText.editingFinished.connect(self.auto_calculate_start_dt)
        self.TM_WINDOW_inputText.editingFinished.connect(self.auto_calculate_start_dt)

        # Button Operation
        self.pushButton_CONFIRM.clicked.connect(self.generate_filename)
        self.pushButton_GETDATA.clicked.connect(self.get_data)
        self.pushButton_CANCEL.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCC Data Selector"))
        self.pushButton_CONFIRM.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_CANCEL.setText(_translate("MainWindow", "Cancel"))

        # X Value
        self.X_label.setText(_translate("MainWindow", "X value"))
        self.FAB_ID_inputText.setText(_translate("MainWindow", "M14"))
        self.FAB_ID_label.setText(_translate("MainWindow", "FAC_ID"))
        self.AREA_CD_label.setText(_translate("MainWindow", "AREA_CD"))
        self.AREA_CD_inputText.setText(_translate("MainWindow", "T/F"))
        self.EQP_MODEL_label.setText(_translate("MainWindow", "EQP_MODEL"))
        self.EQP_MODEL_inputText.setText(_translate("MainWindow", "CHALLENGER_HT"))
        self.EQP_ID_label.setText(_translate("MainWindow", "EQP_ID"))
        self.EQP_ID_inputText.setText(_translate("MainWindow", "4TPE1601"))
        self.RECIPE_ID_label.setText(_translate("MainWindow", "RECIPE_ID"))
        self.RECIPE_ID_inputText.setText(_translate("MainWindow", "DE_ARC_450_ABC"))
        self.END_DT_label.setText(_translate("MainWindow", "END_DT_TM"))
        self.END_DT_inputText.setText(_translate("MainWindow", "20170303"))
        self.END_TM_Text.setText(_translate("MainWindow", "065959"))
        self.TM_WINDOW_label.setText(_translate("MainWindow", "TM_WINDOW"))
        self.TM_WINDOW_inputText.setText(_translate("MainWindow", "2"))
        self.START_DT_label.setText(_translate("MainWindow", "START_DT_TM"))
        self.START_TM_Text.setText(_translate("MainWindow", "070000"))

        # R Value
        self.R_label.setText(_translate("MainWindow", "Resp. value"))
        self.ROPER_label.setText(_translate("MainWindow", "OPER"))
        self.ROPER_inputText.setText(_translate("MainWindow", "A1017014A"))
        self.RPRMT_NM_label.setText(_translate("MainWindow", "PRMT_NM"))
        self.RPRMT_NM_inputText.setText(_translate("MainWindow", "PT1H"))

        # Y Value
        self.Y_label.setText(_translate("MainWindow", "Y value"))
        self.YOPER_label.setText(_translate("MainWindow", "OPER"))
        self.YOPER_inputText.setText(_translate("MainWindow", "Z1020000A"))
        self.YTYPE_label.setText(_translate("MainWindow", "TYPE"))
        self.YTYPE_inputText.setText(_translate("MainWindow", "PT1H"))
        self.YPRMT_NM_label.setText(_translate("MainWindow", "PRMT_NM"))
        self.YPRMT_NM_inputText.setText(_translate("MainWindow", "PT1H"))

        # Save Arguments
        self.FILENAME_label.setText(_translate("MainWindow", "FILENAME"))
        self.FILENAME_inputText.setText(_translate("MainWindow", "Press 'Confirm' to generate"))
        self.DIRECTORY_inputText.setText(_translate("MainWindow", "D:/workspaces/SKHy_MCC/300. Python/mcc_pjt"))
        self.DIRECTORY_label.setText(_translate("MainWindow", "DIRECTORY"))

        self.menuPopup.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionMenu1.setText(_translate("MainWindow", "menu1"))
        self.actionSetting1.setText(_translate("MainWindow", "setting1"))


    def auto_calculate_start_dt(self):
        self.end_dt_tm_str = self.END_DT_inputText.text() + self.END_TM_Text.text()
        self.end_dt_tm_timed = dt.datetime.strptime(self.end_dt_tm_str, '%Y%m%d%H%M%S')
        self.tm_window_timed = dt.timedelta(days=int(self.TM_WINDOW_inputText.text()))

        self.start_dt_tm_timed = self.end_dt_tm_timed - self.tm_window_timed
        self.start_dt_tm_str = self.start_dt_tm_timed.strftime('%Y%m%d%H%M%S')
        self.start_dt_str = self.start_dt_tm_timed.strftime('%Y%m%d')

        _translate = QtCore.QCoreApplication.translate
        self.END_DT_inputText.setText(_translate("MainWindow", self.start_dt_str))


    def generate_filename(self):
        area_str = self.AREA_CD_inputText.text().replace('/', '')
        filename_str = 'MCC-{fab_id}-{area_cd}-{eqp_id}-{recipe_id}-{r_oper_id}-{r_prmt}-{y_prmt}-{start_dt_tm}-{end_dt_tm}.csv'
        self.filename = filename_str.format(fab_id=self.FAB_ID_inputText.text(),
                                            area_cd=self.AREA_CD_inputText.text(),
                                            eqp_id=self.EQP_ID_inputText.text(),
                                            recipe_id=self.RECIPE_ID_inputText.text(),
                                            r_oper_id=self.ROPER_inputText.text(),
                                            r_prmt=self.RPRMT_NM_inputText.text(),
                                            y_prmt=self.YPRMT_NM_inputText.text(),
                                            start_dt_tm=self.start_dt_tm_str,
                                            end_dt_tm=self.end_dt_tm_str)
        _translate = QtCore.QCoreApplication.translate
        self.FILENAME_inputText.setText(_translate("MainWindow", self.filename))


    def get_data(self):
        MainWindow.close
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

