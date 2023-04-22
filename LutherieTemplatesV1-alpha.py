import sys
import logging
import re
import platform
import ctypes

#from ui_pre_email_window import Ui_Dialog
from LutherieTemplatesV1_alpha_ui import Ui_MainWindow
from QuoteRequestDialog import Ui_Dialog

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QFileDialog, QDialog, QMessageBox, QDialogButtonBox
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtCore import QByteArray, Slot, Qt, QTranslator, QLocale, QCoreApplication
from PySide6.QtGui import QActionGroup, QIcon

from QuoteRequest import Quote_request

from FrettingTemplate import FrettingTemplate




languageDic = {QLocale.Language.French : "fr", QLocale.Language.English : "en",
                QLocale.Language.Spanish : "es", QLocale.Language.Italian : "it"}

languageDicAlter = {"French" :  QLocale.Language.French, "English" : QLocale.Language.English,
                    "Spanish" : QLocale.Language.Spanish, "Italian" : QLocale.Language.Italian }

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowIcon(QIcon('./icons/guitar-black-shape-svgrepo-com.png'))
        
        self.setupUi(self)
        #self.actionFrench.setChecked(True)
        self.languageGroup=QActionGroup(self)
        self.languageGroup.setExclusionPolicy(QActionGroup.ExclusionPolicy.Exclusive)
        
        
        for actions in self.menuLanguage.actions():
            self.languageGroup.addAction(actions)

        print(self.languageGroup.actions())

        # Signals 
        self.BuildFretteBoardButton.clicked.connect(self.generateSVG)
        self.SaveAsSVGButton.clicked.connect(self.saveAsSVG)
        self.AskForQuoteButton.clicked.connect(self.askForQuote)

        self.row1ScaleLengthSpinBox.valueChanged.connect(self.resetButtons)
        self.row2ScaleLengthSpinBox.valueChanged.connect(self.resetButtons)
        self.Row1FretteNumSpinBox.valueChanged.connect(self.resetButtons)
        self.Row2FretteNumSpinBox.valueChanged.connect(self.resetButtons)
        self.Row1UnitChoiceBox.currentIndexChanged.connect(self.resetButtons)
        self.Row2UnitChoiceBox.currentIndexChanged.connect(self.resetButtons)

        # actions triggers
        self.languageGroup.triggered.connect(lambda checked: self.changeLanguage(checked, self.languageGroup.checkedAction()))

        


    @Slot()
    def generateSVG(self):
        #print("génération du SVG")
        
        self.monDiapason=FrettingTemplate(float(self.row1ScaleLengthSpinBox.value()),\
                                        str(self.Row1UnitChoiceBox.currentText()),\
                                        int(self.Row1FretteNumSpinBox.value()),\
                                        bool(self.Row1IncludeMarksCheckBox.isChecked()),\
                                        float(self.row2ScaleLengthSpinBox.value()),\
                                        str(self.Row2UnitChoiceBox.currentText()),\
                                        int(self.Row2FretteNumSpinBox.value()),\
                                        bool(self.Row2IncludeMarksCheckBox.isChecked()))
        
        self.renderer2 = QByteArray(self.monDiapason.SVGoutput)
        
        self.SVGDisplay=QGraphicsSvgItem()
        self.SVGDisplay.renderer().load(self.renderer2)
        self.SVGDisplay.setElementId("")
        self.SVGDisplay.setScale(0.5)
        self.SVGDisplay.setRotation(180)

        self.SVGDisplay.setPos(self.monDiapason.total_length*1.8,120)
        
        #self.scene=QGraphicsScene(self.SVGDisplay.boundingRect())
        self.scene=QGraphicsScene(-50,-50,2000,2000)
        self.scene.addItem(self.SVGDisplay)
        
        
        self.graphicsView.setScene(self.scene)
        self.graphicsView.centerOn(0,70)
        self.SaveAsSVGButton.setEnabled(True)
        self.statusBar.showMessage("SVG Done",3000)
        
    @Slot()
    def resetButtons(self):
        self.SaveAsSVGButton.setEnabled(False)
        self.AskForQuoteButton.setEnabled(False)
        if hasattr(self, 'scene'): self.scene.clear()
        if hasattr(self, 'renderer2'): self.renderer2=QByteArray()
        if hasattr(self, 'graphicsView'): self.graphicsView.destroy()
        if hasattr(self, 'monDiapason'): del self.monDiapason



    @Slot()
    def valueChanged(self, value: int):
        self.progress.setValue(value) 

    @Slot()
    def saveAsSVG(self):
        
        suggestedFileName='Diapason '+str(self.row1ScaleLengthSpinBox.value())+' '+\
        str(self.Row1UnitChoiceBox.currentText())+'-'+str(self.row2ScaleLengthSpinBox.value())+\
        ' '+str(self.Row2UnitChoiceBox.currentText())+'.svg' 

        self.SVGFileName=QFileDialog.getSaveFileName(self, dir="./SVGs/"+suggestedFileName,\
            filter="*.svg")
        
        with open(self.SVGFileName[0],'wb') as SVGfile:
            SVGfile.write(self.monDiapason.SVGoutput)
            self.AskForQuoteButton.setEnabled(True)
        
       

    @Slot()
    def askForQuote(self):
        dialogWindow=AskQuoteDialog(self)
        dialogWindow.exec()

    @Slot()
    def changeLanguage(self, checked, checked_action):

       
        print(app.removeTranslator(translator))      

        #very poor :
        language=languageDic[languageDicAlter[checked_action.objectName().replace('action','')]]

        new_installed_tr=translator.load(language+".qm", directory="./i18n")
        logging.debug('Try to install tranlator: {}.qm'.format(language))
    
        if new_installed_tr :
            app.installTranslator(translator)
            self.retranslateUi(self)
            #self.setupUi(self)
        else :
            logging.warn("Failed to load new translator")    
    
    

class AskQuoteDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.SVGFileName=parent.SVGFileName[0]
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        # Signals 
        self.buttonBox.accepted.connect(self.sendFiles)
        self.checkBox.stateChanged.connect(self.changeState)
        self.emailAddressLineEdit.editingFinished.connect(self.changeState)
        self.firstNameLineEdit.editingFinished.connect(self.changeState)
        self.secondNameLineEdit.editingFinished.connect(self.changeState)
        self.language=translator.language()
    @Slot()

    def changeState(self):


        if self.checkBox.isChecked() and \
        self.check(self.emailAddressLineEdit.text()) and \
        self.firstNameLineEdit.text()!="" and \
        self.secondNameLineEdit.text()!="":

            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def sendFiles(self):
        
        
        newRequest=Quote_request(self.SVGFileName,self.firstNameLineEdit.text(),
                                    self.secondNameLineEdit.text(),self.emailAddressLineEdit.text(), self.language)
        r=newRequest.send_request()
        
        if r[0] == False:
            QMessageBox.warning(self, QCoreApplication.translate("MainWindow", "Error, quote request NOT sent"), "{}".format(r[1]) )
        else:
            QMessageBox.information(self, QCoreApplication.translate("MainWindow", "Quote request sent")+"              ", 
                                    QCoreApplication.translate("MainWindow","Thank you, we're working on it ;)"))

    def check(self, emailAddress : str ="") -> bool: 
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return True if re.fullmatch(pattern, emailAddress) else False





app = QApplication(sys.argv)
logging.basicConfig(level=logging.DEBUG)
# pense-bête :
# env_qt\Scripts\pyside6-lupdate.exe LutherieTemplatesV1_alpha.ui -ts i18n\fr.ts
# env_qt\Scripts\pyside6-linguist.exe
# env_qt\Scripts\pyside6-lrelease.exe i18n\fr.ts i18n\fr.qm


translator = QTranslator(app)
loc=QLocale()
logging.debug('found Locale : {}'.format(loc.language()))

#alias for typing faster


if loc.language() in languageDic.keys():
    installed_tr=translator.load(languageDic[loc.language()]+".qm", directory="./i18n")
    logging.debug('Try to install tranlator: {}.qm'.format(languageDic[loc.language()]))
else :
    logging.warn("Local language not supported, fall back to generic")
    installed_tr=False

if installed_tr :
    app.installTranslator(translator)
else :
    logging.warn("Failed to load translator")

if platform.system()=="windows":
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window = MainWindow()
window.show()
app.exec()
