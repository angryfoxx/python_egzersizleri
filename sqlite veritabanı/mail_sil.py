import sqlite3

con = sqlite3.connect("maillerd.db")
curs = con.cursor()

def mail_sil(mail):
    sorgu_0 = "SELECT * FROM mailler"
    mail_listesi = []
    curs.execute(sorgu_0)
    for i in curs.fetchall():
        mail_listesi.append(i[0])
    if mail in mail_listesi:
        sorgu = "Delete From mailler where mail = ?"
        curs.execute(sorgu, (mail,))
        con.commit()
        print("mail başarıyla silindi")
    else:
        print("Böyle bir mail adresi bulunamadı.")

def mailleri_göster():
    sorgu = "Select mail From mailler"
    curs.execute(sorgu)

    mailler = curs.fetchall()
    print(mailler, "test")

mailleri_göster()
con.close()