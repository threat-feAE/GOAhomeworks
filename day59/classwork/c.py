text = input("შეიყვანეთ სტრინგი: ")

total = 0

for chai in text:
     if chai.isdigit():
        total += int(chai)

print(total)


