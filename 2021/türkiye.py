'''import re
a = """Turkey (Turkish: Türkiye [ˈtyɾcije] officially the Republic of Turkey,[a] is a transcontinental country located mainly on the peninsula of Anatolia in Western Asia, with a smaller portion on East Thrace in Southeast Europe. It shares borders with Greece and Bulgaria to the northwest; the Black Sea to the north; Georgia to the northeast; Armenia, Azerbaijan, and Iran to the east; Iraq to the southeast; Syria and the Mediterranean Sea to the south; and the Aegean Sea to the west. Turks form the vast majority of the nation's population and Kurds are the largest minority.[4] Turkey's capital is Ankara, while its largest city and financial centre is Istanbul (the imperial capital until 1923).

One of the world's earliest permanently settled regions, present-day Turkey was home to important Neolithic sites like Göbekli Tepe, and was inhabited by ancient civilisations such as the Hattians, other Anatolian peoples and Mycenaean Greeks.[11][12][13][14] Following the conquests of Alexander the Great which started the Hellenistic period, most of the ancient regions in modern Turkey were culturally Hellenised, which continued during the Byzantine era.[12][15] The Seljuk Turks began migrating in the 11th century, and the Sultanate of Rum ruled Anatolia until the Mongol invasion in 1243, when it disintegrated into small Turkish principalities.[16] Beginning in the late 13th century, the Ottomans united the principalities and conquered the Balkans, and the Turkification of Anatolia increased during the Ottoman period. After Mehmed II conquered Constantinople (Istanbul) in 1453, Ottoman expansion continued under Selim I. During the reign of Suleiman the Magnificent, the Ottoman Empire became a global power.[11][17][18] From the late 18th century onwards, the empire's power declined with a gradual loss of territories.[19] Mahmud II started a period of modernisation in the early 19th century.[20] The Young Turk Revolution of 1908 restricted the authority of the Sultan and restored the Ottoman Parliament after a 30-year suspension, ushering the empire into a multi-party period.[21][22] The 1913 coup d'état put the country under the control of the Three Pashas, who facilitated the Empire's entry into World War I as part of the Central Powers in 1914. During the war, the Ottoman government committed genocides against its Armenian, Assyrian and Pontic Greek subjects.[b][25] After its defeat in the war, the Ottoman Empire was partitioned.[26]

The Turkish War of Independence against the occupying Allied Powers resulted in the abolition of the Sultanate on 1 November 1922, the signing of the Treaty of Lausanne (which superseded the Treaty of Sèvres) on 24 July 1923 and the proclamation of the Republic on 29 October 1923. With the reforms initiated by the country's first president, Mustafa Kemal Atatürk, Turkey became a secular, unitary and parliamentary republic. Turkey played a prominent role in the Korean War and joined NATO in 1952. The country endured several military coups in the latter half of the 20th century. The economy was liberalised in the 1980s, leading to stronger economic growth and political stability. The parliamentary republic was replaced with a presidential system by referendum in 2017. Since then, the new Turkish governmental system under president Recep Tayyip Erdoğan and his party, the AKP, has often been described as Islamist and authoritarian.[27][28][29][30][31]

Turkey is a regional power and. a newly industrialized country,[32] with a geopolitically strategic location.[33] Its economy, which is classified among the emerging and growth-leading economies, is the twentieth-largest in the world by nominal GDP, and the eleventh-largest by PPP. It is a charter member of the United Nations, an early member of NATO, the IMF, and the World Bank, and a founding member of the OECD, OSCE, BSEC, OIC, and G20. After becoming one of the early members of the Council of Europe in 1950, Turkey became an associate member of the EEC in 1963, joined the EU Customs Union in 1995, and started accession negotiations with the European Union in 2005."""

a = a.replace(",", " ")
a = a.replace(".", " ")

sozluk = set()
a_new = ""

with open("text/turkey.txt","w",encoding="utf-8") as file:
    for i in a.split():
        for j in re.findall("(\[)(\w+)(\])", i):
            x = "".join(j)
            sozluk.add(x)
        if not i in sozluk and i[0] != "[":
            file.write(f"{i}\n")
            file.flush()
''' # regex kullanarak texti düzenleme ve yazdırma

turkce = dict()
with open("text/türkiye.txt","r",encoding="utf-8") as file:
    file = file.read().strip().lower()
    file = file.replace("\n"," ")
    file = file.replace(" ","")
    for i in file:
        if i in turkce:
            turkce[i] += 1
        else:
            turkce[i] = 1

ingilizce = dict()
with open("text/turkey.txt","r",encoding="utf-8") as file:
    file = file.read().strip().lower()
    file = file.replace("\n"," ")
    file = file.replace(" ","")
    for i in file:
        if i in ingilizce:
            ingilizce[i] += 1
        else:
            ingilizce[i] = 1

words = dict()
with open("text/words.txt","r",encoding="utf-8") as file:
    file = file.read().strip().lower().replace(".","")
    file = file.replace("\n", " ")
    file = file.replace(" ", "")
    file = file.replace("–","")
    file = file.replace("’","")
    for i in file:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1

print(ingilizce,"\n\n",turkce,"\n\n",words)

"""
import requests
from bs4 import BeautifulSoup

req = requests.get("https://gonaturalenglish.com/1000-most-common-words-in-the-english-language/")
content = req.content
soup = BeautifulSoup(content,"html.parser")
with open("text/words.txt","w",encoding="utf-8") as file:
    for i in soup.find_all("li"):
        for j in  i.find_all("strong"):
            file.write(f"{j.text.strip()}\n")
            file.flush()""" # requests ile top 1000 kelime çekme ve yazdırma

