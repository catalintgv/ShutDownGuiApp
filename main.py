import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMessageBox, QLabel
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import *
import os

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('timer.ui', self)
        #self.spinBox.setRange(2, 99)

        self.pushButton1.clicked.connect(self.inchide)
        self.pushButton2.clicked.connect(self.cancel)
        self.spinBox.valueChanged.connect(self.setval)

        self.label = QLabel('Selecteaza minute!',self)
##        font = label.font() #se seteaza font label
##        font.setPointSize(8)
##        label.setFont(font)
        self.setWindowIcon(QIcon('alarm-clock.png')) #seteaza icon
        self.setWindowTitle('Shutdown PC') #seteaza titlu
        self.setWindowOpacity(0.8) # opacitate
        self.setStyleSheet("""
            background-color: brown;
            color: white;
            selection-color: blue;
            selection-background-color: white;
        """)
        #self.setFixedHeight(265)

        #self.setStyleSheet("background-color: red;") #culoare
        #self.min = 60  # 1min = 60sec
        #self.comanda = ('shutdown -s -t'+' ') #string de comanda pt concatenare
        #self.t = 0 # o variabila care sa preia valoarea functiei setval()

    def setval(self, s):
        self.label.setText('Se inchide in:'+str(self.spinBox.value())+' min')
        self.t = s*60
        self.ss = s
        #print(s)

    def cancel(self):
        #print('cancel')
        os.system('shutdown -a')

        msg = QMessageBox()
        msg.setText("Shutdown was canceled")
        msg.setWindowTitle("Titlu fereastra")
        msg.setWindowIcon(QIcon('cross-script.png'))
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("background-color: brown; color: white") # la fel ca orice buton
#        msg.setStyleSheet("text-color: rgb(255, 255, 255);") #asta e culoare din jurul inconului INFO
        msg.exec_()


    def inchide(self):
        try:
            self.comanda = ('shutdown -s -t '+ str(self.t))
            os.system(self.comanda)
        except:
            self.setval(1)
            os.system('shutdown -s -t 60')

        alert = QMessageBox()
        alert.setText('You chose to shutdown in '+ str(self.ss) + ' min!')
        alert.setWindowTitle("SENT")
        alert.setWindowIcon(QIcon('tick-circle.png'))
        alert.setIcon(QMessageBox.Information)
        alert.setStyleSheet("background-color: brown; color: white")
        alert.exec_()

        #print('inchide')
        #print(self.comanda)
        #print(self.t)

        #print(self.comanda)
        #print(self.comanda + str(self.t))
        #os.system(self.comanda + str(self.t))  #  sau asa daca declari in ini variabilele respective


app = QApplication(sys.argv)
window = Ui()
window.show()

app.exec_()