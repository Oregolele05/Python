import csv
child_expenses = []
school_expenses = []
elder_costs = []
veterinary_expenses = []
pet_insurance = []


def FamCare():
    is_running = True
    total_expenses = 0
    while is_running:
        print("Welcome to the Family Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Child expenses.\n"
                                   "2. School expenses.\n"
                                   "3. Elder expenses.\n"
                                   "4. Veterinary expenses.\n"
                                   "5. Pet insurance.\n"
                                   "choice: "))
                if choice == 1:
                    total_expenses += ChildExpenses()
                elif choice == 2:
                    total_expenses += SchoolExpenses()
                elif choice == 3:
                    total_expenses += ElderCosts()
                elif choice == 4:
                    total_expenses += VeterinaryExpenses()
                elif choice == 5:
                    total_expenses += PetInsurance()
                else:
                    print("Please enter a valid option (1-5).")
                    continue
            except ValueError:
                print("Please enter a numeric value (1-5).")
                continue

        elif option == "quit":
            print("Goodbye!")

            filename = "family_expenses.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # child expenses
                writer.writerow(["Child Expenses"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(child_expenses)
                writer.writerow([])

                writer.writerow(["Schools supplies or Fees"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(school_expenses)
                writer.writerow([])

                writer.writerow(["Elderly Expenses"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(elder_costs)
                writer.writerow([])

                writer.writerow(["Veterinary Expenses"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(veterinary_expenses)
                writer.writerow([])

                writer.writerow(["Pet Insurance"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(pet_insurance)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])

            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
            continue
    return total_expenses


def ChildExpenses():
    is_running = True
    care = ["Child care", "Daycare", "Babysitting"]
    while is_running:
        print("Welcome to the Child Care")
        option = input("Would you like to continue or quit: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which expense did you pay for?\n"
                                   "1. Child care.\n"
                                   "2. Daycare.\n"
                                   "3. Babysitting.\n"
                                   "choice: "))
                if choice == 1:
                    try:
                        child = care[0]
                        fees = float(
                            input(f"How much was the {child} expenses?: R"))
                        if fees > 0:
                            print(f"Your total cost is R{fees:.2f}.")
                            child_expenses.append([
                                child,
                                fees
                            ])
                            return fees
                        else:
                            print("Your fees cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 2:
                    try:
                        child = care[1]
                        fees = float(
                            input(f"How much was the {child} expenses?: R"))
                        if fees > 0:
                            print(f"Your total cost is R{fees:.2f}.")
                            child_expenses.append([
                                child,
                                fees
                            ])
                            return fees
                        else:
                            print("Your fees cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 3:
                    try:
                        child = care[2]
                        fees = float(
                            input(f"How much was the {child} expenses?: R"))
                        if fees > 0:
                            print(f"Your total cost is R{fees:.2f}.")
                            child_expenses.append([
                                child,
                                fees
                            ])
                            return fees
                        else:
                            print("Your fees cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                else:
                    print("Please enter a valid choice (1-3)")
                    continue
            except ValueError:
                print("Please enter a number")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return 0


def SchoolExpenses():
    school = ["Supplies", "Fees"]
    is_running = True
    while is_running:
        print("Welcome to the School Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which expense did you pay for?\n"
                                   "1. School Supplies\n"
                                   "2. School Fees\n"
                                   "choice: "))
                if choice == 1:
                    supplies = school[0]
                    try:
                        price = float(
                            input(f"How much was the {supplies} expenses?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            school_expenses.append([
                                supplies,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 2:
                    fees = school[1]
                    try:
                        price = float(
                            input(f"How much was the {fees} expenses?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            school_expenses.append([
                                fees,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                else:
                    print("Please enter a valid choice (1-2)")
                    continue
            except ValueError:
                print("Please enter a numeric value (1-2).")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return 0


def ElderCosts():
    is_running = True
    care = ["Elder medication", "Elder care"]
    while is_running:
        print("Welcome to the Elder Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which expense did you pay for?\n"
                                   "1. Elder medication.\n"
                                   "2. Elder care.\n"
                                   "choice (1-2): "))
                if choice == 1:
                    elder = care[0]
                    try:
                        price = float(input(f"How much was the {elder} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            elder_costs.append([
                                elder,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 2:
                    elder = care[1]
                    try:
                        price = float(input(f"How much was the {elder} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            elder_costs.append([
                                elder,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                else:
                    print("Please enter a valid choice (1-2)")
                    continue
            except ValueError:
                print("Please enter a number")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return 0


def VeterinaryExpenses():
    is_running = True
    pet = ["Vaccination", "Emergency Treatment", "Routine checkup"]
    while is_running:
        print("Welcome to the Veterinary Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which expense did you pay for?\n"
                                   "1. Vaccination\n"
                                   "2. Emergency treatment\n"
                                   "3. Routine checkup\n"
                                   "choice (1-3): "))
                if choice == 1:
                    visit = pet[0]
                    try:
                        price = float(input(f"How much was the {visit} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            veterinary_expenses.append([
                                visit,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 2:
                    visit = pet[1]
                    try:
                        price = float(input(f"How much was the {visit} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            veterinary_expenses.append([
                                visit,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 3:
                    visit = pet[2]
                    try:
                        price = float(input(f"How much was the {visit} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            veterinary_expenses.append([
                                visit,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                else:
                    print("Please enter a valid choice (1-3)")
                    continue
            except ValueError:
                print("Please enter a number")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return 0


def PetInsurance():
    is_running = True
    insurance = ["Accident-Only Plans", "Illness-Only Plans",
                 "Wellness Plans", "Comprehensive / Extensive Plans"]
    while is_running:
        print("Welcome to the Pet Insurance Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which expense did you pay for?\n"
                                   "1. Accident-Only Plans.\n"
                                   "2. Illness-Only Plans.\n"
                                   "3. Wellness Plans.\n"
                                   "4. Comprehensive / Extensive Plans.\n"
                                   "choice (1-4): "))
                if choice == 1:
                    cover = insurance[0]
                    try:
                        price = float(input(f"How much was the {cover} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            pet_insurance.append([
                                cover,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 2:
                    cover = insurance[1]
                    try:
                        price = float(input(f"How much was the {cover} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            pet_insurance.append([
                                cover,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 3:
                    cover = insurance[2]
                    try:
                        price = float(input(f"How much was the {cover} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            pet_insurance.append([
                                cover,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                elif choice == 4:
                    cover = insurance[3]
                    try:
                        price = float(input(f"How much was the {cover} ?: R"))
                        if price > 0:
                            print(f"Your total cost is R{price:.2f}.")
                            pet_insurance.append([
                                cover,
                                price
                            ])
                            return price
                        else:
                            print("Your price cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a number")
                        continue
                else:
                    print("Please enter a number between 1 and 4")
                    continue
            except ValueError:
                print("Please enter a number")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return 0
