kopa = "Python aris saintereso ena"
lopa = "aeiouAEIOU"
count = 0

for tropa in kopa:
    if tropa in lopa:
        count += 1

print("ხმოვანი ასოების რაოდენობაა:", count)






numbers = [1, 2, 3, 4, 5, 6, 8]
sum = 0

for num in numbers:
    if num % 2 == 0:
        sum += num

print("ლუწი რიცხვების ჯამია:", sum)




numbers = [15, 3, 27, 9, 20]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("ყველაზე დიდი რიცხვია:", largest)





password = input("შეიყვანეთ პაროლი: ")

while len(password) < 6:
    password = input("პაროლი მოკლეა, სცადეთ თავიდან: ")

print("პაროლი სწორიაა")





numbers = [3, 5, 3, 8, 5, 10, 8]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

