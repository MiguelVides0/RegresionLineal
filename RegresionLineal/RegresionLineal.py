# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegresionLineal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1150, 950)
        Dialog.setMinimumSize(QtCore.QSize(1150, 950))
        Dialog.setMaximumSize(QtCore.QSize(1150, 950))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(189, 250, 188);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 10, 571, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblxi = QtWidgets.QLabel(Dialog)
        self.lblxi.setGeometry(QtCore.QRect(70, 150, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblxi.setFont(font)
        self.lblxi.setText("")
        self.lblxi.setObjectName("lblxi")
        self.lblyi = QtWidgets.QLabel(Dialog)
        self.lblyi.setGeometry(QtCore.QRect(260, 150, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblyi.setFont(font)
        self.lblyi.setText("")
        self.lblyi.setObjectName("lblyi")
        self.txtxi1 = QtWidgets.QLineEdit(Dialog)
        self.txtxi1.setEnabled(False)
        self.txtxi1.setGeometry(QtCore.QRect(120, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi1.setFont(font)
        self.txtxi1.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi1.setObjectName("txtxi1")
        self.txtxi2 = QtWidgets.QLineEdit(Dialog)
        self.txtxi2.setEnabled(False)
        self.txtxi2.setGeometry(QtCore.QRect(120, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi2.setFont(font)
        self.txtxi2.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi2.setObjectName("txtxi2")
        self.txtxi3 = QtWidgets.QLineEdit(Dialog)
        self.txtxi3.setEnabled(False)
        self.txtxi3.setGeometry(QtCore.QRect(120, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi3.setFont(font)
        self.txtxi3.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi3.setObjectName("txtxi3")
        self.txtxi4 = QtWidgets.QLineEdit(Dialog)
        self.txtxi4.setEnabled(False)
        self.txtxi4.setGeometry(QtCore.QRect(120, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi4.setFont(font)
        self.txtxi4.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi4.setObjectName("txtxi4")
        self.txtxi5 = QtWidgets.QLineEdit(Dialog)
        self.txtxi5.setEnabled(False)
        self.txtxi5.setGeometry(QtCore.QRect(120, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi5.setFont(font)
        self.txtxi5.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi5.setObjectName("txtxi5")
        self.txtxi6 = QtWidgets.QLineEdit(Dialog)
        self.txtxi6.setEnabled(False)
        self.txtxi6.setGeometry(QtCore.QRect(120, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi6.setFont(font)
        self.txtxi6.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi6.setObjectName("txtxi6")
        self.txtxi7 = QtWidgets.QLineEdit(Dialog)
        self.txtxi7.setEnabled(False)
        self.txtxi7.setGeometry(QtCore.QRect(120, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi7.setFont(font)
        self.txtxi7.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi7.setObjectName("txtxi7")
        self.txtyi1 = QtWidgets.QLineEdit(Dialog)
        self.txtyi1.setEnabled(False)
        self.txtyi1.setGeometry(QtCore.QRect(280, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi1.setFont(font)
        self.txtyi1.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi1.setObjectName("txtyi1")
        self.txtyi3 = QtWidgets.QLineEdit(Dialog)
        self.txtyi3.setEnabled(False)
        self.txtyi3.setGeometry(QtCore.QRect(280, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi3.setFont(font)
        self.txtyi3.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi3.setObjectName("txtyi3")
        self.txtyi5 = QtWidgets.QLineEdit(Dialog)
        self.txtyi5.setEnabled(False)
        self.txtyi5.setGeometry(QtCore.QRect(280, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi5.setFont(font)
        self.txtyi5.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi5.setObjectName("txtyi5")
        self.txtyi2 = QtWidgets.QLineEdit(Dialog)
        self.txtyi2.setEnabled(False)
        self.txtyi2.setGeometry(QtCore.QRect(280, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi2.setFont(font)
        self.txtyi2.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi2.setObjectName("txtyi2")
        self.txtyi6 = QtWidgets.QLineEdit(Dialog)
        self.txtyi6.setEnabled(False)
        self.txtyi6.setGeometry(QtCore.QRect(280, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi6.setFont(font)
        self.txtyi6.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi6.setObjectName("txtyi6")
        self.txtyi7 = QtWidgets.QLineEdit(Dialog)
        self.txtyi7.setEnabled(False)
        self.txtyi7.setGeometry(QtCore.QRect(280, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi7.setFont(font)
        self.txtyi7.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi7.setObjectName("txtyi7")
        self.txtyi4 = QtWidgets.QLineEdit(Dialog)
        self.txtyi4.setEnabled(False)
        self.txtyi4.setGeometry(QtCore.QRect(280, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi4.setFont(font)
        self.txtyi4.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi4.setObjectName("txtyi4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 240, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(310, 240, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(460, 240, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtxiyi1 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi1.setEnabled(False)
        self.txtxiyi1.setGeometry(QtCore.QRect(440, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi1.setFont(font)
        self.txtxiyi1.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi1.setObjectName("txtxiyi1")
        self.txtxiyi2 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi2.setEnabled(False)
        self.txtxiyi2.setGeometry(QtCore.QRect(440, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi2.setFont(font)
        self.txtxiyi2.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi2.setObjectName("txtxiyi2")
        self.txtxiyi7 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi7.setEnabled(False)
        self.txtxiyi7.setGeometry(QtCore.QRect(440, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi7.setFont(font)
        self.txtxiyi7.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi7.setObjectName("txtxiyi7")
        self.txtxiyi5 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi5.setEnabled(False)
        self.txtxiyi5.setGeometry(QtCore.QRect(440, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi5.setFont(font)
        self.txtxiyi5.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi5.setObjectName("txtxiyi5")
        self.txtxiyi3 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi3.setEnabled(False)
        self.txtxiyi3.setGeometry(QtCore.QRect(440, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi3.setFont(font)
        self.txtxiyi3.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi3.setObjectName("txtxiyi3")
        self.txtxiyi6 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi6.setEnabled(False)
        self.txtxiyi6.setGeometry(QtCore.QRect(440, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi6.setFont(font)
        self.txtxiyi6.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi6.setObjectName("txtxiyi6")
        self.txtxiyi4 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi4.setEnabled(False)
        self.txtxiyi4.setGeometry(QtCore.QRect(440, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi4.setFont(font)
        self.txtxiyi4.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi4.setObjectName("txtxiyi4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(620, 240, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtxi22 = QtWidgets.QLineEdit(Dialog)
        self.txtxi22.setEnabled(False)
        self.txtxi22.setGeometry(QtCore.QRect(600, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi22.setFont(font)
        self.txtxi22.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi22.setObjectName("txtxi22")
        self.txtxi32 = QtWidgets.QLineEdit(Dialog)
        self.txtxi32.setEnabled(False)
        self.txtxi32.setGeometry(QtCore.QRect(600, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi32.setFont(font)
        self.txtxi32.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi32.setObjectName("txtxi32")
        self.txtxi62 = QtWidgets.QLineEdit(Dialog)
        self.txtxi62.setEnabled(False)
        self.txtxi62.setGeometry(QtCore.QRect(600, 580, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi62.setFont(font)
        self.txtxi62.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi62.setObjectName("txtxi62")
        self.txtxi72 = QtWidgets.QLineEdit(Dialog)
        self.txtxi72.setEnabled(False)
        self.txtxi72.setGeometry(QtCore.QRect(600, 640, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi72.setFont(font)
        self.txtxi72.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi72.setObjectName("txtxi72")
        self.txtxi12 = QtWidgets.QLineEdit(Dialog)
        self.txtxi12.setEnabled(False)
        self.txtxi12.setGeometry(QtCore.QRect(600, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi12.setFont(font)
        self.txtxi12.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi12.setObjectName("txtxi12")
        self.txtxi52 = QtWidgets.QLineEdit(Dialog)
        self.txtxi52.setEnabled(False)
        self.txtxi52.setGeometry(QtCore.QRect(600, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi52.setFont(font)
        self.txtxi52.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi52.setObjectName("txtxi52")
        self.txtxi42 = QtWidgets.QLineEdit(Dialog)
        self.txtxi42.setEnabled(False)
        self.txtxi42.setGeometry(QtCore.QRect(600, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi42.setFont(font)
        self.txtxi42.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi42.setObjectName("txtxi42")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 880, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtSumxi = QtWidgets.QLineEdit(Dialog)
        self.txtSumxi.setEnabled(False)
        self.txtSumxi.setGeometry(QtCore.QRect(130, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSumxi.setFont(font)
        self.txtSumxi.setStyleSheet("background-color: rgb(255, 221, 220);")
        self.txtSumxi.setObjectName("txtSumxi")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(100, 850, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(400, 240, 20, 691))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(90, 280, 651, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.txtSumyi = QtWidgets.QLineEdit(Dialog)
        self.txtSumyi.setEnabled(False)
        self.txtSumyi.setGeometry(QtCore.QRect(290, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSumyi.setFont(font)
        self.txtSumyi.setStyleSheet("background-color: rgb(255, 221, 220);")
        self.txtSumyi.setObjectName("txtSumyi")
        self.txtSumxiyi = QtWidgets.QLineEdit(Dialog)
        self.txtSumxiyi.setEnabled(False)
        self.txtSumxiyi.setGeometry(QtCore.QRect(450, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSumxiyi.setFont(font)
        self.txtSumxiyi.setStyleSheet("background-color: rgb(255, 221, 220);")
        self.txtSumxiyi.setObjectName("txtSumxiyi")
        self.txtSumxi2 = QtWidgets.QLineEdit(Dialog)
        self.txtSumxi2.setEnabled(False)
        self.txtSumxi2.setGeometry(QtCore.QRect(610, 880, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSumxi2.setFont(font)
        self.txtSumxi2.setStyleSheet("background-color: rgb(255, 221, 220);")
        self.txtSumxi2.setObjectName("txtSumxi2")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(230, 240, 20, 691))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(550, 240, 20, 681))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(40, 920, 711, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(80, 240, 20, 621))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(730, 240, 20, 691))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(30, 860, 20, 71))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(40, 850, 51, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(90, 230, 651, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(780, 380, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(780, 450, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtxiM = QtWidgets.QLineEdit(Dialog)
        self.txtxiM.setEnabled(False)
        self.txtxiM.setGeometry(QtCore.QRect(930, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiM.setFont(font)
        self.txtxiM.setStyleSheet("background-color: rgb(246, 255, 162);")
        self.txtxiM.setObjectName("txtxiM")
        self.txtyiM = QtWidgets.QLineEdit(Dialog)
        self.txtyiM.setEnabled(False)
        self.txtyiM.setGeometry(QtCore.QRect(930, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyiM.setFont(font)
        self.txtyiM.setStyleSheet("background-color: rgb(246, 255, 162);")
        self.txtyiM.setObjectName("txtyiM")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(810, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txtxiSum22 = QtWidgets.QLineEdit(Dialog)
        self.txtxiSum22.setEnabled(False)
        self.txtxiSum22.setGeometry(QtCore.QRect(930, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiSum22.setFont(font)
        self.txtxiSum22.setStyleSheet("background-color: rgb(246, 255, 162);")
        self.txtxiSum22.setObjectName("txtxiSum22")
        self.lblRespuesta = QtWidgets.QLabel(Dialog)
        self.lblRespuesta.setGeometry(QtCore.QRect(830, 630, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.lblRespuesta.setFont(font)
        self.lblRespuesta.setText("")
        self.lblRespuesta.setObjectName("lblRespuesta")
        self.txtEcuacion = QtWidgets.QLineEdit(Dialog)
        self.txtEcuacion.setEnabled(False)
        self.txtEcuacion.setGeometry(QtCore.QRect(820, 700, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.txtEcuacion.setFont(font)
        self.txtEcuacion.setObjectName("txtEcuacion")
        self.btnEcuacion = QtWidgets.QPushButton(Dialog)
        self.btnEcuacion.setEnabled(False)
        self.btnEcuacion.setGeometry(QtCore.QRect(490, 160, 131, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnEcuacion.setFont(font)
        self.btnEcuacion.setStyleSheet("background-color: rgb(211, 202, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Calcu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEcuacion.setIcon(icon1)
        self.btnEcuacion.setIconSize(QtCore.QSize(30, 30))
        self.btnEcuacion.setObjectName("btnEcuacion")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(860, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.txta1 = QtWidgets.QLineEdit(Dialog)
        self.txta1.setEnabled(False)
        self.txta1.setGeometry(QtCore.QRect(930, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txta1.setFont(font)
        self.txta1.setStyleSheet("background-color: rgb(246, 255, 162);")
        self.txta1.setObjectName("txta1")
        self.txta0 = QtWidgets.QLineEdit(Dialog)
        self.txta0.setEnabled(False)
        self.txta0.setGeometry(QtCore.QRect(930, 520, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txta0.setFont(font)
        self.txta0.setStyleSheet("background-color: rgb(246, 255, 162);")
        self.txta0.setText("")
        self.txta0.setObjectName("txta0")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(860, 510, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btnGrafica = QtWidgets.QPushButton(Dialog)
        self.btnGrafica.setEnabled(False)
        self.btnGrafica.setGeometry(QtCore.QRect(920, 840, 161, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnGrafica.setFont(font)
        self.btnGrafica.setStyleSheet("background-color: rgb(211, 202, 255);\n"
"")
        self.btnGrafica.setIcon(icon)
        self.btnGrafica.setIconSize(QtCore.QSize(40, 40))
        self.btnGrafica.setObjectName("btnGrafica")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(760, 730, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.btnBorrar = QtWidgets.QPushButton(Dialog)
        self.btnBorrar.setEnabled(True)
        self.btnBorrar.setGeometry(QtCore.QRect(660, 160, 131, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setStyleSheet("background-color: rgb(211, 202, 255);\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Borrar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrar.setIcon(icon2)
        self.btnBorrar.setIconSize(QtCore.QSize(30, 30))
        self.btnBorrar.setObjectName("btnBorrar")
        self.txtxi8 = QtWidgets.QLineEdit(Dialog)
        self.txtxi8.setEnabled(False)
        self.txtxi8.setGeometry(QtCore.QRect(120, 700, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi8.setFont(font)
        self.txtxi8.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi8.setObjectName("txtxi8")
        self.txtxi9 = QtWidgets.QLineEdit(Dialog)
        self.txtxi9.setEnabled(False)
        self.txtxi9.setGeometry(QtCore.QRect(120, 750, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi9.setFont(font)
        self.txtxi9.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi9.setObjectName("txtxi9")
        self.txtxi10 = QtWidgets.QLineEdit(Dialog)
        self.txtxi10.setEnabled(False)
        self.txtxi10.setGeometry(QtCore.QRect(120, 800, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi10.setFont(font)
        self.txtxi10.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtxi10.setObjectName("txtxi10")
        self.txtyi8 = QtWidgets.QLineEdit(Dialog)
        self.txtyi8.setEnabled(False)
        self.txtyi8.setGeometry(QtCore.QRect(280, 700, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi8.setFont(font)
        self.txtyi8.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi8.setObjectName("txtyi8")
        self.txtyi9 = QtWidgets.QLineEdit(Dialog)
        self.txtyi9.setEnabled(False)
        self.txtyi9.setGeometry(QtCore.QRect(280, 750, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi9.setFont(font)
        self.txtyi9.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi9.setObjectName("txtyi9")
        self.txtyi10 = QtWidgets.QLineEdit(Dialog)
        self.txtyi10.setEnabled(False)
        self.txtyi10.setGeometry(QtCore.QRect(280, 800, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtyi10.setFont(font)
        self.txtyi10.setStyleSheet("background-color: rgb(187, 248, 255);")
        self.txtyi10.setObjectName("txtyi10")
        self.txtxiyi8 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi8.setEnabled(False)
        self.txtxiyi8.setGeometry(QtCore.QRect(440, 700, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi8.setFont(font)
        self.txtxiyi8.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi8.setObjectName("txtxiyi8")
        self.txtxiyi9 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi9.setEnabled(False)
        self.txtxiyi9.setGeometry(QtCore.QRect(440, 760, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi9.setFont(font)
        self.txtxiyi9.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi9.setObjectName("txtxiyi9")
        self.txtxiyi10 = QtWidgets.QLineEdit(Dialog)
        self.txtxiyi10.setEnabled(False)
        self.txtxiyi10.setGeometry(QtCore.QRect(440, 810, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxiyi10.setFont(font)
        self.txtxiyi10.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxiyi10.setObjectName("txtxiyi10")
        self.txtxi82 = QtWidgets.QLineEdit(Dialog)
        self.txtxi82.setEnabled(False)
        self.txtxi82.setGeometry(QtCore.QRect(600, 700, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi82.setFont(font)
        self.txtxi82.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi82.setObjectName("txtxi82")
        self.txtxi92 = QtWidgets.QLineEdit(Dialog)
        self.txtxi92.setEnabled(False)
        self.txtxi92.setGeometry(QtCore.QRect(600, 750, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi92.setFont(font)
        self.txtxi92.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi92.setObjectName("txtxi92")
        self.txtxi102 = QtWidgets.QLineEdit(Dialog)
        self.txtxi102.setEnabled(False)
        self.txtxi102.setGeometry(QtCore.QRect(600, 810, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtxi102.setFont(font)
        self.txtxi102.setStyleSheet("background-color: rgb(250, 255, 198);")
        self.txtxi102.setObjectName("txtxi102")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtn = QtWidgets.QLineEdit(Dialog)
        self.txtn.setGeometry(QtCore.QRect(130, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtn.setFont(font)
        self.txtn.setStyleSheet("background-color: rgb(255, 219, 202);")
        self.txtn.setObjectName("txtn")
        self.btnDefinirN = QtWidgets.QPushButton(Dialog)
        self.btnDefinirN.setEnabled(True)
        self.btnDefinirN.setGeometry(QtCore.QRect(240, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnDefinirN.setFont(font)
        self.btnDefinirN.setStyleSheet("background-color: rgb(211, 202, 255);\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Definir.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDefinirN.setIcon(icon3)
        self.btnDefinirN.setObjectName("btnDefinirN")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(360, 80, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Regresion Lineal"))
        self.label.setText(_translate("Dialog", "Ecuaci??n de regresi??n Lineal"))
        self.label_5.setText(_translate("Dialog", "xi"))
        self.label_6.setText(_translate("Dialog", "yi"))
        self.label_7.setText(_translate("Dialog", "xi*yi"))
        self.label_8.setText(_translate("Dialog", "xi^2"))
        self.label_9.setText(_translate("Dialog", "??"))
        self.label_10.setText(_translate("Dialog", "Media de x="))
        self.label_11.setText(_translate("Dialog", "Media de y="))
        self.label_12.setText(_translate("Dialog", "(??xi)^2="))
        self.btnEcuacion.setText(_translate("Dialog", "Obtener \n"
"Funci??n"))
        self.label_14.setText(_translate("Dialog", "a1="))
        self.label_15.setText(_translate("Dialog", "a0="))
        self.btnGrafica.setText(_translate("Dialog", "Ver \n"
"Gr??fica"))
        self.label_16.setText(_translate("Dialog", "y="))
        self.btnBorrar.setText(_translate("Dialog", "Borrar \n"
"todo"))
        self.label_3.setText(_translate("Dialog", "n="))
        self.btnDefinirN.setText(_translate("Dialog", "Definir"))
        self.label_13.setText(_translate("Dialog", "Nota: n debe ser mayor o igual \n"
"a 5 o menor o igual a 10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
