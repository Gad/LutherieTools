# -*- coding: utf-8 -*-
#
################################################################################
## Form generated from reading UI file 'LutherieTemplatesV1_alpha.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 436)
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icons/guitar-black-shape-svgrepo-com.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionHow_does_it_work = QAction(MainWindow)
        self.actionHow_does_it_work.setObjectName(u"actionHow_does_it_work")
        self.actionFrette_board = QAction(MainWindow)
        self.actionFrette_board.setObjectName(u"actionFrette_board")
        self.actionRouting_Templates = QAction(MainWindow)
        self.actionRouting_Templates.setObjectName(u"actionRouting_Templates")
        self.actionLanguage = QAction(MainWindow)
        self.actionLanguage.setObjectName(u"actionLanguage")
        self.actionLogging_Level = QAction(MainWindow)
        self.actionLogging_Level.setObjectName(u"actionLogging_Level")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setCheckable(True)
        self.actionFrench = QAction(MainWindow)
        self.actionFrench.setObjectName(u"actionFrench")
        self.actionFrench.setCheckable(True)
        self.actionItalian = QAction(MainWindow)
        self.actionItalian.setObjectName(u"actionItalian")
        self.actionItalian.setCheckable(True)
        self.actionSpanish = QAction(MainWindow)
        self.actionSpanish.setObjectName(u"actionSpanish")
        self.actionSpanish.setCheckable(True)
        self.actionLog = QAction(MainWindow)
        self.actionLog.setObjectName(u"actionLog")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 1031, 371))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 1001, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(9, 5, 250, 5)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.row1ScaleLengthSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.row1ScaleLengthSpinBox.setObjectName(u"row1ScaleLengthSpinBox")
        self.row1ScaleLengthSpinBox.setSizeIncrement(QSize(0, 7))
        self.row1ScaleLengthSpinBox.setMaximum(1000.000000000000000)
        self.row1ScaleLengthSpinBox.setValue(25.500000000000000)

        self.horizontalLayout.addWidget(self.row1ScaleLengthSpinBox)

        self.Row1UnitChoiceBox = QComboBox(self.layoutWidget)
        self.Row1UnitChoiceBox.addItem("")
        self.Row1UnitChoiceBox.addItem("")
        self.Row1UnitChoiceBox.setObjectName(u"Row1UnitChoiceBox")
        self.Row1UnitChoiceBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.Row1UnitChoiceBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.Row1FretteNumSpinBox = QSpinBox(self.layoutWidget)
        self.Row1FretteNumSpinBox.setObjectName(u"Row1FretteNumSpinBox")
        self.Row1FretteNumSpinBox.setValue(27)

        self.horizontalLayout.addWidget(self.Row1FretteNumSpinBox)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Row1IncludeMarksCheckBox = QCheckBox(self.layoutWidget)
        self.Row1IncludeMarksCheckBox.setObjectName(u"Row1IncludeMarksCheckBox")
        self.Row1IncludeMarksCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.Row1IncludeMarksCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(9, 5, 250, 5)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.row2ScaleLengthSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.row2ScaleLengthSpinBox.setObjectName(u"row2ScaleLengthSpinBox")
        self.row2ScaleLengthSpinBox.setSizeIncrement(QSize(0, 7))
        self.row2ScaleLengthSpinBox.setMaximum(1000.000000000000000)
        self.row2ScaleLengthSpinBox.setValue(610.000000000000000)

        self.horizontalLayout_2.addWidget(self.row2ScaleLengthSpinBox)

        self.Row2UnitChoiceBox = QComboBox(self.layoutWidget)
        self.Row2UnitChoiceBox.addItem("")
        self.Row2UnitChoiceBox.addItem("")
        self.Row2UnitChoiceBox.setObjectName(u"Row2UnitChoiceBox")
        self.Row2UnitChoiceBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.Row2UnitChoiceBox)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.Row2FretteNumSpinBox = QSpinBox(self.layoutWidget)
        self.Row2FretteNumSpinBox.setObjectName(u"Row2FretteNumSpinBox")
        self.Row2FretteNumSpinBox.setValue(27)

        self.horizontalLayout_2.addWidget(self.Row2FretteNumSpinBox)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.Row2IncludeMarksCheckBox = QCheckBox(self.layoutWidget)
        self.Row2IncludeMarksCheckBox.setObjectName(u"Row2IncludeMarksCheckBox")
        self.Row2IncludeMarksCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.Row2IncludeMarksCheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BuildFretteBoardButton = QPushButton(self.layoutWidget)
        self.BuildFretteBoardButton.setObjectName(u"BuildFretteBoardButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BuildFretteBoardButton.sizePolicy().hasHeightForWidth())
        self.BuildFretteBoardButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.BuildFretteBoardButton)

        self.SaveAsSVGButton = QPushButton(self.layoutWidget)
        self.SaveAsSVGButton.setObjectName(u"SaveAsSVGButton")
        self.SaveAsSVGButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.SaveAsSVGButton.sizePolicy().hasHeightForWidth())
        self.SaveAsSVGButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.SaveAsSVGButton)

        self.AskForQuoteButton = QPushButton(self.layoutWidget)
        self.AskForQuoteButton.setObjectName(u"AskForQuoteButton")
        self.AskForQuoteButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.AskForQuoteButton.sizePolicy().hasHeightForWidth())
        self.AskForQuoteButton.setSizePolicy(sizePolicy1)
        self.AskForQuoteButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.AskForQuoteButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.graphicsView = QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1075, 21))
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menuTool = QMenu(self.menubar)
        self.menuTool.setObjectName(u"menuTool")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuLanguage = QMenu(self.menuOptions)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.actionHow_does_it_work)
        self.menuTool.addAction(self.actionFrette_board)
        self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuOptions.addAction(self.actionLog)
        self.menuOptions.addAction(self.actionAbout)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionFrench)
        self.menuLanguage.addAction(self.actionItalian)
        self.menuLanguage.addAction(self.actionSpanish)

        self.retranslateUi(MainWindow)

        self.Row1UnitChoiceBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lutherie Tools&Jigs", None))
        self.actionHow_does_it_work.setText(QCoreApplication.translate("MainWindow", u"How does it work ?", None))
        self.actionFrette_board.setText(QCoreApplication.translate("MainWindow", u"Fretting Templates", None))
        self.actionRouting_Templates.setText(QCoreApplication.translate("MainWindow", u"Routing Templates", None))
        self.actionLanguage.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.actionLogging_Level.setText(QCoreApplication.translate("MainWindow", u"Logging Level", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionFrench.setText(QCoreApplication.translate("MainWindow", u"French", None))
        self.actionItalian.setText(QCoreApplication.translate("MainWindow", u"Italian", None))
        self.actionSpanish.setText(QCoreApplication.translate("MainWindow", u"Spanish", None))
        self.actionLog.setText(QCoreApplication.translate("MainWindow", u"Enable/disable log", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fretting Template", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1st  Row Scale Length", None))
#if QT_CONFIG(tooltip)
        self.row1ScaleLengthSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"set distance from Bridge to Nut", None))
#endif // QT_CONFIG(tooltip)
        self.Row1UnitChoiceBox.setItemText(0, QCoreApplication.translate("MainWindow", u"mm", None))
        self.Row1UnitChoiceBox.setItemText(1, QCoreApplication.translate("MainWindow", u"inches", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"with", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"frettes ", None))
        self.Row1IncludeMarksCheckBox.setText(QCoreApplication.translate("MainWindow", u"include marks", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2nd Row Scale Length", None))
#if QT_CONFIG(tooltip)
        self.row2ScaleLengthSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"set distance from Bridge to Nut", None))
#endif // QT_CONFIG(tooltip)
        self.Row2UnitChoiceBox.setItemText(0, QCoreApplication.translate("MainWindow", u"mm", None))
        self.Row2UnitChoiceBox.setItemText(1, QCoreApplication.translate("MainWindow", u"inches", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"with", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"frettes ", None))
        self.Row2IncludeMarksCheckBox.setText(QCoreApplication.translate("MainWindow", u"include marks", None))
        self.BuildFretteBoardButton.setText(QCoreApplication.translate("MainWindow", u"Build Fretting Template", None))
        self.SaveAsSVGButton.setText(QCoreApplication.translate("MainWindow", u"Save as SVG File", None))
        self.AskForQuoteButton.setText(QCoreApplication.translate("MainWindow", u"ask for a quote", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menuTool.setTitle(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi

