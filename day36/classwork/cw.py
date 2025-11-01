text = input("შეიყვანეთ სიტყვა ან ტექსტი: ")




if 'a' in text or 'A' in text:
    print("ტექსტში არის ასო 'a' ან 'A'")
else:
    print("ტექსტში არ არის ასო 'a' და არც 'A'")




if 'car' not in text:
    print("ტექსტში არ არის სიტყვა 'car'")
else:
    print("ტექსტში მოიძებნა სიტყვა 'car'")





text = input("შეიყვანეთ ტექსტი: ")


for i in text:

    if i == 'a' or i == 'A':
        continue
  
    print(i)