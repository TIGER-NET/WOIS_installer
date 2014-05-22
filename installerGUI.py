# -*- coding: utf-8 -*-
'''
Created on 07/04/2014

@author: rmgu
'''

from PyQt4 import QtCore, QtGui
from ui import welcomeDialog, installComponentDialog, postInstallComponentDialog, componentInstructionsDialog

# MACROS
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# CONSTANTS
CANCEL = -1
SKIP = 1
NEXT = 2 


##################################################################################
# Parent classes
# Used to avoid overwriting the files produced by QtDesigner and pyuic4
# Mostly assign actions to buttons and set up the dialog

class installerWelcomeWindow(welcomeDialog.Ui_Dialog):
    
    def __init__(self):
        self.MainWindow = QtGui.QDialog()
        self.setupUi(self.MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/WOIS.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/tigernetLogo.png")))
        self.osComboBox.addItem("32 bit")
        self.osComboBox.addItem("64 bit")
        
        self.action = CANCEL

        QtCore.QObject.connect(self.beginButton, QtCore.SIGNAL("clicked()"), self.begin)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)
    
    def exec_(self):
        self.MainWindow.exec_()
        
    def cancel(self):
        self.action = CANCEL
        self.MainWindow.close()
        
    def begin(self):
        self.action = NEXT
        self.MainWindow.close()
        
       
class installWindow(installComponentDialog.Ui_Dialog):
    def __init__(self):
        self.MainWindow = QtGui.QDialog()
        self.setupUi(self.MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/WOIS.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/tigernetLogo.png")))
        
        self.action = CANCEL
        
        QtCore.QObject.connect(self.installButton, QtCore.SIGNAL("clicked()"), self.install)
        QtCore.QObject.connect(self.skipButton, QtCore.SIGNAL("clicked()"), self.skip)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)
    
    def exec_(self):
        self.MainWindow.exec_()
        
    def install(self):
        self.action = NEXT
        self.MainWindow.close()
        
    def skip(self):
        self.action = SKIP
        self.MainWindow.close()
        
    def cancel(self):
        self.action = CANCEL
        self.MainWindow.close()
        
class postInstallWindow(postInstallComponentDialog.Ui_Dialog):
    def __init__(self):
        self.MainWindow = QtGui.QDialog()
        self.setupUi(self.MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/WOIS.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/tigernetLogo.png")))
         
        self.action = CANCEL
        
        QtCore.QObject.connect(self.continueButton, QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)
        QtCore.QObject.connect(self.dirSelectionButton, QtCore.SIGNAL("clicked()"), self.dirSelection)
        
    def exec_(self):
        self.MainWindow.exec_()
    
    def next(self):
        self.action = NEXT
        self.MainWindow.close()    
        
    def cancel(self):
        self.action = CANCEL
        self.MainWindow.close()
        
    def dirSelection(self):
        path = QtGui.QFileDialog.getExistingDirectory(directory=self.dirPathText.toPlainText())
        if not path.isNull():
            self.dirPathText.setPlainText(_translate("MainWindow", path, None))
   
class instructionsWindow(componentInstructionsDialog.Ui_Dialog):
    
    # This window can have a reimplemented QDialog used as the main window to allow
    # for multithreaded operations while the window is displayed
    def __init__(self, MainWindow = None):
        if MainWindow:
            self.MainWindow = MainWindow
        else:
            self.MainWindow = QtGui.QDialog()
        self.setupUi(self.MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/WOIS.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/tigernetLogo.png")))
        
        self.action = CANCEL
        
        QtCore.QObject.connect(self.continueButton, QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)

    def exec_(self):
        self.MainWindow.exec_()

    def next(self):
        self.action = NEXT
        self.MainWindow.close()  
        
    def cancel(self):
        self.action = CANCEL
        self.MainWindow.close()
           
        
###############################################################################
# Child classes
# Individualise the parent classes mostly by changing the text 


# Instructions for activating WOIS plugins
class uninstallInstructionsWindow(instructionsWindow):
    def __init__(self):
        instructionsWindow.__init__(self)
     
    def retranslateUi(self, MainWindow):
        super(uninstallInstructionsWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "For smooth installation process some of the old components of WOIS have to be uninstalled if they are present on your computer.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "Please follow the uninstallation instructions present in the 'WOIS installation' document located in the WOIS installation directory.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Uninstall old version", None)) 

# OSGeo4W       
class osgeo4wInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/osgeo4wLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(osgeo4wInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "QGIS is the main GUI used by WOIS while Orfeo Toolbox and GRASS GIS provide many of the commonly used data processing functions. They are installed together through the OSGeo4W installer.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the OSGeo4W installer will start. The process should be automatic but if any question dialogs pop-up just click OK", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install QGIS, Orfeo Toolbox and GRASS GIS", None))   

# Instructions for activating WOIS plugins
class pluginsInstructionsWindow(instructionsWindow):
    def __init__(self):
        instructionsWindow.__init__(self)
     
    def retranslateUi(self, MainWindow):
        super(pluginsInstructionsWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "The different WOIS components are integrated into QGIS using plugins.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "After clicking on the \"Continue\" button QGIS will start. In the program select \"Plugins\" > \"Manage Plugins…\" from the main menu, find the 1-Band Raster Colour Table, OpenLayers, PostGIS manager, SEXTANTE, SEXTANT BEAM and NEST Provider, SEXTANTE Working Group 9 Hydrological Model Provider, WOIS Workflows and Zonal statistics plugins in the list and tick the boxes next to them and click OK. Afterwards close QGIS.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Activate plugins", None)) 
        
# BEAM       
class beamInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/beamLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(beamInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "BEAM is a software for analyzing optical and thermal data derived with satellites operated by European Space Agency (ESA) and other organisation.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the BEAM installer will start. In the installer you will be asked to accept the BEAM license conditions followed by a couple of installation questions. In all the questions you can keep the default answers by clicking \"Next >\" until the installation starts.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install BEAM", None))   
        
class beamPostInstallWindow(postInstallWindow):
    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        postInstallWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/beamLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(beamPostInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "BEAM is a software for analyzing optical and thermal data derived with satellites operated by European Space Agency (ESA) and other organisation.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "The WOIS installer will now perform additional post installation tasks for BEAM. If you changed the BEAM installation directory during the previous step, make sure that you update the path to the directory below.", None))
        self.dirPathText.setPlainText(_translate("MainWindow", self.defaultPath, None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install BEAM", None))

# NEST        
class nestInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/nestLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(nestInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "NEST is a software for analyzing radar data derived with satellites operated by European Space Agency (ESA) and other organisation.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the NEST installer will start. In the installer you will be asked to accept the NEST license conditions followed by a couple of installation questions. In all the questions you can keep the default answers by clicking \"Next >\" until the installation starts.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install NEST", None))   
        
class nestPostInstallWindow(postInstallWindow):
    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        postInstallWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/nestLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(nestPostInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "NEST is a software for analyzing radar data derived with satellites operated by European Space Agency (ESA) and other organisation.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "The WOIS installer will now perform additional post installation tasks for NEST. If you changed the NEST installation directory during the previous step, make sure that you update the path to the directory below.", None))
        self.dirPathText.setPlainText(_translate("MainWindow", self.defaultPath, None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install NEST", None))
                
# R
class rInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/rLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(rInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "R is a statistical scripting language used by WOIS for various data processing tasks.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the OSGeo4W installer will start. In the installer you will be asked to accept the R license conditions followed by a couple of installation questions. In all the questions you can keep the default answers by clicking \"Next >\" until the installation starts.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install R", None))   

class rPostInstallWindow(postInstallWindow):
    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        postInstallWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/rLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(rPostInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "R is a statistical scripting language used by WOIS for various data processing tasks.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "The WOIS installer will now perform additional post installation tasks for R. If you changed the R installation directory during the previous step, make sure that you update the path to the directory below.", None))
        self.dirPathText.setPlainText(_translate("MainWindow", self.defaultPath, None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install R", None))
        
# PostGre
class postgreInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/postgisLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(postgreInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "PostGIS is a geospatial database used by WOIS for storing certain types of data. It is not necessary to have it installed on every computer using WOIS, since the database can run from a central server. Therefore its installation is optional.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the PostgreSQL (PostGIS back-end) installer will start. You can keep all the default options and set superuser password (e.g. waterinfo) when requested. <b>Remember to write down the superuser name and the password.</b> In the last step make sure that the option to launch Stack Builder is <b>NOT</b> selected.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install PostGIS (Optional)", None)) 

# PostGIS        
class postgisInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/postgisLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(postgisInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "PostGIS is a geospatial database used by WOIS for storing certain types of data. It is not necessary to have it installed on every computer using WOIS, since the database can run from a central server. Therefore its installation is optional.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the PostGIS installer will start. You need to accept the license and in then select both 'PostGIS' and 'Create spatial database'. Two steps later you will need to <b>enter the password set earlier during the installation</b> (e.g. waterinfo) and in the following step the name of the database (e.g. WOIS_local). If any questions pop up just click Yes.", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Install PostGIS (Optional)", None)) 
        
# MapWindow       
class mapwindowInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/swatLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(mapwindowInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "SWAT is used by WOIS for hydrological modeling. It is an advanced component and not every user requires the hydrological modeling functionality. Therefore its installation is optional.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the MapWindow installer will start. MapWindow is used as front end for setting up new SWAT models. During the installation keep all the default options", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - SWAT hydrological model (Optional)", None))  
# MWSWAT        
class mwswatInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/swatLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(mwswatInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "SWAT is used by WOIS for hydrological modeling. It is an advanced component and not every user requires the hydrological modeling functionality. Therefore its installation is optional.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the MWSWAT 2009 installer will start. MWSWAT is the SWAT implementation used by WOIS. During the installation keep all the default options", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - SWAT hydrological model (Optional)", None))  

class mwswatPostInstallWindow(postInstallWindow):
    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        postInstallWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/mwswatLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(mwswatPostInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "SWAT is used by WOIS for hydrological modeling. It is an advanced component and not every user requires the hydrological modeling functionality. Therefore its installation is optional.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "The WOIS installer will now perform additional post installation tasks for SWAT. If you changed the MapWindow installation directory during the previous steps, make sure that you update the path to the directory below.", None))
        self.dirPathText.setPlainText(_translate("MainWindow", self.defaultPath, None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - SWAT hydrological model (Optional)", None))
        

# MWSWAT editor        
class swateditorInstallWindow(installWindow):
    def __init__(self):
        installWindow.__init__(self)
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/swatLogo.png")))
        
    def retranslateUi(self, MainWindow):
        super(swateditorInstallWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "SWAT is used by WOIS for hydrological modeling. It is an advanced component and not every user requires the hydrological modeling functionality. Therefore its installation is optional.", None))
        self.instructionMainLabel.setText(_translate("MainWindow", "After clicking on the \"Install\" button the SWAT editor installer will start. SWAT editor is used for setting up new SWAT models. During the installation keep all the default options", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - SWAT hydrological model (Optional)", None))  
              
# Finish
class finishWindow(instructionsWindow):
    def __init__(self):
        instructionsWindow.__init__(self)
     
    def retranslateUi(self, MainWindow):
        super(finishWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "The WOIS has now been installed on your computer. Thank you.", None))
        self.instructionsMainLabel.setText(_translate("MainWindow", "You can now start QGIS to begin working with the Water Information and Observation System.", None))
        self.continueButton.setVisible(False)
        self.instructionsHeaderLabel.setVisible(False)
        self.bottomLabel.setVisible(False)
        self.instructionsFooterLabel.setText(_translate("MainWindow", "Click \"Finish\" to finish the installation process", None))
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Finished", None))    
        self.cancelButton.setText(_translate("MainWindow", "Finish", None))    

        
# Extracting please wait
class extractingWaitWindow(instructionsWindow, QtCore.QObject):   
    
    def __init__(self, utilities, archivePath, dstPath):
        QtCore.QObject.__init__(self)
        
        self.utilities = utilities
        self.archivePath = archivePath
        self.dstPath = dstPath
        
        # Use a thread and modified QDialog to display the waiting dialog and
        # extract the files at the same time
        self.workerThread = QtCore.QThread(self)
        self.MainWindow = myQDialog(self.workerThread)
        instructionsWindow.__init__(self, self.MainWindow)
        
        self.utilities.moveToThread(self.workerThread)
        self.utilities.finished.connect(self.workerThread.quit)
        self.workerThread.finished.connect(self.slotFinished)
        self.workerThread.started.connect(self.startAction)
        
     
    def retranslateUi(self, MainWindow):
        super(extractingWaitWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "Extracting an archive. Please wait...", None))
        self.instructionsMainLabel.setVisible(False)
        self.continueButton.setVisible(False)
        self.instructionsHeaderLabel.setVisible(False)
        self.bottomLabel.setVisible(False)
        self.instructionsFooterLabel.setVisible(False)
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Extracting an archive", None))    
        self.cancelButton.setVisible(False)  
              
    def startAction(self):
        self.utilities.unzipArchive(self.archivePath, self.dstPath)
        
    def slotFinished(self):
        self.action = NEXT
        self.MainWindow.close()  
        
# Copying please wait
class copyingWaitWindow(instructionsWindow, QtCore.QObject):
    def __init__(self, utilities, srcPath, dstPath, checkDstParentExists = False):
        QtCore.QObject.__init__(self)
        
        self.utilities = utilities
        self.srcPath = srcPath
        self.dstPath = dstPath
        self.checkDstParentExists = checkDstParentExists
        
        # Use a thread and modified QDialog to display the waiting dialog and
        # extract the files at the same time
        self.workerThread = QtCore.QThread(self)
        self.MainWindow = myQDialog(self.workerThread)
        instructionsWindow.__init__(self, self.MainWindow)
        
        self.utilities.moveToThread(self.workerThread)
        self.utilities.finished.connect(self.workerThread.quit)
        self.workerThread.finished.connect(self.slotFinished)
        self.workerThread.started.connect(self.startAction)
     
    def retranslateUi(self, MainWindow):
        super(copyingWaitWindow, self).retranslateUi(MainWindow)
        self.topLabel.setText(_translate("MainWindow", "Copying files. Please wait...", None))
        self.instructionsMainLabel.setVisible(False)
        self.continueButton.setVisible(False)
        self.instructionsHeaderLabel.setVisible(False)
        self.bottomLabel.setVisible(False)
        self.instructionsFooterLabel.setVisible(False)
        self.MainWindow.setWindowTitle(_translate("MainWindow", "WOIS Installation - Copying Files", None))    
        self.cancelButton.setVisible(False)  
     
    def startAction(self):
        self.utilities.copyFiles(self.srcPath, self.dstPath, self.checkDstParentExists)
        
    def slotFinished(self):
        self.action = NEXT
        self.MainWindow.close()  
        
# Reimplement QDialog to start a given thread shortly after the dialog is displayed       
class myQDialog(QtGui.QDialog):
      
        def __init__(self, workerThread):
            super(myQDialog, self).__init__()
            self.workerThread = workerThread 
            self.timer = None  
        
        def showEvent(self, event):
            super(myQDialog, self).showEvent(event)
            self.timer = self.startTimer(200)
            
        def timerEvent(self, event):
            super(myQDialog, self).timerEvent(event)
            self.workerThread.start()
            if (self.timer):
                self.killTimer(self.timer)
                self.timer = None       
