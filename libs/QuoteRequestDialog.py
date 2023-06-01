# -*- coding: utf-8 -*-


################################################################################
## Form generated from reading UI file 'QuoteRequestDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QDialogButtonBox, QFormLayout, QLabel, 
    QLineEdit, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(628, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 260, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 20, 591, 111))
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 130, 591, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.firstNameLabel = QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.firstNameLabel)

        self.firstNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firstNameLineEdit)

        self.secondNameLabel = QLabel(self.formLayoutWidget)
        self.secondNameLabel.setObjectName(u"secondNameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.secondNameLabel)

        self.secondNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.secondNameLineEdit.setObjectName(u"secondNameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.secondNameLineEdit)

        self.emailAddressLabel = QLabel(self.formLayoutWidget)
        self.emailAddressLabel.setObjectName(u"emailAddressLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.emailAddressLabel)

        self.emailAddressLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailAddressLineEdit.setObjectName(u"emailAddressLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.emailAddressLineEdit)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 230, 701, 21))
        font = QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Quote Request", None))  # noqa: E501
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"  # noqa: E501
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"  # noqa: E501
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"  # noqa: E501
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">Thank you for your inquiry. Please note :</span></p>\n"  # noqa: E501
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p>\n"  # noqa: E501
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"  # noqa: E501
                        "k-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">- We ship to all E.U. countries.</span></p>\n"  # noqa: E501
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt;\">- Our frettingboards are made of transparent acrylic glass (PMMA) - 5mm thickness. </span></p>\n"  # noqa: E501
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p>\n"  # noqa: E501
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Please fill in the following details for us to get back to you (usually in 48h)</span></p></body></html>", None))  # noqa: E501
        self.firstNameLabel.setText(QCoreApplication.translate("Dialog", u"First name", None))  # noqa: E501
        self.secondNameLabel.setText(QCoreApplication.translate("Dialog", u"Second Name", None))  # noqa: E501
        self.emailAddressLabel.setText(QCoreApplication.translate("Dialog", u"Email address", None))  # noqa: E501
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"By clicking ok, I agree to transmit my details to Tribricks SAS with the sole purpose of getting a quote.", None))  # noqa: E501
    # retranslateUi

