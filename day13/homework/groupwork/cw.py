# საწყისი მდგომარეობა
bank_name = "PythonBank"
account_number = "45090133"
password = "PROJECT"

# მომხმარებლის სტატუსი და ბალანსი
is_vip = True
balance = 4000.00

# ლიმიტები VIP-სთვის და ჩვეულებრივი კლიენტისთვის
if is_vip == True:
    daily_withdraw_limit = 2000.00       # VIP-ის ყოველდღიური ფულის გამოტანის ლიმიტი
    per_withdraw_limit = 1000.00         # VIP-ის ერთხელ ფულის გამოტანის ლიმიტი
else:
    daily_withdraw_limit = 1000.00       # ჩვეულებრივიკლიენტის ყოველდღიური ფულის გამოტანის ლიმიტი
    per_withdraw_limit = 500.00          # ჩვეულებრივი კლიენტის ერთხელ ფულის გამოტანის ლიმიტი

# დღემდე გატანილი თანხა
withdrawn_today = 0.00

# მისალმება
print("================================================")
print()
print("  კეთილი იყოს თქვენი მობრძანება", bank_name,"-ში!")
print()
print("================================================")
print()

# account-ზე შესვლა (login)
print("შეიყვანეთ თქვენი ანგარიშის ნომერი: ")
entered_account = input("ანგარიშის ნომერი: ")

# ანგარიშის ნომრის შემოწმება
if entered_account == account_number:
    print("ანგარიშის ნომერი სწორია.")
    print("გთხოვთ, შეიყვანეთ პაროლი. გაქვთ მაქსიმუმ 3 ცდა.")

    logged_in = False
    account_locked = False

    # პაროლის შეყვანის 3 ცდა
    for attempt in range(1, 4):
        entered_password = input("ცდა " + str(attempt) + " - პაროლი: ")

        if entered_password == password:
            print("პაროლი სწორია. კეთილი იყოს თქვენი შემოსვლა მთავარ მენიუში!")
            logged_in = True
            break  # break არ გვისწავლია, მაგრამ გამოვიყენე რადგან არ ვიცოდი როგორ შემეჩერებინა კოდი.
        else:
            # !=
            print("პაროლი არასწორია.")
            # ბოლო ცდაზე თუ ვერ შევედით, დავბლოკოთ ანგარიში
            if attempt == 3:
                account_locked = True
                print("ანგარიში დაიბლოკა 3 წარუმატებელი ცდის გამო.")
            else:
                print("სცადეთ ხელახლა.")

 # თუ დაიბლოკა ანგარიში
    if account_locked == True and logged_in == False:
        print("გთხოვთ, დაუკავშირდეთ ბანკის ოპერატორს ანგარიშის განბლოკვისთვის.")
    else:
        # მთავარი მენიუ — while loop
        if logged_in == True:
            running = True
            print()
            print("--------- მთავარი მენიუ ---------")
            print("აირჩიეთ რიცხვის შეყვანით.")

            while running == True:
                print()
                print("1) ბალანსის ნახვა")
                print("2) თანხის გამოტანა")
                print("3) თანხის შეტანა")
                print("4) პაროლის შეცვლა")
                print("5) გასვლა")
                print("------------------------------")
                menu_choice = input("აირჩიეთ (1-5): ")

            # selection — არჩევანი (if / elif / else)

                # 1) ბალანსის ნახვა
                if menu_choice == "1":
                    print()
                    print("---- ბალანსის ინფორმაცია ----")
                    print("კლიენტის სტატუსი (VIP):", is_vip)
                    print("თქვენი მიმდინარე ბალანსი არის:", balance)
                    print("დღიურ ლიმიტზე გატანილი თანხა:", withdrawn_today, "/", daily_withdraw_limit)



