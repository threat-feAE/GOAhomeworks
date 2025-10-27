cities = ["Tbilisi", "Kutaisi", "Batumi", "Rustavi", "Gori", "Telavi", "Marneuli"]

for i in cities:
    if len(i) > 6:
        print(i)





words = ["congratulations", "responsibility", "internationalization", "communication"]

for i in words:
    if len(i) % 15 == 0:
        print(i)






numbers = [3, 7, 12, 45, 9, 23, 56]
kiu = 0

for i in numbers:
    kiu += 1

print("სიის სიგრძეა:", i)







words21 = ["apple", "peach", "grape", "mango", "melon", "pear"]

for i in words21:
    if len(i) == 5:
        print(i)





sentence = input("შეიყვანე წინადადება: ")


print("სულ სიმბოლოებია:", len(sentence))


count = 0
for i in sentence:
    if i == "a" or i == "A":
        count += 1

print("'a' ან 'A' რაოდენობაა:", count)




strings = ["banana", "watermelon", "kiwi", "strawberry", "orange"]

longest = ""
for s in strings:
    if len(s) > len(longest):
        longest = s

print(longest)