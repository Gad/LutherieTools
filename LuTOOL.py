"""This file is part of LuTOOL. LuTOOL is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any later 
version.

LuTOOL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with LuTOOL. 
If not, see <https://www.gnu.org/licenses/>. 
    
    Ce fichier fait partie de LuTOOL. LuTOOL est un logiciel libre; vous pouvez le 
redistribuer ou le modifier suivant les termes de la GNU General Public License telle 
que publiée par la Free Software Foundation; soit la version 3 de la licence, soit 
(à votre gré) toute version ultérieure.
LuTOOL est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE GARANTIE; 
sans même la garantie tacite de QUALITÉ MARCHANDE ou d'ADÉQUATION à UN BUT PARTICULIER. 
Consultez la GNU General Public License pour plus de détails.
Vous devez avoir reçu une copie de la GNU General Public License en même temps que 
LuTOOL; si ce n'est pas le cas, consultez <http://www.gnu.org/licenses>.
"""

import sys
import logging
import re
import platform
import ctypes
import tempfile
import os
import glob
import shutil


#project libs 
from libs.LutherieTemplatesV1_alpha_ui import Ui_MainWindow
from libs.QuoteRequestDialog import Ui_Dialog
from libs.QuoteRequest import Quote_request
from libs.FrettingTemplate import FrettingTemplate
from libs.AboutDialog_ui import Ui_aboutDialog
from libs.LuToolLog_ui import Ui_log


#QT libs
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QFileDialog, \
                                QDialog, QMessageBox, QDialogButtonBox
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtCore import QByteArray, Slot, QTranslator, QLocale, QCoreApplication, \
    QEvent, QTextStream, QObject, Signal
from PySide6.QtGui import QActionGroup, QIcon






languageDic = {QLocale.Language.French : "fr", QLocale.Language.English : "en",
                QLocale.Language.Spanish : "es", QLocale.Language.Italian : "it"}

languageDicAlter = {"French" :  QLocale.Language.French, 
                    "English" : QLocale.Language.English,
                    "Spanish" : QLocale.Language.Spanish, 
                    "Italian" : QLocale.Language.Italian }

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowIcon(QIcon('./icons/guitar-black-shape-svgrepo-com.png'))
        #
        
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        #self.actionFrench.setChecked(True)
        self.languageGroup=QActionGroup(self)
        self.languageGroup.setExclusionPolicy(QActionGroup.ExclusionPolicy.Exclusive)

        # state variables       
        self.initialCompute=False
        self.logging = False # is logging to logging windows active       


        for actions in self.menuLanguage.actions():
            self.languageGroup.addAction(actions)

        # set event filter for "SendAquote" button
        self.AskForQuoteButton.installEventFilter(self)
        self.SaveAsSVGButton.installEventFilter(self)

        #
        self.closeEvent = self.cleaningOnClose


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
        self.Row1IncludeMarksCheckBox.stateChanged.connect(self.resetButtons)
        self.Row2IncludeMarksCheckBox.stateChanged.connect(self.resetButtons)
        

        # actions triggers
        self.languageGroup.triggered.connect(lambda checked:self.changeLanguage(checked,
                                                     self.languageGroup.checkedAction()))
        
        self.actionAbout.triggered.connect(self.about)
        self.actionLog.triggered.connect(self.log)



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
        self.statusBar.showMessage(QCoreApplication.translate("MainWindow","SVG Done"),
                                    3000)

        self.initialCompute = True
        
    @Slot()
    def resetButtons(self):
        self.SaveAsSVGButton.setEnabled(False)
        self.AskForQuoteButton.setEnabled(False)
        if hasattr(self, 'scene'): self.scene.clear()  # noqa: E701
        if hasattr(self, 'renderer2'): self.renderer2=QByteArray()  # noqa: E701
        if hasattr(self, 'graphicsView'): self.graphicsView.destroy()  # noqa: E701
        if hasattr(self, 'monDiapason'): 
            del self.monDiapason

        if self.initialCompute is True :
            self.generateSVG()



    @Slot()
    def valueChanged(self, value: int):
        self.progress.setValue(value) 

    @Slot()
    def saveAsSVG(self):
        
        
        suggestedFileName='Diapason '+str(self.row1ScaleLengthSpinBox.value())+' '+\
        str(self.Row1UnitChoiceBox.currentText())+'-'+str(self.row2ScaleLengthSpinBox.value())+\
        ' '+str(self.Row2UnitChoiceBox.currentText())+'.svg' 

        self.SVGFileName=QFileDialog.getSaveFileName(self, dir="./SVGs/"+
                                                     suggestedFileName,filter="*.svg")
        
        with open(self.SVGFileName[0],'wb') as SVGfile:
            SVGfile.write(self.monDiapason.SVGoutput)
            self.AskForQuoteButton.setEnabled(True)
        
       

    @Slot()
    def askForQuote(self):
        dialogWindow=AskQuoteDialog(self)
        dialogWindow.setFixedSize(dialogWindow.width(),dialogWindow.height())
     
        dialogWindow.exec()

    @Slot()
    def about(self):
        dialogWindow=AboutDialog(self)
        dialogWindow.setFixedSize(dialogWindow.width(),dialogWindow.height())
        dialogWindow.exec_()

    @Slot()
    def log(self):
    
        if self.logging is False:
            self.logWindow=LogDialog(self)
            self.logWindow.setModal(False)

            self.logWindow.setupUi(self.logWindow)

            self.logWindow.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.closeLogWindow) 
            self.logWindow.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.saveLog) 

            tempLogFile.seek(0)
            self.logWindow.logBrowser.insertPlainText(tempLogFile.read())

            self.logWindow.closeEvent = self.closeLogWindow
             
            self.logWindow.show()
            sys.stderr = EmittingStream()
            sys.stderr.textWritten.connect(self.write2Console)

            self.windowsLoggingHandler=logging.StreamHandler(sys.stderr)
            self.windowsLoggingHandler.setFormatter (logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"))
            main_logger.addHandler(self.windowsLoggingHandler)
            print(main_logger.handlers)
            
      
        #dialogWindow.setFixedSize(dialogWindow.width(),dialogWindow.height())
        #dialogWindow.setWindowModality(Qt.WindowModality.NonModal)
    @Slot()    
    def closeLogWindow(self, event=None):
        print("here")
        main_logger.removeHandler(self.windowsLoggingHandler)
        

    def saveLog(self):
        self.LogFileName=QFileDialog.getSaveFileName(self, dir="./logs/LuTOOL_log.txt",filter="*.txt")
        main_logger.info(f'Saved Log file into {self.LogFileName[0]}')
        tempLogFile.close()
        shutil.copy(tempLogFile.name,self.LogFileName[0])
        

        
        
        
    @Slot()
    def changeLanguage(self, checked, checked_action):

       
        print(app.removeTranslator(translator))      

        #very poor :
        language=languageDic[languageDicAlter[checked_action.objectName().replace('action','')]]

        new_installed_tr=translator.load(language+".qm", directory="./i18n")
        main_logger.debug('Try to install tranlator: {}.qm'.format(language))
    
        if new_installed_tr :
            app.installTranslator(translator)
            self.retranslateUi(self)
            #self.setupUi(self)
        else :
            logging.warn("Failed to load new translator")    


    # managing button tooltips depending on enable/disable

    def eventFilter(self, object, event):
        
               

        if event.type() == QEvent.Enter:
            if self.AskForQuoteButton.isEnabled() is False:
                self.AskForQuoteButton.setToolTip(QCoreApplication.translate("MainWindow",\
                                 "Please first save your SVG file"))
            else :
                self.AskForQuoteButton.setToolTip("")
            if self.SaveAsSVGButton.isEnabled() is False:
                self.SaveAsSVGButton.setToolTip(QCoreApplication.translate("MainWindow",\
                                 "Please first build the fretting template"))
            else : 
                self.SaveAsSVGButton.setToolTip("")
        elif event.type() == QEvent.Leave:
            pass
            
        return False
    
    def write2Console(self, text):

        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        self.logWindow.logBrowser.insertPlainText(text) 

    def cleaningOnClose(self,event):

        #cleaning temp files in log

        fileList = glob.glob('./logs/tmp*.log', recursive=True)
     
        # Remove all files one by one
        for file in fileList:
            try:
                os.remove(file)
            except OSError:
                print("Error while deleting file")

            finally :
                event.accept()
        

class AboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self, parent: None) -> None:
        super().__init__()
        self.setupUi(self)   

class LogDialog(QDialog, Ui_log):
    def __init__(self, parent: None) -> None:
        super().__init__()
        
        
class EmittingStream(QObject):

    textWritten = Signal(str)


    def write(self, text):
        self.textWritten.emit(str(text))

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
                                    self.secondNameLineEdit.text(),
                                    self.emailAddressLineEdit.text(), 
                                    self.language)
        r=newRequest.send_request()
        
        if r[0] is False:
            QMessageBox.warning(self, 
                QCoreApplication.translate("MainWindow","Error,quote request NOT sent"),
                                    "{}".format(r[1]) )
        else:
            QMessageBox.information(self, QCoreApplication.translate("MainWindow",
                                                "Quote request sent")+"              ",
                                                QCoreApplication.translate("MainWindow",
                                                "Thank you, we're working on it ;)"))

    def check(self, emailAddress : str ="") -> bool: 
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return True if re.fullmatch(pattern, emailAddress) else False





app = QApplication(sys.argv)

main_logger = logging.getLogger("main_logger")
main_logger.setLevel(logging.DEBUG)

# set tmp file handler 
windowsLoggingHandler=logging.StreamHandler(sys.stderr)
windowsLoggingHandler.setFormatter (logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"))
tempLogFile=tempfile.NamedTemporaryFile(mode="w+",suffix=".log", dir="./logs/", prefix='tmp', delete = False)
tempLogFileHandler=logging.FileHandler(filename=tempLogFile.name, mode="a")
tempLogFileHandler.setFormatter (logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"))
tempLogFileHandler.setLevel(logging.DEBUG)

main_logger.addHandler(tempLogFileHandler)

# pense-bête :
# ./venv/bin/pyside6-lupdate LutherieTemplatesV1-alpha.py LutherieTemplatesV1_alpha.ui QuoteRequestDialog.ui -ts i18n/fr.ts
# env_qt\Scripts\pyside6-linguist.exe
# env_qt\Scripts\pyside6-lrelease.exe i18n\fr.ts i18n\fr.qm


translator = QTranslator(app)
loc=QLocale()
main_logger.debug('found Locale : {}'.format(loc.language()))

#alias for typing faster


if loc.language() in languageDic.keys():
    installed_tr=translator.load(languageDic[loc.language()]+".qm", directory="./i18n")
    main_logger.debug('Try to install tranlator: {}.qm'.format(languageDic[loc.language()]))
else :
    main_logger.warn("Local language not supported, fall back to generic")
    installed_tr=False

if installed_tr :
    app.installTranslator(translator)
else :
    main_logger.warn("Failed to load translator")

if platform.system()=="windows":
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window = MainWindow()
window.show()
app.exec()
