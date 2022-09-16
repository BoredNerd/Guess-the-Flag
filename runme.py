import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from game.playgameLogic import playgameGUI
from game.countrygameLogic import countrygameGUI
import ctypes

class Controller:
    def __init__(self):
        myappid = u'BoredNerd.CountryGame'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) #sets the icon in the taskbar
        self.widget = QtWidgets.QStackedWidget()
        self.widget.setWindowTitle("Country Game")
        self.widget.setWindowIcon(QtGui.QIcon("./image/icon/globe.png"))
        self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget.setFixedWidth(889)
        self.widget.setFixedHeight(680)
        self.widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def Show_FirstWindow(self):
        self.ui1 = playgameGUI()
        self.ui1.gui.pushButton.clicked.connect(self.Switch_SecondWindow)
        self.setHeader(self.ui1)
        self.widget.addWidget(self.ui1)
        self.widget.setCurrentIndex(0)
        self.widget.show()

    def Switch_SecondWindow(self):
        self.ui2 = countrygameGUI()
        self.setHeader(self.ui2)
        self.widget.addWidget(self.ui2)
        self.widget.setCurrentIndex(1)

    def mousePress(self, event):
        self.dragPos = self.widget.pos()
        self.mouse_original_pos = self.widget.mapToGlobal(event.pos())

    def moveWindow(self, event):#  mousePress and moveWindow allow the user to move the Frameless Window
        if event.buttons() == Qt.LeftButton:
            MainWindow_last_pos = self.dragPos + self.widget.mapToGlobal(event.pos()) - self.mouse_original_pos
            self.widget.move(MainWindow_last_pos)
            event.accept()

    def setHeader(self, window): #add an invisible header in the Qmainwindow which will be used by the user in order to move the window
        self.header = QtWidgets.QFrame(window.gui.centralwidget)
        self.header.setGeometry(QtCore.QRect(-10, 0, 901, 31))
        self.header.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.header.lower()
        self.header.mouseMoveEvent = self.moveWindow
        self.header.mousePressEvent = self.mousePress

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    app.exec_()
