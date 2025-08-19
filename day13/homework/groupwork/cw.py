bank_name = "PythonBank"
account_number = "45090133"
password = "PROJECT"


is_vip = True
balance = 4000.00


if is_vip == True:
    daily_withdraw_limit = 2000.00       
    per_withdraw_limit = 1000.00         
else:
    daily_withdraw_limit = 1000.00       
    per_withdraw_limit = 500.00          


withdrawn_today = 0.00


print("================================================")
print()
print("  კეთილი იყოს თქვენი მობრძანება", bank_name,"-ში!")
print()
print("================================================")
print()


print("შეიყვანეთ თქვენი ანგარიშის ნომერი: ")
entered_account = input("ანგარიშის ნომერი: ")


if entered_account == account_number:

    print("ანგარიშის ნომერი სწორია.")
    print("გთხოვთ, შეიყვანეთ პაროლი. გაქვთ მაქსიმუმ 3 ცდა.")

    logged_in = False
    account_locked = False

    
    for attempt in range(1, 4):
        entered_password = input("ცდა " + str(attempt) + " - პაროლი: ")

        if entered_password == password:
            print("პაროლი სწორია. კეთილი იყოს თქვენი შემოსვლა მთავარ მენიუში!")
            logged_in = True
            break  
        else:
            
            print("პაროლი არასწორია.")
           
            if attempt == 3:
                account_locked = True
                print("ანგარიში დაიბლოკა 3 წარუმატებელი ცდის გამო.")
            else:
                print("სცადეთ ხელახლა.")


    if account_locked == True and logged_in == False:
        print("გთხოვთ, დაუკავშირდეთ ბანკის ოპერატორს ანგარიშის განბლოკვისთვის.")
    else:
        
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

          
                if menu_choice == "1":
                    print()
                    print("---- ბალანსის ინფორმაცია ----")
                    print("კლიენტის სტატუსი (VIP):", is_vip)
                    print("თქვენი მიმდინარე ბალანსი არის:", balance)
                    print("დღიურ ლიმიტზე გატანილი თანხა:", withdrawn_today, "/", daily_withdraw_limit)

bank_name = "PythonBank"
account_number = "45090133"
password = "PROJECT"


is_vip = True
balance = 4000.00


if is_vip == True:
    daily_withdraw_limit = 2000.00       
    per_withdraw_limit = 1000.00         
else:
    daily_withdraw_limit = 1000.00       
    per_withdraw_limit = 500.00          


withdrawn_today = 0.00


print()
print("================================================")
print()
print("  კეთილი იყოს თქვენი მობრძანება", bank_name,"-ში!")
print()
print("================================================")
print()


print("შეიყვანეთ თქვენი ანგარიშის ნომერი: ")
entered_account = input("ანგარიშის ნომერი: ")


if entered_account == account_number:
    print("ანგარიშის ნომერი სწორია.")
    print()
    print("გთხოვთ, შეიყვანეთ პაროლი. გაქვთ მაქსიმუმ 3 ცდა.")

    logged_in = False
    account_locked = False

    
    for attempt in range(1, 4):
        entered_password = input("ცდა " + str(attempt) + " - პაროლი: ")

        if entered_password == password:
            print("პაროლი სწორია. კეთილი იყოს თქვენი შემოსვლა მთავარ მენიუში!")
            logged_in = True
            break  
        else:
           
            print("პაროლი არასწორია.")
            
            if attempt == 3:
                account_locked = True
                print("ანგარიში დაიბლოკა 3 წარუმატებელი ცდის გამო.")
            else:
                print("სცადეთ ხელახლა.")


    if account_locked == True and logged_in == False:
        print("გთხოვთ, დაუკავშირდეთ ბანკის ოპერატორს ანგარიშის განბლოკვისთვის.")
    else:
        
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

                
                if menu_choice == "1":
                    print()
                    print("---- ბალანსის ინფორმაცია ----")
                    print("კლიენტის სტატუსი (VIP):", is_vip)
                    print("თქვენი მიმდინარე ბალანსი არის:", balance)
                    print("დღიურ ლიმიტზე გატანილი თანხა:", withdrawn_today, "/", daily_withdraw_limit)

                
                elif menu_choice == "2":
                    print()
                    print("---- თანხის გამოტანა ----")
                    amount = float(input("შეიყვანეთ თანხა: "))

                    if amount <= 0:
                        print("არასწორი თანხა. შეიყვანეთ დადებითი რიცხვი.")
                    elif amount > balance:
                        print("ბალანსი არასაკმარისია.")
                    elif amount > per_withdraw_limit:
                        print("შეყვანილი თანხა აღემატება ერთჯერად ლიმიტს (", per_withdraw_limit, ").")
                    elif withdrawn_today + amount > daily_withdraw_limit:
                        print("ეს ოპერაცია გადააჭარბებს დღიურ ლიმიტს. დღემდე გატანილია:", withdrawn_today)
                    else:
                        balance = balance - amount
                        withdrawn_today = withdrawn_today + amount
                        print("თანხა წარმატებით გატანილია:", amount)
                        print("ახალი ბალანსი:", balance)
                        print("დღემდე გატანილი თანხა:", withdrawn_today, "/", daily_withdraw_limit)

               
                elif menu_choice == "3":
                    print()
                    print("---- თანხის შეტანა ----")
                    deposit = float(input("შეიყვანეთ შესატანი თანხა: "))
                    if deposit <= 0:
                        print("გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
                    else:
                        balance = balance + deposit
                        print("თანხა წარმატებით ჩაირიცხა:", deposit)
                        print("ახალი ბალანსი:", balance)

               
                elif menu_choice == "4":
                    print()
                    print("---- პაროლის შეცვლა ----")
                    old_pass = input("შეიყვანეთ ძველი პაროლი: ")
                    if old_pass == password:
                        new_pass = input("შეიყვანეთ ახალი პაროლი: ")
                        confirm_pass = input("გაიმეორეთ ახალი პაროლი: ")
                        if new_pass == confirm_pass and new_pass != "":
                            password = new_pass
                            print("პაროლი წარმატებით შეიცვალა.")
                        else:
                            print("პაროლები არ ემთხვევა ან ცარიელია.")
                    else:
                        print("ძველი პაროლი არასწორია.")

                
                elif menu_choice == "5":
                    print()
                    print("===========================================")
                    print()
                    print("მადლობა, რომ სარგებლობთ", bank_name,"-ით!")
                    print()
                    print("===========================================")
                    print()
                    running = False

                else:
                    print("არასწორი არჩევანი. სცადეთ ხელახლა.")
else:
    account_locked_number = False
    logged_in_number = False
    for attempt in range(1, 4):
        entered_account = input("ცდა " + str(attempt) + " - ანგარიშის ნომერი: ")
        if entered_account == account_number:
            print("ანგარიშის ნომერი სწორია.")
            print()
            print("გთხოვთ, შეიყვანეთ პაროლი. გაქვთ მაქსიმუმ 3 ცდა.")

            logged_in = False
            account_locked = False

           
            for pass_attempt in range(1, 4):
                entered_password = input("ცდა " + str(pass_attempt) + " - პაროლი: ")

                if entered_password == password:
                    print("პაროლი სწორია. კეთილი იყოს თქვენი შემოსვლა მთავარ მენიუში!")
                    logged_in = True
                    break
                else:
                    print("პაროლი არასწორია.")
                    if pass_attempt == 3:
                        account_locked = True
                        print("ანგარიში დაიბლოკა 3 წარუმატებელი ცდის გამო.")
                    else:
                        print("სცადეთ ხელახლა.")

            if account_locked == True and logged_in == False:
                print("გთხოვთ, დაუკავშირდეთ ბანკის ოპერატორს ანგარიშის განბლოკვისთვის.")
            else:
                if logged_in == True:
                    running = True
                    print()
                    print("--------- მთავარი მენიუ ---------")
                    print("აირჩიეთ რიცხვის შეყვანით.")
            break
        else:
            print("ანგარიშის ნომერი არასწორია.")
            if attempt == 3:
                account_locked_number = True
                print("ანგარიში დაიბლოკა 3 წარუმატებელი ცდის გამო.")
            else:
                print("სცადეთ ხელახლა.")

    if account_locked_number == True and logged_in_number == False:
        print("გთხოვთ, დაუკავშირდეთ ბანკის ოპერატორს ანგარიშის განბლოკვისთვის.")



