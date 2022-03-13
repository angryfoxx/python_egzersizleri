__author__ = "Fox"
'''
#CardNumber

n = int(input().strip())
for _ in range(n):
    i = input().strip()
    if re.search(r"^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$",i) and not re.search(r'(\d)\1{3,}',re.sub("-","",i)):
        print("Valid")
    else:
        print("Invalid")

##########################################################################

import re
dosya = open("adres.txt")
for i in dosya.readlines():
    nesne = re.search("(\w+)\s+:\s(\w+)\s+(\d+)",i)
    if nesne:
        print("{} > {}".format(nesne.group(1), nesne.group(3)))


##########################################################################

#PostalCodes

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'

P = input().strip()

print(bool(re.match(regex_integer_in_range, P)))
print(len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
print(re.findall(regex_alternating_repetitive_digit_pair, P))

##########################################################################

#HexColorCode

n = int(input().strip())
for _ in range(n):
    i = input()
    n = (re.findall(r"(?<=\W)#[A-Fa-f0-9]{6}",i))
    m = (re.findall(r"(?<=\W)#[A-Fa-f0-9]{3}(?=\W)",i))
    if n:
        print("\n".join(n))
    if m:
        print("\n".join(m))

##########################################################################

#HtmlParser1

def StartTag(text):
    for i in text:
        i = i.replace("<","")
        print(f"Start : {i}")
def EndTag(text):
    for i in text:
        i = i.replace("<","").replace("/","")
        print(f"End : {i}")
def Empty(text):
    for i in text:
        i = i.replace(" ","").replace("/","").replace(">","").replace("<","")
        print(f"Empty : {i}")
def Attrs(text):
    for i in "".join(text).strip().split(" "):
        i = i.replace("'","")
        i = i.split("=")
        if len(i) == 2:
            print(f"-> {i[0]} > {i[1]}")
        else:
            if i[0] != "":
                print(f"-> {i[0]} > None")


if __name__ == "__main__":
    n = int(input().strip(  ))
    for _ in range(n):
        txt = input().strip()
        StartTag(re.findall(r"(?!<\w+\s/>)<\w+",txt))
        Attrs(re.findall(r"\s.*?'?\"?",txt))
        Empty(re.findall(r"<\w+\s/>",txt))
        EndTag(re.findall(r"</\w+",txt))

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for attr in attrs:
            print ('->',attr[0],'>',attr[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        for attr in attrs:
            print ('->',attr[0],'>',attr[1])
if __name__ == "__main__":
    n = int(input().strip(  ))
    parser = MyHTMLParser()
    for _ in range(n):
        parser.feed(input().strip())


##########################################################################

import re
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        if re.match(r"^[7-9][0-9]{1,14}$",input().strip()):
            print("YES")
        else:
            print("NO")

##########################################################################

#Detect Floating Point Number

import re
a = "\n"
if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        i = input().strip()
        if re.match(r"^[\+\-\.]?\.?[0-9]{1,}?\.?[0-9]{1,}$",i): # r'^[-+]?[0-9]*\.[0-9]+$'
            a+="True"
            a+="\n"
        else:
            a+="False"
            a+="\n"

print(a)

##########################################################################

#Regex substitution

import re
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = input().rstrip()
        print(re.sub(r"(?<= )(&&|\|\|)(?= )",lambda x: "and" if x.group() == "&&" else "or",n))

##########################################################################

#Validating UID

import re
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = input().strip()
        print("Valid" if all([re.search(i,n) for i in[r"[a-zA-Z0-9]{10}",r"([A-Z].*){2}",r"([0-9].*){3}",r"(?!.*(.).*\1)"]]) else "Invalid")

##########################################################################

#re.findall()
import re
v = "aeiouAEIOU"
c = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
regex =re.findall(r"(?<=[%s])[%s]{2,}(?=[%s])" % (c, v, c),input().strip())
print("\n".join(regex) if len(regex) != 0 else -1)

##########################################################################

#Romen Num

regex_pattern = r"([IVXLCDM].*)\1{3,}"	# Do not delete 'r'.

import re
print(re.match(regex_pattern, input()))

##########################################################################

#Email

import re
for _ in range(int(input().strip())):
    try:
        print(re.search(r"^([a-zA-Z])+(\s<)([a-zA-Z])+(\w|[,.-])+(@)([a-zA-Z]+)(\.)([a-zA-Z]){,3}(>)$",input().strip(),re.I).group())
    except:
        pass

##########################################################################

'''
