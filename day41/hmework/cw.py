# append()  -> სიას ბოლოში ამატებს ერთ ელემენტს.
# insert(index, value) -> ამატებს ელემენტს კონკრეტულ ინდექსზე. index = პოზიცია, value = რასაც ვამატებთ.
# pop() -> შლის ბოლო ელემენტს და აბრუნებს მას.
# pop(index) -> შლის კონკრეტული ინდექსის ელემენტს.
# remove() -> შლის კონკრეტულ მნიშვნელობას სიიდან (პირველივე დამთხვევას).
# clear() -> ასუფთავებს მთლიან სიას.
# extend() -> აერთიანებს ორ სიას ერთმანეთში
# reverse() -> აბრუნებს სიას უკუღმა
# index() -> გვიბრუნებს ფრჩხილებში გადმოცემული ელემენტის ინდექს
# count() -> ითვლის ფრჩხილებში გადმოცემული ელემენტების რაოდენობას

#2) 
numbers = [1, 2, 3, 4, 5]
numbers.append(10)
print(numbers)

#3)
names = ["goga", "luka", "dato"]
names.append("kopa") 
print(names)

#4) 
names = ["goga", "luka", "nika", "dato"]
kopa_name = input("შეიყვანე სახელი: ")

names.append(kopa_name)
print(names)

#5) 
names = ["ana", "nino", "mari", "lile", "dato"]
names.insert(3, "kopa")  
print(names)

#6) 
kopa13 = ["a", "b", "c", "d", "e", "f"]

tropa_name = input("შეიყვანე სახელი: ")
lopa_index = int(input("შეიყვანე რიცხვი 0-დან 6-მდე: "))

kopa13.insert(lopa_index, tropa_name)

print(kopa13)

#7) 
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

#8) 
names = ["goga", "saba", "luka"]
names.insert(-1, "irakli")  
print(names)

#9)
foods = ["bread", "milk", "cheese"]
foods.insert(0, "water")
print(foods)

#10) 

numbers = [5, 10, 15]
numbers.pop()
print(numbers)

#11) 

fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)

#12)

names = ["goga", "saba", "luka"]
names.pop(1)
print(names)

#13) 
colors = ["red", "green", "blue", "yellow", "black", "purple"]

colors.pop(0)      
colors.pop(2)     

print(colors)