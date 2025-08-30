# 1) შეამოწმეთ თუ რიცხვი მეტია 10-ზე
num = 12   # ინტეჯერ ტიპის მონაცემი
if num > 10:
    print("more than 10")
else:
    print("less than 10")


# 2) მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ თუ უდრის 15-ს
number = int(input("Enter a number: "))
if number == 15:
    print("equal to 15")
else:
    print("not equal to 15")


# 3) მომხმარებლის სტრინგის შემოწმება
name = input("Enter your name: ")
if name == "giorgi":
    print("you are correct")
else:
    print("you are wrong")


# 4) for ციკლი 50-დან 100-მდე 5-ის გამოტოვებით
for i in range(50, 101, 5):
    print(i)


# 5) for ციკლი – თქვენი სახელი და გვარი
for i in range(5):   # რამდენჯერაც გინდათ იმდენჯერ
    print("Temo Kopadze")   # აქ ჩაწერე შენი სახელი და გვარი


# 6) while loop – რიცხვები 20-დან 50-მდე
i = 20
while i <= 50:
    print(i)
    i += 1