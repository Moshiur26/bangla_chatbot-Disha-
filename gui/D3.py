from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import chat

class Window(QWidget):
    def __init__(self):
        self.checker = False

        QWidget.__init__(self)
        self.resize(600, 600)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)
        self.mainLayout()

    def on_button_Send_clicked(self):
        self.question = self.lineedit.text()
        self.lineedit.clear()


        blueColor = QColor(70,130,180)
        blackColor = QColor(0, 0, 0)

        self.textedit.setTextColor(blueColor)


        self.textedit.setAlignment(Qt.AlignRight)
        self.textedit.append("Me\n"+self.question + '\n')
        #self.textedit.append("Me\n"+self.question + '\n'.decode("utf-8", "replace"))

        self.textedit.setTextColor(blackColor)

        reply = chat.chat(self.question)
        self.textedit.setAlignment(Qt.AlignLeft)
        self.textedit.append("Chatboat\n"+reply)
        #self.textedit.append("Chatboat\n"+reply.decode("utf-8", "replace"))

    def mainLayout(self):
        layout = QVBoxLayout()

        button_Exit = QPushButton("Exit")
        button_Exit.setFont(QFont('Arial', 15))
        button_Exit.clicked.connect(QCoreApplication.instance().quit)

        labelTextTitle = QLabel("Bangla Intelligent ChatBot")
        labelTextTitle.setFont(QFont('Arial', 18))

        self.textedit = QTextEdit()
        self.textedit.setFont(QFont('Arial', 15))
        self.textedit.setReadOnly(True)
        self.textedit.setPlaceholderText("তুমার উত্তর এইখানে থাকবে")

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont('Arial', 15))
        self.lineedit.resize(300, 500)
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
        layout.addWidget(button_Exit)

        QWidget.setLayout(self, layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())
