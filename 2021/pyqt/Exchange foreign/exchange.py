__author__ = "FOX"

import sys

import requests
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtGui import QDoubleValidator, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QDesktopWidget,
                             QFileDialog, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget, qApp)


class Hata(QWidget): # Hatalı bir işlem ya da internet olmadığı gibi durumlarda hata mesajı çıkması için tasarlandı QMessageBox/QErrorBox'ta kullanılabilir ben OOP için birkaç deneme yapmak için kendim tasarladım
    def __init__(self):
        super(Hata, self).__init__()
        self.resize(300,100)
        self.setWindowTitle("HATA")
        self.setWindowIcon(QIcon("assets/unsuccesful70x64.svg"))
        self.setWindowFlags(Qt.Window |
                            Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowStaysOnTopHint |
                            Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()
    def init_ui(self):
        self.q_buton = QPushButton("Tamam", self)
        self.q_buton.move(130, 53)
        self.mess = QLabel("\tHATA!!!!!!\nİnternet bağlantınızı kontrol edin.", self)
        self.mess.setStyleSheet("color: Red; font-size 15px; font-weight: bold;")
        self.mess.move(90, 15)
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap("assets/unsuccesful70x64.svg"))
        self.img.resize(70, 64)
        self.img.move(20, 13)

        self.q_buton.clicked.connect(self.close_)
    def close_(self) :
        self.close()

class Doviz(QWidget):
    def __init__(self):
        super(Doviz, self).__init__()
        self.hata = Hata()
        self.now = QDateTime.currentDateTime().toString("hh.mm.ss dd-MM-yyyy dddd")
        self.firstCurrency = ""
        self.secondCurrency = ""
        self.init_ui()

    def init_ui(self):
        self.to_combo_box = QComboBox(self)
        self.combo_box = QComboBox(self)
        self.to_box = QLineEdit(self)
        self.to_box.setValidator(QDoubleValidator()) # Float ve Int girişi ile kısıtlıyoruz
        self.to_box.setEnabled(False)
        self.box = QLineEdit(self)
        self.box.setValidator(QDoubleValidator())
        self.box.setEnabled(False)

        self.to_combo_box.resize(115,29)
        self.to_combo_box.move(25, 20)
        self.combo_box.resize(115,29)
        self.combo_box.move(25, 90)
        self.to_box.resize(105,29)
        self.to_box.move(170, 20)
        self.box.resize(105,29)
        self.box.move(170, 90)

        self.foreign_json = {"Seçiniz...":None,"Amerikan Doları": "USD","Avustralya Doları": "AUD","Bulgar Levi": "BGN",
                             "Brezilya Reali": "BRL","Kanada Doları": "CAD","İsviçre Frangı": "CHF",
                             "Çin Yuanı": "CNY","Çek Korunası": "CZK","Danimarka Kronu": "DKK",
                             "Euro": "EUR","İngiliz Sterlini": "GBP","Hong Kong Doları": "HKD","Hırvatistan Kunası": "HRK",
                             "Macar Forinti": "HUF","Endonezya Rupisi": "IDR","Yeni İsrail Şekeli": "ILS","Hindistan Rupisi": "INR",
                             "İzlanda Kronu": "ISK","Japon Yeni": "JPY","Güney Kore Wonu": "KRW","Meksika Pesosu": "MXN",
                             "Malezya Ringgiti": "MYR","Norveç Kronu": "NOK","Yeni Zelanda Doları": "NZD","Filipin Pesosu": "PHP",
                             "Polonya Zlotisi": "PLN","Rumen Leyi": "RON","İsveç Kronu": "SEK",
                             "Singapur Doları": "SGD","Tayland Bahtı": "THB","Türk Lirası": "TRY",
                             "Güney Afrika Randı": "ZAR"}

        self.foreign_list = list(self.foreign_json.keys()) # json verisinin 'key'lerini ilerde kullanabilmek için listeye atadım

        self.to_combo_box.addItems(self.foreign_json.keys())
        self.combo_box.addItems(self.foreign_json.keys()) # Combo boxlara json içindeki verimizi aktarıyoruz (Seçiniz...,Amerikan Doları vs.)

        self.to_combo_box.textActivated.connect(self.click_to) # Veri seçtiğimiz zaman miktar girişimiz aktif oluyor
        self.combo_box.textActivated.connect(self.click)

        self.to_box.textChanged.connect(self.response) # Anlık olarak veri girdiysek çevirme işlemi yapıyor

    def html_content(self): # Döviz kurlarının aktarımı
        url = f"https://api.frankfurter.app/latest?from={self.foreign_json[self.firstCurrency]}"
        self.url = requests.get(url)
        self.content = self.url.json()
        self.data = self.content["rates"][self.foreign_json[self.secondCurrency]]

    def response(self): # Verilerin çevrilmesi için çağrışım yapıyoruz
        try:
            if self.firstCombo == self.secondCombo:
                self.box.setText(self.to_box.text())
            else:
                self.exchange(self.firstCombo, self.secondCombo) # firstCombo seçtiğimiz döviz secondCombo çevireceğimiz döviz
        except:
            pass

    def click_to(self, action):# combo boxlarda veri seçildiyse Qlineeditleri aktif ediyoruz
        self.firstCombo = action
        if self.firstCombo != "Seçiniz...":
            self.to_box.setEnabled(True)
            self.box.setEnabled(True)
            self.response() # combo boxları değiştirdiysek çevirme işlemi yapıyor
        else:
            self.to_box.setEnabled(False)
            self.box.setEnabled(False)

    def click(self, action):
        self.secondCombo = action
        self.response()

    def exchange(self,first,second):
        if self.to_box.text(): # Qlineedit doluysa işleme giriyor
            if not first == self.firstCurrency or not second == self.secondCurrency:
               if not (first == self.firstCurrency):
                  self.firstCurrency = first
                  self.secondCurrency = second
                  self.html_content()
                  self.box.setText(str(self.data * float(self.to_box.text())))
               else: #
                  self.secondCurrency = second
                  self.data_ = self.content["rates"][self.foreign_json[self.secondCurrency]]
                  self.box.setText(str(self.data_ * float(self.to_box.text())))
            else: # Dövizler aynı kalır ama girdiğimiz miktar değişirse internetten kuru çekmeden hafızadaki kur ile işlem yapıyor
                self.box.setText(str(self.data * float(self.to_box.text())))  # Girdiğimiz miktarı kurla çarpıp yazdırıyoruz

    def save_data(self): # Anlık olarak çevirdiğimiz kurları kaydediyor
        if self.to_box.isEnabled() and self.box.isEnabled():
            currency_ = f"{self.firstCombo} ----------> {self.secondCombo}\n{self.to_box.text()} tane {self.firstCombo}  =  {self.box.text()} tane {self.secondCombo}\nTarih: {self.now}\n\n"
            folder_name = QFileDialog.getSaveFileName(self,"Verinizi Kaydedin...", '', "Text Files (*.txt)")
            with open(folder_name[0],"a",encoding="utf-8") as file:
                file.write(currency_)
                file.flush()

    def save_currency(self): # Bütün kurları kaydediyor
        currency_ = ""
        if not self.foreign_list.count("Seçiniz..."):
            for i in self.foreign_list:
                for j in self.foreign_list:
                    if i != j: # Kendileri hariç bütün kurları birbiriyle eşleştirip anlık olarak kur çevirisini hesaplıyoruz
                        self.to_box.setEnabled(True)
                        self.to_box.setText("1")
                        self.to_combo_box.setCurrentText(i)
                        self.combo_box.setCurrentText(j)
                        self.exchange(i,j)
                        currency_ += ("{:<20} {:<5} {:<20} = {}\n".format(i,"--",j,self.box.text()))

            currency_ += f"\nTarih: {self.now}\n\n"
            folder_name = QFileDialog.getSaveFileName(self, "Verinizi Kaydedin...", 'DövizKuru', "Text Files (*.txt)")
            with open(folder_name[0], "a", encoding="utf-8") as file:
                file.write(currency_)
                file.flush()

        else:
            self.foreign_list.remove("Seçiniz...")
            self.save_currency()

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.doviz = Doviz()
        self.setCentralWidget(self.doviz)
        self.setWindowTitle("Döviz Çevirici")
        qtRectangle = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(cp)
        self.move(qtRectangle.topLeft())
        self.setWindowFlags(Qt.Window |
                            Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowMinimizeButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint
                            )
        self.init_ui()

    def init_ui(self):
        self.date = QLabel(self)
        self.date.resize(200, 20)
        self.date.move(140, 140)

        self.exc_png = QLabel(self)
        self.exc_png.setPixmap(QPixmap("assets/vectorpaint0.svg"))
        self.exc_png.resize(48, 48)
        self.exc_png.move(130, 67)

        self.setWindowIcon(QIcon("assets/vectorpaint.svg"))

        self.menubar = self.menuBar()
        self.dosya = self.menubar.addMenu("Dosya")
        self.kayit = self.dosya.addAction("Verinizi Kaydedin...")
        self.kur = self.dosya.addAction("Kurları Kaydedin...")

        self.dosya.addSeparator()

        self.cikis = self.dosya.addAction("Çıkış")

        self.kayit.setShortcut("Ctrl+S")
        self.kur.setShortcut("Ctrl+Shift+S")
        self.cikis.setShortcut("Ctrl+Q")

        self.menubar.triggered.connect(self.topBar)

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)

    def showTime(self):
        self.date.setText(QDateTime.currentDateTime().toString("hh.mm.ss dd-MM-yyyy dddd"))

    def topBar(self, action):
        try: # Eğer Qlineeditler boşsa hata çıkarmasın diye try-except kullanıyoruz
            if action.text() == "Verinizi Kaydedin...":
                self.doviz.save_data()
            elif action.text() == "Kurları Kaydedin...":
                self.doviz.save_currency()
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

