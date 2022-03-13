from PyQt5.QtWidgets import *
import sys
import random

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.liste = []
        self.init_ui()
    def init_ui(self):
        self.text_line = QLineEdit()
        self.text_line.setPlaceholderText("Asıl metin")
        self.chng_txt_line = QLineEdit()
        self.chng_txt_line.setPlaceholderText("Yeni metin")
        self.label = QLabel()
        self.check_lable = QLabel("0")
        self.button = QPushButton("Değiştir")

        h_box = QVBoxLayout()
        h_box.addWidget(self.text_line)
        h_box.addWidget(self.chng_txt_line)
        h_box.addWidget(self.label)
        h_box.addWidget(self.button)
        h_box.addWidget(self.check_lable)
        v_box = QHBoxLayout()
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.text_line.textChanged.connect(self.changed)

        self.button.clicked.connect(self.push)
        with open("text.txt","r",encoding="utf-8") as file:
            print(len(file.readlines()))
            print(file.read())
            file.flush()

    def push(self):
        self.label.setText(self.chng_txt_line.text())

    def changed(self):
        try:
            a = self.text_line.text()[-1]
            if a != "0":
                self.liste.append(self.text_line.text()[-1])
                if a == self.label.text()[len(self.liste) - 1]:
                    self.check_lable.setText("1")
                else:
                    self.check_lable.setText("0")
            else:
                print(self.liste,len(self.liste),len(self.label.text()))
                self.liste = []
        except:
            print("hata xd")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())