from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
import sys
import chat
import variables.Variables as v


class Window(QWidget):
    def __init__(self):
        self.checker = False

        QWidget.__init__(self)
        self.resize(700, 600)
        self.setWindowIcon(QtGui.QIcon('./../pic/icon.jpg'))
        self.setWindowTitle("সেবিকা")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
        self.mainLayout()


    def on_button_Send_clicked(self):
        self.question = self.lineedit.text()
        self.lineedit.clear()
        blueColor = QColor(0,0,255)
        blackColor = QColor(0,0,0)
        white = QColor(255,255,255)
        gray=QColor(221,221,221)

        DodgerBlue=QColor(30,144,255)
        DeepSkyBlue=QColor(0,191,255)
        SkyBlue	=QColor(135,206,250)
        LightSkyBlue=QColor(135,206,250)

        self.textedit.setTextColor(blackColor)

        #self.textedit.setFontPointSize(10)
        #self.textedit.setFont(QFont(10))
        self.textedit.setTextBackgroundColor(gray)


        #self.textedit.viewport()

        #p = w.viewport().palette()
        ##p = self.textedit.viewport
        #p.setColor(w.viewport().backgroundRole(), QtGui.QColor(0,0,0))
        #wt.viewport().setPalette(p)

        #self.textedit.setTextBackgroundColor()
        #self.textedit.setLineWrapMode(True)
        #self.textedit.setLineWidth()

        self.textedit.setAlignment(Qt.AlignRight)
        self.textedit.setFont(QFont('Arial', 17))
        #QTextCharFormat format

        #self.textedit.setFontWeight('Bold')
        #self.textedit.append(v.info_map["name"]+"\n"+self.question + '\n')
        self.textedit.append(v.info_map["name"])
        self.textedit.setFont(QFont('Arial', 13))
        self.textedit.append(self.question+'\n')
        #self.textedit.append("Me\n"+self.question + '\n'.decode("utf-8", "replace"))

        self.textedit.setTextColor(blackColor)
        self.textedit.setTextBackgroundColor(white)

        reply = chat.chat(self.question)
        self.textedit.setAlignment(Qt.AlignLeft)
        #self.textedit.append("Chatboat\n"+reply+"\n")
        self.textedit.setFont(QFont('Arial', 17))
        self.textedit.append("Chatboat")
        self.textedit.setFont(QFont('Arial', 13))
        self.textedit.append(reply+'\n')

        #self.textedit.append("Chatboat\n"+reply.decode("utf-8", "replace"))

    def mainLayout(self):
        layout = QVBoxLayout()

        button_Exit = QPushButton("Exit")
        button_Exit.setFont(QFont('Arial', 15))
        button_Exit.clicked.connect(QCoreApplication.instance().quit)

        labelTextTitle = QLabel("সেবিকা")
        labelTextTitle.setAlignment(Qt.AlignHCenter)
        labelTextTitle.setFont(QFont('Arial', 18))


        self.textedit = QTextEdit()
        #self.textedit.setFont(QFont('Arial', 15))
        self.textedit.setReadOnly(True)
        #self.textedit.setMidLineWidth(100)

        #self.textedit.setPlaceholderText("প্রথমে আপনার নাম বলুন।")
        #self.textedit.setFontPointSize(20)
        self.textedit.setFont(QFont('Arial', 17))
        self.textedit.append("Chatboat")


        #self.textedit.insertPlainText("\n")
        self.textedit.setFont(QFont('Arial', 13))
        self.textedit.append("প্রথমে আপনার নাম বলুন।\n")

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont('Arial', 17))
        self.lineedit.resize(600, 500)
        self.lineedit.setPlaceholderText("তুমার প্রশ্ন এইখানে লিখো")
        self.lineedit.setAlignment(Qt.AlignHCenter)

        button_Send = QPushButton("Send")
        button_Send.setFont(QFont('Arial', 15))
        button_Send.clicked.connect(self.on_button_Send_clicked)
        self.lineedit.returnPressed.connect(self.on_button_Send_clicked)

        layout.addWidget(labelTextTitle)
        layout.addWidget(self.textedit)
        layout.addWidget(self.lineedit)
        layout.addWidget(button_Send)
        #layout.addWidget(button_Exit)

        QWidget.setLayout(self, layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())
