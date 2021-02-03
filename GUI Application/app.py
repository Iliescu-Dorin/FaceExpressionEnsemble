from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import utils
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 1000)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xrayImage = QtWidgets.QLabel(self.centralwidget)
        self.xrayImage.setGeometry(QtCore.QRect(20, 30, 200, 251))
        self.xrayImage.setText("")
        self.xrayImage.setObjectName("xrayImage")
        
        self.predictedLabel = QtWidgets.QLabel(self.centralwidget)
        self.predictedLabel.setGeometry(QtCore.QRect(40, 280, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.predictedLabel.setFont(font)
        self.predictedLabel.setObjectName("predictedLabel")

        self.browseImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseImageBtn.setGeometry(QtCore.QRect(250, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.browseImageBtn.setFont(font)
        self.browseImageBtn.setObjectName("browseImageBtn")
        self.browseImageBtn.clicked.connect(self.browseImage)

        self.predictBtn = QtWidgets.QPushButton(self.centralwidget)
        self.predictBtn.setGeometry(QtCore.QRect(250, 80, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.predictBtn.setFont(font)
        self.predictBtn.setObjectName("predictBtn")
        self.predictBtn.clicked.connect(self.prediction)

        
        self.probLabel = QtWidgets.QLabel(self.centralwidget)
        self.probLabel.setGeometry(QtCore.QRect(40, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.probLabel.setFont(font)
        self.probLabel.setObjectName("probLabel")

        self.afraid_Prob = QtWidgets.QLabel(self.centralwidget)
        self.afraid_Prob.setGeometry(QtCore.QRect(40, 360, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.afraid_Prob.setFont(font)
        self.afraid_Prob.setObjectName("afraid_Prob")
        self.afraid_Prob.setWordWrap(True)

        self.angry_Prob = QtWidgets.QLabel(self.centralwidget)
        self.angry_Prob.setGeometry(QtCore.QRect(40, 400, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.angry_Prob.setFont(font)
        self.angry_Prob.setObjectName("angry_Prob")
        self.angry_Prob.setWordWrap(True)

        self.disgusted_Prob = QtWidgets.QLabel(self.centralwidget)
        self.disgusted_Prob.setGeometry(QtCore.QRect(40, 440, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.disgusted_Prob.setFont(font)
        self.disgusted_Prob.setObjectName("disgusted_Prob")
        self.disgusted_Prob.setWordWrap(True)

        self.happy_Prob = QtWidgets.QLabel(self.centralwidget)
        self.happy_Prob.setGeometry(QtCore.QRect(40, 480, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.happy_Prob.setFont(font)
        self.happy_Prob.setObjectName("happy_Prob")
        self.happy_Prob.setWordWrap(True)

        self.neutral_Prob = QtWidgets.QLabel(self.centralwidget)
        self.neutral_Prob.setGeometry(QtCore.QRect(40, 520, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.neutral_Prob.setFont(font)
        self.neutral_Prob.setObjectName("neutral_Prob")
        self.neutral_Prob.setWordWrap(True)

        self.sad_Prob = QtWidgets.QLabel(self.centralwidget)
        self.sad_Prob.setGeometry(QtCore.QRect(40, 560, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sad_Prob.setFont(font)
        self.sad_Prob.setObjectName("sad_Prob")
        self.sad_Prob.setWordWrap(True)

        self.surprised_Prob = QtWidgets.QLabel(self.centralwidget)
        self.surprised_Prob.setGeometry(QtCore.QRect(40, 600, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.surprised_Prob.setFont(font)
        self.surprised_Prob.setObjectName("surprised_Prob")
        self.surprised_Prob.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion Detector"))
        self.predictedLabel.setText(_translate("MainWindow", "PREDICTION:"))
        self.browseImageBtn.setText(_translate("MainWindow", "Browse Image"))
        self.predictBtn.setText(_translate("MainWindow", "Analyse"))
        self.probLabel.setText(_translate("MainWindow", "Probabilities"))
        self.afraid_Prob.setText(_translate("MainWindow", "afraid:"))
        self.angry_Prob.setText(_translate("MainWindow", "angry:"))
        self.disgusted_Prob.setText(_translate("MainWindow", "disgusted:"))
        self.happy_Prob.setText(_translate("MainWindow", "happy:"))
        self.neutral_Prob.setText(_translate("MainWindow", "neutral:"))
        self.sad_Prob.setText(_translate("MainWindow", "sad:"))
        self.surprised_Prob.setText(_translate("MainWindow", "surprised:"))


    def browseImage(self):
        fm = QtWidgets.QFileDialog.getOpenFileName(None,"OpenFile")
        filename = fm[0]
        self.image = cv2.imread(filename)        
        self.xrayImage.setPixmap(QtGui.QPixmap(filename))
        self.xrayImage.setScaledContents(True)
    
    def prediction(self):
        self.image = cv2.resize(self.image, (utils.image_size, utils.image_size))
        print("Analysis....")        
        try:
            label, probabilities = utils.predict(self.image)   #("COVID",[0.98,0.02])
            self.predictedLabel.setText("PREDICTION: "+label)
            print(probabilities)
            self.afraid_Prob.setText("afraid: " + str(probabilities[0]))
            self.angry_Prob.setText("angry: " + str(probabilities[1]))
            self.disgusted_Prob.setText("disgusted: " + str(probabilities[2]))
            self.happy_Prob.setText("happy: " + str(probabilities[3]))
            self.neutral_Prob.setText("neutral: " + str(probabilities[4]))
            self.sad_Prob.setText("sad: " + str(probabilities[5]))
            self.surprised_Prob.setText("surprised: " + str(probabilities[6]))
            print("Analysis done")
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())