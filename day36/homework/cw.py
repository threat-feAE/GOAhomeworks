word = input("შეიტანეთ სიტყვა: ")

for l in word:
    if l == 'e' or l == 'E':
        break
    print(l)


# 2)
text = input("შეიტანეთ წინადადება: ")

if "bad" in text:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")


# 3) 
sentence = input("შეიტანეთ წინადადება: ")

for kopa in sentence:
    if kopa == " ":
        continue
    print(kopa)


# 4)

text = input("შეიტანეთ წინადადება: ")

vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        continue
    print(i)


# 5)
start = int(input("შეიტანეთ პირველი რიცხვი: "))
end = int(input("შეიტანეთ მეორე რიცხვი: "))

for i in range(start, end + 1):
    if i % 15 == 0:
        print("პირველი რიცხვი რომელიც იყოფა 15-ზე არის:", i)
        break


# 6)

while True:
    user_input = input("შეიტანეთ ტექსტი: ")
    if user_input == "python is best":
        break
    print("you should learn python")


