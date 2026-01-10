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

numbers = [3, 6, 5, 8, 7, 4]
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