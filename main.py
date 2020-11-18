import chat
import sys, time, datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        # Main Window
        self.setGeometry(400, 100, 700, 500)
        self.setWindowTitle('বাংলা ইন্টেলিজেন্ট চ্যাটবট')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(self.size())

        #Main Layout
        mainVBox = QVBoxLayout()
        self.setLayout(mainVBox)

        # Conversation Field
        self.conversation = QTextEdit()
        self.conversation.setFontPointSize(11)
        self.conversation.setReadOnly(True)
        mainVBox.addWidget(self.conversation)

        # input Field & Button
        hbox = QHBoxLayout()
        self.inputText = QLineEdit()
        self.inputText.setPlaceholderText("এখানে লিখুন।")
        self.inputText.setMaxLength(60)
        self.sendBtn = QPushButton('পাঠান')
        self.clearBtn = QPushButton('মুছুন')
        mainVBox.addWidget(self.inputText)
        hbox.addWidget(self.clearBtn)
        hbox.addWidget(self.sendBtn)

        mainVBox.addLayout(hbox)

        # Button Press Handling
        self.sendBtn.clicked.connect(self.btn_clk)
        self.clearBtn.clicked.connect(self.btn_clk)
        self.inputText.returnPressed.connect(self.sendBtn.click)

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'মুছুন':
            self.inputText.clear()
        elif sender.text() == 'পাঠান':
            if self.inputText.text() == '':
                pass
            else:
                text = self.inputText.text()
                self.inputText.clear()
                self.conversation.setAlignment(Qt.AlignRight)
                self.conversation.append(text + '\n')

                reply = chat.chat(text)
                self.conversation.setAlignment(Qt.AlignLeft)
                self.conversation.append(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())