#1
m=["gio","saba","temo","mari","nika"]
result=[]
for i in m:
     if i.islower() and i.startswith("g"):
        result.append("goga")
     elif i.isupper() or i.startswith("N"):
        result.append("Nika")
     else:
        result.append("ლიდერი")

print(result)


o=["cat","dog","monkey","goose","lion"]
result=[]
for animal in o:
     if animal.isupper() or animal.startswith("tiger"):
         result.append("jungle")
     elif animal.islower() or animal.endswith("lion"):
         result.append("animals")
     else:
         result.append("error")

print(result)






#2

numbers = [3, 6, 5, 8, 7, 4, 9, 7]
result = []

i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 2 == 0 or i % 2 == 0:
        result.append(num ** 2)   
    else:
        result.append(num * 2)    
    i += 1
print(result)







#3
words = ["Nika", "PROGRAMMING", "python", "HELLO", "Data123"]
list = []

i = 0
while i < len(words):
    word = words[i]
    if len(word) > 6 or word.isupper():
        list.append(word.lower())
    else:
        list.append(word + word)
    i += 1

print(list)




#4
numbers = (0,1, 2, 3 ,4 ,5, 6, 7, 8, 9)
result_for = []

for i in range(len(numbers)):
    kopa = int(numbers[i])
    if i % 2 == 0 or kopa > 7:
        result_for.append(kopa)

print(result_for)
