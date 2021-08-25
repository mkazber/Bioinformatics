# -*- coding: utf-8 -*-
# komentarz
#trzeba pilnować wcięć w programie
#ctrl+/ cała linia zakomentowana
#string w '' lub ""

#przypisanie do zmiennej
# a = 1
# print(a)
# c=input("Podaj liczbe")
# print(13/5)
# print(13//5)
# print(13%5)

# student="Jestem studentem"
# rok=input("Podaj ktorego roku?")
# kierunek=input("Podaj jakiego kierunku?")
# print("Jestem studentem",rok,"roku na kierunku: ",kierunek)

# a=2
# print(type(a))
# x="Komórka ludzka ma"
# y="23"
# z="pary chromosomów"
# zadanie=x+y+z
# print(zadanie)
# print(y,x,z)
# X="Pies"
# Y=39
# print('Zmienna X ma typ: ',type(X))
# print(' Zmienna Y ma typ: ',type(Y))
# print(X,"ma: ",str(X))

#print('The answer is %s'%42)
#print('The answer is',str(42))

#x=4
#int(x)
#3str(x)
#float(x)
#chr(x)
#oct(x)


#from math import floor
#from math import sqrt
#from math import pow

#print(sqrt(125))
#print(floor(32.69))
#print(pow(3,4))

#tablica = ["jeden","dwa","trzy","cztery"];
#liczba = input('Wybierz liczbe: ');
#ile = int(liczba);
#print("Ta liczba to:" + tablica[ile-1]);
#print(tablica.index("trzy"))

#tablica = ["a","b","c","k"];
#liczba = input('Wybierz liczbe: ');
#ile = int(liczba);
#print("Ta litera to:" + tablica[ile-1]);
#print(tablica.index("c"))

#d1=['Tomek','lat',25];
#d2=['Szerel',1996,'Białystok']
#d3=[d1,d2];
#print(d3)

#tablica="morskie oko";
#print(tablica[4])
#print(tablica[-4])
#print(tablica[-5:])
#print(tablica[0:-4])
#print(tablica[-2:0:-1])
from builtins import len

#dane=['Tomek','Adam','Karol','Stefan']
#x=input("Podaj imie ")
#print(x in dane)
#del dane[1]
#': :' .join("Bioinformatyka")
#list("Bioinformatyka")
#print(len(dane))
#zbior=[1,2,3,4,5]
#zbior[2:2]=list("pi")
#print(len(zbior))

#zb=[3,2,3,4,5]
#dane=['kot','pies','kot','kot','chomik']
#zb.append(10)
#zb.insert(0,100)
#zb.pop(2)
#zb.reverse()
#zb.index(5)
#zb.pop()
#zb.remove(5)
#print(dane.count('kot'))
#print(len("Tomasz")>len("Szerel"))
#print(len("Tomasz")<len("Szerel"))
#print(len("Tomasz")<=len("Szerel"))
#print(len("Tomasz")>=len("Szerel"))
#print(len("Tomasz")==len("Szerel"))
#print(len("Tomasz")!=len("Szerel"))
from builtins import pow

from math import pow

#x=int(input("Podaj liczbe: "))
#if x>0:
#    print(x,"jest > 0")
#
#if x>3:
#    print(x)
#elif x>=-1 and x<=3:
#    print(pow(x,2))
#elif x<-1:
#    print(pow(x,3))

#i=0
#while i<100:
#    i=i+1
#    print(i)

#nazwa = ('Bioinformatyka')
#for x in range(5):
#    print(nazwa)

#def powiedz(wiadomosc,ile-1);
#    print(wiadomosc*ile)
#    powiedz('Koniec sesji')
#    powiedz('Koniec sesji',5)
import math

def liczpierwiastki(a,b,c):
    delta=(pow(b,2))-(4*a*c)
    if delta>0:
        x1= (-b - math.sqrt(delta)) / (2 * a)
        x2=(-b+ math.sqrt(delta))/ (2 * a)
        return x1,x2
    elif delta==0:
        x1=-b/(2*a)
        return x1
    else:
        print("Nie ma miejsc zerowych")

print(liczpierwiastki(2,2,-12))


