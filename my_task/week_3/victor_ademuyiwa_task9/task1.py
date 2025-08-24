# Simulated USSD Menu Interaction
# Ussd code
ussd = ""
while ussd != "*977#":
    ussd = input("\nWelcome to Standard Bank\nDial *977# to make your transaction: ")
    if ussd != "*977#":
        print("Incorrect ussd")

while True:
    balance = 2000.0
    # Options (selecting transaction type)
    option = input("\n1. Buy Data\n2. Buy Airtime\n3. Check Balance\n4. Exit\nChoose an option between 1 - 4: ")
    if option == "1":
        # picking user
        data_service = input("\nPick data bundle\n1. self\n2. Other\n: ")
        if data_service == "1":
            # selecting data bundle
            pick_data_bundle = input("\nPick data bundle\n1>1.5GB Daily plan + 100MB YouTube Music for ₦400\n2>750MB + 500 talktime 7days for ₦500\n3>2.5GB 2 days plan for ₦900\n4>1.8GB + 5mins Monthly plan for ₦1500\n5>8GB + 25mins Monthly Plan for ₦4500\n6> cancel\n: ")
            if pick_data_bundle == "1":
                if 400 <= balance:
                    balance -= 400
                    print("\nTransation successful")
                    print(f"StanChart\nDebit Alert!\nAmt: ₦400\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                    break
                else:
                    print("\nInsufficient Funds")
                    break
            elif pick_data_bundle == "2":
                if 500 <= balance:
                    balance -= 500
                    print("\nTransation successful")
                    print(f"StanChart\nDebit Alert!\nAmt: ₦500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                    break
                else:
                    print("\nInsufficient Funds")
            elif pick_data_bundle == "3":
                if 900 <= balance:
                    balance -= 900
                    print("\nTransation successful")
                    print(f"StanChart\nDebit Alert!\nAmt: ₦900\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                    break
                else:
                    print("\nInsufficient Funds")
                    break
            elif pick_data_bundle == "4":
                if 1500 <= balance:
                    balance -= 1500
                    print("\nTransation successful")
                    print(f"StanChart\nDebit Alert!\nAmt: ₦1500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                    break
                else:
                    print("\nInsufficient Funds")
                    break
            elif pick_data_bundle == "5":
                if 4500 <= balance:
                    balance -= 4500
                    print("\nTransation successful")
                    print(f"StanChart\nDebit Alert!\nAmt: ₦4500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                    break
                else:
                    print("\nInsufficient Funds")
                    break
            elif pick_data_bundle == "6":
                break
            else:
                print("Incorrect option")
                break
        elif data_service == "2":
            # collecting phone number
            while True:
                phone_no = input("\nEnter phone number: ")
                if len(phone_no) == 11 and phone_no.isdigit():
                    # selecting data bundle
                    pick_data_bundle = input("\nPick data bundle\n1>1.5GB Daily plan + 100MB YouTube Music for ₦400\n2>750MB + 500 talktime 7days for ₦500\n3>2.5GB 2 days plan for ₦900\n4>1.8GB + 5mins Monthly plan for ₦1500\n5>8GB + 25mins Monthly Plan for ₦4500\n6> cancel\n: ")
                    if pick_data_bundle == "1":
                        if 400 <= balance:
                            balance -= 400
                            print("\nTransation successful")
                            print(f"StanChart\nDebit Alert!\nAmt: ₦400\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                            break
                        else:
                            print("\nInsufficient Funds")
                            break
                    elif pick_data_bundle == "2":
                        if 500 <= balance:
                            balance -= 500
                            print("\nTransation successful")
                            print(f"StanChart\nDebit Alert!\nAmt: ₦500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                            break
                        else:
                            print("\nInsufficient Funds")
                    elif pick_data_bundle == "3":
                        if 900 <= balance:
                            balance -= 900
                            print("\nTransation successful")
                            print(f"StanChart\nDebit Alert!\nAmt: ₦900\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                            break
                        else:
                            print("\nInsufficient Funds")
                            break
                    elif pick_data_bundle == "4":
                        if 1500 <= balance:
                            balance -= 1500
                            print("\nTransation successful")
                            print(f"StanChart\nDebit Alert!\nAmt: ₦1500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                            break
                        else:
                            print("\nInsufficient Funds")
                            break
                    elif pick_data_bundle == "5":
                        if 4500 <= balance:
                            balance -= 4500
                            print("\nTransation successful")
                            print(f"StanChart\nDebit Alert!\nAmt: ₦4500\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                            break
                        else:
                            print("\nInsufficient Funds")
                            break
                    elif pick_data_bundle == "6":
                        break
                    else:
                        print("Incorrect option")
                        break
                else:
                    print("\nIncorrect number")
            break
        else:
            print("Incorrect option")
            break
    elif option == "2":
        # selecting user
        airtime_service = input("Buy Airtime\n1. Self\n2. Others\n: ")
        if airtime_service == "1":
            # Entering amount
            amount = float(input("Enter the amount: "))
            if amount <= balance:
                balance -= amount
                print("\nTransation successful")
                print(f"StanChart\nDebit Alert!\nAmt: ₦{amount:,.2f}\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                break
            else:
                print("Insuffient balance")
        elif airtime_service == "2":
            # Collecting phone number
            while True:
                phone_no = input("\nEnter phone number: ")
                if len(phone_no) == 11 and phone_no.isdigit():
                    # Entering amount
                    amount = float(input("Enter amount: "))
                    if amount <= balance:
                        balance -= amount
                        print("\nTransation successful")
                        print(f"StanChart\nDebit Alert!\nAmt: ₦{amount:,.2f}\nDesc: USSD PAYMENT\nBal: ₦{balance:,.2f}")
                        break
                    else:
                        print("\nInsufficient Funds")
                        break
                else:
                    print("\nIncorrect number")
            break
    elif option == "3":
        # checking data balance
        print(f"Your account balance is ₦{balance:,.2f}")
        pass
    elif option == "4":
        break