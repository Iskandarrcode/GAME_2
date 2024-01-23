import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random

class dastur(QMainWindow):
    __numbers = set()
    __popitka = 0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(925,500)
        self.setMinimumSize(925,500)
        self.setWindowTitle("Pyatnashki")
        self.setWindowIcon(QIcon("D:\\photo\\photo1.ico"))
        
        self.tab_lb = QLabel("Urinishlar soni: ",self)
        self.tab_lb.setGeometry(500,150,250,50)
        self.tab_lb.setFont(QFont("Calibri",24))
        
        self.tablo = QSpinBox(self)
        self.tablo.setFont(QFont("Consolas",40))
        self.tablo.setGeometry(760,125,150,100)
        self.tablo.setValue(dastur.__popitka)
        self.tablo.setEnabled(False)
        
        self.btn1 = QPushButton("1",self)
        self.btn1.resize(100,100)
        self.btn1.setFont(QFont("Poor Richard",42))
        self.btn1.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn2 = QPushButton("2",self)
        self.btn2.resize(100,100)
        self.btn2.setFont(QFont("Poor Richard",42))
        self.btn2.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn3 = QPushButton("3",self)
        self.btn3.resize(100,100)
        self.btn3.setFont(QFont("Poor Richard",42))
        self.btn3.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn4 = QPushButton("4",self)
        self.btn4.resize(100,100)
        self.btn4.setFont(QFont("Poor Richard",42))
        self.btn4.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn5 = QPushButton("5",self)
        self.btn5.resize(100,100)
        self.btn5.setFont(QFont("Poor Richard",42))
        self.btn5.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn6 = QPushButton("6",self)
        self.btn6.resize(100,100)
        self.btn6.setFont(QFont("Poor Richard",42))
        self.btn6.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn7 = QPushButton("7",self)
        self.btn7.resize(100,100)
        self.btn7.setFont(QFont("Poor Richard",42))
        self.btn7.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn8 = QPushButton("8",self)
        self.btn8.resize(100,100)
        self.btn8.setFont(QFont("Poor Richard",42))
        self.btn8.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn9 = QPushButton("9",self)
        self.btn9.resize(100,100)
        self.btn9.setFont(QFont("Poor Richard",42))
        self.btn9.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn10 = QPushButton("10",self)
        self.btn10.resize(100,100)
        self.btn10.setFont(QFont("Poor Richard",42))
        self.btn10.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn11 = QPushButton("11",self)
        self.btn11.resize(100,100)
        self.btn11.setFont(QFont("Poor Richard",42))
        self.btn11.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn12 = QPushButton("12",self)
        self.btn12.resize(100,100)
        self.btn12.setFont(QFont("Poor Richard",42))
        self.btn12.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn13 = QPushButton("13",self)
        self.btn13.resize(100,100)
        self.btn13.setFont(QFont("Poor Richard",42))
        self.btn13.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn14 = QPushButton("14",self)
        self.btn14.resize(100,100)
        self.btn14.setFont(QFont("Poor Richard",42))
        self.btn14.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn15 = QPushButton("15",self)
        self.btn15.resize(100,100)
        self.btn15.setFont(QFont("Poor Richard",42))
        self.btn15.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        self.btn16 = QPushButton("",self)
        self.btn16.resize(100,100)
        self.btn16.setFont(QFont("Poor Richard",42))
        self.btn16.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);""")
        
        
        self.btn1.move(50,50)
        self.btn2.move(150,50)
        self.btn3.move(250,50)
        self.btn4.move(350,50)
        self.btn5.move(50,150)
        self.btn6.move(150,150)
        self.btn7.move(250,150)
        self.btn8.move(350,150)
        self.btn9.move(50,250)
        self.btn10.move(150,250)
        self.btn11.move(250,250)
        self.btn12.move(350,250)
        self.btn13.move(50,350)
        self.btn14.move(150,350)
        self.btn15.move(250,350)
        self.btn16.move(350,350)
        self.__buttons =[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,
                         self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,
                         self.btn13,self.btn14,self.btn15]
        self.__buttons_click =[self.btn1_c,self.btn2_c,self.btn3_c,self.btn4_c,self.btn5_c,self.btn6_c,
                         self.btn7_c,self.btn8_c,self.btn9_c,self.btn10_c,self.btn11_c,self.btn12_c,
                         self.btn13_c,self.btn14_c,self.btn15_c]
        self.btn16.clicked.connect(self.btn16_c)
        self.btn_text()
        for x,y in zip(self.__buttons,self.__buttons_click):
            x.clicked.connect(y)
            
        self.new_game = QPushButton("New Game",self)
        self.new_game.setFont(QFont("Times New Roman",24))
        self.new_game.setGeometry(600,270,250,50)
        self.new_game.setStyleSheet("""
            border-style: solid;
            border-width: 3px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(72,61,139);
            border-radius: 15px;""")
        self.new_game.clicked.connect(self.new_game_click)
        
        self.end_game = QPushButton("Quit Game",self)
        self.end_game.setFont(QFont("Times New Roman",24))
        self.end_game.setGeometry(600,325,250,50)
        self.end_game.setStyleSheet("""
            border-style: solid;
            border-width: 3px;
            border-color: rgb(0,255,0);
            color: rgb(0,255,0);
            background-color: rgb(72,61,139);
            border-radius: 15px;""")
        self.end_game.clicked.connect(self.quit_game)
        
            
    def new_game_click(self):
        dastur.__popitka = 0
        self.btn_text()
        self.btn16.setText("")
        self.tablo.setValue(dastur.__popitka)
    
    
    def quit_game(self):
        msg = QMessageBox(self)
        msg.setFont(QFont("Poor Richard",18))
        msg.setWindowTitle("Information ")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setWindowIcon(QIcon("D:\\photo\\exit.ico"))
        msg.setText("Siz o'yindan chiqmoqchimisiz? ")
        msg.buttonClicked.connect(self.check_quit)
        msg.show()
    
    def check_quit(self,x):
        if x.text() == "&Yes":
            exit()
        else: 
            print(x.text())
        
    def btn_text(self):
        while len(dastur.__numbers) != 15:
            dastur.__numbers.add(random.randint(1,15))
        dastur.__numbers = list(dastur.__numbers)
        random.shuffle(dastur.__numbers)
        print(dastur.__numbers)
        for x,y in zip(self.__buttons,dastur.__numbers):
            x.setText(str(y))
    
    def btn1_c(self):
        dastur.__popitka += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn1.text())
            self.btn1.setText("")
        elif (self.btn5.text()==""):
            self.btn5.setText(self.btn1.text())
            self.btn1.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn2_c(self):
        dastur.__popitka += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn2.text())
            self.btn2.setText("")
        elif (self.btn3.text() == ""):
            self.btn3.setText(self.btn2.text())
            self.btn2.setText("")
        elif (self.btn6.text()==""):
            self.btn6.setText(self.btn2.text())
            self.btn2.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn3_c(self):
        dastur.__popitka += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn3.text())
            self.btn3.setText("")
        elif (self.btn4.text() == ""):
            self.btn4.setText(self.btn3.text())
            self.btn3.setText("")
        elif (self.btn7.text()==""):
            self.btn7.setText(self.btn3.text())
            self.btn3.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn4_c(self):
        dastur.__popitka += 1
        if self.btn3.text() == "":
            self.btn3.setText(self.btn4.text())
            self.btn4.setText("")
        elif (self.btn8.text()==""):
            self.btn8.setText(self.btn4.text())
            self.btn4.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn5_c(self):
        dastur.__popitka += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn5.text())
            self.btn5.setText("")
        elif (self.btn6.text() == ""):
            self.btn6.setText(self.btn5.text())
            self.btn5.setText("")
        elif (self.btn9.text()==""):
            self.btn9.setText(self.btn5.text())
            self.btn5.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn6_c(self):
        dastur.__popitka += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn6.text())
            self.btn6.setText("")
        elif (self.btn5.text() == ""):
            self.btn5.setText(self.btn6.text())
            self.btn6.setText("")
        elif (self.btn7.text() == ""):
            self.btn7.setText(self.btn6.text())
            self.btn6.setText("")
        elif (self.btn10.text()==""):
            self.btn10.setText(self.btn6.text())
            self.btn6.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn7_c(self):
        dastur.__popitka += 1
        if self.btn3.text() == "":
            self.btn3.setText(self.btn7.text())
            self.btn7.setText("")
        elif (self.btn6.text() == ""):
            self.btn6.setText(self.btn7.text())
            self.btn7.setText("")
        elif (self.btn8.text() == ""):
            self.btn8.setText(self.btn7.text())
            self.btn7.setText("")
        elif (self.btn11.text()==""):
            self.btn11.setText(self.btn7.text())
            self.btn7.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn8_c(self):
        dastur.__popitka += 1
        if self.btn7.text() == "":
            self.btn7.setText(self.btn8.text())
            self.btn8.setText("")
        elif (self.btn4.text() == ""):
            self.btn4.setText(self.btn8.text())
            self.btn8.setText("")
        elif (self.btn12.text()==""):
            self.btn12.setText(self.btn8.text())
            self.btn8.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn9_c(self):
        dastur.__popitka += 1
        if self.btn5.text() == "":
            self.btn5.setText(self.btn9.text())
            self.btn9.setText("")
        elif (self.btn10.text() == ""):
            self.btn10.setText(self.btn9.text())
            self.btn9.setText("")
        elif (self.btn13.text()==""):
            self.btn13.setText(self.btn9.text())
            self.btn9.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn10_c(self):
        dastur.__popitka += 1
        if self.btn6.text() == "":
            self.btn6.setText(self.btn10.text())
            self.btn10.setText("")
        elif (self.btn9.text() == ""):
            self.btn9.setText(self.btn10.text())
            self.btn10.setText("")
        elif (self.btn11.text() == ""):
            self.btn11.setText(self.btn10.text())
            self.btn10.setText("")
        elif (self.btn14.text()==""):
            self.btn14.setText(self.btn10.text())
            self.btn10.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn11_c(self):
        dastur.__popitka += 1
        if self.btn7.text() == "":
            self.btn7.setText(self.btn11.text())
            self.btn11.setText("")
        elif (self.btn10.text() == ""):
            self.btn10.setText(self.btn11.text())
            self.btn11.setText("")
        elif (self.btn12.text() == ""):
            self.btn12.setText(self.btn11.text())
            self.btn11.setText("")
        elif (self.btn15.text()==""):
            self.btn15.setText(self.btn11.text())
            self.btn11.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn12_c(self):
        dastur.__popitka += 1
        if self.btn8.text() == "":
            self.btn8.setText(self.btn12.text())
            self.btn12.setText("")
        elif (self.btn11.text() == ""):
            self.btn11.setText(self.btn12.text())
            self.btn12.setText("")
        elif (self.btn16.text()==""):
            self.btn16.setText(self.btn12.text())
            self.btn12.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn13_c(self):
        dastur.__popitka += 1
        if self.btn9.text() == "":
            self.btn9.setText(self.btn13.text())
            self.btn13.setText("")
        elif (self.btn14.text()==""):
            self.btn14.setText(self.btn13.text())
            self.btn13.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn14_c(self):
        dastur.__popitka += 1
        if self.btn10.text() == "":
            self.btn10.setText(self.btn14.text())
            self.btn14.setText("")
        elif (self.btn13.text() == ""):
            self.btn13.setText(self.btn14.text())
            self.btn14.setText("")
        elif (self.btn15.text()==""):
            self.btn15.setText(self.btn14.text())
            self.btn14.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn15_c(self):
        dastur.__popitka += 1
        if self.btn14.text() == "":
            self.btn14.setText(self.btn15.text())
            self.btn15.setText("")
        elif (self.btn11.text() == ""):
            self.btn11.setText(self.btn15.text())
            self.btn15.setText("")
        elif (self.btn16.text()==""):
            self.btn16.setText(self.btn15.text())
            self.btn15.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def btn16_c(self):
        dastur.__popitka += 1
        if self.btn12.text() == "":
            self.btn12.setText(self.btn16.text())
            self.btn16.setText("")
        elif (self.btn15.text()==""):
            self.btn15.setText(self.btn16.text())
            self.btn16.setText("")
        else:
            dastur.__popitka -= 1
            msg = QMessageBox(self)
            msg.setText("Siljitishni iloji yo'q")
            msg.setFont(QFont("Consolas",14))
            msg.show()
        self.check_game()
        self.tablo.setValue(dastur.__popitka)
    def check_game(self):
        check = False
        for x in range(len(self.__buttons)):
            if self.__buttons[x].text() == str(x + 1):
                continue
            else:
                check = True
                break
        if check == False:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Win")
            msg.setText(f"Siz {dastur.__popitka} ta urinishda yutdingiz")
            msg.show()
                
            

if __name__ == "__main__":
    os.system("cls")
    app = QApplication(sys.argv)
    ilova = dastur()
    ilova.show()
    sys.exit(app.exec_())
    