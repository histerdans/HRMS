# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HRM_Signup_view(object):
    def setupUi(self, HRM_Signup_view):
        HRM_Signup_view.setObjectName("HRM_Signup_view")
        HRM_Signup_view.resize(871, 696)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HRM_Signup_view.setWindowIcon(icon)
        HRM_Signup_view.setStyleSheet("background-color:rgb(40, 93, 117);color:rgb(0, 255, 255)")
        self.verticalLayoutWidget = QtWidgets.QWidget(HRM_Signup_view)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 681, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(22)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_fn = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.horizontalLayout_2.addWidget(self.lineEdit_fn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_mn = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_mn.setObjectName("lineEdit_mn")
        self.horizontalLayout_3.addWidget(self.lineEdit_mn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_ln = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_ln.setObjectName("lineEdit_ln")
        self.horizontalLayout_4.addWidget(self.lineEdit_ln)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_un = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_un.setObjectName("lineEdit_un")
        self.horizontalLayout_5.addWidget(self.lineEdit_un)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_tell = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_tell.setObjectName("lineEdit_tell")
        self.horizontalLayout_6.addWidget(self.lineEdit_tell)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_7.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_pswrd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_pswrd.setObjectName("lineEdit_pswrd")
        self.horizontalLayout_8.addWidget(self.lineEdit_pswrd)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_cpswrd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cpswrd.setObjectName("lineEdit_cpswrd")
        self.horizontalLayout_9.addWidget(self.lineEdit_cpswrd)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.dateEdit_dob = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_dob.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 7, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit_dob.setCalendarPopup(True)
        self.dateEdit_dob.setObjectName("dateEdit_dob")
        self.horizontalLayout_11.addWidget(self.dateEdit_dob)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(120, 80))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 73, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_m = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(82)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.radioButton_m.sizePolicy().hasHeightForWidth())
        self.radioButton_m.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.radioButton_m.setFont(font)
        self.radioButton_m.setObjectName("radioButton_m")
        self.verticalLayout_4.addWidget(self.radioButton_m)
        self.radioButton_f = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(82)
        sizePolicy.setVerticalStretch(17)
        sizePolicy.setHeightForWidth(self.radioButton_f.sizePolicy().hasHeightForWidth())
        self.radioButton_f.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("System")
        self.radioButton_f.setFont(font)
        self.radioButton_f.setObjectName("radioButton_f")
        self.verticalLayout_4.addWidget(self.radioButton_f)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_signup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.horizontalLayout.addWidget(self.pushButton_signup)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.label_10.setBuddy(self.dateEdit_dob)

        self.retranslateUi(HRM_Signup_view)
        QtCore.QMetaObject.connectSlotsByName(HRM_Signup_view)

    def retranslateUi(self, HRM_Signup_view):
        _translate = QtCore.QCoreApplication.translate
        HRM_Signup_view.setWindowTitle(_translate("HRM_Signup_view", "Registration"))
        self.label_11.setText(_translate("HRM_Signup_view", "Human Resource Management System"))
        self.label.setText(_translate("HRM_Signup_view", "Super User Registration"))
        self.lineEdit_fn.setStatusTip(_translate("HRM_Signup_view", "Please Enter your First Name"))
        self.lineEdit_fn.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your First Name"))
        self.lineEdit_mn.setStatusTip(_translate("HRM_Signup_view", "Please Enter your Middle Name"))
        self.lineEdit_mn.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your Middle Name"))
        self.lineEdit_ln.setStatusTip(_translate("HRM_Signup_view", "Please Enter your Last Name"))
        self.lineEdit_ln.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your Last Name"))
        self.lineEdit_un.setStatusTip(_translate("HRM_Signup_view", "Please Enter your User  Name"))
        self.lineEdit_un.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your User Name"))
        self.lineEdit_tell.setStatusTip(_translate("HRM_Signup_view", "Please Enter your Phone Number"))
        self.lineEdit_tell.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your Phone Number"))
        self.lineEdit_email.setStatusTip(_translate("HRM_Signup_view", "Please Enter your Email Address"))
        self.lineEdit_email.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your Email Address"))
        self.lineEdit_pswrd.setStatusTip(_translate("HRM_Signup_view", "Please Enter your account Password"))
        self.lineEdit_pswrd.setPlaceholderText(_translate("HRM_Signup_view", "Enter Your Password"))
        self.lineEdit_cpswrd.setStatusTip(_translate("HRM_Signup_view", "Please Confirm your account Password"))
        self.lineEdit_cpswrd.setPlaceholderText(_translate("HRM_Signup_view", "Comfirm Your account Password"))
        self.label_10.setText(_translate("HRM_Signup_view", "DOB :"))
        self.dateEdit_dob.setDisplayFormat(_translate("HRM_Signup_view", "d/M/yyyy"))
        self.groupBox.setTitle(_translate("HRM_Signup_view", "Gender"))
        self.radioButton_m.setText(_translate("HRM_Signup_view", "Male"))
        self.radioButton_f.setText(_translate("HRM_Signup_view", "Female"))
        self.pushButton_signup.setText(_translate("HRM_Signup_view", "Create Account"))
        self.pushButton_login.setText(_translate("HRM_Signup_view", "Login"))
        self.pushButton_back.setText(_translate("HRM_Signup_view", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HRM_Signup_view = QtWidgets.QDialog()
    ui = Ui_HRM_Signup_view()
    ui.setupUi(HRM_Signup_view)
    HRM_Signup_view.show()
    sys.exit(app.exec_())

