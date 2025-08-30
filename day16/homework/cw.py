# 1) მომხმარებლის რიცხვის შემოწმება (დადებითი/უარყოფითი/ნული)
num = float(input("შეიყვანეთ რიცხვი: "))
if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")


# 2) ასაკის შემოწმება
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")


# 3) Password guesser პროგრამა
password = "12345"   # აქ შენს პაროლს ჩაწერე
tries = 0

while True:
    guess = input("შეიყვანე პაროლი (ან დაწერე 'nah strong password' გამოსასვლელად): ")
    tries += 1
    if guess == password:
        print("სწორია! გამოიცანი {} ცდაში.".format(tries))
        break
    elif guess == "nah strong password":
        print("გამოსვლა... პაროლი იყო:", password)
        break
    else:
        print("არასწორია, სცადე თავიდან.")


# 4) სამი რიცხვიდან უდიდესის პოვნა
a = float(input("შეიყვანე პირველი რიცხვი: "))
b = float(input("შეიყვანე მეორე რიცხვი: "))
c = float(input("შეიყვანე მესამე რიცხვი: "))

print("უდიდესი რიცხვია:", max(a, b, c))


# 5) კვირის დღეების ამოცნობა
day = int(input("შეიყვანეთ რიცხვი (1-7): "))

if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")