for i in range(1, 50):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")




for i in range(0, 20):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(i, "იყოფა 3-ზე")
    elif i % 5 == 0:
        print(i, "იყოფა 5-ზე")
    else:
        print(i, "არ იყოფა არცერთზე")






name=int(input("write a num: "))

x=0
y=0

for i in range(0,name):
    if i % 2==0:
        x +=1
    else:
        y+=1

print("ლუწი რიცხვების რაოდენობა:",x)
print("კენტი რიცხვების რაოდენობა:",y)










nums = [10, 25, 33, 47, 80, 99]

for n in nums:
    if n > 50:
        print(n, "more than 50")
    else:
        print(n, "less than 50")





x=0

for i in range(0,100):
    if i % 2==0:
        print(i)
        x+=i

print("ლუწი რიცხვების ჯამია: X")







fruits=["apple" , "peach" , "avocado" , "banana" , "grape"]

for i in range(5):
    if fruits[i][0]=="a":
        print(fruits[i])






for i in range(0,20):
    if i == 0:
        print(i,"zero")
    elif i % 2 ==0:
        print(i,"even")
    else:
        print(i,"odd")








numbers=[1,2,5,89,3,6,9]

for i in range(7):
    if i % 5 == 0:
        print(i)




name=input("enter: ")
for i in name:
    print(i)




total = 0 
for i in range(1,10):
    total += i

print("ჯამი არის:",total)