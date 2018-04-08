#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import urllib2
import sys

'''urls = ["http://www.tripadvisor.com/Hotel_Review-g188590-d1946024-Reviews-DoubleTree_by_Hilton_Hotel_Amsterdam_Centraal_Station-Amsterdam_North_Holland_Province.html",
"http://www.tripadvisor.com/Hotel_Review-g187497-d1465497-Reviews-W_Barcelona-Barcelona_Catalonia.html",
"http://www.tripadvisor.com/Hotel_Review-g187323-d230550-Reviews-Park_Inn_by_Radisson_Berlin_Alexanderplatz-Berlin.html",
"http://www.tripadvisor.com/Hotel_Review-g186605-d1765611-Reviews-The_Gibson_Hotel-Dublin_County_Dublin.html",
"http://www.tripadvisor.com/Hotel_Review-g187895-d296175-Reviews-Hotel_Davanzati-Florence_Tuscany.html",
"http://www.tripadvisor.com/Hotel_Review-g293974-d654651-Reviews-Sirkeci_Mansion-Istanbul.html",
"http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-Park_Plaza_Westminster_Bridge_London-London_England.html",
"http://www.tripadvisor.com/Hotel_Review-g187514-d190569-Reviews-The_Westin_Palace_Madrid-Madrid.html",
"http://www.tripadvisor.com/Hotel_Review-g187309-d291533-Reviews-Sofitel_Munich_Bayerpost-Munich_Upper_Bavaria_Bavaria.html",
"http://www.tripadvisor.com/Hotel_Review-g187147-d197656-Reviews-Mercure_Paris_Centre_Tour_Eiffel-Paris_Ile_de_France.html",
"http://www.tripadvisor.com/Hotel_Review-g274707-d275254-Reviews-Hilton_Prague_Old_Town-Prague_Bohemia.html",
"http://www.tripadvisor.com/Hotel_Review-g187791-d205044-Reviews-Artemide_Hotel-Rome_Lazio.html",
"http://www.tripadvisor.com/Hotel_Review-g187870-d613798-Reviews-Hilton_Molino_Stucky_Venice_Hotel-Venice_Veneto.html"]
'''

urltest0 = "http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-Park_Plaza_Westminster_Bridge_London-London_England.html"
urltest = "http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-or7590-Park_Plaza_Westminster_Bridge_London-London_England.html"

j = 1
print "Tworzenie pliku z recenzjami"

for i in range(10, 7601, 10):
    url = "http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-or" + str(i) + "-Park_Plaza_Westminster_Bridge_London-London_England.html"
    karta = urllib2.urlopen(url)
    html = karta.read()
    nazwa = "Karta" + str(j) + ".txt"
    plik = open(nazwa, 'w')
    plik.write(html)
    plik.close()
    j += 1
    p = i / 7600
    print p + "%"
    
#ZAKOMENTOWANE ZE WZGLEDU NA BRAK INTERNETU
#karta = urllib2.urlopen("http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-Park_Plaza_Westminster_Bridge_London-London_England.html")
#karta = urllib2.urlopen("http://www.tripadvisor.com/Hotel_Review-g186338-d1657415-Reviews-or10-Park_Plaza_Westminster_Bridge_London-London_England.html")
#html = karta.read()

#TYMCZASOWE ROZWIAZANIE Z POWODU BRAKU INTERNETU (ZAPISANIE RECENZJI Z PIERWSZEJ KARTY W PLIKU)
#plik = open("Karta0.txt", 'w')
#plik.write(html)
#plik.close() 

#TYMCZASOWE ROZWIAZANIE CZYTANIA Z PLIKU
plik = open("Karta0.txt")
try:
    tekst = plik.read().lower()
finally:
    plik.close()

    
#wzorzec = "alt=\"(\d) of 5 stars\">(<p class=\"partial_entry\">\n(.*)|.|\n)*"
#DZIAŁA POPRAWNIE DLA JEDNEJ RECENZJI (WYLUSKUJE OCENE I OPIS)
#wzorzec = "alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>"
#DZIAŁA POPRAWNIEJ NIZ TO NA GORZE
#wzorzec = "(?:alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*)"

#wzorzec = "alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>"
#DZIALA IDEALNIE (to linijke nizej)!
#wzorzec = "alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)[^(?:<span class=\"partnerRvw\">)]\n</p>.*"
#DZIALA LEPIEJ NIZ IDEALNIE (dla 2 recenzji)
#wzorzec = "alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)[^(?:<span class=\"partnerRvw\">)]\n</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>"
#wzorzec = "alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)</p>.*alt=\"(\d) of 5 stars\">.*<p class=\"partial_entry\">\n(.*)\n</p>"
#wzorzec = "alt=\"([1-5])\sof\s5\sstars\">"
#wzorzec = "<div class=\"rating reviewItemInline\">\n<span class=\"rate sprite-rating_s rating_s\"> <img class=\"sprite-rating_s_fill rating_s_fill s(?:10|20|30|40|50)\" width='(?:14|28|42|56|70)' src=\"http://static.tacdn.com/img2/x.gif\" alt=\"(1|2|3|4|5) of 5 stars\">"
wzorzec = "alt=\"(1|2|3|4|5) of 5 stars\">"

#wzorzec2 = "<p class=\"partial_entry\">\n\s*(?:\n<span class=\"partnerRvw\">|\n</p>|(.*))"

wzorzec2 = "<p class=\"partial_entry\">\n(?:\n<span class=\"partnerRvw\">|\n</p>|(.*))"

#wzorzec = re.compile(r'alt=\"(\d) 5 gwiazdkowych\">(<p class=\"partial_entry\">\n(.*)|.|\n)*')
#wzorzec = re.compile(r"alt=\"(\d) 5 gwiazdkowych\">")
#recenzje = re.search(wzorzec, html, re.S)
oceny = re.findall(wzorzec, tekst)
print "ilosc ocen = " + str(len(oceny))
print oceny
recenzje = re.findall(wzorzec2, tekst)
print "ilosc recenzji = " + str(len(recenzje))
print recenzje
oceny = oceny[-len(recenzje):]
print oceny
#recenzje = re.search(wzorzec, tekst, re.S)

#for i in range(1, 4):
#    if i != 4:
#        print recenzje.group(i)

#print recenzje.group()
#print recenzje.group(1) #ocena
#print recenzje.group(2) #tresc recenzji
#print recenzje.group(3)
#print recenzje.group(4)
#print recenzje.group(5)
#print recenzje.group(6)


'''
tekst = ""
plik = open("Karty.txt", 'r+')
print plik
print "*******************"
try:
    for line in plik.readlines():
        print line
        print "*******************"
        tekst += line
except:
    print "Ups!"
        #tekst = plik.read()
plik.close()
recenzje = wzorzec.search(tekst)

#except:
    #print("Ups, cos poszlo nie tak!")
    #sys.exit(0)

#STRUKTURA POJEDYNCZEJ RECENZJI
#<span class="rate sprite-rating_s rating_s"> <img class="sprite-rating_s_fill rating_s_fill s50" width='70' src="http://static.tacdn.com/img2/x.gif" alt="5 5 gwiazdkowych">

#<p class="partial_entry">\n
#recenzja
#</p>


#wzorzec = re.compile(r'alt=\"(\d) 5 gwiazdkowych\">(<p class=\"partial_entry\">\n((?:\w\s)*|ą*|ć*|ę*|ł*|ń*|ó*|ś*|ź*|ż*|Ą*|Ć*|Ę*|Ł*|Ń*|Ó*|Ś*|Ź*|Ż*)|.|\n)*')
#<p class=\"partial_entry\">\n(.+)\n</p>', re.UNICODE) 
#recenzje = wzorzec.search(html)

#Recenzje zaczynaja sie od 2039 linii

print recenzje

if recenzje:
    print recenzje.group(0)
    print recenzje.group(1)
    print "---------------"
#blednie znajduje?    print recenzje.group(2)
    print recenzje.group(3)

print "Tworzenie pliku z wyluskanymi recenzjami"
#try:
plik2 = open("Recenzje.txt", 'w')
plik2.write(recenzje)
plik2.close()
#except:
    #print "Nie wyluskano recenzji?!"
    #sys.exit(0)
    
#plik.close()    
#for i in range(10, 2230, 10):
#    karta = 
'''