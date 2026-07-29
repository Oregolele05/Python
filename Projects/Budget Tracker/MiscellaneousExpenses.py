import csv
gift_cost = []
charity_donations = []
memberships_cost = []
development_costs = []
unexpected_costs = []


def Misc():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the Miscellaneous Expenses calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Gift costs.\n"
                                   "2. Charity donations.\n"
                                   "3. Membership costs.\n"
                                   "4. Development costs.\n"
                                   "5. Unexpected costs.\n"
                                   "choice (1-5)"))
                if choice == 1:
                    total_expenses += GiftCost()
                elif choice == 2:
                    total_expenses += CharityDonations()
                elif choice == 3:
                    total_expenses += MembershipsCost()
                elif choice == 4:
                    total_expenses += DevelopmentCosts()
                elif choice == 5:
                    total_expenses += UnexpectedCosts()
                else:
                    print("Invalid choice. Please choose from 1-5.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
            filename = "miscellaneous_expenses.csv"
            with open(filename, 'w', newline=' ') as file:
                writer = csv.writer(file)

                
                writer.writerow(["Gift"])
                writer.writerow(["Amount"])
                writer.writerow(gift_cost)
                writer.writerow([])

                writer.writerow(["Charity Donations"])
                writer.writerow(["Amount"])
                writer.writerow(charity_donations)
                writer.writerow([])

                writer.writerow(["Memberships"])
                writer.writerow(["Amount"])
                writer.writerow(memberships_cost)
                writer.writerow([])

                writer.writerow(["Developmen costs"])
                writer.writerow(["Amount"])
                writer.writerow(development_costs)
                writer.writerow([])

                writer.writerow(["Unexpected costs"])
                writer.writerow(["Amount"])
                writer.writerow(unexpected_costs)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses


def GiftCost():
    is_running = True
    while is_running:
        print("Welcome to the Gift costs calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you spend?: R"))
                if price > 0:
                    print(f"You have spent R{price:.2f} on gifts.")
                    gift_cost.append([price])
                    return price
                else:
                    print(f"You cannot spend R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def CharityDonations():
    is_running = True
    while is_running:
        print("Welcome to the Charity donations calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you spend?: R"))
                if price > 0:
                    print(f"You have spent R{price:.2f} on charity donations.")
                    charity_donations.append([price])
                    return price
                else:
                    print(f"You cannot spend R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def MembershipsCost():
    is_running = True
    while is_running:
        print("Welcome to the Membership costs calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you spend?: R"))
                if price > 0:
                    print(f"You have spent R{price:.2f} on membership costs.")
                    memberships_cost.append([price])
                    return price
                else:
                    print(f"You cannot spend R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def DevelopmentCosts():
    is_running = True
    while is_running:
        print("Welcome to the Development costs calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you spend?: R"))
                if price > 0:
                    print(f"You have spent R{price:.2f} on development costs.")
                    development_costs.append([price])
                    return price
                else:
                    print(f"You cannot spend R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def UnexpectedCosts():
    is_running = True
    while is_running:
        print("Welcome to the Unexpected costs calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you spend?: R"))
                if price > 0:
                    print(f"You have spent R{price:.2f} on unexpected costs.")
                    unexpected_costs.append([price])
                    return price
                else:
                    print(f"You cannot spend R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0
