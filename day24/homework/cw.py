numbers = [1, 8, 3, 7, 5, 0, 1]

result = numbers[-7] * numbers[-1]
print(numbers[-5])
print(numbers[-3])


fruits = ["apple", "bannana", "peach", "cherry", "grape" ,"kiwi"]

print(fruits[2])
print(fruits[3])

print(fruits[-4])
print(fruits[-3])



nums = [3,4,5,1,2,9,8,6]

random_num = int(input("airchie cipri tore dagxvritav: "))

if random_num>0 and random_num<10:
    print("sagol ")
elif random_num<0 or random_num>10:
    print(nums[random_num])


u=["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]

print(u[-11],u[-9],u[-7],u[-4],u[-6],u[-1],u[-5])

print(u[0],u[2],u[4],u[7],u[5],u[10],u[6])

print(u[8],u[2],u[10],u[3])


f=["dog", "cat", "horse", "cow", "sheep", "goat"]

e=int(input("enter number: "))

if f[e] == "cat":
    print("shen airchie cat")
elif f[e] == "goat":
    print("shen airchie goat")
else:
    print("shen sxva cxoveli airchie")



t=["tbilisi","samtredia","batumi","kutaisi","kobuleti","zugdidi"]

r=int(input("choose: "))

l=int(input("choose: "))

if r<l:
    print(t[r],t[l])
elif r>l:
    print("შეცვალე ინდექსები ადგილებით")
    print(t[l],t[r])
else:
    print("orive ertia")
    print(t[r])



b=input("dawere sityva: ")

if b[0] == "a":
   print("სიტყვა იწყება a-თი")
elif b[-1] == "z":
    print("სიტყვა მთავრდება z-ით")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")



x=input("dawere: ")

if x[0] == x[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")


z=["agivorsbgitr"]

print(z[1],z[4],z[0])
print(z[6],z[0],z[7],z[0])
print(z[7],z[0],z[10],z[2],z[3],z[0],z[11])
print(z[1],z[2],z[4],z[11],z[1],z[2])



j="giorgi"

i = 0
word = "giorgi"
while i < len(word):
    print(word[i])
    i+=1


word="giorgi"

for k in word:
    print(k)

