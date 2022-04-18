#Ohmův zákon
#I=U/R
#U=R*I
#R=U/I
print("Vítej v kalkulačce Ohmova zákona")
print("Pro každou veličinu zadej buď hodnotu a nebo stiskni ENTER")
print("Vždy je třeba zadat dvě veličiny")
print("Pro pokračování stiskni ENTER")
input("")
kalkulacka = True
while kalkulacka:
 print("Zadej R")
 r = input().replace(",",".")
 print("Zadej U")
 u = input().replace(",",".")
 print("Zadej I")
 i = input().replace(",",".")
 if r == "" and i == float and u == float: #zadat otaznik a nebo zmáčknutí ENTER
    napeti = float(u)
    proud = float(i)
    vysledek = napeti / proud
    print("výsledek je", vysledek, "ohm")
 if u == "" and i == float and r == float: #zadat otaznik a nebo zmáčknutí ENTER
    odpor = float(r)
    proud = float(i)
    vysledek = odpor * proud
    print("výsledek je", vysledek, "V")
 if i == "" and u == float and r == float: #zadat otaznik a nebo zmáčknutí ENTER
    napeti = float(u)
    odpor = float(r)
    vysledek = napeti / odpor
    print("výsledek je", vysledek, "A")

 else:
    print("Nebyla zadána žádná veličina. Nelze provést výpočet.")
    print("Zadej opět veličiny k výpočtu: \n")
    kalkulacka = True




