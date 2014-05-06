# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installComponentDialog.ui'
#
# Created: Tue May 06 09:13:19 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 464)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 320, 531, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(470, 420, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.topLabel = QtGui.QLabel(Dialog)
        self.topLabel.setGeometry(QtCore.QRect(20, 70, 401, 41))
        self.topLabel.setWordWrap(True)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.installButton = QtGui.QPushButton(Dialog)
        self.installButton.setGeometry(QtCore.QRect(290, 420, 75, 23))
        self.installButton.setObjectName(_fromUtf8("installButton"))
        self.bottomLabel2 = QtGui.QLabel(Dialog)
        self.bottomLabel2.setGeometry(QtCore.QRect(20, 380, 511, 31))
        self.bottomLabel2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.bottomLabel2.setWordWrap(True)
        self.bottomLabel2.setObjectName(_fromUtf8("bottomLabel2"))
        self.bottomLabel1 = QtGui.QLabel(Dialog)
        self.bottomLabel1.setGeometry(QtCore.QRect(20, 340, 511, 31))
        self.bottomLabel1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.bottomLabel1.setWordWrap(True)
        self.bottomLabel1.setObjectName(_fromUtf8("bottomLabel1"))
        self.skipButton = QtGui.QPushButton(Dialog)
        self.skipButton.setGeometry(QtCore.QRect(380, 420, 75, 23))
        self.skipButton.setObjectName(_fromUtf8("skipButton"))
        self.instructionMainLabel = QtGui.QLabel(Dialog)
        self.instructionMainLabel.setGeometry(QtCore.QRect(30, 180, 511, 61))
        self.instructionMainLabel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.instructionMainLabel.setWordWrap(True)
        self.instructionMainLabel.setObjectName(_fromUtf8("instructionMainLabel"))
        self.componentLogoLabel = QtGui.QLabel(Dialog)
        self.componentLogoLabel.setGeometry(QtCore.QRect(420, 90, 131, 51))
        self.componentLogoLabel.setText(_fromUtf8(""))
        self.componentLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("../images/beamLogo.png")))
        self.componentLogoLabel.setScaledContents(False)
        self.componentLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.componentLogoLabel.setObjectName(_fromUtf8("componentLogoLabel"))
        self.instructionsHeaderLabel = QtGui.QLabel(Dialog)
        self.instructionsHeaderLabel.setGeometry(QtCore.QRect(20, 150, 101, 41))
        self.instructionsHeaderLabel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.instructionsHeaderLabel.setWordWrap(True)
        self.instructionsHeaderLabel.setObjectName(_fromUtf8("instructionsHeaderLabel"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 140, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.logoLabel = QtGui.QLabel(Dialog)
        self.logoLabel.setGeometry(QtCore.QRect(420, 30, 131, 51))
        self.logoLabel.setText(_fromUtf8(""))
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8("../images/tigernetLogo.png")))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "WOIS Installation", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.topLabel.setText(_translate("Dialog", "BEAM is a software for analysing optical and thermal data derived with satellites operated by Europen Space Agency (ESA) and other organisation.", None))
        self.installButton.setText(_translate("Dialog", "Install", None))
        self.bottomLabel2.setText(_translate("Dialog", "If you would like to abandon the installation altogether, click \"Cancel\". The WOIS components that were already installed will remain on your computer.", None))
        self.bottomLabel1.setText(_translate("Dialog", "If you do not want to install this WOIS component click \"Skip\" to go the installation of the next component. However, note that by doing so you will not get the full WOIS functionality.", None))
        self.skipButton.setText(_translate("Dialog", "Skip", None))
        self.instructionMainLabel.setText(_translate("Dialog", "After clicking on the \"Install\" button the BEAM installer will start. In the installer you will be asked to accept the BEAM licence conditions followed by a couple of installation questions. In all the questions you can keep the defauly answers by clicking \"Next >\" untill the installation starts.", None))
        self.instructionsHeaderLabel.setText(_translate("Dialog", "Instructions:", None))

