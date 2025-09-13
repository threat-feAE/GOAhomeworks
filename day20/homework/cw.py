#matematikuri operatorebi --> + : - : * : /


# // --> es aris igive gayopis xazi


print(10/3)
print(15//7) #aseti gayopa yoveltvis gvibrunebs integer tipis monacems;mtel ricxvs da pasuxad gvadzlevs tu ramdenjer motavsdeba eri ricxvi moreshi



print(2*4)
print(2**4)  #nishnavs 2*2*2*2


#samnairi gayopa gvakvs /  //  %
print(10%6)
#% gveubneba nashts



print(13/3)
print(123/56)
print(56/8)

print(13//3)
print(123//56)
print(56//8)




print(13*3)
print(123*56)
print(56*8)

print(13**3)
print(123**56)
print(56**8)




print(13%3)
print(123%56)
print(56%8)


#  15 / 3 = 5
#  20 / 4 = 5
#  100 / 20 = 5

#  15 // 10 = 1
#  10 // 7 =1
#  40 // 12 = 3

#  4 * 3 = 12
#  40 * 3 = 120
#  120 * 3 = 360

#  4 ** 3 = 64
#  10 ** 3 = 100
#  2 ** 6 = 64
#  3 ** 4 = 81
#  10 % 7 =3 
#  3 % 2 = 1
#  50 % 25 = 0
#  14 % 11 = 3
#  110 % 50 = 10


# სიები (list) გამოიყენება მაშინ, როცა გვინდა ერთ ცვლადში რამდენიმე მნიშვნელობის შენახვა.
# მაგალითად: სახელების სია, რიცხვების სია, პროდუქტების სია და ა.შ.
# განსხვავება ცვლადთან:
# ცვლადი ინახავს ერთ მნიშვნელობას, ხოლო სია ინახავს ბევრ მნიშვნელობას ერთდროულად.


string_list = ["apple", "banana", "cherry", "dog"]
print(string_list)


int_list = [1, 2, 3, 4, 5]
print(int_list)


float_list = [1.5, 2.3, 3.14, 4.0]
print(float_list)


bool_list = [True, False, True, False]
print(bool_list)


mixed_list = ["hello", 42, 3.14, True]
print(mixed_list)


a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)



num = int(input("შეიყვანე რიცხვი: "))

if num > 30 and num < 100:
    print("between 30 and 100")
elif num > 100 and num < 200:
    print("between 100 and 200")
else:
    print("other number")


a = "hello"       # string
b = 25            # int
c = 3.14          # float
d = True          # boolean
e = [1, 2, 3]     # list

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



num = 50
while num <= 100:
    print(num)
    num += 5

for i in range(40, 91, 3):
    print(i)

for i in range(15):
    print("Temo Kopadze")

count = 0
while count < 15:
    print("Temo Kopadze")
    count += 1

my_name = "Temo"
my_surname = "Kopadze"

user_name = input("შეიყვანე შენი სახელი: ")

if user_name == my_name:
    user_surname = input("შეიყვანე შენი გვარი: ")
    if user_surname == my_surname:
        print("same name and surname")
    else:
        print("same name but different surname")
else:
    print("aqedan moshordi")

password = "1234"

while True:
    user_pass = input("შეიყვანე პაროლი: ")
    if user_pass == password:
        print("გამოიცანი")
        break
    else:
        print("თავიდან სცადე")
num = 50
while num <= 100:
    print(num)
    num += 5

for i in range(40, 91, 3):
    print(i)

for i in range(15):
    print("Temo Kopadze")

count = 0
while count < 15:
    print("Temo Kopadze")
    count += 1

my_name = "Temo"
my_surname = "Kopadze"

user_name = input("შეიყვანე შენი სახელი: ")

if user_name == my_name:
    user_surname = input("შეიყვანე შენი გვარი: ")
    if user_surname == my_surname:
        print("same name and surname")
    else:
        print("same name but different surname")
else:
    print("aqedan moshordi")

password = "1234"

while True:
    user_pass = input("შეიყვანე პაროლი: ")
    if user_pass == password:
        print("გამოიცანი")
        break
    else:
        print("თავიდან სცადე")
