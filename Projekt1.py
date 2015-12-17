#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import linear_model
import math
import numpy as np
import re
import sys

wzorzec = "alt=\"(1|2|3|4|5) of 5 stars\">\n</span>\n<span\sclass=\"rating"
wzorzec2 = "<p class=\"partial_entry\">\n(?:\n<span class=\"partnerRvw\">|\n</p>|([^<].*))"

oceny, opinie, slownik, ocenyTest, opinieTest = [], [], [], [], []

for i in range(300):
    nazwa = "Karta" + str(i) + ".txt"
    plik = open(nazwa, encoding="utf8")
    
    try:
        tekst = plik.read().lower()

        ocenyTemp = re.findall(wzorzec, tekst)
        opinieTemp = re.findall(wzorzec2, tekst)
        
        for k in opinieTemp:
            k = k.replace(',', ' ')
            k = k.replace("&#39", ' ')
            k = k.replace('.', ' ')
            k = k.replace('\'', ' ')
            k = k.replace('"', ' ')
            k = k.replace('!', ' ')
            k = k.replace('?', ' ')
            k = k.replace(':', ' ')
            k = k.replace('+', ' ')
            k = k.replace('(', ' ')
            k = k.replace(')', ' ')
            k = k.replace('@', ' ')
            k = k.replace('#', ' ')
            k = k.replace('$', ' ')
            k = k.replace('%', ' ')
            k = k.replace('^', ' ')
            k = k.replace('&', ' ')
            k = k.replace('*', ' ')
            k = k.replace('=', ' ')
            k = k.replace('/', ' ')
            k = k.replace('-', ' ')
            k = k.replace('<', ' ')
            k = k.replace('>', ' ')
            k = k.replace('|', ' ')
            k = k.replace('`', ' ')
            k = k.replace('~', ' ')
            k = k.replace(';', ' ')
            k = k.replace('\'', ' ')
            k = k.replace('[', ' ')
            k = k.replace(']', ' ')
            k = k.replace('{', ' ')
            k = k.replace('}', ' ')
            k = k.replace('_', ' ')
            tempK = k.split()
            
            for slowo in tempK:
                slownik.append(slowo)
                
            opinie.append(k)
            
        for j in ocenyTemp:
            oceny.append(float(j))
            
            
    finally:
        plik.close()
        
    print ("Czytam recenzje, tworzę słownik oraz wyłuskuję oceny: " + str(round(((float(i) / float(300)) * 100), 1)) + '%')

oceny = np.array(oceny)

for i in range(330, 331):
    nazwa = "Karta" + str(i) + ".txt"
    plik = open(nazwa, encoding="utf8")
    
    try:
        tekst = plik.read().lower()
        
        opinieTemp = re.findall(wzorzec2, tekst)
        ocenyTemp = re.findall(wzorzec, tekst)

        if len(opinieTemp) != len(ocenyTemp):
            print ("Ilosc opinii: " + str(len(opinieTemp)))
            print ("Ilosc ocen: " + str(len(ocenyTemp)))
            print ("W karcie nr " + str(i) + "ilosc ocen i opinii jest rozna!")

        for k in opinieTemp:
            k = k.replace(',', ' ')
            k = k.replace("&#39", ' ')
            k = k.replace('.', ' ')
            k = k.replace('\'', ' ')
            k = k.replace('"', ' ')
            k = k.replace('!', ' ')
            k = k.replace('?', ' ')
            k = k.replace(':', ' ')
            k = k.replace('+', ' ')
            k = k.replace('(', ' ')
            k = k.replace(')', ' ')
            k = k.replace('@', ' ')
            k = k.replace('#', ' ')
            k = k.replace('$', ' ')
            k = k.replace('%', ' ')
            k = k.replace('^', ' ')
            k = k.replace('&', ' ')
            k = k.replace('*', ' ')
            k = k.replace('=', ' ')
            k = k.replace('/', ' ')
            k = k.replace('-', ' ')
            k = k.replace('<', ' ')
            k = k.replace('>', ' ')
            k = k.replace('|', ' ')
            k = k.replace('`', ' ')
            k = k.replace('~', ' ')
            k = k.replace(';', ' ')
            k = k.replace('\'', ' ')
            k = k.replace('[', ' ')
            k = k.replace(']', ' ')
            k = k.replace('{', ' ')
            k = k.replace('}', ' ')
            k = k.replace('_', ' ')
    
            tempK = k.split()
            
            for slowo in tempK:
                slownik.append(slowo)
            
            opinieTest.append(k)
        for j in ocenyTemp:
            ocenyTest.append(float(j))
            
    finally:
        plik.close()
        
    print ("Czytam recenzje testowe, dodaję wyrazy do słownika oraz wyłuskuję oceny testowe: " + str(round((float(i) / float(760)) * 100, 1)))

slownik = set(slownik)

slownik = list(slownik)
                
print ("Ilość opinii: " + str(len(opinie)))

print ("Ilość ocen: " + str(len(oceny)))
    
#ZMIANA NA NP.ARRAY
wektor = np.zeros((len(opinie), len(slownik)))

print ("Jestem już po stworzeniu wektorów i słownika, teraz zajmę się wypełnieniem wektorów wagami")


p = len(slownik)
#obliczanie frekwencji wyrazów w opiniach
for i in range(p):
    for k in range(len(opinie)):
        if slownik[i] in opinie[k]:
            wektor[k,i] = 1.
    print ("Wypełnianie wektorów wagami: " + str(round((float(i) / float(p)) * 100, 1)) + '%')
print ("CZAS NA REGRESJĘ LINIOWĄ!")
print ("\n")

m, n = wektor.shape 
#m - ilość wierszy (= ilość opinii)
#n - ilość kolumn (= ilość słów w słowniku)

clf = linear_model.LinearRegression(fit_intercept = False)
       
print ("Ilość opinii uczących: " + str(len(wektor)))
print ("Ilość ocen uczących: " + str(len(oceny)))

clf.fit(wektor, oceny)
               
wektorTest = np.zeros((len(opinieTest), len(slownik)))
print ("Jestem już po stworzeniu wektorów i słownika, teraz zajmę się wypełnieniem wektorów wagami")
 
pTest = len(slownik)

#obliczanie frekwencji wyrazów w opiniach testowych
for i in range(len(slownik)):
    for k in range(len(opinieTest)):
        if slownik[i] in opinieTest[k]:
            wektorTest[k,i] = 1.
    print ("Efekt procentowy testów: " + str(round(float(i) / float(p) * 100, 1)) + '%')

print ("Ilosc opinii testowych: " + str(len(opinieTest)))
print ("Ilosc ocen testowych: " + str(len(ocenyTest)))

mTest, nTest = wektorTest.shape
    
print ("Wektor testowy: ")
print (wektorTest)
 
print ("Clf coef: ")
print (clf.coef_)

ocenyRegresyjne = [] 

ocena = np.dot(wektorTest, clf.coef_)    
    
for i in range(mTest):
    if ocena[i] > 5.:
        ocena[i] = 5.
    elif ocena[i] < 1.:
        ocena[i] = 1.
    ocenyRegresyjne.append(ocena[i])

    

print ("Oceny regresyjne: ")
print (ocenyRegresyjne)
print ("Oceny testowe: ")
print (ocenyTest)
print ("Wektor Teta: ")
print (clf.coef_)
 
blad = int(0)
print ("Ilość ocen regresyjnych: ")
print (len(ocenyRegresyjne))
print ("Ilość ocen testowych: ")
print (len(ocenyTest))

for j in range(mTest):
    blad += (ocenyRegresyjne[j] - ocenyTest[j])**2
bladSredniokwadratowy = blad / mTest

print ("Błąd średniokwadratowy (dla przypadku regresji) wynosi tyle: " + str(bladSredniokwadratowy))

#Dla przypadku, gdy każdą recenzję ocenia na 2.5
blad = 0
ocenyZawszeTeSame = [2.5] * mTest
for k in range(mTest):
    blad += (ocenyZawszeTeSame[k] - ocenyTest[k])**2
bladSredniokwadratowy = blad / mTest

print ("Dla przypadku, gdy każda recenzja dostaje ocenę 2,5 błąd wynosi tyle: " +  str(bladSredniokwadratowy))
