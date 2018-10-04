# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HRM_Dashboard_view(object):
    def setupUi(self, HRM_Dashboard_view):
        HRM_Dashboard_view.setObjectName("HRM_Dashboard_view")
        HRM_Dashboard_view.resize(1405, 691)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HRM_Dashboard_view.setWindowIcon(icon)
        HRM_Dashboard_view.setStyleSheet("background-color:rgb(40, 93, 117);")
        self.centralwidget = QtWidgets.QWidget(HRM_Dashboard_view)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 1361, 597))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(48, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/logo.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(85, 255, 255)")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_user_login = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        self.pushButton_user_login.setFont(font)
        self.pushButton_user_login.setStyleSheet("color:rgb(85, 255, 255)")
        self.pushButton_user_login.setObjectName("pushButton_user_login")
        self.verticalLayout_2.addWidget(self.pushButton_user_login)
        self.pushButton_user_reg = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        self.pushButton_user_reg.setFont(font)
        self.pushButton_user_reg.setStyleSheet("color:rgb(85, 255, 255)")
        self.pushButton_user_reg.setObjectName("pushButton_user_reg")
        self.verticalLayout_2.addWidget(self.pushButton_user_reg)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:rgb(85, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:rgb(85, 255, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setMinimumSize(QtCore.QSize(1150, 519))
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(10)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/solar.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.splitter)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1090, -30, 251, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_9 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_2.addWidget(self.line_9)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/services.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/comments.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.toolButton_3 = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/maintenance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.line_8 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.line_7 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.toolButton_4 = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon4)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_2.addWidget(self.toolButton_4)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.toolButton_5 = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon5)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_2.addWidget(self.toolButton_5)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.toolButton_6 = QtWidgets.QToolButton(self.layoutWidget_3)
        self.toolButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon6)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_2.addWidget(self.toolButton_6)
        HRM_Dashboard_view.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HRM_Dashboard_view)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuRecruitment = QtWidgets.QMenu(self.menuNew)
        self.menuRecruitment.setObjectName("menuRecruitment")
        self.menuNewContract = QtWidgets.QMenu(self.menuNew)
        self.menuNewContract.setObjectName("menuNewContract")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuAppraisals = QtWidgets.QMenu(self.menuOpen)
        self.menuAppraisals.setObjectName("menuAppraisals")
        self.menuTraining = QtWidgets.QMenu(self.menuOpen)
        self.menuTraining.setObjectName("menuTraining")
        self.menuRecruitment_2 = QtWidgets.QMenu(self.menuOpen)
        self.menuRecruitment_2.setObjectName("menuRecruitment_2")
        self.menuContracts = QtWidgets.QMenu(self.menuOpen)
        self.menuContracts.setObjectName("menuContracts")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEmployees = QtWidgets.QMenu(self.menuView)
        self.menuEmployees.setObjectName("menuEmployees")
        self.menuEmployers = QtWidgets.QMenu(self.menuView)
        self.menuEmployers.setObjectName("menuEmployers")
        self.menuRevenue = QtWidgets.QMenu(self.menuView)
        self.menuRevenue.setObjectName("menuRevenue")
        self.menuTaxes = QtWidgets.QMenu(self.menuView)
        self.menuTaxes.setObjectName("menuTaxes")
        self.menuCompany_Profits = QtWidgets.QMenu(self.menuView)
        self.menuCompany_Profits.setObjectName("menuCompany_Profits")
        self.menuBonuses = QtWidgets.QMenu(self.menuView)
        self.menuBonuses.setObjectName("menuBonuses")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuUpdates = QtWidgets.QMenu(self.menuEdit)
        self.menuUpdates.setObjectName("menuUpdates")
        self.menuDeals = QtWidgets.QMenu(self.menuEdit)
        self.menuDeals.setObjectName("menuDeals")
        self.menuPayments = QtWidgets.QMenu(self.menubar)
        self.menuPayments.setObjectName("menuPayments")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMore_Settings = QtWidgets.QMenu(self.menuHelp)
        self.menuMore_Settings.setObjectName("menuMore_Settings")
        HRM_Dashboard_view.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HRM_Dashboard_view)
        self.statusbar.setObjectName("statusbar")
        HRM_Dashboard_view.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNewWorker = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionNewWorker.setObjectName("actionNewWorker")
        self.actionNewClient = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionNewClient.setObjectName("actionNewClient")
        self.actionNewEmployer = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionNewEmployer.setObjectName("actionNewEmployer")
        self.actionNewEmployee = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionNewEmployee.setObjectName("actionNewEmployee")
        self.actionQiut_Application = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionQiut_Application.setObjectName("actionQiut_Application")
        self.actionRequests = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRequests.setObjectName("actionRequests")
        self.actionLeave_Forms = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionLeave_Forms.setObjectName("actionLeave_Forms")
        self.actionRequests_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRequests_2.setObjectName("actionRequests_2")
        self.actionWorker_2 = QtWidgets.QAction(HRM_Dashboard_view)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWorker_2.setIcon(icon7)
        self.actionWorker_2.setObjectName("actionWorker_2")
        self.actionEmployee_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployee_2.setObjectName("actionEmployee_2")
        self.actionClients = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionClients.setObjectName("actionClients")
        self.actionEmployees = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployees.setObjectName("actionEmployees")
        self.actionProfiles = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionProfiles.setObjectName("actionProfiles")
        self.actionLoans_Advances = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionLoans_Advances.setObjectName("actionLoans_Advances")
        self.actionBonus_Payments = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionBonus_Payments.setObjectName("actionBonus_Payments")
        self.actionSalaries = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionSalaries.setObjectName("actionSalaries")
        self.actionProfiles_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionProfiles_2.setObjectName("actionProfiles_2")
        self.actionPayments = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionPayments.setObjectName("actionPayments")
        self.actionArrears = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionArrears.setObjectName("actionArrears")
        self.actionResource_Level = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionResource_Level.setObjectName("actionResource_Level")
        self.actionRates = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRates.setObjectName("actionRates")
        self.actionStatements = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionStatements.setObjectName("actionStatements")
        self.actionRates_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRates_2.setObjectName("actionRates_2")
        self.actionStatements_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionStatements_2.setObjectName("actionStatements_2")
        self.actionProfit_Statement = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionProfit_Statement.setObjectName("actionProfit_Statement")
        self.actionRates_3 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRates_3.setObjectName("actionRates_3")
        self.actionStatements_3 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionStatements_3.setObjectName("actionStatements_3")
        self.actionMy_Profile = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionMy_Profile.setObjectName("actionMy_Profile")
        self.actionCompany = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionCompany.setObjectName("actionCompany")
        self.actionEmployee_Records = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployee_Records.setObjectName("actionEmployee_Records")
        self.actionEmployer_Record = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployer_Record.setObjectName("actionEmployer_Record")
        self.actionClient_Records = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionClient_Records.setObjectName("actionClient_Records")
        self.actioncontracts = QtWidgets.QAction(HRM_Dashboard_view)
        self.actioncontracts.setObjectName("actioncontracts")
        self.actionHandshakes = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionHandshakes.setObjectName("actionHandshakes")
        self.actionHandshakes_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionHandshakes_2.setObjectName("actionHandshakes_2")
        self.actioncontracts_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actioncontracts_2.setObjectName("actioncontracts_2")
        self.actionEarnings = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEarnings.setObjectName("actionEarnings")
        self.actionDeductions = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionDeductions.setObjectName("actionDeductions")
        self.actionLoans_Advances_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionLoans_Advances_2.setObjectName("actionLoans_Advances_2")
        self.actionBonuses_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionBonuses_2.setObjectName("actionBonuses_2")
        self.actionPayments_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionPayments_2.setObjectName("actionPayments_2")
        self.actionLogs = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionLogs.setObjectName("actionLogs")
        self.actionClients_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionClients_2.setObjectName("actionClients_2")
        self.actionWorkers = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionWorkers.setObjectName("actionWorkers")
        self.actionEmployees_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployees_2.setObjectName("actionEmployees_2")
        self.actionEmployers = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionEmployers.setObjectName("actionEmployers")
        self.actionInvoices = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionInvoices.setObjectName("actionInvoices")
        self.actionReceipts = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionReceipts.setObjectName("actionReceipts")
        self.actionRevenue = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionRevenue.setObjectName("actionRevenue")
        self.actionPayments_3 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionPayments_3.setObjectName("actionPayments_3")
        self.actionTaxes_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionTaxes_2.setObjectName("actionTaxes_2")
        self.actionBonuses_3 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionBonuses_3.setObjectName("actionBonuses_3")
        self.actionOver_Time = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionOver_Time.setObjectName("actionOver_Time")
        self.actionAbout = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdates_2 = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionUpdates_2.setObjectName("actionUpdates_2")
        self.actionReset_System = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionReset_System.setObjectName("actionReset_System")
        self.actionWebsite = QtWidgets.QAction(HRM_Dashboard_view)
        self.actionWebsite.setObjectName("actionWebsite")
        self.menuRecruitment.addAction(self.actionNewWorker)
        self.menuRecruitment.addAction(self.actionNewEmployee)
        self.menuNewContract.addAction(self.actionNewClient)
        self.menuNewContract.addAction(self.actionNewEmployer)
        self.menuNew.addAction(self.menuRecruitment.menuAction())
        self.menuNew.addAction(self.menuNewContract.menuAction())
        self.menuAppraisals.addAction(self.actionRequests)
        self.menuAppraisals.addAction(self.actionLeave_Forms)
        self.menuTraining.addAction(self.actionRequests_2)
        self.menuRecruitment_2.addAction(self.actionWorker_2)
        self.menuRecruitment_2.addAction(self.actionEmployee_2)
        self.menuContracts.addAction(self.actionClients)
        self.menuContracts.addAction(self.actionEmployees)
        self.menuOpen.addAction(self.menuRecruitment_2.menuAction())
        self.menuOpen.addAction(self.menuContracts.menuAction())
        self.menuOpen.addAction(self.menuTraining.menuAction())
        self.menuOpen.addAction(self.menuAppraisals.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQiut_Application)
        self.menuEmployees.addAction(self.actionProfiles)
        self.menuEmployees.addAction(self.actionLoans_Advances)
        self.menuEmployees.addAction(self.actionBonus_Payments)
        self.menuEmployees.addAction(self.actionSalaries)
        self.menuEmployers.addAction(self.actionProfiles_2)
        self.menuEmployers.addAction(self.actionPayments)
        self.menuEmployers.addAction(self.actionArrears)
        self.menuEmployers.addAction(self.actionResource_Level)
        self.menuRevenue.addAction(self.actionRates)
        self.menuRevenue.addAction(self.actionStatements)
        self.menuTaxes.addAction(self.actionRates_2)
        self.menuTaxes.addAction(self.actionStatements_2)
        self.menuCompany_Profits.addAction(self.actionProfit_Statement)
        self.menuBonuses.addAction(self.actionRates_3)
        self.menuBonuses.addAction(self.actionStatements_3)
        self.menuView.addAction(self.menuEmployees.menuAction())
        self.menuView.addAction(self.menuEmployers.menuAction())
        self.menuView.addAction(self.menuRevenue.menuAction())
        self.menuView.addAction(self.menuTaxes.menuAction())
        self.menuView.addAction(self.menuCompany_Profits.menuAction())
        self.menuView.addAction(self.menuBonuses.menuAction())
        self.menuView.addAction(self.actionHandshakes_2)
        self.menuView.addAction(self.actioncontracts_2)
        self.menuUpdates.addAction(self.actionCompany)
        self.menuUpdates.addAction(self.actionEmployee_Records)
        self.menuUpdates.addAction(self.actionEmployer_Record)
        self.menuUpdates.addAction(self.actionClient_Records)
        self.menuDeals.addAction(self.actioncontracts)
        self.menuDeals.addAction(self.actionHandshakes)
        self.menuEdit.addAction(self.actionMy_Profile)
        self.menuEdit.addAction(self.menuUpdates.menuAction())
        self.menuEdit.addAction(self.menuDeals.menuAction())
        self.menuPayments.addAction(self.actionEarnings)
        self.menuPayments.addAction(self.actionDeductions)
        self.menuPayments.addAction(self.actionLoans_Advances_2)
        self.menuPayments.addAction(self.actionBonuses_2)
        self.menuPayments.addAction(self.actionPayments_2)
        self.menuPayments.addAction(self.actionLogs)
        self.menuSearch.addAction(self.actionClients_2)
        self.menuSearch.addAction(self.actionWorkers)
        self.menuSearch.addAction(self.actionEmployees_2)
        self.menuSearch.addAction(self.actionEmployers)
        self.menuSearch.addAction(self.actionInvoices)
        self.menuSearch.addAction(self.actionReceipts)
        self.menuTools.addAction(self.actionRevenue)
        self.menuTools.addAction(self.actionPayments_3)
        self.menuTools.addAction(self.actionTaxes_2)
        self.menuTools.addAction(self.actionBonuses_3)
        self.menuTools.addAction(self.actionOver_Time)
        self.menuMore_Settings.addAction(self.actionReset_System)
        self.menuMore_Settings.addAction(self.actionWebsite)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdates_2)
        self.menuHelp.addAction(self.menuMore_Settings.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPayments.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(HRM_Dashboard_view)
        QtCore.QMetaObject.connectSlotsByName(HRM_Dashboard_view)

    def retranslateUi(self, HRM_Dashboard_view):
        _translate = QtCore.QCoreApplication.translate
        HRM_Dashboard_view.setWindowTitle(_translate("HRM_Dashboard_view", "MainWindow"))
        self.label.setText(_translate("HRM_Dashboard_view", "Human Resourse Management System"))
        self.pushButton_user_login.setToolTip(_translate("HRM_Dashboard_view", "<html><head/><body><p>User Login</p></body></html>"))
        self.pushButton_user_login.setStatusTip(_translate("HRM_Dashboard_view", "Member login"))
        self.pushButton_user_login.setText(_translate("HRM_Dashboard_view", "User Login"))
        self.pushButton_user_reg.setStatusTip(_translate("HRM_Dashboard_view", "New User Registration"))
        self.pushButton_user_reg.setText(_translate("HRM_Dashboard_view", "Register A New account"))
        self.pushButton_3.setText(_translate("HRM_Dashboard_view", "Demo"))
        self.pushButton_4.setText(_translate("HRM_Dashboard_view", "Website"))
        self.toolButton.setToolTip(_translate("HRM_Dashboard_view", "System Services"))
        self.toolButton.setStatusTip(_translate("HRM_Dashboard_view", "Services"))
        self.toolButton_2.setToolTip(_translate("HRM_Dashboard_view", "System Records"))
        self.toolButton_2.setStatusTip(_translate("HRM_Dashboard_view", "Meetings"))
        self.toolButton_3.setToolTip(_translate("HRM_Dashboard_view", "system Settings"))
        self.toolButton_3.setStatusTip(_translate("HRM_Dashboard_view", "System Settings"))
        self.toolButton_4.setToolTip(_translate("HRM_Dashboard_view", "system Users"))
        self.toolButton_4.setStatusTip(_translate("HRM_Dashboard_view", "System Users"))
        self.toolButton_5.setToolTip(_translate("HRM_Dashboard_view", "system Error correction"))
        self.toolButton_5.setStatusTip(_translate("HRM_Dashboard_view", "Error Debugging"))
        self.toolButton_6.setToolTip(_translate("HRM_Dashboard_view", "Need Help"))
        self.toolButton_6.setStatusTip(_translate("HRM_Dashboard_view", "Help"))
        self.menuFile.setTitle(_translate("HRM_Dashboard_view", "File"))
        self.menuNew.setTitle(_translate("HRM_Dashboard_view", "New"))
        self.menuRecruitment.setTitle(_translate("HRM_Dashboard_view", "Recruitment"))
        self.menuNewContract.setTitle(_translate("HRM_Dashboard_view", "Contract"))
        self.menuOpen.setTitle(_translate("HRM_Dashboard_view", "Open"))
        self.menuAppraisals.setTitle(_translate("HRM_Dashboard_view", "Appraisals"))
        self.menuTraining.setTitle(_translate("HRM_Dashboard_view", "Training"))
        self.menuRecruitment_2.setTitle(_translate("HRM_Dashboard_view", "Recruitment"))
        self.menuContracts.setTitle(_translate("HRM_Dashboard_view", "Contracts"))
        self.menuView.setTitle(_translate("HRM_Dashboard_view", "View"))
        self.menuEmployees.setTitle(_translate("HRM_Dashboard_view", "Employees"))
        self.menuEmployers.setTitle(_translate("HRM_Dashboard_view", "Employers"))
        self.menuRevenue.setTitle(_translate("HRM_Dashboard_view", "Revenue"))
        self.menuTaxes.setTitle(_translate("HRM_Dashboard_view", "Taxes"))
        self.menuCompany_Profits.setTitle(_translate("HRM_Dashboard_view", "Company Profits"))
        self.menuBonuses.setTitle(_translate("HRM_Dashboard_view", "Bonuses"))
        self.menuEdit.setTitle(_translate("HRM_Dashboard_view", "Edit"))
        self.menuUpdates.setTitle(_translate("HRM_Dashboard_view", "Updates"))
        self.menuDeals.setTitle(_translate("HRM_Dashboard_view", "Deals"))
        self.menuPayments.setTitle(_translate("HRM_Dashboard_view", "Payments"))
        self.menuSearch.setTitle(_translate("HRM_Dashboard_view", "Search"))
        self.menuTools.setTitle(_translate("HRM_Dashboard_view", "Tools"))
        self.menuHelp.setTitle(_translate("HRM_Dashboard_view", "Help"))
        self.menuMore_Settings.setTitle(_translate("HRM_Dashboard_view", "More Settings"))
        self.actionSave.setText(_translate("HRM_Dashboard_view", "Save"))
        self.actionSave_As.setText(_translate("HRM_Dashboard_view", "Save As"))
        self.actionNewWorker.setText(_translate("HRM_Dashboard_view", "Worker"))
        self.actionNewClient.setText(_translate("HRM_Dashboard_view", "Client"))
        self.actionNewEmployer.setText(_translate("HRM_Dashboard_view", "Employer"))
        self.actionNewEmployee.setText(_translate("HRM_Dashboard_view", "Employee"))
        self.actionQiut_Application.setText(_translate("HRM_Dashboard_view", "Quit Application"))
        self.actionRequests.setText(_translate("HRM_Dashboard_view", "Requests"))
        self.actionLeave_Forms.setText(_translate("HRM_Dashboard_view", "Leave Forms"))
        self.actionRequests_2.setText(_translate("HRM_Dashboard_view", "Requests"))
        self.actionWorker_2.setText(_translate("HRM_Dashboard_view", "Workers"))
        self.actionEmployee_2.setText(_translate("HRM_Dashboard_view", "Employee"))
        self.actionClients.setText(_translate("HRM_Dashboard_view", "Clients"))
        self.actionEmployees.setText(_translate("HRM_Dashboard_view", "Employers"))
        self.actionProfiles.setText(_translate("HRM_Dashboard_view", "Profiles"))
        self.actionLoans_Advances.setText(_translate("HRM_Dashboard_view", "Loans /Advances"))
        self.actionBonus_Payments.setText(_translate("HRM_Dashboard_view", "Bonus Payments"))
        self.actionSalaries.setText(_translate("HRM_Dashboard_view", "Salaries"))
        self.actionProfiles_2.setText(_translate("HRM_Dashboard_view", "Profiles"))
        self.actionPayments.setText(_translate("HRM_Dashboard_view", "Payments"))
        self.actionArrears.setText(_translate("HRM_Dashboard_view", "Arrears"))
        self.actionResource_Level.setText(_translate("HRM_Dashboard_view", "Resource Level"))
        self.actionRates.setText(_translate("HRM_Dashboard_view", "Rates"))
        self.actionStatements.setText(_translate("HRM_Dashboard_view", "Statements"))
        self.actionRates_2.setText(_translate("HRM_Dashboard_view", "Rates"))
        self.actionStatements_2.setText(_translate("HRM_Dashboard_view", "Statements"))
        self.actionProfit_Statement.setText(_translate("HRM_Dashboard_view", "Profit Statement"))
        self.actionRates_3.setText(_translate("HRM_Dashboard_view", "Rates"))
        self.actionStatements_3.setText(_translate("HRM_Dashboard_view", "Statements"))
        self.actionMy_Profile.setText(_translate("HRM_Dashboard_view", "My Profile"))
        self.actionCompany.setText(_translate("HRM_Dashboard_view", "Company"))
        self.actionEmployee_Records.setText(_translate("HRM_Dashboard_view", "Employee Records"))
        self.actionEmployer_Record.setText(_translate("HRM_Dashboard_view", "Employer Record"))
        self.actionClient_Records.setText(_translate("HRM_Dashboard_view", "Client Records"))
        self.actioncontracts.setText(_translate("HRM_Dashboard_view", "Contracts"))
        self.actionHandshakes.setText(_translate("HRM_Dashboard_view", "Handshakes"))
        self.actionHandshakes_2.setText(_translate("HRM_Dashboard_view", "Handshakes"))
        self.actioncontracts_2.setText(_translate("HRM_Dashboard_view", "Contracts"))
        self.actionEarnings.setText(_translate("HRM_Dashboard_view", "Earnings"))
        self.actionDeductions.setText(_translate("HRM_Dashboard_view", "Deductions"))
        self.actionLoans_Advances_2.setText(_translate("HRM_Dashboard_view", "Loans/Advances"))
        self.actionBonuses_2.setText(_translate("HRM_Dashboard_view", "Bonuses"))
        self.actionPayments_2.setText(_translate("HRM_Dashboard_view", "Statements"))
        self.actionLogs.setText(_translate("HRM_Dashboard_view", "Logs"))
        self.actionClients_2.setText(_translate("HRM_Dashboard_view", "Clients"))
        self.actionWorkers.setText(_translate("HRM_Dashboard_view", "Workers"))
        self.actionEmployees_2.setText(_translate("HRM_Dashboard_view", "Employees"))
        self.actionEmployers.setText(_translate("HRM_Dashboard_view", "Employers"))
        self.actionInvoices.setText(_translate("HRM_Dashboard_view", "Invoices"))
        self.actionReceipts.setText(_translate("HRM_Dashboard_view", "Receipts"))
        self.actionRevenue.setText(_translate("HRM_Dashboard_view", "Revenue"))
        self.actionPayments_3.setText(_translate("HRM_Dashboard_view", "Payments"))
        self.actionTaxes_2.setText(_translate("HRM_Dashboard_view", "Taxes"))
        self.actionBonuses_3.setText(_translate("HRM_Dashboard_view", "Bonuses"))
        self.actionOver_Time.setText(_translate("HRM_Dashboard_view", "Over-Time"))
        self.actionAbout.setText(_translate("HRM_Dashboard_view", "About"))
        self.actionUpdates_2.setText(_translate("HRM_Dashboard_view", "Updates"))
        self.actionReset_System.setText(_translate("HRM_Dashboard_view", "Reset System"))
        self.actionWebsite.setText(_translate("HRM_Dashboard_view", "Website"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HRM_Dashboard_view = QtWidgets.QMainWindow()
    ui = Ui_HRM_Dashboard_view()
    ui.setupUi(HRM_Dashboard_view)
    HRM_Dashboard_view.show()
    sys.exit(app.exec_())

