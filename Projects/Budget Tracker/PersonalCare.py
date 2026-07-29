import csv
import os
import traceback

hygiene_products = []
grooming_services = []
laundry_dryCleaning = []
cosmetics = []
wellness_treatments = []

def SelfCare():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the Personal Care calculator.")
        option = input("Would you like to quit or continue?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Personal Hygiene.\n"
                                   "2. Grooming Services.\n"
                                   "3. Laundry Dry Cleaning.\n"
                                   "4. Cosmetics.\n"
                                   "5. Wellness Treatments.\n"
                                   "choice (1-5): "))
                if choice == 1:
                    total_expenses += PersonalHygiene()
                elif choice == 2:
                    total_expenses += SalonAndBarber()
                elif choice == 3:
                    total_expenses += LaundryAndDryCleaning()
                elif choice == 4:
                    total_expenses += Cosmetics()
                elif choice == 5:
                    total_expenses += WellnessTreatments()
                else:
                    print("Please choose between 1-5.")
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
            folder = os.path.join(os.path.dirname(__file__), "Files")
            filename = os.path.join(folder, "personal_expenses.csv")
            try:
                os.makedirs(folder, exist_ok=True)
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Personal hygiene"])
                    writer.writerow(["Item", "Amount"])
                    writer.writerows(hygiene_products)
                    writer.writerow([])
                    writer.writerow(["Hair services"])
                    writer.writerow(["Amount"])
                    writer.writerows(grooming_services)
                    writer.writerow([])
                    writer.writerow(["Clothing care"])
                    writer.writerow(["Amount"])
                    writer.writerows(laundry_dryCleaning)
                    writer.writerow([])
                    writer.writerow(["Cosmetics"])
                    writer.writerow(["Type", "Amount"])
                    writer.writerows(cosmetics)
                    writer.writerow([])
                    writer.writerow(["Wellness treatments"])
                    writer.writerow(["Amount"])
                    writer.writerows(wellness_treatments)
                    writer.writerow([])
                    writer.writerow(["Total Expenses", total_expenses])
            except OSError as e:
                print(f"Could not save personal_expenses.csv: {e}")
                traceback.print_exc()
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses

# Sub‑functions unchanged.


def PersonalHygiene():
    hygiene = ["Soap or Body Wash", "Deodorant", "Toilet paper",
               "Moisturizer", "Toothbrush and Toothpaste"]
    is_running = True
    while is_running:
        print("Welcome to the Personal Hygiene calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which product did you purchase?\n"
                                   "1. Soap or Body wash.\n"
                                   "2. Deodorant.\n"
                                   "3. Toilet paper.\n"
                                   "4. Moisturizer.\n"
                                   "5. Toothbrush and Toothpaste.\n"
                                   "choice (1-5):"))
                if choice == 1:
                    product = hygiene[0]
                    try:
                        price = float(
                            input(f"How much did you spend on {product}: R"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {product}.")
                            hygiene_products.append([
                                product,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {product} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    product = hygiene[1]
                    try:
                        price = float(
                            input(f"How much did you spend on {product}: R"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {product}.")
                            hygiene_products.append([
                                product,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {product} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    product = hygiene[2]
                    try:
                        price = float(
                            input(f"How much did you spend on {product}: R"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {product}.")
                            hygiene_products.append([
                                product,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {product} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 4:
                    product = hygiene[3]
                    try:
                        price = float(
                            input(f"How much did you spend on {product}: R"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {product}.")
                            hygiene_products.append([
                                product,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {product} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 5:
                    product = hygiene[4]
                    try:
                        price = float(
                            input(f"How much did you spend on {product}: R"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {product}.")
                            hygiene_products.append([
                                product,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {product} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1-5")
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


def SalonAndBarber():
    is_running = True
    while is_running:
        print("Welcome to Grooming services calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay?: R"))
                if price > 0:
                    print(f"You paid R{price:.2f} for grooming.")
                    grooming_services.append([price])
                    return price
                else:
                    print(f"Your price cannot be R{price:.2f}.")
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


def LaundryAndDryCleaning():
    is_running = True
    while is_running:
        print("Welcome to the Laundry and Dry cleaning calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay?: R"))
                if price > 0:
                    print(
                        f"You paid R{price:.2f} for laundry and dry cleaning.")
                    laundry_dryCleaning.append([price])
                    return price
                else:
                    print(f"Your price cannot be R{price:.2f}.")
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


def Cosmetics():
    products = ["Skincare", "Makeup", "Hair care", "Fragrances"]
    is_running = True
    while is_running:
        print("Welcome to the Cosmetics calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which cosmetic did you purchase?\n"
                                   "1. Skincare.\n"
                                   "2. Makeup.\n"
                                   "3. Hair care.\n"
                                   "4. Fragrances.\n"
                                   "choice (1-4): "))
                if choice == 1:
                    cos = products[0]
                    try:
                        price = float(
                            input(f"How much did you pay for {cos}?: R"))
                        if price > 0:
                            print(f"You paid R{price:.2f} for {cos}.")
                            cosmetics.append([
                                cos,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {cos} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    cos = products[1]
                    try:
                        price = float(
                            input(f"How much did you pay for {cos}?: R"))
                        if price > 0:
                            print(f"You paid R{price:.2f} for {cos}.")
                            cosmetics.append([
                                cos,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {cos} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    cos = products[2]
                    try:
                        price = float(
                            input(f"How much did you pay for {cos}?: R"))
                        if price > 0:
                            print(f"You paid R{price:.2f} for {cos}.")
                            cosmetics.append([
                                cos,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {cos} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 4:
                    cos = products[3]
                    try:
                        price = float(
                            input(f"How much did you pay for {cos}?: R"))
                        if price > 0:
                            print(f"You paid R{price:.2f} for {cos}.")
                            cosmetics.append([
                                cos,
                                price
                            ])
                            return price
                        else:
                            print(f"Your {cos} cannot be R{price:.2f}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1-4.")
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


def WellnessTreatments():
    is_running = True
    while is_running:
        print("Welcome to Wellness treatment calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay?: R"))
                if price > 0:
                    print(f"You paid R{price:.2f} for the treatment.")
                    wellness_treatments.append([price])
                    return price
                else:
                    print(f"Your price cannot be R{price:.2f}.")
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
