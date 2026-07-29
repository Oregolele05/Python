import csv
renting_expenses = []
grocery_expenses = []
utility_expenses = []
maintenance_expenses = []
clothing_expenses = []
property_taxes_expenses = []
insurance_expenses = []


def Expenses():
    is_running = True
    total_expenses = 0
    while is_running:
        print("Welcome to the Living Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Rent or Mortgage.\n"
                                   "2. Grocery.\n"
                                   "3. Utility.\n"
                                   "4. Maintenance or Repairs.\n"
                                   "5. Clothing.\n"
                                   "6. Property Taxes.\n"
                                   "7. Homeowners Insurance.\n"
                                   "input: "))
                if choice == 1:
                   total_expenses += RentOrMortgage()
                elif choice == 2:
                   total_expenses += Grocery()
                elif choice == 3:
                   total_expenses += Utility()
                elif choice == 4:
                    total_expenses += MaintenanceAndRepair()
                elif choice == 5:
                    total_expenses += Clothing()
                elif choice == 6:
                    total_expenses += PropertyTaxes()
                elif choice == 7:
                    total_expenses += HomeownersInsurance()

                else:
                    print("Please enter a valid option (1-7).")
                    continue
            except ValueError:
                print("Please enter a numeric value (1-7).")
                continue

        elif option == "quit":
            print("Thank you for using Living Expenses Calculator!")
            print(f"Your total expenses is R{total_expenses:.2f}.")
            filename = "living_expenses.csv"
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)

                # Rent or Mortgage
                writer.writerow(["Rent or Mortgage"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(renting_expenses)
                writer.writerow([])

                # Grocery
                writer.writerow(["Grocery"])
                writer.writerow(["Item", "Price", "Quantity", "Cost"])
                writer.writerows(grocery_expenses)
                writer.writerow([])

                # Utilities
                writer.writerow(["Utilities"])
                writer.writerow(["Utility", "Amount"])
                writer.writerows(utility_expenses)
                writer.writerow([])

                # Maintenance
                writer.writerow(["Maintenance and Repairs"])
                writer.writerow(["Service", "Amount"])
                writer.writerows(maintenance_expenses)
                writer.writerow([])

                # Clothing
                writer.writerow(["Clothing"])
                writer.writerow(["Item", "Price", "Quantity", "Cost"])
                writer.writerows(clothing_expenses)
                writer.writerow([])

                # Property Taxes
                writer.writerow(["Property Taxes"])
                writer.writerow(["Tax Type", "Amount"])
                writer.writerows(property_taxes_expenses)
                writer.writerow([])

                # Insurance
                writer.writerow(["Homeowners Insurance"])
                writer.writerow(["Policy", "Amount"])
                writer.writerows(insurance_expenses)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
                is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return total_expenses


def RentOrMortgage():
        is_running = True
        while is_running:
            print("Welcome to the Rent/Mortgage Calculator!")
            option = input("Would you like to continue or quit?: ").lower()
            if option == "continue":
                choice = input("Are you paying your rent or mortgage?: ").lower()
                if choice == "rent":
                    try:
                        rent = float(input("How much is your rent?: R"))
                        if rent > 0:
                            print(f"Your rent is R{rent:.2f}.")
                            renting_expenses.append([
                                choice,
                                rent
                            ])
                            return rent
                        else:
                            print("Your rent cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == "mortgage":
                    try:
                        mortgage = float(input("How much is your mortgage?: R"))
                        if mortgage > 0:
                            print(f"Your mortgage is {mortgage:.2f}.")
                            renting_expenses.append([
                                choice,
                                mortgage
                            ])
                            return mortgage
                        else:
                            print("Your mortgage cannot be less than zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a valid option.")
                    continue
            elif option == "quit":
                is_running = False
            else:
                print("Please enter a valid option. 'continue' or 'quit'.")
                continue
        return 0


#This method will calculate how much groceries cost
def Grocery():
    is_running = True
    while is_running:
        print("Welcome to the Grocery Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            item = input("Which item did you purchase?: ")
            if item.isalpha():
                try:
                    price = float(input(f"How much was the item '{item}': R"))
                    if price > 0:
                        print(f"{item} is R{price:.2f}.")
                        try:
                            quantity = int(input(f"How many {item}(s) did you purchase?: "))
                            if quantity <= 0:
                                print("Your item cannot be less than or equal to 0")
                                continue
                            else:
                                cost = quantity * price
                                print(f"Your grocery is total cost was {cost:.2f}.")
                                grocery_expenses.append([
                                    item,
                                    price,
                                    quantity,
                                    cost,
                                ])
                                return cost
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    else:
                        print("Enter a numeric value greater than 0.")
                        continue

                except ValueError:
                    print("Please enter a numeric value.")
                    continue
            else:
                print("Please enter a valid option. e.g apple")
                continue

        elif option == "quit":
            print(f"What you bought today: {grocery_expenses}")
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0


def Utility():
    is_running = True
    utilities = ["Water", "Electricity", "Gas"]
    print("Welcome to the Utility Calculator!")
    while is_running:
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                item = int(input("Which utility did you purchase/pay?\n"
                             "1. Water\n"
                             "2. Electricity\n"
                             "3. Gas.\n "
                             "choice (1-3): "))
                if item == 1:
                    try:
                        price = float(input(f"How much was the '{utilities[0]}' bill?: "))
                        if price > 0:
                            print(f"{utilities[0]} is R{price:.2f}.")
                            utility_expenses.append([
                                utilities[0],
                                price
                            ])
                            return price
                        else:
                            print(f"Your {utilities[0]} bill cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif item == 2:
                    try:
                        price = float(input(f"How much was the '{utilities[1]}' bill?: "))
                        if price > 0:
                            print(f"{utilities[1]} is R{price:.2f}.")
                            utility_expenses.append([
                                utilities[1],
                                price
                            ])
                            return price
                        else:
                            print(f"Your {utilities[1]} bill cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif item == 3:
                    try:
                        price = float(input(f"How much was the '{utilities[2]}' bill?: "))
                        if price > 0:
                            print(f"{utilities[2]} is R{price:.2f}.")
                            utility_expenses.append([
                                utilities[2],
                                price
                            ])
                            return price
                        else:
                            print(f"Your {utilities[2]} bill cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1-3")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0


def MaintenanceAndRepair():
    is_running = True
    inside = ["Drywall cracks and holes", "Plumbing issue", "Electrical repairs", "Door and Window fixes."]
    outside = ["Roof repairs", "Foundation repairs", "Gutter and Siding maintenance", "Landscaping and Outdoor maintenance"]

    while is_running:
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            print("Welcome to the Maintenance and Repair Calculator!")
            service_type = input("Was it an exterior or interior fix: ").lower()
            if service_type == "interior":
                try:
                    interior = int(input("What type of interior was it? (1-4)\n"
                                         "1. Drywall cracks and holes.\n"
                                         "2. Plumbing issue.\n"
                                         "3. Electrical repairs.\n"
                                         "4. Door and Window fixes.\n"
                                         ": "))
                    if interior == 1:
                        try:
                            price = float(input(f"How much did'{inside[0]}' cost you?: R"))
                            if price > 0:
                                print(f"{inside[0]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    inside[0],
                                    price
                                ])
                                return price
                            else:
                                print(f"{inside[0]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif interior == 2:
                        try:
                            price = float(input(f"How much did {inside[1]} cost you?: R"))
                            if price > 0:
                                print(f"{inside[1]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    inside[1],
                                    price
                                ])
                                return price
                            else:
                                print(f"{inside[1]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif interior == 3:
                        try:
                            price = float(input(f"How much did {inside[2]} cost you?: R"))
                            if price > 0:
                                print(f"{inside[2]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    inside[2],
                                    price
                                ])
                                return price
                            else:
                                print(f"{inside[2]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif interior == 4:
                        try:
                            price = float(input(f"How much did {inside[3]} cost you?: R"))
                            if price > 0:
                                print(f"{inside[3]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    inside[3],
                                    price
                                ])
                                return price
                            else:
                                print(f"{inside[3]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    else:
                        print("Please choose between 1-4")
                        continue
                except ValueError:
                    print("Please enter a numeric value.")
                    continue
            elif service_type == "exterior":
                try:
                    exterior = int(input("What type of exterior service was it? (1-4)\n"
                                         "1. Roof repairs.\n"
                                         "2. Foundation repairs.\n"
                                         "3. Gutter and Siding maintenance.\n"
                                         "4. Landscaping and Outdoor maintenance.\n"
                                         ": "))
                    if exterior == 1:
                        try:
                            price = float(input(f"How much did {outside[0]} cost you?: R"))
                            if price > 0:
                                print(f"{outside[0]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    outside[0],
                                    price
                                ])
                                return price
                            else:
                                print(f"{outside[0]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif exterior == 2:
                        try:
                            price = float(input(f"How much did {outside[1]} cost you?: R"))
                            if price > 0:
                                print(f"{outside[1]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    outside[1],
                                    price
                                ])
                                return price
                            else:
                                print(f"{outside[1]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif exterior == 3:
                        try:
                            price = float(input(f"How much did {outside[2]} cost you?: R"))
                            if price > 0:
                                print(f"{outside[2]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    outside[2],
                                    price
                                ])
                                return price
                            else:
                                print(f"{outside[2]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    elif exterior == 4:
                        try:
                            price = float(input(f"How much did {outside[3]} cost you?: R"))
                            if price > 0:
                                print(f"{outside[3]} cost is R{price:.2f}.")
                                maintenance_expenses.append([
                                    outside[3],
                                    price
                                ])
                                return price
                            else:
                                print(f"{outside[3]} cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    else:
                        print("Please choose between 1-4")
                        continue
                except ValueError:
                    print("Please enter a numeric value.")
                    continue
            else:
                print("Please choose between interior or exterior")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0


def Clothing():
    is_running = True
    while is_running:
        print("Welcome to the Clothing Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            clothing = input("What type of clothing did you purchase?: ").lower()
            if clothing.isalpha():
                try:
                    price = float(input(f"How much was the clothing '{clothing}': R"))
                    if price > 0:
                        print(f"{clothing} is R{price:.2f}.")
                        try:
                            quantity = int(input(f"How many {clothing}(s) did you purchase?: "))
                            cost = quantity * price
                            if quantity > 0:
                                print(f"Your total for {clothing} is {cost:.2f}.")
                                clothing_expenses.append([
                                    clothing,
                                    price,
                                    quantity,
                                    cost
                                ])
                                return cost
                            else:
                                print("Your clothing cannot be less than or equal to 0")
                                continue
                        except ValueError:
                            print("Please enter a numeric value.")
                            continue
                    else:
                        print("Your clothing cannot be less than or equal to 0")
                        continue
                except ValueError:
                    print("Please enter a numeric value.")
                    continue
            else:
                print("Please enter valid option. eg. shirt")
                continue
        elif option == "quit":
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0


def PropertyTaxes():
    is_running = True
    types = ["Municipal property rates", "Transfer duty", "Capital gains tax", "VAT on property", "Estate duty" ]
    while is_running:
        print("Welcome to the Property Taxes Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                taxes = int(input("What type of taxes did you pay?"
                                  "1. Municipal property rates. \n"
                                  "2. Transfer duty.\n"
                                  "3. Capital gains tax (CGT).\n"
                                  "4. VAT on property.\n"
                                  "5. Estate duty.\n"
                                  ": "))
                if taxes == 1:
                    try:
                        price = float(input(f"How much was {types[0]}?: "))
                        if price > 0:
                            print(f"{types[0]} is R{price:.2f}.")
                            property_taxes_expenses.append([
                                types[0],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{types[0]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif taxes == 2:
                    try:
                        price = float(input(f"How much was {types[1]}?: "))
                        if price > 0:
                            print(f"{types[1]} is R{price:.2f}.")
                            property_taxes_expenses.append([
                                types[1],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{types[1]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif taxes == 3:
                    try:
                        price = float(input(f"How much was {types[2]}?: "))
                        if price > 0:
                            print(f"{types[2]} is R{price:.2f}.")
                            property_taxes_expenses.append([
                                types[2],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{types[2]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif taxes == 4:
                    try:
                        price = float(input(f"How much was {types[3]}?: "))
                        if price > 0:
                            print(f"{types[3]} is R{price:.2f}.")
                            property_taxes_expenses.append([
                                types[3],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{types[3]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif taxes == 5:
                    try:
                        price = float(input(f"How much was {types[4]}?: "))
                        if price > 0:
                            print(f"{types[4]} is R{price:.2f}.")
                            property_taxes_expenses.append([
                                types[4],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{types[4]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a valid option.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0


def HomeownersInsurance():
    insurance = ["Building Insurance", "Contents Insurance", " Household Contents", "Homeowners Insurance"]
    is_running = True
    while is_running:
        print("Welcome to the Homeowners Insurance Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                policy = int(input("Which insurance policy did you buy/pay?\n"
                                   "1. Building Insurance.\n"
                                   "2. Contents Insurance.\n"
                                   "3. Household Contents.\n"
                                   "4. Homeowners Insurance.\n"
                                   "input: "))
                if policy == 1:
                    try:
                        price = float(input(f"How much was {insurance[0]}?: "))
                        if price > 0:
                            print(f"{insurance[0]} is R{price:.2f}.")
                            insurance_expenses.append([
                                insurance[0],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{insurance[0]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif policy == 2:
                    try:
                        price = float(input(f"How much was {insurance[1]}?: "))
                        if price > 0:
                            print(f"{insurance[1]} is R{price:.2f}.")
                            insurance_expenses.append([
                                insurance[1],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{insurance[1]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif policy == 3:
                    try:
                        price = float(input(f"How much was {insurance[2]}?: "))
                        if price > 0:
                            print(f"{insurance[2]} is R{price:.2f}.")
                            insurance_expenses.append([
                                insurance[2],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{insurance[2]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif policy == 4:
                    try:
                        price = float(input(f"How much was {insurance[3]}?: "))
                        if price > 0:
                            print(f"{insurance[3]} is R{price:.2f}.")
                            insurance_expenses.append([
                                insurance[3],
                                price
                            ])
                            return price
                        else:
                            print(f"Your '{insurance[3]}' cannot be less than or equal to 0")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a valid option.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return 0