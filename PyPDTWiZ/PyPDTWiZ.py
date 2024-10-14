

import nest_asyncio
nest_asyncio.apply()

import math
import asyncio
from PyQt5.QtCore import Qt
from pywizlight import wizlight, PilotBuilder, discovery
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, QComboBox,
                             QMenu,QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QPlainTextEdit)
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #CFD8DC ;");


        #FRAME
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 25, 540, 120))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(85)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        
        #Lights IP adress:
            
        #title:
        self.label1= QLabel(self.centralwidget)
        self.label1.setText("<font color=black>Lights IP adress:</font>")
        self.label1.setGeometry(QtCore.QRect(188, 40, 120, 22))
        font1 = QtGui.QFont()
        font1.setFamily("Verdana")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label1.setFont(font1)


        #Light 1:
        ##label text
        self.label2= QLabel(self.centralwidget)
        self.label2.setText("<font color=black>Light 1: </font>")
        self.label2.setGeometry(QtCore.QRect(188, 70, 90, 22))
        font2 = QtGui.QFont()
        font2.setFamily("Verdana")
        font2.setPointSize(8)
        font2.setWeight(75)
        font2.setBold(False)
        self.label2.setFont(font2)
        ##insert ip1
        self.text1=QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(245,68,100,27))
        self.text1.setObjectName("text1")    
        self.text1.setStyleSheet("background-color: white")
        #Light 2:
        ##label text
        self.label3= QLabel(self.centralwidget)
        self.label3.setText("<font color=black>Light 2: </font>")
        self.label3.setGeometry(QtCore.QRect(188, 103, 90, 22))
        self.label3.setFont(font2)
        ##insert ip2
        self.text2=QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(245,99,100,27))
        self.text2.setObjectName("text1")    
        self.text2.setStyleSheet("background-color: white")
        
        
        
        #IPs Search Button
        font3 = QtGui.QFont()
        font3.setFamily("Verdana")
        font3.setPointSize(8)
        font3.setWeight(65)
        font3.setBold(False)
        self.text4=QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text4.setGeometry(QtCore.QRect(450,80,120,30))
        self.text4.setObjectName("text1")    
        self.text4.setStyleSheet("background-color: white")
        self.label9= QLabel(self.centralwidget)
        self.label9.setText("<font color=black>Broadcast Space:</font>")
        self.label9.setGeometry(QtCore.QRect(452, 50, 161, 30))
        self.label9.setFont(font1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(580, 82, 28, 28))
        self.button2.setObjectName("button1")
        self.button2.clicked.connect(self.button2_searchIP)
        self.button2.setStyleSheet("background-color: white")
        self.button2.setFont(font3)
        
        
        
        
        #Wavelenght Range
        self.label4 = QLabel(self.centralwidget)
        self.label4.setText("<font color=black>Wavelength Ranges:</font>")
        self.label4.setGeometry(QtCore.QRect(144, 178, 161, 31))
        self.label4.setFont(font1)
        self.checkbox1 = QtWidgets.QCheckBox(' ( 466 \u00B1 30 ) nm', self.centralwidget)
        self.checkbox1.setGeometry(156, 207, 140, 28)
        self.checkbox1.setFont(font3)
        self.checkbox2 = QtWidgets.QCheckBox(' ( 520 \u00B1 28 ) nm', self.centralwidget)
        self.checkbox2.setGeometry(156, 234, 140, 28)
        self.checkbox2.setFont(font3)
        self.checkbox3 = QtWidgets.QCheckBox(' ( 629 \u00B1 19 ) nm', self.centralwidget)
        self.checkbox3.setGeometry(156, 261, 140, 28)
        self.checkbox3.setFont(font3)
        
        
        
        #Energy
        self.label5 = QLabel(self.centralwidget)
        self.label5.setText("<font color=black>Energy:</font>")
        self.label5.setGeometry(QtCore.QRect(429, 178, 161, 31))
        self.label5.setFont(font1)
        self.label6 = QLabel(self.centralwidget)
        self.label6.setText("<font color=black>(in J/m\u00b2)</font>")
        self.label6.setGeometry(QtCore.QRect(427, 200, 161, 31))
        self.label6.setFont(font3)
        self.text3=QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(408,234,90,31))
        self.text3.setObjectName("text1")    
        self.text3.setStyleSheet("background-color: white")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(515, 238, 25, 25))
        self.button7.clicked.connect(self.button7_conversion)
        self.button7.setStyleSheet("background-color: white")
        self.button7.setFont(font3)

        
        #Timer
        self.label7 = QLabel(self.centralwidget)
        self.label7.setText("<font color=black>Timer:</font>")
        self.label7.setGeometry(QtCore.QRect(581, 178, 161, 31))
        self.label7.setFont(font1)
        self.label8 = QLabel(self.centralwidget)
        self.label8.setText("<font color=black>(in seconds)</font>")
        self.label8.setGeometry(QtCore.QRect(569, 200, 161, 31))
        self.label8.setFont(font3)
        self.text5=QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text5.setGeometry(QtCore.QRect(558,234,90,31))
        self.text5.setObjectName("text1")    
        self.text5.setStyleSheet("background-color: white")

        
        
        #Set All Values - Button
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(100, 335, 120, 31))
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.button3_setvalues)
        self.button3.setStyleSheet("background-color: white")
        self.button3.setFont(font3)
        
        
        
        #Clear All Values - Button
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(260, 335, 120, 31))
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(self.button4_clearvalues)
        self.button4.setStyleSheet("background-color: white")        
        self.button4.setFont(font3)
        
 
        #Turn On - Button
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(420, 335, 120, 31))
        self.button5.setObjectName("button5")
        self.button5.clicked.connect(self.button5_turnon)
        self.button5.setStyleSheet("background-color: white")  
        self.button5.setFont(font3)
        
        
        
        #Turn Off - Button
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(580, 335, 120, 31))
        self.button6.setObjectName("button6")
        self.button6.clicked.connect(self.button6_turnoff)
        self.button6.setStyleSheet("background-color: white")  
        self.button6.setFont(font3)
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPDTWiZ"))
        self.button2.setText(_translate("MainWindow", u"\U0001F50D"))
        self.button3.setText(_translate("MainWindow", "Set All Values"))
        self.button4.setText(_translate("MainWindow", "Clear All Values"))
        self.button5.setText(_translate("MainWindow", "Turn On"))
        self.button6.setText(_translate("MainWindow", "Turn Off"))
        self.button7.setText(_translate("MainWindow", u"\u2194"))


    
    
    def button2_searchIP(self):
        self.broadcspace=str(self.text4.toPlainText())
        async def main():
            bulbs = await discovery.discover_lights(broadcast_space=self.broadcspace)
            self.text1.setPlainText(str(bulbs[0].ip))
            self.text2.setPlainText(str(bulbs[1].ip))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    
    
    
    def button3_setvalues(self):
        self.ip1=self.text1.toPlainText()
        self.ip2=self.text2.toPlainText()
        self.brightness=255
        self.time=str(self.text5.toPlainText())
        self.r=0
        self.b=0
        self.g=0
        
        if self.checkbox1.isChecked()==True:
            self.b=255

        if self.checkbox2.isChecked()==True:
            self.g=255
            
        if self.checkbox3.isChecked()==True:
            self.r=255
            

        
    
    def button4_clearvalues(self):
        self.text1.clear()
        self.text2.clear()
        self.text3.clear()
        self.text4.clear()
        self.text5.clear()
        self.checkbox1.setChecked(False)
        self.checkbox2.setChecked(False)
        self.checkbox3.setChecked(False)
        
    
    def button5_turnon(self):
        if self.time=="+":
            self.button5.setStyleSheet("background-color: dark grey")
            async def main():
                light1 = wizlight(self.ip1)
                light2 = wizlight(self.ip2)
                await asyncio.gather(light1.turn_on(PilotBuilder(rgb = (self.r,self.g,self.b))),light2.turn_on(PilotBuilder(rgb = (self.r,self.g,self.b))))
                await asyncio.gather(light1.turn_on(PilotBuilder(brightness = self.brightness)),light2.turn_on(PilotBuilder(brightness = self.brightness)))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            self.label10.setText("")
        else:
            self.button5.setStyleSheet("background-color: dark grey") 
            self.time=int(self.text5.toPlainText())
            async def main():
                light1 = wizlight(self.ip1)
                light2 = wizlight(self.ip2)
                await asyncio.gather(light1.turn_on(PilotBuilder(rgb = (self.r,self.g,self.b))),light2.turn_on(PilotBuilder(rgb = (self.r,self.g,self.b))))
                await asyncio.gather(light1.turn_on(PilotBuilder(brightness = self.brightness)),light2.turn_on(PilotBuilder(brightness = self.brightness)))
                await asyncio.sleep(self.time)
                await asyncio.gather(light1.turn_off(),light2.turn_off())
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            self.button5.setStyleSheet("background-color: white")

    
    
    
    def button6_turnoff(self):
        self.button5.setStyleSheet("background-color: white") 
        self.button6.setStyleSheet("background-color: dark grey") 
        async def main():
            light1 = wizlight(self.ip1)
            light2 = wizlight(self.ip2)
            await asyncio.gather(light1.turn_off(),light2.turn_off())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        self.button6.setStyleSheet("background-color: white") 
    
    def button7_conversion(self):
        cd_max=[59.35,262.02,127.67]
        input_user=float(self.text3.toPlainText())
        aux=2*math.pi*(1-math.cos(math.pi/180))/91
        
        if self.checkbox1.isChecked()==True:
            p=cd_max[0]*aux
            self.time=input_user/p
            self.text5.setPlainText(str(round(self.time)))

        if self.checkbox2.isChecked()==True:
            p=cd_max[1]*aux
            self.time=input_user/p
            self.text5.setPlainText(str(round(self.time)))
            
        if self.checkbox3.isChecked()==True:
            p=cd_max[2]*aux
            self.time=input_user/p
            self.text5.setPlainText(str(round(self.time)))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
