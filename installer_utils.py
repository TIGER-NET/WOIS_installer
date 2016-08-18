import os
import sys
import re
import shutil
from PyQt4 import QtGui

import ctypes
from ctypes import wintypes

def _ram():
    """Get amount of physical memory"""
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


def modifyRamInBatFiles(batFilePath, useRamFraction):
    # Check how much RAM the system has. Only works in Windows
    if sys.platform != 'win32':
        msgBox = QtGui.QMessageBox()
        msgBox.setText("This installer is only meant for Windows!\n\n The installed WOIS might not work properly.")
        msgBox.exec_()
        return
    totalRam = _ram()
    totalRam = totalRam / (1024*1024)

    # Make sure the BEAM/SNAP batch file exists in the given directory
    if not os.path.isfile(batFilePath):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Could not find the batch file!\n\n The amount of RAM available to the program was not changed.")
        msgBox.exec_()
        return

    if batFilePath.endswith('.bat'):
        # Beam
        # In the batch file replace the amount of RAM to be used
        # by BEAM to some % of system RAM, first in a temp file
        # and then copy the temp file to the correct dir
        ram_flag = "-Xmx"+str(int(totalRam*useRamFraction))+"M"
        backupfile = batFilePath + '.backup'
        try:
            os.remove(backupfile)
        except WindowsError:
            pass
        shutil.move(batFilePath, backupfile)
        try:
            with open(backupfile, 'r') as infile, open(batFilePath, 'w') as outfile:
                for line in infile:
                    line = re.sub(r"-Xmx\d+[Mm]", ram_flag, line)
                    outfile.write(line)
        except:
            shutil.move(backupfile, batFilePath)
            raise

    elif batFilePath.endswith('.vmoptions'):
        # Snap
        # In the vmoptions file replace the amount of RAM to be used
        # by SNAP to some % of system RAM, first in a temp file
        # and then copy the temp file to the correct dir
        ram_flag = "-Xmx"+str(int(totalRam*useRamFraction))+"m"
        backupfile = batFilePath + '.backup'
        try:
            os.remove(backupfile)
        except WindowsError:
            pass
        shutil.move(batFilePath, backupfile)
        try:
            with open(backupfile, 'r') as infile, open(batFilePath, 'w') as outfile:
                for line in infile:
                    if '-Xmx' in line:
                        # omit old -Xmx flags
                        continue
                    outfile.write(line)
                outfile.write(ram_flag)
        except:
            shutil.move(backupfile, batFilePath)
            raise


def check_file_exists(filepath):
    if not os.path.isfile(filepath):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Could not find the required file \'{}\'.\n\n Skipping this step.".format(filepath))
        msgBox.exec_()
        return False
    else:
        return True
