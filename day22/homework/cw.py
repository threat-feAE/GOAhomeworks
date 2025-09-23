# Index არის ელემენტის უნიკალური ნომერი სიაში ან სტრინგში.
# მას ვიყენებთ იმისათვის, რომ კონკრეტულ ელემენტს მივწვდეთ.
# ინდექსი იწყება 0-დან. მაგალითად list[0] - პირველი ელემენტია.


nums = [4, 6, 1, 5, 9, 8, 4]

print(nums[0] + nums[1])   
print(nums[2] + nums[2])  
print(nums[4] + nums[5])   
print(nums[5] + nums[3] + nums[1] + nums[0]) 
print(nums[0] + nums[6] - nums[2]) 
print(nums[4] + nums[2] + nums[0]) 



names = ["გიორგი", "ნიკა", "ლაშა", "თამარ", "ანა", "მარიამი", "დავით", "სოფო", "ელენე", "ირაკლი"]

print(names[5])   # მე–5 ინდექსი
print(names[9])   # მე–9 ინდექსი
print(names[3])   # მე–3 ინდექსი
print(names[7])   # მე–7 ინდექსი
print(names[1])   # პირველი ინდექსი

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი"]

# for loop
for item in fruits:
    print(item)

# while loop
i = 0
while i < (fruits):
    print(fruits[i])
    i += 1

items = [1, 2, 3, 4, 5, 6, 7]

items[3] = "vashli"
items[6] = "msxali"
items[4] = "atami"

print(items)

result = True and False or False and True or False and False or True
print(result)   # პასუხი = True

animals = ["dog", "cat", "tiger", "lion", "elephant"]

if animals[3] == "lion":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")

basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]

print(basket[0])
print(basket[2])  

basket[1] = "კივი"   

print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

print(letters[2])        
print(letters[4], letters[5])  
print(letters[1])        


print(letters[6] + letters[5] + letters[7] + letters[5])  
print(letters[2] + letters[3] + letters[4] + letters[5])  
print(letters[2] + letters[3] + letters[2] + letters[5])  






letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

# 1) მე–4 ინდექსზე არსებული ასო
letter1 = letters[4]

if letter1 == "ლ":
    print("სწორია! ასო ლ ა")
else:
    print("არასწორია, სცადე თავიდან")

# 2) ბოლო ასო
last_letter = letters[-1]

if last_letter == "ე":
    print("საიდუმლო სიტყვა იწყება სწორად")
else:
    print("საიდუმლო სიტყვა არასწორია")

# 3) სიტყვა "გელა"
word = letters[2] + letters[4] + letters[5] + letters[0]

if word == "გელა":
    print("გაარტყი სახელი!")
else:
    print("შტერი ხარ!დ")

names = ["გიორგი", "ნიკა", "მარიამი", "ანა", "ლუკა", "თამარ"]

index = int(input("შეიყვანე რიცხვი (ინდექსი): "))

if index (names):   # ვამოწმებთ რომ ინდექსი არ იყოს დიდი
    print("ამ ინდექსზე მდგომი ელემენტია:", names[index])
else:
    print("ასეთი ინდექსი არ არსებობს სიაში")
