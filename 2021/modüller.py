"""
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
suan = datetime.now()
print(suan.strftime("%A %d %B %y"))
suan_saniye = suan.timestamp()
print(suan_saniye)
suan_saniye_reverse = suan.fromtimestamp(1631786264.477288)
print(suan_saniye_reverse)
print(suan.time())
print(suan.timetz())
print(suan.timetuple())
print(suan.ctime())
print(suan.min)
print(suan.isoweekday())
print(suan.isocalendar())
print(suan.utcnow())
print(suan.utcoffset())
print(suan.month)
""" #datetime
import os

"""
import os
os.chdir("C:/Users/Fox/Desktop")
print(os.getcwd())
os.mkdir("DENEME1/DENEME2")
os.makedirs("DENEME2/DENEME3/DENEME4")
os.removedirs("DENEME2/DENEME3/DENEME4")
os.removedirs("DENEME1/DENEME2")
for i,j,t in os.walk("C:/Users/Fox/Desktop"):
    for x in t:
        if x.endswith("nesne_tabanli_programlama1.rst.txt"):
            print(i)
""" #os
"""
import sys
def toplama(x,y):
    return x+y
if len(sys.argv) == 3:
    print(f"{sys.argv[1]} + {sys.argv[2]} =",toplama(int(sys.argv[1]),int(sys.argv[2])))
else:
    sys.stderr.write("BİRDEN FAZLA DEĞER GİRMEYİNİZ...")
print(help(sys))
sys.exit()

a = input("sdfsdf:")
b = input("sdfjsdlf")
""" #sys
"""
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
film_verisi = soup.find_all("td",{"class":"titleColumn"})
for i in film_verisi:
    a = "".join(i.text)
    a = a.replace("\n","")
    a = a.strip()
    print(a)
    print("**********************************")
""" #imdb top 250 film verisi çekme
          #requests & bs4
"""
import requests
import sys
url = "https://www.bloomberght.com/piyasa/intradaydata/dolar/#chartContainer/"
response = requests.get(url)
html_icerik = response.json()
TRY = html_icerik["SeriesData"][-1][-1]
try:
    base_currency = int(input("TRY'ye çevireceğiniz dolar miktarı:"))
    payload = base_currency * TRY
    print(f"{payload} Türk Lirası")
except:
    sys.stderr.write("LÜTFEN DOĞRU DEĞERLER GİRİNİZ")
    sys.stderr.flush()
""" #döviz çevirici
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
email_list = []
with open("text/emails.txt","r",encoding="utf-8") as file:
    for i in file:
        i0 = i.strip()
        if i0.endswith(".com") and i0.find("@"):
            email_list.append(i0)
for i in email_list:
    suan = datetime.now()
    mess = MIMEMultipart()
    mess["From"] = "omusgomus@gmail.com"
    mess["To"] = f"{i}"
    mess["Subject"] = "Yazılımsal işler!!!!"
    yazi = f"""
Bu mesaj python ile {suan.strftime("%d %B %A %Y")} saat {suan.strftime("%H:%M:%S")}'da atıldı.

Bu bir SMTP modülü deneme mailidir ciddiye almayınız!!!

Ömer Faruk Korkmaz as FOX
    """
    mess_govdesi = MIMEText(yazi,"plain")
    mess.attach(mess_govdesi)
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("omusgomus@gmail.com","12491811asd")
        mail.sendmail(mess["From"],mess["To"],mess.as_string())
        print("Mail başarıyla gönderildi !!!!!!")
    except:
        sys.stderr.write("""!!!!!!HATA!!!!!!
        Mail gönderilemedi.""")
        sys.stderr.flush()
''' #oto mail
'''
import sys
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")
con = sqlite3.connect("C:/Users/Fox/PycharmProjects/python_egzersizleri/pythonProject1/sqlite veritabanı/deneme.db")
curs = con.cursor()
curs.execute("SELECT email FROM email_list")
for i in curs.fetchall():
    suan = datetime.now()
    mess = MIMEMultipart()
    mess["From"] = "omusgomus@gmail.com"
    mess["To"] = f"{i[0]}"
    mess["Subject"] = "Python ile e-mail"
    yazi =f"""
    Bu mail {suan.strftime("%d %B %Y %A")} saat {suan.strftime("%H.%M.%S")}'de atılmıştır.
    Mail python'smtp kütüphanesi aracılığı ile atılmıştır.
    Ömer Faruk Korkmaz as FOX
    """
    govde = MIMEText(yazi, "plain")
    mess.attach(govde)
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("omusgomus@gmail.com", "12491811asd")
        mail.sendmail(mess["From"],mess["To"],mess.as_string())
        print("Mail başarıyla gönderildi")
        mail.close()
    except:
        sys.stderr.write("!!!!!!HATA!!!!!!\n\t\tMail gönderilemedi")
        sys.stderr.flush()
''' #oto mail with db
"""
    highChartsOptions.push({
        sec_id: "88",
        sec_slug: 'dolar',
        sec_name: 'USD/TRY',
        sec_datatype: "intraday",
        container_id: "#intradayContainer",
        "credits": {
            enabled: true,
            href: "https:\/\/www.bloomberght.com",
            text: "Bloomberght.com"        },
        rangeSelector: {
            enabled: false
        },
        "xAxis": {
            "type": "datetime"
        }
    });

highChartsOptions.push({
    sec_id: "88",
    sec_slug: 'dolar',
    sec_name: 'USD/TRY',
    sec_datatype: "refdata",
    container_id: "#chartContainer",
    "credits": {
        enabled: true,
        href: "https:\/\/www.bloomberght.com",
        text: "Bloomberght.com"    },
    rangeSelector: {
        selected: 0,
        buttons: [
            {
                type: 'month',
                count: 1,
                text: '1Ay'
            }, {
                type: 'month',
                count: 3,
                text: '3Ay'
            }, {
                type: 'month',
                count: 6,
                text: '6Ay'
            }, {
                type: 'ytd',
                text: 'Yılbaşı'
            }, {
                type: 'year',
                count: 1,
                text: '1Yıl'
            }, {
                type: 'all',
                text: 'Tümü'
            }]
    },
    "xAxis": {
        "type": "datetime"
    }
});
head.ready("layout", function() {
    $.each(highChartsOptions, function (key, option) {
        option.series = [
            {
                type: 'area',
                gapSize: 5,
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                threshold: null,
                "index": 0,
                "name": option.sec_name
            }
        ];
        var _dataTypeUrl;
        if (option.sec_datatype && option.sec_datatype == "intraday") {
            _dataTypeUrl = "intradaydata";
        } else {
            _dataTypeUrl = "refdata";
        }

        var _dataContainerId;
        if (option.container_id) {
            _dataContainerId = option.container_id;
        } else {
            _dataContainerId = "#chartContainer";
        }
        $.getJSON('/piyasa/' + _dataTypeUrl + '/' + option.sec_slug, function (data) {
            option.series[0].data = data.SeriesData;
            $(_dataContainerId + option.sec_id).highcharts("StockChart", option);
        });
    });
});
https:\/\/www.bloomberght.com/piyasa/intradaydata/dolar/#chartContainer/"""
"""import os
with open("text\\txt_dosyalari.txt","a",encoding="utf-8") as file:
    for dosya_yolu,klasor_adi,dosya_ismi in os.walk("C:\\Users\\Fox"):
        for i in dosya_ismi:
            if i.endswith(".txt"):
                file.write(f"{dosya_yolu} =========> {i}\n")
with open("text\\mp4_dosyalari.txt","a",encoding="utf-8") as file:
    for dosya_yolu,klasor_adi,dosya_ismi in os.walk("C:\\Users\\Fox"):
        for i in dosya_ismi:
            if i.endswith(".mp4"):
                file.write(f"{dosya_yolu} =========> {i}\n")
with open("text\\pdf_dosyalari.txt","a",encoding="utf-8") as file:
    for dosya_yolu,klasor_adi,dosya_ismi in os.walk("C:\\Users\\Fox"):
        for i in dosya_ismi:
            if i.endswith(".pdf"):
                file.write(f"{dosya_yolu} =========> {i}\n")""" #dosyaları derleme
