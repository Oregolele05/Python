expenses = []
cost = []
total = []
is_running = True
total_expenses = 0

def RentOrMortgage(total_expenses = 0):
    option = input("Are you paying your rent or mortgage?: ").lower()
    if option.__contains__("rent"):
        expenses.append(option.upper())
        rent = input("How much is your rent?: ")
        rent = float(rent)
        if rent <= 0:
            print("Your rent cannot be less than or equal to 0")
            return 0
        else:
            print(f"Your rent is {rent:.2f}.")
            cost.append(rent)
            total_expenses += rent
            return rent
    elif option.__contains__("mortgage"):
        expenses.append(option.upper())
        mortgage = input("How much is your mortgage?: ")
        mortgage = float(mortgage)
        if mortgage <= 0:
            print("Your mortgage cannot be less than or equal to 0")
            return 0
        else:
            print(f"Your mortgage is {mortgage:.2f}.")
            cost.append(mortgage)
            total_expenses += mortgage
            total.append(total_expenses)
            return mortgage
    else:
        print("Please enter a valid option.")
        return 0


#This method will calculate how much groceries cost
def Grocery(total_expenses=0):
    is_listing = True
    print("Welcome to the Grocery Calculator!")
    while is_listing:
        option = input("Would you like to continue or quit?: ").lower()
        if option.__contains__("continue") :
            item = input("Which item did you purchase?: ")
            if item.isdigit() or item.isnumeric() or item.isascii() or item == "":
                print("Please enter a valid item.")
            else:
                expenses.append(item.upper())
                price = input(f"How much was the item '{item}'")
                if price.isdigit():
                    price = float(price)
                    if price <= 0:
                        print("Your item cannot be less than or equal to 0")
                        return 0
                    else:
                        print(f"{item} is R{price:.2f}.")
                        quantity = (input(f"How many {item}(s) did you purchase?: "))
                        if quantity.isdigit():
                            quantity = int(quantity)
                            if quantity <= 0:
                                print("Your item cannot be less than or equal to 0")
                                return 0
                            else:
                                groceries = quantity * price
                                print(f"Your grocery is total cost was {groceries:.2f}.")
                                total_expenses += groceries
                                return total_expenses
                        else:
                            print("Please enter a numeric value.")
                else:
                    print("Please enter a numeric value.")
        elif option.__contains__("quit"):
            is_listing = False
        else:
            print("Please enter a valid option.")


def Utility():
    pass


def MaintenanceAndRepair():
    pass


def Clothing():
    print("Welcome to the Clothing Calculator!")
    is_buying = True
    while is_buying:
        option = input("Would you like to continue or quit?: ").lower()
        if option.__contains__("continue") :
            clothing = input("What type of clothing did you purchase?: ")
            if clothing.isdigit():
                print("Only use letters")
            else:
                price = input(f"How much was the clothing '{clothing}'")
                if price.isdigit():
                    price = float(price)
                    if price <= 0:
                        print("Your clothing cannot be less than or equal to 0")
                    else:
                        print(f"{clothing} is R{price:.2f}.")
                        quantity = input(f"How many {clothing}(s) did you purchase?: ")
                        if quantity.isdigit():
                            quantity = int(quantity)
                            if quantity <= 0:
                                print("Your clothing cannot be less than or equal to 0")
                            else:
                                clothes = quantity * price
                                print(f"Your total for {clothing} is {clothes:.2f}.")
                                cost.append(clothes)
                                expenses.append(clothing)
                                return clothes
                        else:
                            print("Please enter a numeric value.")
                else:
                    print("Please enter a numeric value.")
        elif option.__contains__("quit"):
            is_buying = False

def PropertyTaxes():
    pass


def HouseInsurance():
    pass