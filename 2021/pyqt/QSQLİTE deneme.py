import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QGroupBox,QHBoxLayout,QVBoxLayout,QLabel,QWidget

class Deneme(QWidget):
    def __init__(self):
        super(Deneme, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.group_box = QGroupBox("Deneme")
        self.group_box.setGeometry(0, 0, 591, 161)

        h_box = QHBoxLayout()
        h_box.addWidget(self.group_box)
        h_box.addWidget(QLabel("adasd",self))
        v = QVBoxLayout()
        v.addLayout(h_box)
        self.setLayout(v)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deneme = Deneme()
    deneme.show()
    app.exec()