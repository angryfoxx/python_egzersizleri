__author__ = "FOX"

import os
import sys

from plyer import notification
from PyQt5.QtCore import QDateTime, Qt, QTimer, QUrl
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QFrame, QLabel,
                             QMainWindow, QMessageBox, QProgressBar,
                             QPushButton, QWidget)


class Design(QWidget):
    def __init__(self):
        super(Design, self).__init__()
        self.init_ui()

    def init_ui(self):
        self._font = QFont()
        self._font.setFamily("Arial Rounded MT Bold")

        self.up_btn_style = ("border: none;"
                             "border-radius: 4px;"
                             "font-size: 16px;"
                             "color: white;"
                             "background-color:none;")

        self.bottom_btn_style = ("QPushButton{"
                                 "background-color:#ffffff;"
                                 "color:#d75550;"
                                 "font-size:22px;"
                                 "border-radius:4px;"
                                 "border-bottom:2px solid #BFBFBF;"
                                 "border-right:2px solid #BFBFBF;}"

                                 "QPushButton:hover{"
                                 "border:none;"
                                 "border-top:2px solid #BFBFBF;"
                                 "border-left:2px solid #BFBFBF;}")

        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color:#F57428;")
        self.frame.setGeometry(0, 0, 781, 561)

        self.progress_bar = QProgressBar(self.frame)
        self.progress_bar.setMaximum(4500)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("QProgressBar {"
                                        "border-radius: 7px;"
                                        "background: black;}"

                                        "QProgressBar::chunk {"
                                        "background-color:white; }")

        self.progress_bar.setGeometry(70, 50, 631, 1)

        self.name_label = QLabel("Pomo-Fox", self.frame)
        self.name_label.setFont(self._font)
        self.name_label.setStyleSheet("font-size:22px;color:white;background-color:none;")
        self.name_label.setGeometry(80, 10, 191, 31)

        self.nof_label = QLabel("Pomodoro #", self.frame)
        self.nof_label.setFont(self._font)
        self.nof_label.setStyleSheet("font-size:22px;font-weight:bold;background-color:none;")
        self.nof_label.setGeometry(310, 440, 191, 20)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color:rgba(255, 255, 255, 0.1);\n"
                                   "width: 100px;")
        self.frame_2.setGeometry(100, 90, 581, 341)

        self.timer_label = QLabel("25:00", self.frame_2)
        self.timer_label.setStyleSheet("font-size: 150px;color:white;background-color:none;")
        self.timer_label.setGeometry(100, 90, 391, 139)

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.setWindowFlags(Qt.Window |
                            Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowMinimizeButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint
                            )

        self.design = Design()
        self.setWindowIcon(QIcon("assets/533-tomato.ico"))
        self.setWindowTitle("POMODORO")
        self.setCentralWidget(self.design)

        self.info = "Pomodoro Zamanı !"
        self.number_of_pomo = 0
        self.time = 0
        self.event = 0
        self.bar_value = 0
        self.updt_up_btn_style = ("border: none;"
                                  "border-radius: 4px;"
                                  "font-size: 16px;"
                                  "color: white;"
                                  "background: none rgba(0, 0, 0, 0.15);"
                                  "font-weight: bold;")
                             
        self.init_ui()

    def init_ui(self):
        self.btn_pomo = QPushButton("Pomodoro", self.design.frame_2)
        self.btn_pomo.setGeometry(70, 30, 141, 31)
        self.btn_pomo.setStyleSheet(self.design.up_btn_style)

        self.btn_short_br = QPushButton("Kısa Mola", self.design.frame_2)
        self.btn_short_br.setGeometry(220, 30, 141, 31)
        self.btn_short_br.setStyleSheet(self.design.up_btn_style)

        self.btn_long_br = QPushButton("Uzun Mola", self.design.frame_2)
        self.btn_long_br.setGeometry(370, 30, 141, 31)
        self.btn_long_br.setStyleSheet(self.design.up_btn_style)

        self.btn_start = QPushButton("BAŞLAT", self.design.frame_2)
        self.btn_start.setStyleSheet(self.design.bottom_btn_style)
        self.btn_start.setFont(self.design._font)
        self.btn_start.setGeometry(100, 260, 176, 55)

        self.btn_skip = QPushButton("GEÇ", self.design.frame_2)
        self.btn_skip.setStyleSheet(self.design.bottom_btn_style)
        self.btn_skip.setFont(self.design._font)
        self.btn_skip.setGeometry(310, 260, 176, 55)

        self.btn_group = QButtonGroup()

        self.btn_group.addButton(self.btn_start)
        self.btn_group.addButton(self.btn_skip)
        self.btn_group.addButton(self.btn_pomo)
        self.btn_group.addButton(self.btn_short_br)
        self.btn_group.addButton(self.btn_long_br)

        self.btn_group.buttonClicked.connect(self.click)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        self.player = QMediaPlayer()

    def click(self, button):
        text = button.text()
        if text == "Pomodoro":
            self.pomodoro()

        if text == "Kısa Mola":
            self.short_br()

        if text == "Uzun Mola":
            self.long_br()

        if text == "BAŞLAT" or text == "DURDUR":
            if text == "BAŞLAT":
                self._startTimer()
            else:
                self.endTimer()

        if text == "GEÇ":
            self.endTimer()
            self.msg_Box()
            if self.i == "OK":
                self.time = 0
                self._startTimer()
            else:
                self._startTimer()
                self.player.stop()

    def alarm(self):
        file_path = os.path.join(os.getcwd(), "assets/alarm.mp3")
        url = QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.player.setVolume(10)

    def desk_noti(self):
        notification.notify(
            title = "Pomo-Fox",
            message = f"{self.info}",
            app_icon = "assets/533-tomato.ico"
        )

    def msg_Box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QIcon("assets/533-tomato.ico"))

        msg.setWindowTitle("Emin Misin ? ")
        msg.setText("Daha süren bitmedi !!! ")
        msg.setInformativeText("Süren bitmeden geçmek istediğine emin misin ? ")

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        msg.buttonClicked.connect(self.msgbtn)

        msg.exec_()

    def msgbtn(self,i):
        self.i = i.text()

    def for_break(self):
        self.alarm()
        if self.event == 0:
            self.pomodoro()
        elif self.event == 1 and self.number_of_pomo % 4 == 0:
            self.long_br()
        else:
            self.short_br()

    def pomodoro(self):
        self.endTimer()
        self.setWindowTitle("POMODORO")
        self.info = "Pomodoro Zamanı !"
        self.desk_noti()
        self.design.frame.setStyleSheet("background-color:#F57428;")
        self.time = 1500
        self.event = 1
        self._for_bar()
        self.btn_pomo.setStyleSheet(self.updt_up_btn_style)
        self.btn_long_br.setStyleSheet(self.design.up_btn_style)
        self.btn_short_br.setStyleSheet(self.design.up_btn_style)
        self.design.timer_label.setText("25:00")

    def short_br(self):
        self.endTimer()
        self.setWindowTitle("KISA MOLA !")
        self.info = "Sadece kısa bir mola :)"
        self.desk_noti()
        self.design.frame.setStyleSheet("background-color:#898FE8")
        self.time = 300
        self.event = 0
        self._for_bar()
        self.btn_pomo.setStyleSheet(self.design.up_btn_style)
        self.btn_long_br.setStyleSheet(self.design.up_btn_style)
        self.btn_short_br.setStyleSheet(self.updt_up_btn_style)
        self.design.timer_label.setText("05:00")

    def long_br(self):
        self.endTimer()
        self.setWindowTitle("UZUN MOLA !")
        self.info = "Gerçekten dinlenmenin vakti gelmiş !!!"
        self.desk_noti()
        self.design.frame.setStyleSheet("background-color:#A1D1BB;")
        self.time = 900
        self.event = 0
        self._for_bar()
        self.btn_pomo.setStyleSheet(self.design.up_btn_style)
        self.btn_long_br.setStyleSheet(self.updt_up_btn_style)
        self.btn_short_br.setStyleSheet(self.design.up_btn_style)
        self.design.timer_label.setText("15:00")
                             
    def _for_bar(self):
        self.design.progress_bar.setValue(0)
        self.amount_of_increase = 4500 / self.time
        self.bar_value = 0

    def for_bar(self):
        self.bar_value += int(self.amount_of_increase)
        self.design.progress_bar.setValue(self.bar_value)

    def showTime(self):
        self.design.nof_label.setText(f"Pomodoro #{self.number_of_pomo}")
        if self.time != 0:
            self.time -= 1
            self.for_bar()
            time_ = QDateTime.fromSecsSinceEpoch(self.time)
            self.time_display = time_.toString('mm:ss')
            self.design.timer_label.setText(self.time_display)

        else:
            self.for_break()
            if self.event == 1:
                self.number_of_pomo += 1

    def _startTimer(self):
        self.btn_start.setText("DURDUR")
        self.timer.start(1000)

    def endTimer(self):
        self.btn_start.setText("BAŞLAT")
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    menu.resize(781,561)
    sys.exit(app.exec())
