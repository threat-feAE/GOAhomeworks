# 1)მოცემულია სია --> [1, 2, 3, 4, 5, 6]
# შეცვალე შუა ორი ელემენტი რიცხვებით [10, 20, 30].


ew=[1, 2, 3, 4, 5, 6]
ew[2:4]=[10, 20, 30]
print(ew)





# 2)მოცემულია სია --> ["apple", "banana", "cherry", "kiwi", "mango"]
# შეცვალე პირველი ორი ელემენტი სიით ["pear", "plum"].


re=["apple", "banana", "cherry", "kiwi", "mango"]
re[0:2]=["pear", "plum"]






# 3)ოცემულია სია --> ["a", "b", "c", "d", "e", "f"]
# შეცვალე ბოლო სამი ელემენტი სიით ["x", "y", "z"].


na=["a", "b", "c", "d", "e", "f"]
na[3:6]=["x", "y", "z"]
print(na)






# 4)მოცემულია სია --> ["red", "green", "blue", "yellow", "black", "white"]
# შეცვალე ინდექსებზე 2-დან 5-მდე ელემენტები სიით ["purple", "orange"].


color=["red", "green", "blue", "yellow", "black", "white"]
color[2:5]=["purple", "orange"]
print(color)






# 5)მოცემულია სია --> ["გიორგი" , "ირმა" , "საბა" ]
# შეცვალე მთლიანი სია შემდეგი სიით -->  ["red", "green", "blue", "yellow", "black", "white"]


name=["გიორგი" , "ირმა" , "საბა" ]
name[0:3]= ["red", "green", "blue", "yellow", "black", "white"]
print(name)





kopex = int(input("შეიყვანე რიცხვი: "))


if kopex % 2 == 0:
    print("EVEN")
else:
    print("Odd")






numbers = [5, 321, 6735, 1, 3, 67]


num = numbers[3]


if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")









numbers = [15, 28, 49, 62, 77, 54]


kola = numbers[-1]


if kola % 2 == 0 and kola > 50:
    print("even and more than 50")
elif kola % 2 != 0 and kola < 50:
    print("odd and less than 50")










numbers = [20, 45, 67, 89, 150, 102, 75]


num1 = numbers[5]


num2 = numbers[3]


if num1 % 2 == 0 or num1 > 100:
    print("even or more than 100")


if num2 % 2 != 0 or num2 < 100:
    print("odd or less than 100")








lopa = "hello"
dopa = "world"


if lopa != dopa:
    print("სტრინგები არ არის თანასწორი")
else:
    print("სტრინგები თანასწორია")



