from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QCursor, QPixmap
import sys
from game.playgameGUI import Ui_MainWindow

class playgameGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(playgameGUI, self).__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.set_exiticon()

    def set_exiticon(self): #set icon "X" so the user can close the window
        exit_nothover = QPixmap("./image/icon/exit.png")
        exit_hover = QPixmap("./image/icon/exit_hover.png")
        self.gui.exit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.gui.exit.setPixmap(exit_nothover)
        self.gui.exit.leaveEvent = lambda e: self.gui.exit.setPixmap(exit_nothover)
        self.gui.exit.enterEvent = lambda e: self.gui.exit.setPixmap(exit_hover)
        self.gui.exit.mousePressEvent = self.quit

    def quit(self, *arg, **kwargs):
        sys.exit()
