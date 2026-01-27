numbers = [5, 12, 7, 3, 20, 15]

kopa = numbers[0]
koba = numbers[0]

for num in numbers:
    if num > kopa:
        koba = kopa
        kopa = num
    elif num > koba and num != kopa:
        koba = num

print("second biggest number  isss:", koba)







sentence = input("შეიყვანეთ წინადადება: ")

words = sentence.split()
count = 0
i = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print("blablablaa:", count)






word = input("word:  ")

is_palindrome = True
lenght = len(word)
for i in range(lenght // 2):
    if word[i] != word[lenght - 1 -i]:
        is_palindrome = True
        break

print(is_palindrome)



