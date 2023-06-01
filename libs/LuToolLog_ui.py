# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LuToolLog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_log(object):
    def setupUi(self, log):
        if not log.objectName():
            log.setObjectName(u"log")
        log.resize(946, 300)
        self.buttonBox = QDialogButtonBox(log)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(840, 10, 101, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.logBrowser = QTextBrowser(log)
        self.logBrowser.setObjectName(u"logBrowser")
        self.logBrowser.setGeometry(QRect(10, 10, 821, 261))

        self.retranslateUi(log)
        self.buttonBox.accepted.connect(log.accept)
        self.buttonBox.rejected.connect(log.reject)

        QMetaObject.connectSlotsByName(log)
    # setupUi

    def retranslateUi(self, log):
        log.setWindowTitle(QCoreApplication.translate("log", u"Lutool - log", None))
    # retranslateUi

