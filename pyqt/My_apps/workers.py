# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workers.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HRM_Workers_view(object):
    def setupUi(self, HRM_Workers_view):
        HRM_Workers_view.setObjectName("HRM_Workers_view")
        HRM_Workers_view.resize(1218, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HRM_Workers_view.setWindowIcon(icon)
        HRM_Workers_view.setStyleSheet("background-color:rgb(40, 93, 117);")
        self.tabWidget = QtWidgets.QTabWidget(HRM_Workers_view)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 1181, 591))
        font = QtGui.QFont()
        font.setFamily("System")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 1111, 521))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lcdNumber_user_id = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber_user_id.setGeometry(QtCore.QRect(80, 20, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_user_id.sizePolicy().hasHeightForWidth())
        self.lcdNumber_user_id.setSizePolicy(sizePolicy)
        self.lcdNumber_user_id.setMinimumSize(QtCore.QSize(31, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_user_id.setFont(font)
        self.lcdNumber_user_id.setObjectName("lcdNumber_user_id")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 89, 1051, 423))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_12.addWidget(self.label_19)
        self.lineEdit_IDNo = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_IDNo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_IDNo.setObjectName("lineEdit_IDNo")
        self.verticalLayout_12.addWidget(self.lineEdit_IDNo)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_13.addWidget(self.label_20)
        self.lineEdit_hrm_code = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_hrm_code.setEnabled(False)
        self.lineEdit_hrm_code.setObjectName("lineEdit_hrm_code")
        self.verticalLayout_13.addWidget(self.lineEdit_hrm_code)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_14.addWidget(self.label_21)
        self.dateTimeEdit_stamp = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_stamp.setEnabled(False)
        self.dateTimeEdit_stamp.setMinimumDate(QtCore.QDate(2018, 7, 12))
        self.dateTimeEdit_stamp.setObjectName("dateTimeEdit_stamp")
        self.verticalLayout_14.addWidget(self.dateTimeEdit_stamp)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_15.addWidget(self.label_22)
        self.lineEdit_kra_pin = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_kra_pin.setObjectName("lineEdit_kra_pin")
        self.verticalLayout_15.addWidget(self.lineEdit_kra_pin)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        self.lineEdit_regNo = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_regNo.setEnabled(False)
        self.lineEdit_regNo.setObjectName("lineEdit_regNo")
        self.verticalLayout_10.addWidget(self.lineEdit_regNo)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_4.addWidget(self.label_33)
        self.textEdit_address = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_address.setObjectName("textEdit_address")
        self.verticalLayout_4.addWidget(self.textEdit_address)
        self.verticalLayout_14.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem)
        self.verticalLayout_11.addLayout(self.verticalLayout_14)
        self.horizontalLayout_24.addLayout(self.verticalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem1)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_16.addWidget(self.line_2)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_6.addWidget(self.label_23)
        self.lineEdit_fn = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_fn.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.horizontalLayout_6.addWidget(self.lineEdit_fn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.lineEdit_mn = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_mn.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_mn.setObjectName("lineEdit_mn")
        self.horizontalLayout_5.addWidget(self.lineEdit_mn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        self.lineEdit_ln = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ln.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_ln.setObjectName("lineEdit_ln")
        self.horizontalLayout_8.addWidget(self.lineEdit_ln)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.lineEdit_tell = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tell.sizePolicy().hasHeightForWidth())
        self.lineEdit_tell.setSizePolicy(sizePolicy)
        self.lineEdit_tell.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_tell.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_tell.setObjectName("lineEdit_tell")
        self.horizontalLayout_11.addWidget(self.lineEdit_tell)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_10.addWidget(self.label_30)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_10.addWidget(self.lineEdit_email)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)
        self.radioButton_m = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_m.setObjectName("radioButton_m")
        self.horizontalLayout_4.addWidget(self.radioButton_m)
        self.radioButton_f = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_f.setObjectName("radioButton_f")
        self.horizontalLayout_4.addWidget(self.radioButton_f)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_3.addWidget(self.label_26)
        self.dateEdit_dob = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_dob.setMaximumDate(QtCore.QDate(2018, 9, 14))
        self.dateEdit_dob.setMinimumDate(QtCore.QDate(1920, 9, 14))
        self.dateEdit_dob.setCalendarPopup(True)
        self.dateEdit_dob.setObjectName("dateEdit_dob")
        self.horizontalLayout_3.addWidget(self.dateEdit_dob)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_17.addLayout(self.verticalLayout_7)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_skill = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_skill.sizePolicy().hasHeightForWidth())
        self.comboBox_skill.setSizePolicy(sizePolicy)
        self.comboBox_skill.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_skill.setObjectName("comboBox_skill")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.comboBox_skill.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_skill)
        self.verticalLayout_16.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(170, 210))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 150, 178))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_hr = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_hr.setObjectName("radioButton_hr")
        self.verticalLayout.addWidget(self.radioButton_hr)
        self.radioButton_day = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_day.setObjectName("radioButton_day")
        self.verticalLayout.addWidget(self.radioButton_day)
        self.radioButton_5day = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_5day.setObjectName("radioButton_5day")
        self.verticalLayout.addWidget(self.radioButton_5day)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(160, 160))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget_6 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 20, 131, 131))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_9.addWidget(self.radioButton_2)
        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_9.addWidget(self.radioButton_8)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_9 = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_9.addWidget(self.radioButton_9)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_9.addWidget(self.radioButton)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.spinBox_experience = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_experience.setObjectName("spinBox_experience")
        self.horizontalLayout_13.addWidget(self.spinBox_experience)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_16.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(270, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem3)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_16.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_24.addLayout(self.verticalLayout_16)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(360, 20, 471, 54))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.layoutWidget.raise_()
        self.label.raise_()
        self.lcdNumber_user_id.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1121, 521))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget_records = QtWidgets.QTableView(self.formLayoutWidget)
        self.tableWidget_records.setMinimumSize(QtCore.QSize(1000, 500))
        self.tableWidget_records.setAlternatingRowColors(True)
        self.tableWidget_records.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_records.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_records.setObjectName("tableWidget_records")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tableWidget_records)
        self.tabWidget.addTab(self.tab_4, "")
        self.layoutWidget2 = QtWidgets.QWidget(HRM_Workers_view)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 650, 687, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem4)
        self.pushButton_reg = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.horizontalLayout_23.addWidget(self.pushButton_reg)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem5)
        self.pushButton_update = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_23.addWidget(self.pushButton_update)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem6)
        self.pushButton_delete = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_23.addWidget(self.pushButton_delete)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.pushButton_login = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_23.addWidget(self.pushButton_login)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem8)
        self.pushButton_back = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_23.addWidget(self.pushButton_back)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem9)
        self.label_19.setBuddy(self.lineEdit_IDNo)
        self.label_20.setBuddy(self.lineEdit_hrm_code)
        self.label_21.setBuddy(self.dateTimeEdit_stamp)
        self.label_22.setBuddy(self.lineEdit_kra_pin)
        self.label_18.setBuddy(self.lineEdit_regNo)
        self.label_33.setBuddy(self.textEdit_address)
        self.label_23.setBuddy(self.lineEdit_fn)
        self.label_24.setBuddy(self.lineEdit_mn)
        self.label_25.setBuddy(self.lineEdit_ln)
        self.label_29.setBuddy(self.lineEdit_tell)
        self.label_30.setBuddy(self.lineEdit_email)
        self.label_27.setBuddy(self.radioButton_f)
        self.label_26.setBuddy(self.dateEdit_dob)
        self.label_2.setBuddy(self.comboBox_skill)

        self.retranslateUi(HRM_Workers_view)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HRM_Workers_view)

    def retranslateUi(self, HRM_Workers_view):
        _translate = QtCore.QCoreApplication.translate
        HRM_Workers_view.setWindowTitle(_translate("HRM_Workers_view", "New Worker Registration"))
        self.groupBox_3.setTitle(_translate("HRM_Workers_view", "Enter New Worker Details"))
        self.lcdNumber_user_id.setStatusTip(_translate("HRM_Workers_view", "Auto Count the number of worker in the system"))
        self.label_19.setText(_translate("HRM_Workers_view", "National ID No."))
        self.lineEdit_IDNo.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Nation ID Number "))
        self.label_20.setText(_translate("HRM_Workers_view", "Worker HRM Code :"))
        self.lineEdit_hrm_code.setStatusTip(_translate("HRM_Workers_view", "Auto filled HRM Code"))
        self.label_21.setText(_translate("HRM_Workers_view", "Registration Date Stamp"))
        self.dateTimeEdit_stamp.setStatusTip(_translate("HRM_Workers_view", "System time stamp"))
        self.label_22.setText(_translate("HRM_Workers_view", "KRA PIN"))
        self.lineEdit_kra_pin.setStatusTip(_translate("HRM_Workers_view", "Enter Kenya Revenue of Authority Personal Identification Number"))
        self.label_18.setText(_translate("HRM_Workers_view", "Registration Number:"))
        self.lineEdit_regNo.setStatusTip(_translate("HRM_Workers_view", "Auto-filled User Registration number"))
        self.label_33.setText(_translate("HRM_Workers_view", "Address :"))
        self.textEdit_address.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Physical address"))
        self.label_23.setText(_translate("HRM_Workers_view", "First Name :"))
        self.lineEdit_fn.setStatusTip(_translate("HRM_Workers_view", "Enter Worker First Name"))
        self.label_24.setText(_translate("HRM_Workers_view", "Middle Name :"))
        self.lineEdit_mn.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Middle name"))
        self.label_25.setText(_translate("HRM_Workers_view", "Last Name :"))
        self.lineEdit_ln.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Last Name"))
        self.label_29.setText(_translate("HRM_Workers_view", "Phone Number :"))
        self.lineEdit_tell.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Phone  Number"))
        self.label_30.setText(_translate("HRM_Workers_view", "Email :"))
        self.lineEdit_email.setStatusTip(_translate("HRM_Workers_view", "Enter Worker Email address"))
        self.label_27.setStatusTip(_translate("HRM_Workers_view", "Select worker gender"))
        self.label_27.setText(_translate("HRM_Workers_view", "Gender"))
        self.radioButton_m.setText(_translate("HRM_Workers_view", "Male"))
        self.radioButton_f.setText(_translate("HRM_Workers_view", "Female"))
        self.label_26.setText(_translate("HRM_Workers_view", "Date Of Birth :"))
        self.dateEdit_dob.setStatusTip(_translate("HRM_Workers_view", "select woker date of birth"))
        self.dateEdit_dob.setDisplayFormat(_translate("HRM_Workers_view", "d/M/yyyy"))
        self.label_2.setText(_translate("HRM_Workers_view", "Skill- Set Category"))
        self.comboBox_skill.setStatusTip(_translate("HRM_Workers_view", "Select worker skill set"))
        self.comboBox_skill.setItemText(0, _translate("HRM_Workers_view", "Select a Speciallity Category..."))
        self.comboBox_skill.setItemText(1, _translate("HRM_Workers_view", "House Keeping"))
        self.comboBox_skill.setItemText(2, _translate("HRM_Workers_view", "Personal/Property Security"))
        self.comboBox_skill.setItemText(3, _translate("HRM_Workers_view", "Property Management"))
        self.comboBox_skill.setItemText(4, _translate("HRM_Workers_view", "Catering Services"))
        self.comboBox_skill.setItemText(5, _translate("HRM_Workers_view", "Chef/Cook"))
        self.comboBox_skill.setItemText(6, _translate("HRM_Workers_view", "Engineer- Electrical"))
        self.comboBox_skill.setItemText(7, _translate("HRM_Workers_view", "Engineer- water"))
        self.comboBox_skill.setItemText(8, _translate("HRM_Workers_view", "Engineer- vehicle"))
        self.comboBox_skill.setItemText(9, _translate("HRM_Workers_view", "Engineer- constraction"))
        self.comboBox_skill.setItemText(10, _translate("HRM_Workers_view", "Engineer- Agriculture"))
        self.comboBox_skill.setItemText(11, _translate("HRM_Workers_view", "Engineer- computer"))
        self.comboBox_skill.setItemText(12, _translate("HRM_Workers_view", "Engineer- telecommunication"))
        self.groupBox_2.setTitle(_translate("HRM_Workers_view", "Payment Mode"))
        self.radioButton_hr.setText(_translate("HRM_Workers_view", "per Hour"))
        self.radioButton_day.setText(_translate("HRM_Workers_view", "per Day"))
        self.radioButton_5day.setText(_translate("HRM_Workers_view", "per Week(5 days)"))
        self.radioButton_4.setText(_translate("HRM_Workers_view", "per Week(6 days)"))
        self.radioButton_5.setText(_translate("HRM_Workers_view", "per Week(7 days)"))
        self.radioButton_6.setText(_translate("HRM_Workers_view", "per Month(21 days)"))
        self.radioButton_7.setText(_translate("HRM_Workers_view", "per Month(25)"))
        self.groupBox_4.setStatusTip(_translate("HRM_Workers_view", "Select worker availabilty"))
        self.groupBox_4.setTitle(_translate("HRM_Workers_view", "Availability"))
        self.radioButton_2.setText(_translate("HRM_Workers_view", "Immediatelly"))
        self.radioButton_8.setText(_translate("HRM_Workers_view", "a day Notice"))
        self.radioButton_3.setText(_translate("HRM_Workers_view", "two weeks Notice"))
        self.radioButton_9.setText(_translate("HRM_Workers_view", "a week Notice"))
        self.radioButton.setText(_translate("HRM_Workers_view", "a Month Notice"))
        self.label_3.setText(_translate("HRM_Workers_view", "Experience :Years"))
        self.spinBox_experience.setStatusTip(_translate("HRM_Workers_view", "Select woker experience Level"))
        self.label.setText(_translate("HRM_Workers_view", "Human Resource Managment System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("HRM_Workers_view", "Data Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("HRM_Workers_view", "Data View"))
        self.pushButton_reg.setText(_translate("HRM_Workers_view", "Register"))
        self.pushButton_update.setText(_translate("HRM_Workers_view", "Update"))
        self.pushButton_delete.setText(_translate("HRM_Workers_view", "Delete"))
        self.pushButton_login.setText(_translate("HRM_Workers_view", "Reset"))
        self.pushButton_back.setText(_translate("HRM_Workers_view", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HRM_Workers_view = QtWidgets.QDialog()
    ui = Ui_HRM_Workers_view()
    ui.setupUi(HRM_Workers_view)
    HRM_Workers_view.show()
    sys.exit(app.exec_())

