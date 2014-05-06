# -*- coding: utf-8 -*-
'''
Created on 07/04/2014

@author: rmgu
'''
from PyQt4 import QtCore, QtGui
from  installerGUI import  installerWelcomeWindow, beamInstallWindow, beamPostInstallWindow, nestInstallWindow, nestPostInstallWindow 
from installerGUI import osgeo4wInstallWindow, rInstallWindow, postgreInstallWindow, postgisInstallWindow
from installerGUI import mapwindowInstallWindow, mwswatInstallWindow, mwswatPostInstallWindow, swateditorInstallWindow, pluginsInstructionsWindow, finishWindow
from installerGUI import extractingWaitWindow, copyingWaitWindow
from installerGUI import CANCEL,SKIP,NEXT
import sys
import os
import shutil
import subprocess
import _winreg
import ctypes
from ctypes import wintypes
import re
from tempfile import NamedTemporaryFile
from zipfile import ZipFile
from distutils import dir_util

class woisInstaller():

    def __init__(self):
        self.util = Utilities()
        self.runInstaller()
        
        
    def runInstaller (self):
        ########################################################################
        # welcome window with license
        self.dialog =  installerWelcomeWindow();
        self.showDialog()
        
        if self.dialog.action == NEXT:
            # select installation files for 32 or 64 bit install
            if self.dialog.osComboBox.itemText(self.dialog.osComboBox.currentIndex()) == "32 bit":
                is32bit = True
                installationsDir = "installations_x32"
                osgeo4wInstall = os.path.join(installationsDir, "osgeo4w-setup.bat")
                beamInstall = os.path.join(installationsDir, "beam_4.10.3_win32_installer.exe")
                nestInstall = os.path.join(installationsDir, "NEST-4C-1.1-windows-installer.exe")
                rInstall = os.path.join(installationsDir, "R-2.15.2-win.exe")
                postgreInstall = os.path.join(installationsDir, "postgresql-9.2.4-1-windows.exe")
                postgisInstall = os.path.join(installationsDir, "postgis-pg92-setup-2.0.1-1.exe")
                mapwindowInstall = os.path.join(installationsDir, "MapWindowx86Full-v48Final-installer.exe")
                mwswatInstall = os.path.join(installationsDir, "MWSWAT2009.exe")
                swateditorInstall = "MWSWAT additional software\\SwatEditor_Install\\Setup.exe"
            else:
                is32bit = False
                installationsDir = "installations_x64"
                osgeo4wInstall = os.path.join(installationsDir, "osgeo4w-setup.bat")
                beamInstall = os.path.join(installationsDir, "beam_4.10.3_win64_installer.exe")
                nestInstall = os.path.join(installationsDir, "NEST-4C-1.1-windows64-installer.exe")
                rInstall = os.path.join(installationsDir, "R-2.15.2-win.exe")
                postgreInstall = os.path.join(installationsDir, "postgresql-9.2.2-1-windows-x64.exe")
                postgisInstall = os.path.join(installationsDir, "postgis-pg92x64-setup-2.0.1-1.exe")
                mapwindowInstall = os.path.join(installationsDir, "MapWindowx86Full-v48Final-installer.exe")
                mwswatInstall = os.path.join(installationsDir, "MWSWAT2009.exe")
                swateditorInstall = "MWSWAT additional software\\SwatEditor_Install\\Setup.exe"
            # select default installation directories for 32 or 64 bit install
            if is32bit:
                osgeo4wDefaultDir = "C:\\OSGeo4W"
                nestDefaultDir = "C:\\Program Files\\NEST4C-1.1"
                beamDefaultDir = "C:\\Program Files\\beam-4.10.3"
                mapwindowDefaultDir = "C:\\Program Files\\MapWindow"
            else:
                osgeo4wDefaultDir = "C:\\OSGeo4W" # in next version change this one to OSGeo4W64
                nestDefaultDir = "C:\\Program Files (x86)\\NEST4C-1.1"
                beamDefaultDir = "C:\\Program Files\\beam-4.10.3"
                mapwindowDefaultDir = "C:\\Program Files (x86)\\MapWindow"
                
        elif self.dialog.action == CANCEL:
            return  
        else:
            self.unknownActionPopup() 
        
        ########################################################################
        # Install OSGeo4W (QGIS, OTB, SAGA, GRASS)
        
        if not self.dialog.action == CANCEL:
            self.dialog = osgeo4wInstallWindow();
            self.showDialog()
        
        # run the OSGeo4W installation here as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(osgeo4wInstall)
            # copy the plugins
            # for QGIS 1.8 copy the plugins to the user directory because of a bug in Atlas plugin. In QGIS 2.0 use the qgis directory
            #dstPath = os.path.join(osgeo4wDefaultDir,"apps\\qgis\\python")
            dstPath = os.path.join(os.path.expanduser("~"),".qgis","python")
            srcPath = os.path.join("QGIS WOIS plugins", "plugins.zip")
            self.dialog = extractingWaitWindow(self.util, srcPath, dstPath) # show dialog because it might take some time on slower computers
            self.showDialog()
            # copy the config file
            dstPath = os.path.join(os.path.expanduser("~"),".qgis","sextante")
            srcPath = os.path.join(installationsDir,"sextante_qgis.conf")
            self.util.copyFiles(srcPath, dstPath, checkDstParentExists = False)   
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
        
#         # start QGIS so that user can activate plugins    
#         if self.dialog.action == NEXT:
#             qgisExePath = os.path.join(osgeo4wDefaultDir,"bin","qgis.bat")
#             self.util.execSubprocess(qgisExePath)
#         elif self.dialog.action == SKIP:
#             pass
#         elif self.dialog.action == CANCEL:
#             self.quit()
#         else:
#             self.unknownActionPopup()
        
        ########################################################################
        # Install BEAM
        
        if not self.dialog.action == CANCEL:
            self.dialog = beamInstallWindow();
            self.showDialog()    
         
        # run the BEAM installation here as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(beamInstall)
            self.dialog =  beamPostInstallWindow(beamDefaultDir);
            self.showDialog()
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()  
         
        # copy the additional BEAM modules and set the amount of memory to be used with GPT    
        if self.dialog.action == NEXT:
            dirPath = str(self.dialog.dirPathText.toPlainText())
            dstPath = os.path.join(dirPath,"modules")
            srcPath = "BEAM additional modules"
            self.dialog = copyingWaitWindow(self.util, srcPath, dstPath) # show dialog because it might take some time on slower computers
            self.showDialog()
            #self.util.copyFiles(srcPath, dstPath)
            self.util.modifyRamInBatFiles(os.path.join(dirPath,"bin",'gpt.bat'))
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup() 
                 
        ########################################################################
        # Install NEST
         
        if not self.dialog.action == CANCEL:
            self.dialog = nestInstallWindow();
            self.showDialog()
         
        # run the NEST installation here as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(nestInstall)
            self.dialog =  nestPostInstallWindow(nestDefaultDir);
            self.showDialog()
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
             
        # Set the amount of memory to be used with NEST GPT    
        if self.dialog.action == NEXT:
            self.util.modifyRamInBatFiles(os.path.join(str(self.dialog.dirPathText.toPlainText()),'gpt.bat'))
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup() 
         
         
        ########################################################################
        # Install R
         
        if not self.dialog.action == CANCEL:
            self.dialog = rInstallWindow();
            self.showDialog()
         
        # run the R installation here as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(rInstall)
             
            dstPath = os.path.join(os.path.expanduser("~"),".qgis","sextante","rlibs")
            srcPath = "R additional libraries"
            self.dialog = extractingWaitWindow(self.util, os.path.join(srcPath, "libraries.zip"), dstPath) # show dialog because it might take some time on slower computers
            self.showDialog()
            #self.unzipArchive(os.path.join(srcPath, "libraries.zip"), dstPath )
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
             
             
        ########################################################################
        # Install PostGIS
         
        if not self.dialog.action == CANCEL:
            self.dialog = postgreInstallWindow();
            self.showDialog()
         
        # run the postgresql installer as an outside process
        if self.dialog.action == NEXT:
            self.util.execSubprocess(postgreInstall)
            self.dialog = postgisInstallWindow();
            self.showDialog()    
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()    
         
        # run the postgis installer as an outside process
        if self.dialog.action == NEXT:
            self.util.execSubprocess(postgisInstall)  
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()  
             
        ########################################################################
        # Install MapWindow, SWAT and PEST
         
        if not self.dialog.action == CANCEL:
            self.dialog = mapwindowInstallWindow();
            self.showDialog()  
         
        # run the MapWindow installer as an outside process
        if self.dialog.action == NEXT:
            self.util.execSubprocess(mapwindowInstall)
            self.dialog = mwswatInstallWindow();
            self.showDialog()    
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
         
        # run the MWSWAT installer as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(mwswatInstall)
            self.dialog = swateditorInstallWindow();
            self.showDialog()    
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
         
        # run the SWAT editor installer as an outside process    
        if self.dialog.action == NEXT:
            self.util.execSubprocess(swateditorInstall)
            self.dialog = mwswatPostInstallWindow(mapwindowDefaultDir);
            self.showDialog()    
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup()
             
        if self.dialog.action == NEXT:
            # copy the DTU customised MWSWAT 2009 installation
            mwswatPath = os.path.join(str(self.dialog.dirPathText.toPlainText()),"Plugins","MWSWAT2009")
            dstPath = os.path.join(mwswatPath,'swat2009DtuEnvVers0.1')
            srcPath = "MWSWAT additional software\\swat2009DtuEnvVers0.1"
            self.dialog = copyingWaitWindow(self.util, srcPath, dstPath) # show dialog because it might take some time on slower computers
            self.showDialog()
            #self.copyFiles(srcPath, dstPath)
            # copy and rename the customised MWSWAT exe
            if os.path.isfile(os.path.join(mwswatPath,"swat2009rev481.exe_old")):
                os.remove(os.path.join(mwswatPath,"swat2009rev481.exe_old"))
            os.rename(os.path.join(mwswatPath,"swat2009rev481.exe"), os.path.join(mwswatPath,"swat2009rev481.exe_old"))
            self.util.copyFiles(os.path.join(dstPath, "swat2009DtuEnv.exe"), mwswatPath)
            if os.path.isfile(os.path.join(mwswatPath,"swat2009rev481.exe")):
                os.remove(os.path.join(mwswatPath,"swat2009rev481.exe"))
            os.rename(os.path.join(mwswatPath,"swat2009DtuEnv.exe"), os.path.join(mwswatPath, "swat2009rev481.exe"))
            # copy the modified database file
            self.util.copyFiles("MWSWAT additional software\\mwswat2009.mdb", mwswatPath)
            # copy PEST
            self.dialog = copyingWaitWindow(self.util, "MWSWAT additional software\\PEST", os.path.join(mwswatPath,"PEST")) # show dialog because it might take some time on slower computers
            self.showDialog()
            #self.copyFiles("MWSWAT additional software\\PEST", os.path.join(mwswatPath,"PEST"))
        elif self.dialog.action == SKIP:
            pass
        elif self.dialog.action == CANCEL:
            return
        else:
            self.unknownActionPopup() 
         
        # Finish
        if not self.dialog.action == CANCEL:
            self.dialog = finishWindow();
            self.showDialog()     
            
    def showDialog(self):
        self.dialog.exec_()
        
    
    ##########################################
    # helper functions
    
class Utilities(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self):
        
        QtCore.QObject.__init__(self)
        
    def execSubprocess(self, command):
        # command should be a path to an exe file so check if it exists
        if not os.path.isfile(command):
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Could not find the installation file for this component!\n\n Skipping to next component")
            msgBox.exec_()
            self.dialog.action = SKIP
            return
            
        proc = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                ).stdout   
        for line in iter(proc.readline, ""):
            pass
                
    def unknownActionPopup(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Unknown action chosen in the previous installation step. Ask the developer to check the installation script!\n\n Quitting installation")
        msgBox.exec_()
        self.quit() 
        
    def copyFiles(self, srcPath, dstPath, checkDstParentExists = True):
        
        # a simple check to see if we are copying to the right directory by making sure that 
        # its parent exists
        if checkDstParentExists:
            if not os.path.isdir(os.path.dirname(dstPath)):
                msgBox = QtGui.QMessageBox()
                msgBox.setText("Could not find the destination directory!\n\n No files were copied.")
                msgBox.exec_()
                self.finished.emit()
                return
        
        # for directories copy the whole directory recursivelly
        if os.path.isdir(srcPath):
            dir_util.copy_tree(srcPath, dstPath)
        # for files create destination directory is necessary and copy the file
        elif os.path.isfile(srcPath):
            if not os.path.isdir(dstPath):
                os.makedirs(dstPath)
            shutil.copy(srcPath, dstPath)
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Cannot find the source directory!\n\n No files were copied.")
            msgBox.exec_()
            
        self.finished.emit()
    
    def unzipArchive(self, archivePath, dstPath):
        if not os.path.isfile(archivePath):
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Could not find the archive!\n\n No files were extracted.")
            msgBox.exec_()
            self.finished.emit()
            return
        if not os.path.isdir(dstPath):
            os.makedirs(dstPath)
        
        archive = ZipFile(archivePath)
        archive.extractall(dstPath)
        archive.close()
        self.finished.emit()
                
    def modifyRamInBatFiles(self, batFilePath):
        # Check how much RAM the system has. Only works in Windows
        if sys.platform != 'win32':
            msgBox = QtGui.QMessageBox()
            msgBox.setText("This installer is only meant for Windows!\n\n The installed WOIS might not work properly.")
            msgBox.exec_()
            return
        totalRam = self._ram()
        totalRam = totalRam / (1024*1024)
        
        # Make sure the BEAM/NEST batch file exists in the given directory
        if not os.path.isfile(batFilePath):
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Could not find the batch file!\n\n The amount of RAM available to the program was not changed.")
            msgBox.exec_()
            return
        
        # In the batch file replace the amount of RAM to be used by BEAM/NEST to 70% of system RAM, first in a temp file 
        # and then copy the temp file to the correct dir
        tempFile = NamedTemporaryFile(delete=False)
        tempFilePath = tempFile.name
        tempFile.close()
        with open(tempFilePath, 'w') as outfile, open(batFilePath, 'r') as infile:
            for line in infile:
                line = re.sub(r"-Xmx\d{4}M", "-Xmx"+str(int(totalRam*0.70))+"M", line)
                outfile.write(line)
        tempDir = os.path.dirname(tempFilePath)
        if os.path.isfile(os.path.join(tempDir,"gpt.bat")):
            os.remove(os.path.join(tempDir,"gpt.bat"))
        os.rename(tempFilePath, os.path.join(tempDir,"gpt.bat"))
        shutil.copy(os.path.join(tempDir,"gpt.bat"), batFilePath)
    
    
    def _ram(self):
        kernel32 = ctypes.windll.kernel32
        c_ulonglong = ctypes.c_ulonglong
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ('dwLength', wintypes.DWORD),
                ('dwMemoryLoad', wintypes.DWORD),
                ('ullTotalPhys', c_ulonglong),
                ('ullAvailPhys', c_ulonglong),
                ('ullTotalPageFile', c_ulonglong),
                ('ullAvailPageFile', c_ulonglong),
                ('ullTotalVirtual', c_ulonglong),
                ('ullAvailVirtual', c_ulonglong),
                ('ullExtendedVirtual', c_ulonglong),
            ]
 
        memoryStatus = MEMORYSTATUSEX()
        memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        kernel32.GlobalMemoryStatusEx(ctypes.byref(memoryStatus))
        return (memoryStatus.ullTotalPhys)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    installer = woisInstaller()
    app.exec_()
