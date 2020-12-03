import random

baza = ["krokodyl","wieloryb","pies","kot","rekin","zebra","ryba"]
slowo = random.choice(baza)
odpowiedz = slowo
dlugosc = len(slowo)
print("Wylosowane slowo ma ",dlugosc, "liter")
while (True):
    x = input("Podaj litere: ")
    if (x in slowo):
        slowo = slowo.replace(x,"")
        dlugosc = len(slowo)
        print(slowo,dlugosc)
        print(x,"wystepuje w slowie")
        if (dlugosc==0):
            print("Gratulacje! odgadniete slowo to ",odpowiedz) 
    else: print(x," nie wystepuje w slowie")
