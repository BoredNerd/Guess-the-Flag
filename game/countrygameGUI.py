# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_flag.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 680)
        MainWindow.setStyleSheet("background-color : #161219;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 340, 801, 349))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(37, 0, 7, 0)
        self.gridLayout_2.setHorizontalSpacing(46)
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QtCore.QSize(355, 111))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border: 4px  groove #BC006C;\n"
"    border-radius: 20px;\n"
"    color:white;\n"
"    font: 20pt \"Lexend SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : #800048;\n"
"    \n"
"}\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QtCore.QSize(355, 111))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border: 4px  groove #BC006C;\n"
"    border-radius: 20px;\n"
"    color:white;\n"
"    font: 20pt \"Lexend SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : #800048;\n"
"    \n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setMinimumSize(QtCore.QSize(355, 111))
        self.pushButton_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    border: 4px  groove #BC006C;\n"
"    border-radius: 20px;\n"
"    color:white;\n"
"    font: 20pt \"Lexend SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : #800048;\n"
"    \n"
"}\n"
"")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QtCore.QSize(355, 111))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 4px  groove #BC006C;\n"
"    border-radius: 20px;\n"
"    color:white;\n"
"    font: 20pt \"Lexend SemiBold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color : #800048;\n"
"    \n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.flag = QtWidgets.QLabel(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(180, 40, 541, 311))
        self.flag.setStyleSheet("")
        self.flag.setText("")
        self.flag.setObjectName("flag")
        self.exit = QtWidgets.QLabel(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(840, 20, 31, 41))
        self.exit.setStyleSheet("")
        self.exit.setText("")
        self.exit.setPixmap(QtGui.QPixmap(":/source1/exit.png"))
        self.exit.setScaledContents(False)
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
