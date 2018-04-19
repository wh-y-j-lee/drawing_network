# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\ui\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 491, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hWidget = QtWidgets.QWidget(self.centralwidget)
        self.hWidget.setGeometry(QtCore.QRect(140, 20, 491, 561))
        self.hWidget.setObjectName("hWidget")
        self.hLayout = QtWidgets.QHBoxLayout(self.hWidget)
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.setObjectName("hLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.value1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.value1.setObjectName("textEdit")
        self.gridLayout.addWidget(self.value1, 1, 2, 1, 1)
        self.value2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.value2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.value2, 2, 2, 1, 1)
        self.value3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.value3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.value3, 3, 2, 1, 1)
        self.value4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.value4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.value4, 4, 2, 1, 1)
        self.value5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.value5.setObjectName("textEdit_5")
        self.gridLayout.addWidget(self.value5, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.hWidget)
        self.pushButton.setObjectName("Apply")
        self.pushButton2 = QtWidgets.QPushButton(self.hWidget)
        self.pushButton2.setObjectName("Undo")
        self.hLayout.addWidget(self.pushButton,1)
        self.hLayout.addWidget(self.pushButton2, 1)
        # self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        # self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        self.gridLayout.addWidget(self.hWidget, 6, 2,1,1)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.title = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.title.setObjectName("textEdit_6")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_6 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("background-color:rgb(255,255,255)")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # initialize value

        self._structure = []
        self._out = []
        self.l = []

        self.comboBox.currentTextChanged['QString'].connect(self.changeText)
        self.pushButton.clicked.connect(self.textadd)
        self.pushButton2.clicked.connect(self.textdelete)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Batch_Size"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.pushButton2.setText(_translate("MainWindow", "Undo"))
        self.label_3.setText(_translate("MainWindow", "Height"))
        self.label_4.setText(_translate("MainWindow", "Channel"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.comboBox.setItemText(1, _translate("MainWindow", "Input"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Conv"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Maxpool"))
        self.label_6.setText(_translate("MainWindow", "=========Result======="))
        self.title.setText(_translate("MainWindow","Network Size 계산기 입니다."))
    def changeText(self):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox.currentText() == 'Input':
            self.label.setText(_translate("MainWindow","Batch_Size"))
            self.label_2.setText(_translate("MainWindow", "Width"))
            self.label_3.setText(_translate("MainWindow", "Height"))
            self.label_4.setText(_translate("MainWindow", "Channel"))
            self.label_5.setText(_translate("MainWindow", ""))
        elif self.comboBox.currentText() == 'Conv':
            self.label.setText(_translate("MainWindow","Channel"))
            self.label_2.setText(_translate("MainWindow", "Kernel"))
            self.label_3.setText(_translate("MainWindow", "Stride"))
            self.label_4.setText(_translate("MainWindow", "Padding"))
            self.label_5.setText(_translate("MainWindow", ""))
        elif self.comboBox.currentText() == 'Maxpool':
            self.label.setText(_translate("MainWindow","Channel"))
            self.label_2.setText(_translate("MainWindow", "Kernel"))
            self.label_3.setText(_translate("MainWindow", "Stride"))
            self.label_4.setText(_translate("MainWindow", "Padding"))
            self.label_5.setText(_translate("MainWindow", ""))
    def textadd(self):
        if self.comboBox.currentText()=="Input":
        # input_layer = input("Input을 입력해주세요 EX) -1 28 28 1\n:")
        # l = input_layer.split(" ")

            b_size = int(self.value1.text())
            I_w = int(self.value2.text())
            I_h = int(self.value3.text())
            I_c = int(self.value4.text())
            self.l = [b_size, I_w, I_h, I_c]
            if len(self._out)==0:
                self._out.append(self.l)
            else:
                self._out = []
                self._out.append(self.l)
            print(self._out)
            self.label_6.append("Input: b_size: {} width: {} height: {} channel: {}".format(self.l[0],self.l[1],self.l[2],self.l[3]))
        elif self.comboBox.currentText()=="Conv":

            err_count = 0
            Channel = self.value1.text()
            if Channel.isdigit() == False:
                print("Wrong Value of Channel!")
                err_count = err_count+1
            else:
                if int(Channel) <= 0:
                    print("Wrong Value of Channel!")
                    err_count = err_count + 1
                else:
                    Channel = int(Channel)
            Kernel = self.value2.text()
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                err_count = err_count + 1
            else:
                if int(Kernel) <= 0 or int(Kernel) % 2 == 0:
                    print("Wrong Value of Kernel!")
                    err_count = err_count + 1
                else:
                    Kernel = int(Kernel)
            Stride = self.value3.text()
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                err_count = err_count + 1
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    err_count = err_count + 1
                else:
                    Stride = int(Stride)
            Padding = self.value4.text()
            if Padding.isdigit() == False:
                print("Wrong Value of Padding!")
                err_count = err_count + 1
            else:
                if int(Padding) < 0:
                    print("Wrong Value of Padding!")
                    err_count = err_count + 1
                else:
                    Padding = int(Padding)
            if err_count ==0:
                self._structure.append(["Conv", "Channel: {}".format(Channel), "Kernel: {}x{}".format(Kernel, Kernel),
                     "Stride: {}".format(Stride), "Padding: {}".format(Padding)])
                result = [self._out[0][0], (self.l[1] - Kernel + 2 * Padding) / Stride + 1, (self.l[2] - Kernel + 2 * Padding) / Stride + 1,
                      Channel]
                self.temp = self.l
                self.l = result
                self._out.append(result)
                print("here")

                self.label_6.append("{} {} {} {} {}".format(self._structure[-1][0],self._structure[-1][1],self._structure[-1][2],self._structure[-1][3],self._structure[-1][4]))
                self.label_6.append(
                    "result: {} {} {} {}".format(self._out[-1][0], self._out[-1][1], self._out[-1][2],self._out[-1][3]))
        elif self.comboBox.currentText()=="Maxpool":

            err_count = 0
            Channel = self.value1.text()
            if Channel.isdigit() == False:
                print("Wrong Value of Channel!")
                err_count = err_count+1
            else:
                if int(Channel) <= 0:
                    print("Wrong Value of Channel!")
                    err_count = err_count + 1
                else:
                    Channel = int(Channel)
            Kernel = self.value2.text()
            if Kernel.isdigit() == False:
                print("Wrong Value of Kernel!")
                err_count = err_count + 1
            else:
                if int(Kernel) <= 0 :
                    print("Wrong Value of Kernel!")
                    err_count = err_count + 1
                else:
                    Kernel = int(Kernel)
            Stride = self.value3.text()
            if Stride.isdigit() == False:
                print("Wrong Value of Stride!")
                err_count = err_count + 1
            else:
                if int(Stride) <= 0:
                    print("Wrong Value of Stride!")
                    err_count = err_count + 1
                else:
                    Stride = int(Stride)
            Padding = self.value4.text()
            if Padding.isdigit() == False:
                print("Wrong Value of Padding!")
                err_count = err_count + 1
            else:
                if int(Padding) < 0:
                    print("Wrong Value of Padding!")
                    err_count = err_count + 1
                else:
                    Padding = int(Padding)
            if err_count ==0:
                self._structure.append(["Conv", "Channel: {}".format(Channel), "Kernel: {}x{}".format(Kernel, Kernel),
                     "Stride: {}".format(Stride), "Padding: {}".format(Padding)])
                result = [self._out[0][0], (self.l[1] - Kernel + 2 * Padding) / Stride + 1, (self.l[2] - Kernel + 2 * Padding) / Stride + 1,
                      Channel]
                self.temp = self.l
                self.l = result
                self._out.append(result)

                self.label_6.append("{} {} {} {} {}".format(self._structure[-1][0],self._structure[-1][1],self._structure[-1][2],self._structure[-1][3],self._structure[-1][4]))
                self.label_6.append(
                    "result: {} {} {} {}".format(self._out[-1][0], self._out[-1][1], self._out[-1][2],
                                            self._out[-1][3]))
    def textdelete(self):
        self._structure.pop(-1)
        self._out.pop(-1)
        self.l = self._out[-1]
        self.label_6.undo()
        self.label_6.undo()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

