from PyQt5.QtWidgets import QMainWindow,QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QLineEdit,\
    QApplication,QLabel,QComboBox,QWidget
from PyQt5 import QtCore
import sys

class Tema(QWidget):
    def __init__(self):
        super(Tema, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.btn = QPushButton("İndir")
        self.btn.setStyleSheet("background-color:green;")

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("URL'yi yapıştırınız !!")

        self.path_line = QLineEdit()
        self.path_line.setPlaceholderText("Dosya nereye kaydedilecek ?")

        self.label = QLabel()
        self.label.setStyleSheet("color:green;font-size:20px;")

        self.res_box = QComboBox()
        self.res_list = ["144p","240p","360p","480p","720p","1080p","1440p","2160p","4320p"]
        self.res_box.addItems(self.res_list)

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.line_edit)
        v_box.addWidget(self.path_line)
        v_box.addWidget(self.btn)
        v_box.addWidget(self.label)
        v_box.addWidget(self.res_box)
        v_box.addStretch()

        h_box = QHBoxLayout()
        h_box.addLayout(v_box)

        self.setLayout(h_box)


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.tema = Tema()
        self.setCentralWidget(self.tema)
        self.setGeometry(500, 190, 700, 500)
        self.resize(400, 250)
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
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())