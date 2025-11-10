#1
kio=input("type: ")

print("თქვენი სახელი დიდი ასოებით:", kio.upper())



#2
yu=input("write: ") 

print("თქვენი სახელი პატარა ასოებით:", kio.lower())




#3
name=input("shemoiyvane sityva: ")

print(name.capitalize())




#4

names = ["gio", "nino", "dato", "mari", "luka"]


for i in names:

    print(i.upper())



#5

names = ["GIO", "NINO", "DATO", "MARI", "LUKA"]


for i in names:

    print(i.lower())



#6

names = ["gio", "nino", "dato", "mari", "luka"]


for i in names:

    print(i.capitalize())



#7

items = ["ვაშლი", "ბანანი", "მსხალი", "ატამი", "კივი"]

print("list comtains", len(items), "elements")




#8

name = "ალექსანდრე"

print("string contains", len(name))  



#9

numbers = [2, 5, 8, 11, 14, 17, 20]

even_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1

print("even numbers: ", even_count)




#10

numbers = [3, 4, 7, 10, 13, 16, 19]


odd_count = 0
for i in numbers:
    if i % 2 != 0:
        odd_count += 1

print("odd numbers: ", odd_count)



#11

start = int(input("(start): "))
end = int(input("(end): "))
step = int(input("(step): "))


for i in range(start, end, step):
    if i % 2 == 0:
        print(i)