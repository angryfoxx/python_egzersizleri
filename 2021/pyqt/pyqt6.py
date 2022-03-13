__author__ = "FOX"

import time
import sqlite3
from datetime import date,datetime,timedelta
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import  sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QTextEdit,QLabel,QPushButton,QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import QAction,QMainWindow,qApp,QLineEdit,QComboBox,QMessageBox
from PyQt5 import QtCore,QtPrintSupport,QtWidgets,QtGui
"""def pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt6 Dersi")
    pencere.setGeometry(350,130,700,500)
    okay = QtWidgets.QPushButton(pencere)
    cancel = QtWidgets.QPushButton(pencere)
    okay.setText("Tamam")
    cancel.setText("İptal")


    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere.setLayout(v_box)


    pencere.show()

    sys.exit(app.exec())
pencere()"""
"""
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.setWindowTitle("Döviz Programı")
        self.yazi = QtWidgets.QLabel("Bana henüz tıklanmadı!!!!")
        self.buton = QtWidgets.QPushButton("!?-\-Bana tıkla-/-?!")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):
        self.say += 1
        self.yazi.setText(f"Bana {self.say} defa tıklandı!!!")
        if self.say == 1 or self.say == 69 or self.say == 52:
            self.yazi.setText(F"OLUM {self.say} DEDİ LAN SDFHGŞSDHGKLSDFŞLGUASOIEHLKŞSFDGHLDİHFGLKHSİILDILKSHTIWHSDKLFHLHGTHSDLFGHLSIFHWQFIHIOFOIEASGFIASHDFJHQWELRJHSLDFGHLKAJHFKJSAEF")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())"""
"""
class Hosgeldin(QtWidgets.QWidget):
    def __init__(self):
        super(Hosgeldin, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setStyleSheet("background-color:aqua")
        self.mess = QtWidgets.QLabel("HOŞGELDİN")
        self.mess.setStyleSheet("color: Green; font-size: 100px")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch(2)
        v_box.addWidget(self.mess)
        v_box.addStretch(2)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch(1)
        h_box.addLayout(v_box)
        h_box.addStretch(1)

        self.setLayout(h_box)
        self.show()

class Registry(QtWidgets.QWidget):
    def __init__(self):
        super(Registry, self).__init__()
        self.connection()
        self.init_ui()
        self.setGeometry(350, 130, 700, 500)
    def connection(self):
        self.con = sqlite3.connect("forPyQt6.db")
        self.curs = self.con.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS member(Username TEXT, Password TEXT)")
    def init_ui(self):
        self.setStyleSheet("background-color:purple")
        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QtWidgets.QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.mess = QtWidgets.QLabel()
        self.register = QtWidgets.QPushButton("Register")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch(2)

        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.mess)
        v_box.addStretch()
        v_box.addWidget(self.register)
        v_box.addStretch(2)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch(1)
        h_box.addLayout(v_box)
        h_box.addStretch(1)

        self.setLayout(h_box)
        self.setWindowTitle("Kayıt ekranı")

        self.register.clicked.connect(self.click)

        self.show()
    def click(self):
        self.mess.setText("Kullanıcı adı ve parolayı sırasıyla giriniz...")
        userN = self.username.text()
        passw = self.password.text()
        query = "INSERT INTO member VALUES(?,?)"
        if not userN or not passw:
            self.mess.setStyleSheet("color: Red")
            self.mess.setText("Kayıt olurken satırları boş bırakmayınız!!!!")
        else:
            self.curs.execute(query, (userN, passw))
            self.con.commit()
            self.con.close()
            self.mess.setStyleSheet("color: Green")
            self.mess.setText("Kayıt Başarıyla tamamlandı :))")

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super(Pencere, self).__init__()
        self.connection()
        self.init_ui()
        self.setGeometry(350,130,700,500)
    def connection(self):
        self.con = sqlite3.connect("forPyQt6.db")
        self.curs = self.con.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS member(Username TEXT, Password TEXT)")
    def init_ui(self):

        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QtWidgets.QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.mess = QtWidgets.QLabel()
        self.login = QtWidgets.QPushButton("Login")
        self.register = QtWidgets.QPushButton("Register")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch(2)

        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.mess)
        v_box.addStretch()
        v_box.addWidget(self.login)
        v_box.addWidget(self.register)
        v_box.addStretch(2)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch(1)
        h_box.addLayout(v_box)
        h_box.addStretch(1)

        self.setLayout(h_box)
        self.setWindowTitle("Giriş ekranı")

        self.login.clicked.connect(self.click)
        self.register.clicked.connect(self.reg)


        self.show()

    def click(self):
        userN = self.username.text()
        passw = self.password.text()
        query = "SELECT * FROM member WHERE Username = ? and Password = ?"
        self.curs.execute(query,(userN, passw))
        data = self.curs.fetchall()
        if len(data) == 0:
            self.mess.setStyleSheet("color: Red")
            self.mess.setText("Kullanıcı adı veya şifre hatalı!!!!!\nEğer kaydınız yoksa oluşturun...")
        else:
            self.mess.setText("Hoşgeldin")
            self.login = Hosgeldin()
            self.login.show()


    def reg(self):
        self.register = Registry()
        self.register.show()



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())
"""
"""
class NotePad(QWidget):
    def __init__(self):
        super(NotePad, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.say = 0
        self.dosya_ismi = "Adsız"
        self.yazi = QTextEdit()

        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box)

        self.setLayout(v_box)


    def yeni(self):
        self.yazi.clear()
        self.dosya_ismi = "Adsız"
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç",os.getenv("HOME"))[0]
        with open(dosya_ismi,"r",encoding="utf-8") as file:
            liste = dosya_ismi.split("/")
            self.dosya_ismi = liste[-1]
            self.yazi.setText(file.read())

    def farkli_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))[0]
        with open(dosya_ismi, "w", encoding="utf-8") as file:
            file.write(self.yazi.toPlainText())
    def yazdir(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            self.yazi.document().print_(dialog.printer())
    def onizleme(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.yazi.print_)
        dialog.exec()
    def cikis(self):
        qApp.quit()
    def geri_al(self):
        par("Ctrl+Z")
    def kes(self):
        par("Ctrl+X")
    def kopyala(self):
        par("Ctrl+C")
    def yapistir(self):
        par("Ctrl+V")
    def sil(self):
        par("Del")
    def tumunu_sec(self):
        par("Ctrl+A")
    def saat_ve_tarih(self):
        self.yazi.append(datetime.now().strftime("%H.%M %d.%m.%Y"))
    def zoomIn(self):
        self.yazi.zoomIn(1)
        self.say += 1
        print(self.say)
    def zoomOut(self):
        if self.say > -6:
            self.yazi.zoomOut(1)
            self.say -= 1
        print(self.say)
    def zoomDefault(self):
        if self.say < 0:
            self.yazi.zoomIn(abs(self.say))
            self.say = 0
        elif self.say > 0:
            self.yazi.zoomOut(self.say)
            self.say = 0




class Bul(QWidget):
    def __init__(self):
        super(Bul, self).__init__()
        self.pencere_ = NotePad()
        kelimeler = self.file.split()
        self.sade_kelimeler = list()
        for i in kelimeler:
            i = i.strip()
            i = i.strip("\n")
            i = i.strip(".")
            i = i.strip(",")
            self.sade_kelimeler.append(i)

        self.resize(295,85)
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Bul")
        self.aranan = QLabel("Aranan:",self)
        self.girdi = QLineEdit(self)
        self.girdi.setPlaceholderText("Kelime aratın...")
        self.arama = QPushButton("Ara...",self)
        self.arama.setEnabled(False)
        self.iptal = QPushButton("İptal",self)
        self.aranan.move(10,20)
        self.girdi.move(60,17)
        self.arama.move(200,15)
        self.iptal.move(200,45)

        self.girdi.textChanged.connect(self.check_empty)
        self.iptal.clicked.connect(self.cikis_)
        self.arama.clicked.connect(self.finder)

        self.show()

    def check_empty(self,s):
        if s:
            self.arama.setEnabled(True)
        else:
            self.arama.setEnabled(False)
    def finder(self):
        try:
            for i, j in enumerate(self.sade_kelimeler):
                if j == self.girdi.text():
                    print(f"{self.girdi.text()} Kelimesi tam burada {i}")
        except ValueError:
            print("Lütfen metin içinde olan kelimeleri giriniz.")
    def cikis_(self):
        self.close()





class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.pencere = NotePad()
        self.setWindowTitle(f"{self.pencere.dosya_ismi} - NotePad")
        self.setCentralWidget(self.pencere)
        self.menuolustur()
        self.pencere.yazi.textChanged.connect(self.check_isEmpty)


    def menuolustur(self):

        self.menubar = self.menuBar()
        self.dosya = self.menubar.addMenu("Dosya")
        self.duzen = self.menubar.addMenu("Düzen")
        self.bicim = self.menubar.addMenu("Biçim")
        self.gorunum = self.menubar.addMenu("Görünüm")
        self.actionYeni = QAction("Yeni",self)
        self.actionAc = QAction("Aç",self)
        self.actionFarkli_Kaydet = QAction("Farklı Kaydet",self)
        self.actionYazdir = QAction("Yazdır",self)
        self.actionOnIzleme = QAction("Ön İzleme",self)
        self.actioncikis = QAction("Çıkış",self)
        self.actionGeri_AL = QAction("Geri Al",self)
        self.actionKes = QAction("Kes",self)
        self.actionKopyala = QAction("Kopyala",self)
        self.actionYapistir = QAction("Yapıştır",self)
        self.actionSil = QAction("Sil",self)
        self.actionBul = QAction("Bul",self)
        self.actionDegistir = QAction("Değiştir",self)
        self.actionTumunusec = QAction("Tümünü Seç",self)
        self.actionSaat_ve_Tarih = QAction("Saat ve Tarih",self)
        self.actionYaziTipi = QAction("Yazı Tipi",self)
        self.actionYakinlastir = QAction("Yakınlaştır",self)
        self.actionUzaklastir = QAction("Uzaklaştır",self)
        self.actionVarsayilan_yakinlastirma = QAction("Varsayılan Yakınlaştırma",self)
        self.dosya.addAction(self.actionYeni)
        self.dosya.addAction(self.actionAc)
        self.dosya.addAction(self.actionFarkli_Kaydet)
        self.dosya.addSeparator()
        self.dosya.addAction(self.actionYazdir)
        self.dosya.addAction(self.actionOnIzleme)
        self.dosya.addSeparator()
        self.dosya.addAction(self.actioncikis)
        self.duzen.addAction(self.actionGeri_AL)
        self.duzen.addSeparator()
        self.duzen.addAction(self.actionKes)
        self.duzen.addAction(self.actionKopyala)
        self.duzen.addAction(self.actionYapistir)
        self.duzen.addAction(self.actionSil)
        self.duzen.addSeparator()
        self.duzen.addAction(self.actionBul)
        self.duzen.addAction(self.actionDegistir)
        self.duzen.addSeparator()
        self.duzen.addAction(self.actionTumunusec)
        self.duzen.addAction(self.actionSaat_ve_Tarih)
        self.bicim.addAction(self.actionYaziTipi)
        self.gorunum.addAction(self.actionYakinlastir)
        self.gorunum.addAction(self.actionUzaklastir)
        self.gorunum.addAction(self.actionVarsayilan_yakinlastirma)
        self.menubar.addAction(self.dosya.menuAction())
        self.menubar.addAction(self.duzen.menuAction())
        self.menubar.addAction(self.bicim.menuAction())
        self.menubar.addAction(self.gorunum.menuAction())

        self.actionYeni.setShortcut("Ctrl+N")
        self.actionAc.setShortcut("Ctrl+O")
        self.actionYazdir.setShortcut("Ctrl+P")
        self.actionOnIzleme.setShortcut("Ctrl+Shift+P")
        self.actioncikis.setShortcut("Ctrl+Q")
        self.actionGeri_AL.setShortcut("Ctrl+Z")
        self.actionKes.setShortcut("Ctrl+X")
        self.actionKopyala.setShortcut("Ctrl+C")
        self.actionYapistir.setShortcut("Ctrl+V")
        self.actionSil.setShortcut("Del")
        self.actionBul.setShortcut("Ctrl+F")
        self.actionTumunusec.setShortcut("Ctrl+A")
        self.actionSaat_ve_Tarih.setShortcut("F5")
        self.actionDegistir.setShortcut("Ctrl+R")
        self.actionYakinlastir.setShortcut("Ctrl++")
        self.actionUzaklastir.setShortcut("Ctrl+-")
        self.actionVarsayilan_yakinlastirma.setShortcut("Ctrl+0")

        self.dosya.triggered.connect(self.response_dosya)
        self.duzen.triggered.connect(self.response_duzen)
        self.bicim.triggered.connect(self.response_bicim)
        self.gorunum.triggered.connect(self.response_gorunum)
    def response_dosya(self, act):
        act = act.text()
        if act == "Yeni":
            self.pencere.yeni()
        elif act == "Aç":
            self.pencere.dosya_ac()
        elif act == "Farklı Kaydet":
            self.pencere.farkli_kaydet()
        elif act == "Yazdır":
            self.pencere.yazdir()
        elif act == "Ön İzleme":
            self.pencere.onizleme()
        else:
            self.pencere.cikis()

    def response_duzen(self,action):
        act = action.text()
        if act == "Geri Al":
            self.pencere.geri_al()
        elif act == "Kopyala":
            self.pencere.kopyala()
        elif act == "Yapıştır":
            self.pencere.yapistir()
        elif act == "Sil":
            self.pencere.sil()
        elif act == "Bul":
            imageData = QtCore.QByteArray()
            dosya_ismi = QFileDialog.saveFileContent(imageData, "ffcv.txt")
            with open(dosya_ismi, "w", encoding="utf-8") as file:
                file.write(self.pencere.yazi.toPlainText())
            self.bul = Bul()
        elif act == "Değiştir":
            pass
        elif act == "Tümünü Seç":
            self.pencere.tumunu_sec()
        else:
            self.pencere.saat_ve_tarih()
    def response_bicim(self,action):
        pass
    def response_gorunum(self,action):
        act = action.text()
        if act == "Yakınlaştır":
            self.pencere.zoomIn()
        elif act == "Uzaklaştır":
            self.pencere.zoomOut()
        else:
            self.pencere.zoomDefault()
    def check_isEmpty(self):
        enable = not self.pencere.yazi.document().isEmpty()
        self.actionYazdir.setEnabled(enable)
        self.actionOnIzleme.setEnabled(enable)
        self.actionGeri_AL.setEnabled(enable)
        self.actionKes.setEnabled(enable)
        self.actionKopyala.setEnabled(enable)
        self.actionYapistir.setEnabled(enable)
        self.actionSil.setEnabled(enable)
        self.actionBul.setEnabled(enable)
        self.actionDegistir.setEnabled(enable)
        self.actionTumunusec.setEnabled(enable)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = Menu()
    menu.resize(640,480)
    menu.show()
    sys.exit(app.exec())
""" # NotePad

"""
__author__ = "FOX"

import random
import  sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QLineEdit,QMainWindow
from PyQt5 import QtGui

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
        self.setWindowIcon(QtGui.QIcon("unlock-alt-solid.svg"))
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

""" # Password generator - bitti - r = PyQt5

"""
import requests
import sys
from datetime import datetime
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QFileDialog,QMainWindow,qApp,QLineEdit,QComboBox,QPushButton
from PyQt5 import QtCore,QtGui

class Hata(QWidget): # Hatalı bir işlem ya da internet olmadığı gibi durumlarda hata mesajı çıkması için tasarlandı QMessageBox/QErrorBox'ta kullanılabilir ben OOP için birkaç deneme yapmak için kendim tasarladım
    def __init__(self):
        super(Hata, self).__init__()
        self.resize(300,100)
        self.setWindowTitle("HATA")
        self.setWindowIcon(QtGui.QIcon("assets/unsuccesful70x64.svg"))
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()
    def init_ui(self):
        self.q_buton = QPushButton("Tamam", self)
        self.q_buton.move(130, 53)
        self.mess = QLabel("\tHATA!!!!!!\nİnternet bağlantınızı kontrol edin.", self)
        self.mess.setStyleSheet("color: Red; font-size 15px; font-weight: bold;")
        self.mess.move(90, 15)
        self.img = QLabel(self)
        self.img.setPixmap(QtGui.QPixmap("assets/unsuccesful70x64.svg"))
        self.img.resize(70, 64)
        self.img.move(20, 13)

        self.q_buton.clicked.connect(self.close_)
    def close_(self) :
        self.close()

class Doviz(QWidget):
    def __init__(self):
        super(Doviz, self).__init__()
        self.hata = Hata()
        self.now = datetime.now().strftime("%H.%M  |  %d.%m.%Y")
        self.currency = ""
        self.data_for_currency = "intradaydata"
        self.init_ui()

    def html_content(self):
        url = "https://www.bloomberght.com/piyasa/" + self.data_for_currency + "/" + self.currency + "/#chartContainer/"
        self.url = requests.get(url)  #
        self.content = self.url.json()
        self.data = self.content["SeriesData"][-1][-1]

    def init_ui(self):
        self.to_combo_box = QComboBox(self)
        self.combo_box = QComboBox(self)
        self.to_box = QLineEdit(self)
        self.to_box.setValidator(QtGui.QDoubleValidator())
        self.to_box.setEnabled(False)
        self.box = QLineEdit(self)
        self.box.setValidator(QtGui.QDoubleValidator())
        self.box.setEnabled(False)

        self.to_combo_box.resize(105,29)
        self.to_combo_box.move(25, 20)
        self.combo_box.resize(105,29)
        self.combo_box.move(25, 90)
        self.to_box.resize(105,29)
        self.to_box.move(165, 20)
        self.box.resize(105,29)
        self.box.move(165, 90)

        self.foreign_list = ["Seçiniz...", "Türk Lirası", "Dolar", "Euro", "Sterlin", "Yen"]
        self.to_combo_box.addItems(self.foreign_list)
        self.combo_box.addItems(self.foreign_list)

        self.to_combo_box.textActivated.connect(self.click_to)
        self.combo_box.textActivated.connect(self.click)

        self.to_box.textChanged.connect(self.response) # Anlık olarak veri girdiysek çevirme işlemi yapıyor

    def response(self):
        try:
            if self.firstCombo == self.secondCombo:
                self.box.setText(self.to_box.text())
            else:
                self.Exchange(self.firstCombo, self.secondCombo)
        except:
            pass

    def click_to(self, firstCombo):# combo boxlarda veri seçildiyse Qlineeditleri aktif ediyoruz
        self.firstCombo = firstCombo
        if self.firstCombo != "Seçiniz...":
            self.to_box.setEnabled(True)
            self.response() # combo boxları değiştirdiysek çevirme işlemi yapıyor
        else:
            self.to_box.setEnabled(False)

    def click(self, secondCombo):
        self.secondCombo = secondCombo
        if self.secondCombo != "Seçiniz...":
            self.box.setEnabled(True)
            self.response()
        else:
            self.box.setEnabled(False)

    def Exchange(self,first,second):
        self.jsonn = {
            "Türk Lirası": {"Dolar": ["dolar", "intradaydata"], "Euro": ["euro", "intradaydata"],
                              "Sterlin": ["ingiliz-sterlini", "refdata"], "Yen": ["japon-yeni", "refdata"]},

            "Dolar": {"Türk Lirası": ["dolar", "intradaydata"], "Euro": ["usd-eur", "intradaydata"],
                        "Sterlin": ["usd-gbp", "intradaydata"], "Yen": ["usd-jpy", "intradaydata"]},

            "Euro": {"Dolar": ["eur-usd", "intradaydata"], "Türk Lirası": ["euro", "intradaydata"],
                       "Sterlin": ["eur-gbp", "intradaydata"], "Yen": ["eur-jpy", "refdata"]},

            "Sterlin": {"Dolar": ["sterlin-usd", "intradaydata"], "Euro": ["gbp-eur", "refdata"],
                          "Türk Lirası": ["ingiliz-sterlini", "refdata"], "Yen": ["gbp-jpy", "refdata"]},

            "Yen": {"Dolar": ["usd-jpy", "intradaydata"], "Euro": ["eur-jpy", "refdata"],
                      "Sterlin": ["gbp-jpy", "refdata"], "Türk Lirası": ["japon-yeni", "refdata"]},

        }

        if self.to_box.text(): # Qlineedit boş değilse işleme giriyor
            self.currency = f"{self.jsonn[first][second][0]}"
            self.data_for_currency = f"{self.jsonn[first][second][1]}"
            self.html_content()
            data = float(self.to_box.text()) # Float verileri de algılasın diye yapıldı

            if first == "Türk Lirası" or first == "Yen": # Türk lirası ve Yende işlemlerimizi bölerek yaptığımız için diğerlerinden ayrı tuttum
                process = str(self.data).split(".")
                process_ = float("0.0" + process[0] + process[1])  # Bu iki işlem japon yeni içindir sebebi japon yeninin json verisinde başında 0'ı eksik yazıldığı için onu bu işlemle düzelttim

                if first == "Yen" and second == "Türk Lirası":
                    self.box.setText(str(data * process_))

                elif first == "Türk Lirası" and second == "Yen": # TRY-JPY  ya da JPY-TRY işlemlerinde diğerlerinden ayrı işlem yapmamız lazım o yüzden onları ayrı tuttum
                    self.box.setText(str(data / process_))

                else:
                    self.box.setText(str(data / self.data))

            else: # Türk lirası ve Yen dışında işlemlerimizi çarparak yapıyoruz
                self.box.setText(str(data * self.data))

    def veri_kaydet(self): # Anlık olarak çevirdiğimiz kurları kaydediyor
        if self.to_box.isEnabled() and self.box.isEnabled():
            f_name = f"{self.firstCombo} ----------> {self.secondCombo}\n{self.to_box.text()} tane {self.firstCombo}  =  {self.box.text()} tane {self.secondCombo}\nTarih: {self.now}\n\n"
            dosya_ismi = QFileDialog.getSaveFileName(self,"Verinizi Kaydedin...", '', "Text Files (*.txt)")
            with open(dosya_ismi[0],"a",encoding="utf-8") as file:
                file.write(f_name)
                file.flush()

    def kur_kaydet(self): # Bütün kurları kaydediyor
        f_name = ""
        if not self.foreign_list.count("Seçiniz..."):
            for i in self.foreign_list:
                for j in self.foreign_list:
                    if i != j:
                        self.to_box.setEnabled(True)
                        self.to_box.setText("1")
                        self.Exchange(i,j)
                        f_name += f"{i} -- {j} = {self.box.text()}\n"
        else:
            self.foreign_list.remove("Seçiniz...")
            self.kur_kaydet()

        dosya_ismi = QFileDialog.getSaveFileName(self, "Verinizi Kaydedin...", 'DövizKuru', "Text Files (*.txt)")
        with open(dosya_ismi[0], "a", encoding="utf-8") as file:
            file.write(f_name + f"\nTarih: {self.now}\n\n")
            file.flush()

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.doviz = Doviz()
        self.setCentralWidget(self.doviz)
        self.setWindowTitle("Döviz Çevirici")
        self.setGeometry(578, 280, 0, 0)
        self.dat = datetime.now().strftime("%d.%m.%Y")
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()

    def init_ui(self):
        self.date = QLabel(self)
        self.date.setText(self.dat)
        self.date.move(237, 137)

        self.exc_png = QLabel(self)
        self.exc_png.setPixmap(QtGui.QPixmap("assets/vectorpaint0.svg"))
        self.exc_png.resize(48, 48)
        self.exc_png.move(123, 66)

        self.setWindowIcon(QtGui.QIcon("assets/vectorpaint.svg"))

        self.menubar = self.menuBar()
        self.dosya = self.menubar.addMenu("Dosya")
        self.kayit = self.dosya.addAction("Verinizi Kaydedin...")
        self.kur = self.dosya.addAction("Kurları Kaydedin...")

        self.dosya.addSeparator()

        self.cikis = self.dosya.addAction("Çıkış")

        self.kayit.setShortcut("Ctrl+S")
        self.kur.setShortcut("Ctrl+Shift+S")
        self.cikis.setShortcut("Ctrl+Q")

        self.menubar.triggered.connect(self.upBar)

    def upBar(self,action):
        try: # Eğer Qlineeditler boşsa hata çıkarmasın diye try-except kullanıyoruz
            if action.text() == "Verinizi Kaydedin...":
                self.doviz.veri_kaydet()
            elif action.text() == "Kurları Kaydedin...":
                self.doviz.kur_kaydet()
            else:
                qApp.quit()
        except:
            pass

if __name__ == "__main__":
    App = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    menu.resize(300,160)
    sys.exit(App.exec())

 """ # döviz çevirici - bitti - r = PyQt5, requests

"""
__author__ = "FOX"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import  sys
from datetime import datetime
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QTextEdit,QLabel,QPushButton,QFileDialog,QMainWindow,QLineEdit,qApp
from PyQt5 import QtCore,QtGui

class Info(QWidget):# Hata mesajı çıkması için tasarlandı QMessageBox/QErrorBox'ta kullanılabilir

    def __init__(self):
        super(Info, self).__init__()
        self.resize(300,100)

        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("HATA")
        self.setWindowIcon(QtGui.QIcon("unsuccesful70x64.svg"))
        self.i_buton = QPushButton("Bilgi", self)
        self.i_buton.move(180, 53)
        self.q_buton = QPushButton("Tamam", self)
        self.q_buton.move(100, 53)
        self.mess_label = QLabel("           Mail gönderilemedi!\n   Mail adresiniz hatalı veya mailiniz\n         3.Parti yazılımlarına kapalı",self)
        self.mess_label.setStyleSheet("color: Red; font-size 15px; font-weight: bold;")
        self.mess_label.move(86, 10)
        self.img = QLabel(self)
        self.img.setPixmap(QtGui.QPixmap("unsuccesful70x64.svg"))
        self.img.resize(70, 64)
        self.img.move(20, 13)

        self.q_buton.clicked.connect(self.close_)
        self.i_buton.clicked.connect(self.info_)

    def successful(self):
        self.mess_label.setText("     Mailiniz başarıyla gönderildi!!")
        self.mess_label.setStyleSheet("color: Green; font-size 15px; font-weight: bold;")
        self.img.setPixmap(QtGui.QPixmap("succesful70x64.svg"))
        self.setWindowIcon(QtGui.QIcon("succesful70x64.svg"))
        self.setWindowTitle("Başarılı")
    def info_(self):
        os.system("start \"\" https://myaccount.google.com/lesssecureapps")
    def close_(self) :
        self.close()

class LogIn(QWidget):
    def __init__(self):
        super(LogIn, self).__init__()
        self.setWindowIcon(QtGui.QIcon("Circle-icons-mail.svg"))
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.MSWindowsFixedSizeDialogHint
                            )
        self.setWindowTitle("Giriş")
        self.init_ui()

    def init_ui(self):
        self.login_but = QPushButton("Login",self)
        self.login_but.setEnabled(False)
        self.login_but.move(50,90)
        self.login_but.resize(150,33)

        self.email_line = QLineEdit(self)
        self.email_line.setPlaceholderText("Email:")
        self.email_line.move(50, 10)
        self.email_line.resize(150, 33)

        self.password_line = QLineEdit(self)
        self.password_line.setEnabled(False)
        self.password_line.setPlaceholderText("Password:")
        self.password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line.resize(150, 33)
        self.password_line.move(50, 50)

        self.label = QLabel("Kullandığınız mail adresinizi giriniz...",self)
        self.label.setStyleSheet("color: Red")
        self.label.move(52,123)

        self.email_line.textChanged.connect(self.enable)
        self.password_line.textChanged.connect(self.enable)
        self.login_but.clicked.connect(self.connect)

    def enable(self):
        if self.email_line.text():
            self.password_line.setEnabled(True)
            if self.password_line.text():
                self.login_but.setEnabled(True)
            else:
                self.login_but.setEnabled(False)
        else:
            self.password_line.setEnabled(False)

    def connect(self):
        split_mail = self.email_line.text().split("@")
        if len(split_mail) == 2 and self.email_line.text().rfind("."):
            self.menu = Menu(self.email_line.text(),self.password_line.text())
            self.menu.resize(600,400)
            self.menu.show()
            self.close()
        else:
            self.label.setText("Gerçek bir email girin!!!!")

class Functions_of_mail(QWidget):
    def __init__(self, sent_control = 0):
        super(Functions_of_mail, self).__init__()
        self.sent_control = sent_control
        self.info = Info()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText("Yazmaya başlayın...")
        self.text_area.setEnabled(False)

        self.to_Line = QLineEdit(self)
        self.to_Line.setPlaceholderText("Kime:")

        self.subj_line = QLineEdit(self)
        self.subj_line.setPlaceholderText("Konu:")
        self.subj_line.setEnabled(False)

        v_box = QVBoxLayout()
        v_box.addWidget(self.to_Line)
        v_box.addWidget(self.subj_line)
        v_box.addWidget(self.text_area)


        h_box = QHBoxLayout()
        h_box.addLayout(v_box)


        self.setLayout(h_box)

    def mail_process(self,email,passw):

        mess = MIMEMultipart()
        mess["From"] = email
        mess["To"] = self.to_Line.text()
        mess["Subject"] = self.subj_line.text()

        text = self.text_area.toPlainText()
        mess_govde = MIMEText(text,"plain")
        mess.attach(mess_govde)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(email, passw)
            mail.sendmail(mess["From"], mess["To"], mess.as_string())
            self.info.show()
            self.info.successful()
            self.sent_control += 1

        except:
            self.info.show()

class Menu(QMainWindow):
    def __init__(self,email = "",password = ""):
        super(Menu, self).__init__()
        self.setWindowIcon(QtGui.QIcon("Circle-icons-mail.svg"))
        self.email = email
        self.password = password
        self.setWindowTitle("Mail")
        self.setGeometry(440, 150, 0, 0)
        self.zoom_size = 0
        self.function = Functions_of_mail()
        self.setCentralWidget(self.function)
        self.now = datetime.now().strftime("%H.%M  |  %d.%m.%Y")
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        self.folder = menubar.addMenu("Dosya")

        self.new = self.folder.addAction("Yeni")
        self.new.setShortcut("Ctrl+N")

        self.save = self.folder.addAction("Kaydet")
        self.save.setShortcut("Ctrl+Shift+S")

        self.folder.addSeparator()

        self.quit = self.folder.addAction("Çıkış")
        self.quit.setShortcut("Ctrl+Q")

        self.view = menubar.addMenu("Görünüm")

        self.zoom_in = self.view.addAction("Yakınlaştır")
        self.zoom_in.setShortcut("Ctrl++")

        self.zoom_out = self.view.addAction("Uzaklaştır")
        self.zoom_out.setShortcut("Ctrl+-")

        self.view.addSeparator()

        self.zoom_def = self.view.addAction("Varsayılan yakınlaştırmayı geri yükle")
        self.zoom_def.setShortcut("Ctrl+0")


        statusbar = self.statusBar()
        self.sent_button = QPushButton("Gönder")
        self.sent_button.setStyleSheet("font-size: 13px")
        self.sent_button.setEnabled(False)
        statusbar.addWidget(QLabel(),1)
        statusbar.addWidget(self.sent_button)

        self.function.to_Line.textChanged.connect(self.enable)
        self.folder.triggered.connect(self.response_folder)
        self.view.triggered.connect(self.response_view)
        self.sent_button.clicked.connect(self.sent)

    def enable(self):
        if self.function.to_Line.text().rfind(".") and self.function.to_Line.text().find("@"):
            self.function.subj_line.setEnabled(True)
            self.function.text_area.setEnabled(True)
            self.sent_button.setEnabled(True)
        else:
            self.function.subj_line.setEnabled(False)
            self.function.text_area.setEnabled(False)
            self.sent_button.setEnabled(False)

    def sent(self):
        self.function.mail_process(self.email, self.password)

    def response_folder(self, action):
        act = action.text()
        if act == "Yeni":
            self.function.text_area.clear()
            self.function.to_Line.clear()
            self.function.subj_line.clear()
            self.function.text_area.setEnabled(False)
            self.function.subj_line.setEnabled(False)
            self.sent_button.setEnabled(False)
            self.function.sent_control -= 1
        elif act == "Kaydet":
            if self.function.sent_control == 1:
                text =f"Gönderen:\t{self.email}\nAlıcı:\t{self.function.to_Line.text()}\nTarih:\t{self.now}\nKonu:\t{self.function.subj_line.text()}\n\n\n\n{self.function.text_area.toPlainText()}\n\n\n"
                folder_name = QFileDialog.getSaveFileName(self, "Verinizi Kaydedin...", 'mail', "Text Files (*.txt)")
                with open(folder_name[0], "a", encoding="utf-8") as file:
                    file.write(text)
                    file.flush()

        else:
            qApp.quit()

    def response_view(self, action):
        act = action.text()

        if act == "Yakınlaştır":
            self.function.text_area.zoomIn(1)
            self.zoom_size += 1

        elif act == "Uzaklaştır":

            if self.zoom_size > -6:
                self.function.text_area.zoomOut(1)
                self.zoom_size -= 1

        else:
            if self.zoom_size < 0:
                self.function.text_area.zoomIn(abs(self.zoom_size))
                self.zoom_size = 0
            elif self.zoom_size > 0:
                self.function.text_area.zoomOut(self.zoom_size)
                self.zoom_size = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LogIn()
    login.resize(250,150)
    login.show()
    sys.exit(app.exec())
""" # smtp - bitti - r = PyQt5
"""
for _ in range(5):
    print(".", end="")
    time.sleep(0.8)"""


