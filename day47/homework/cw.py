names = ["Gio", "nino", "Ana", "luka", "Mari", "dato"]
Upper_name = []

for name in names:
    if name[0].isupper():
        Upper_name.append(name)

print(Upper_name)





names = ["gio", "nino", "ana"]
surnames = ["BERIDZE", "KAPANADZE", "GELASHVILI"]

print([n.upper() for n in names] + [s.lower() for s in surnames])






words = ["Python", "Code", "PROGRAM", "School", "test", "HelloA"]
result = []

for word in words:
    if len(word) >= 6 and not word[-1].isupper():
        result.append(word)

print(result)






numbers = [5.5, 12.3, 45.6, 9.9, 100.5, 77.7, 10.1, 99.9, 3.3, 150.2]
new_list = []

for num in numbers:
    if num > 10 and num < 100:
        new_list.append(num)

print(new_list)







cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Zugdidi"]

countries = ["Georgia", "Italy","Portugal", "Greece", "Turkey", "Armenia"]

for i in range(5):
    countries.insert(i, cities[i])

print(countries)



