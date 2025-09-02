a = ("1")
b = ("23")
c = ("3")

if a == b == c :
    print("samive tolia")
elif a == b :
    print("pirveli da meore tolia")
elif a == c :
    print("pirveli da mesame tolia")
elif c == b :
    print("mesame da meore sworia")
else :
    print("arceti ar aris swori")















month = int(input())

if month == 12 or month == 1 or month == 2:
    print("ზამთარი")
elif month == 3 or month == 4 or month == 5:
    print("გაზაფხული")
elif month == 6 or month == 7 or month == 8:
    print("ზაფხული")
elif month == 9 or month == 10 or month == 11:
    print("შემოდგომა")
else:
    print("არასწორი თვეა")










# მომხმარებლის სახელი
name = input("შეიყვანეთ თქვენი სახელი: ")

if name == "admin":
    # პაროლის მოთხოვნა
    password = input("შეიყვანეთ ადმინის პაროლი: ")
    if password == "adminpassword123":
        print("სალამი, ადმინ!")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი, მომხმარებელო!")