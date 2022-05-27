__author__ = "FOX"

import os
import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QPushButton, QTextEdit,
                             QVBoxLayout, QWidget, qApp)


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
        self.setWindowIcon(QtGui.QIcon("assets/unsuccesful70x64.svg"))
        self.i_buton = QPushButton("Bilgi", self)
        self.i_buton.move(180, 53)
        self.q_buton = QPushButton("Tamam", self)
        self.q_buton.move(100, 53)
        self.mess_label = QLabel("           Mail gönderilemedi!\n   Mail adresiniz hatalı veya mailiniz\n         3.Parti yazılımlarına kapalı",self)
        self.mess_label.setStyleSheet("color: Red; font-size 15px; font-weight: bold;")
        self.mess_label.move(86, 10)
        self.img = QLabel(self)
        self.img.setPixmap(QtGui.QPixmap("assets/unsuccesful70x64.svg"))
        self.img.resize(70, 64)
        self.img.move(20, 13)

        self.q_buton.clicked.connect(self.close_)
        self.i_buton.clicked.connect(self.info_)

    def successful(self):
        self.mess_label.setText("     Mailiniz başarıyla gönderildi!!")
        self.mess_label.setStyleSheet("color: Green; font-size 15px; font-weight: bold;")
        self.img.setPixmap(QtGui.QPixmap("assets/succesful70x64.svg"))
        self.setWindowIcon(QtGui.QIcon("assets/succesful70x64.svg"))
        self.setWindowTitle("Başarılı")
    def info_(self):
        os.system("start \"\" https://myaccount.google.com/lesssecureapps")
    def close_(self) :
        self.close()

class LogIn(QWidget):
    def __init__(self):
        super(LogIn, self).__init__()
        self.setWindowIcon(QtGui.QIcon("assets/Circle-icons-mail.svg"))
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
        self.setWindowIcon(QtGui.QIcon("assets/Circle-icons-mail.svg"))
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
