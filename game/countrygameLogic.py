from PyQt5 import QtCore, QtWidgets, QtMultimedia
from PyQt5.QtGui import QCursor, QPixmap
import os
import random
import sys
from countrygameGUI import Ui_MainWindow

class countrygameGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(countrygameGUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.set_exiticon()
        self.randomflag()

    def set_exiticon(self): #set icon "X" so the user can close the window
        exit_nothover = QPixmap("./image/icon/exit.png")
        exit_hover = QPixmap("./image/icon/exit_hover.png")
        self.gui.exit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gui.exit.setPixmap(exit_nothover)
        self.gui.exit.leaveEvent = lambda e: self.gui.exit.setPixmap(exit_nothover)
        self.gui.exit.enterEvent = lambda e: self.gui.exit.setPixmap(exit_hover)
        self.gui.exit.mousePressEvent = self.quit #if pressed, it ends the program

    def quit(self, *arg, **kwargs):
        sys.exit()

    def randomflag(self):  # set the flag on the label
        self.indexflag = random.choice(range(len(os.listdir("./image/flags/"))))   # choose a flag from the  folder flagcode
        self.nameflag_correct = os.listdir('./image/flags/')[self.indexflag].replace(".svg", "").replace("1","\n") if "1" in os.listdir('./image/flags/')[self.indexflag] \
                                else os.listdir('./image/flags/')[self.indexflag].replace(".svg", "")
        self.gui.flag.setStyleSheet( f"image : url('image/flags/{os.listdir('./image/flags/')[self.indexflag]}')")  # set the chosen flag on the label
        self.checkFlag()

    def checkFlag(self):
        self.randomnumber = random.randint(1,4)  # the name of the country of the flag will be stored inside a random button, if randomnumber = 1 then it will be stored in the first button, if 2 in the second button and so on..
        list_flag = self.generateotherflag()  # generate other country name and return a list which contains 3 different index
        if self.randomnumber == 1:
            self.gui.pushButton_1.setText(self.nameflag_correct) # set name of the right country
            self.gui.pushButton_1.clicked.connect(lambda:self.disconnectbutton("1", False) if (self.randomnumber == 1) else None)

            self.gui.pushButton_2.setText(os.listdir('./image/flags/')[list_flag[0]].replace(".svg", "").replace("1","\n"))  # set name of the wrong country
            self.gui.pushButton_2.clicked.connect(lambda: self.disconnectbutton("2", True) if (self.randomnumber == 1) else None)

            self.gui.pushButton_3.setText(os.listdir('./image/flags/')[list_flag[1]].replace(".svg", "").replace("1","\n"))  # set name of the wrong country
            self.gui.pushButton_3.clicked.connect(lambda: self.disconnectbutton("3", True) if (self.randomnumber == 1) else None)

            self.gui.pushButton_4.setText(os.listdir('./image/flags/')[list_flag[2]].replace(".svg", "").replace("1","\n"))  # set name of the wrong country
            self.gui.pushButton_4.clicked.connect(lambda: self.disconnectbutton("4", True) if (self.randomnumber == 1) else None)

        elif self.randomnumber == 2:
            self.gui.pushButton_1.setText(os.listdir('./image/flags/')[list_flag[0]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_1.clicked.connect(lambda: self.disconnectbutton("1", True) if (self.randomnumber == 2) else None )

            self.gui.pushButton_2.setText(self.nameflag_correct)
            self.gui.pushButton_2.clicked.connect(lambda:  self.disconnectbutton("2", False) if (self.randomnumber == 2) else None )

            self.gui.pushButton_3.setText(os.listdir('./image/flags/')[list_flag[1]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_3.clicked.connect(lambda: self.disconnectbutton("3", True) if (self.randomnumber == 2) else None )

            self.gui.pushButton_4.setText(os.listdir('./image/flags/')[list_flag[2]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_4.clicked.connect(lambda: self.disconnectbutton("4", True) if (self.randomnumber == 2) else None )
        elif self.randomnumber == 3:
            self.gui.pushButton_1.setText(os.listdir('./image/flags/')[list_flag[0]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_1.clicked.connect(lambda: self.disconnectbutton("1", True) if (self.randomnumber == 3) else None )

            self.gui.pushButton_2.setText(os.listdir('./image/flags/')[list_flag[1]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_2.clicked.connect(lambda: self.disconnectbutton("2", True) if (self.randomnumber == 3) else None )

            self.gui.pushButton_3.setText(self.nameflag_correct)
            self.gui.pushButton_3.clicked.connect(lambda: self.disconnectbutton("3", False) if (self.randomnumber == 3) else None)

            self.gui.pushButton_4.setText(os.listdir('./image/flags/')[list_flag[2]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_4.clicked.connect(lambda: self.disconnectbutton("4", True) if (self.randomnumber == 3) else None)

        else:
            self.gui.pushButton_1.setText(os.listdir('./image/flags/')[list_flag[0]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_1.clicked.connect(lambda: self.disconnectbutton("1", True) if (self.randomnumber == 4) else None)

            self.gui.pushButton_2.setText(os.listdir('./image/flags/')[list_flag[1]].replace(".svg", "").replace("1","\n") )
            self.gui.pushButton_2.clicked.connect(lambda: self.disconnectbutton("2", True) if (self.randomnumber == 4) else None)

            self.gui.pushButton_3.setText(os.listdir('./image/flags/')[list_flag[2]].replace(".svg", "").replace("1","\n"))
            self.gui.pushButton_3.clicked.connect(lambda: self.disconnectbutton("3", True) if (self.randomnumber == 4) else None)

            self.gui.pushButton_4.setText(self.nameflag_correct)
            self.gui.pushButton_4.clicked.connect(lambda: self.disconnectbutton("4", False) if (self.randomnumber == 4) else None)

    def disconnectbutton(self, number, audio):
        if audio: #if audio is true, then play a wrong sound effect
            if random.randint(1,2) == 1:
                QtMultimedia.QSound.play("./Sound/Wrong_Answer/bruh_sound.wav")
            else:
                QtMultimedia.QSound.play("./Sound/Wrong_Answer/nope_sound.wav")
        else: #if audio is false, then play a right sound effect
            if random.randint(1, 2) == 1:
                QtMultimedia.QSound.play("./Sound/Right_Answer/noice_sound.wav")
            else:
                QtMultimedia.QSound.play("./Sound/Right_Answer/yeay_sound.wav")
        if number == "1":
            self.gui.pushButton_1.disconnect()
        elif number == "2":
            self.gui.pushButton_2.disconnect()
        elif number == "3":
            self.gui.pushButton_3.disconnect()
        else:
            self.gui.pushButton_4.disconnect()
        self.randomflag() # new flag

    def generateotherflag(self):
        list_flag = []
        for i in range(3):
            x = random.choice(list(range(0, self.indexflag)) + list(range(self.indexflag + 1, 245)))  # choose country name except the country name of the label
            if x not in list_flag:
                list_flag.append(x)
            else:  # if x is already in list, there will be a while true loop in order to generate a number that is not present in the list, therefore the button will not have the same name country
                while True:
                    x = random.choice(list(range(0, self.indexflag)) + list(range(self.indexflag + 1, 245)))
                    if x not in list_flag:
                        list_flag.append(x)
                        break
        return list_flag  # return a list containg 3 different random number and also they are not equal to the country flag label's index
