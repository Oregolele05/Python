import csv
import os
import traceback

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
                                   "choice (1-5): "))
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
            folder = os.path.join(os.path.dirname(__file__), "Files")
            filename = os.path.join(folder, "miscellaneous_expenses.csv")
            try:
                os.makedirs(folder, exist_ok=True)
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Gift"])
                    writer.writerow(["Amount"])
                    writer.writerows(gift_cost)
                    writer.writerow([])
                    writer.writerow(["Charity Donations"])
                    writer.writerow(["Amount"])
                    writer.writerows(charity_donations)
                    writer.writerow([])
                    writer.writerow(["Memberships"])
                    writer.writerow(["Amount"])
                    writer.writerows(memberships_cost)
                    writer.writerow([])
                    writer.writerow(["Development costs"])
                    writer.writerow(["Amount"])
                    writer.writerows(development_costs)
                    writer.writerow([])
                    writer.writerow(["Unexpected costs"])
                    writer.writerow(["Amount"])
                    writer.writerows(unexpected_costs)
                    writer.writerow([])
                    writer.writerow(["Total Expenses", total_expenses])
            except OSError as e:
                print(f"Could not save miscellaneous_expenses.csv: {e}")
                traceback.print_exc()
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses

# Sub‑functions unchanged.


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
