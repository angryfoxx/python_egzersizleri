__author__ = "FOX"

import random
import  sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QLineEdit,QMainWindow
from PyQt5 import QtGui,QtCore

class Tema(QWidget):
    def __init__(self):
        super(Tema, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.block_line = QLineEdit("5")
        self.block_line.setStyleSheet("font-size:15px")

        self.key_line = QLineEdit("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        self.key_line.setStyleSheet("font-size: 15px")

        self.num_line = QLineEdit("0123456789")
        self.num_line.setStyleSheet("font-size: 15px")

        self.punc_line = QLineEdit("!'£^#+$%&/{([)]=}?*_|<>.:;,")
        self.punc_line.setStyleSheet("font-size: 15px")

        self.generate_button = QPushButton("GENERATE")
        self.generate_button.setStyleSheet("color: white; font-size: 100px; background-color: #3CAE40;")

        self.passw = QLineEdit()
        self.passw.setStyleSheet("font-size: 25px")
        self.passw.setPlaceholderText("Your so secret password")

        self.warning = QLabel()
        self.warning.setStyleSheet("color: red; font-size: 20px")

        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addWidget(self.generate_button)
        v_box.addWidget(self.passw)
        v_box.addWidget(self.warning)
        v_box.addStretch()
        v_box.addWidget(self.key_line)
        v_box.addWidget(self.num_line)
        v_box.addWidget(self.punc_line)
        v_box.addStretch(4)

        h_box = QHBoxLayout()
        h_box.addStretch()

        h_box.addLayout(v_box)

        h_box.addStretch()

        self.setLayout(h_box)

        self.generate_button.clicked.connect(self.generator)

    def default(self):
        self.key_line.setText("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        self.num_line.setText("0123456789")
        self.punc_line.setText("!'£^#+$%&/{([)]=}?*_|<>.:;,")
        self.block_line.setText("5")
        self.passw.clear()

    def generator(self):
        try:
            self.password = ""
            password_list = list()
            keyword_list = [self.key_line.text(), self.num_line.text(), self.punc_line.text()]
            random.shuffle(keyword_list)
            for i in keyword_list[0]:
                for j in keyword_list[1]:
                    for z in keyword_list[2]:
                        a = i, j, z
                        password_list.append(a)

            block = random.choices(population=password_list, k=int(self.block_line.text()))
            print(len(password_list))

            for i in block:
                self.password += i[0] + i[1] + i[2] + "-"

            self.warning.setText("Parolanızı kimseyle paylaşmayın  !!!!!!!!!!!!")
            self.passw.setText(self.password.strip("-"))

        except:
            self.warning.setText("Lütfen satırları boş bırakmayınız  !!!!!!!!!!!!")
            self.default()

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.tema = Tema()
        self.setCentralWidget(self.tema)
        self.setGeometry(500, 190, 700, 500)
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QtGui.QIcon("assets/unlock-alt-solid.svg"))
        self.resize(0, 0)
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )


        self.init_ui()

    def init_ui(self):
        self.def_button = QPushButton("Sıfırla", self)
        self.def_button.move(402, 185)
        self.def_button.setStyleSheet("font-size:15px")

        statusbar = self.statusBar()
        statusbar.setSizeGripEnabled(False)
        statusbar.addWidget(QLabel(),1)
        statusbar.addWidget(self.tema.block_line)
        statusbar.addWidget(self.def_button)

        self.def_button.clicked.connect(self.tema.default)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())
