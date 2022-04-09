#Kalkulačka BMI ve verzi pro muže a pro ženy. Vytvořeno uživatelem loticzek
print ("Vítáme vás v kalkulačce BMI")
print ("Pokud jste žena, zadejte prosím 1")
print ("Pokud jste muž, zadejte prosím 2")
pohlavi = int(input())

def BMI_muz():
 print ("zadej svoji hmotnost (kg)")
 hmotnost = float(input().replace(",",".")) #umožnuje zadání hmotnosti s desetinnou čárkou
 print("zadej svoji výšku (cm)")
 vyska = float(input()) / 100
 BMI = round ((hmotnost / (vyska ** 2)), 1)
 print("vaše BMI je", BMI)
 """ 
 Muž
 podváha <19,9
 normální 20-24,9
 nadváha 25-29,9
 obezita 30-39,9
 extrémní obezita >40
 """

 if (BMI <= 19.9):
    print ("Vaše BMI říká že trpíte podváhou")
 if (BMI >= 20 and BMI <= 24.9):
    print ("Vaše BMI říká, že je vaše hmostnost normální")
 if (BMI >= 25 and BMI <= 29.9):
    print("Vaše BMI říká, že trpíte nadváhou")
 if (BMI >= 30 and BMI <= 39.9):
    print("Vaše BMI říká, že trpíte obezitou")
 if (BMI >= 40):
    print("Vaše BMI říká, že trpíte extrémní obezitou")
    pass

def BMI_zena():
 print ("zadej svoji hmotnost (kg)")
 hmotnost = float(input().replace(",",".")) #umožnuje zadání hmotnosti s desetinnou čárkou
 print("zadej svoji výšku (cm)")
 vyska = float(input()) / 100
 BMI = round ((hmotnost / (vyska ** 2)), 1)
 print("vaše BMI je", BMI)

 """
 Žena
 podváha <18,9
 normální 19-23,9
 nadváha 24-28,9
 obezita 29-38,9
 extrémní obezita >39
 """
 if (BMI <= 18.9):
    print ("Vaše BMI říká že trpíte podváhou")
 if (BMI >= 19 and BMI <= 23.9):
    print ("Vaše BMI říká, že je vaše hmostnost normální")
 if (BMI >= 24 and BMI <= 28.9):
    print("Vaše BMI říká, že trpíte nadváhou")
 if (BMI >= 29 and BMI <= 38.9):
    print("Vaše BMI říká, že trpíte obezitou")
 if (BMI >= 39):
    print("Vaše BMI říká, že trpíte extrémní obezitou")
    pass

if pohlavi == 1:
    BMI_zena()
if pohlavi == 2:
    BMI_muz()
print("Děkujeme za využití kalkulačky")



