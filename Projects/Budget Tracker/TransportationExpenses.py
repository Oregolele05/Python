import csv
car_payments = []
public_transport = []
toll_fees = []
car_insurance = []
gas_costs = []
maintenance_costs = []
registration_fees = []


def Transportation():
    is_running = True
    total_expenses = 0
    while is_running:
        print("Welcome to the Transportation Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Car installment payments.\n"
                                   "2. Public transport fees.\n"
                                   "3. Toll gate fees.\n"
                                   "4. Car insurance payments.\n"
                                   "5. Gas costs.\n"
                                   "6. Maintenance and Repairs.\n"
                                   "7. Car registration fees.\n"
                                   "input: "))
                if choice == 1:
                    total_expenses += CarPayments()
                elif choice == 2:
                    total_expenses += PublicTransport()
                elif choice == 3:
                    total_expenses += TollFees()
                elif choice == 4:
                    total_expenses += CarInsurance()
                elif choice == 5:
                    total_expenses += GasCosts()
                elif choice == 6:
                    total_expenses += MaintenanceCosts()
                elif choice == 7:
                    total_expenses += RegistrationFees()

                else:
                    print("Please enter a valid option (1-7).")
                    continue
            except ValueError:
                print("Please enter a numeric value (1-7).")
                continue

        elif option == "quit":
            print("Goodbye!")
            filename = "transportation_expenses.csv"
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)

                
                writer.writerow(["Car installments"])
                writer.writerow(["Amount"])
                writer.writerows(car_payments)
                writer.writerow([])

                
                writer.writerow(["Public transport"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(public_transport)
                writer.writerow([])

                
                writer.writerow(["Toll fees"])
                writer.writerow(["Amount"])
                writer.writerows(toll_fees)
                writer.writerow([])

                
                writer.writerow(["Car Insurance"])
                writer.writerow(["Plan", "Amount"])
                writer.writerows(car_insurance)
                writer.writerow([])

                
                writer.writerow(["Gas cost"])
                writer.writerow(["Fuel", "Amount"])
                writer.writerows(gas_costs)
                writer.writerow([])

                
                writer.writerow(["Maintenance costs"])
                writer.writerow(["Type", "Amount"])
                writer.writerows(maintenance_costs)
                writer.writerow([])

                
                writer.writerow(["Registration fees"])
                writer.writerow(["Amount"])
                writer.writerows(registration_fees)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
            is_running = False
        else:
            print("Please enter a valid option.")
            continue
    return total_expenses


def CarPayments():
    is_running = True
    while is_running:
        print("Welcome to Car Installment Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                brand = input("What car brand is it?: ").lower()
                if brand == "":
                    print("Please enter a valid brand.")
                    continue
                else:
                    print(f"Your car brand is {brand}.")
                    model = input("What car model is it?: ").lower()
                    if model == "":
                        print("Please enter a valid model.")
                        continue
                    else:
                        print(f"Your car model is {model}.")
                installment = float(
                    input("How much was your car installment?: "))
                if installment > 0:
                    print(f"Your car installment is: R{installment:.2f}")
                    car_payments.append([
                        brand,
                        model,
                        installment

                    ])
                    return installment
                else:
                    print("Your payment cannot be less than or equal to zero.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye")
            is_running = False
        else:
            print("Please enter a valid option 'continue' or 'quit'.")
            continue
    return 0


def PublicTransport():
    is_running = True
    transport = ["Bus", "Taxi", "Train", "E-hailing", "Plane"]
    while is_running:
        print("Welcome to the Public Transport Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                mode = int(input("What mode transport did you use? (1-5)\n"
                                 "1. Bus.\n"
                                 "2. Taxi.\n"
                                 "3. Train.\n"
                                 "4. E-hailing.\n"
                                 "5. Plane.\n"
                                 "input: "))
                if mode == 1:
                    try:
                        bus = transport[0]
                        fair = int(input(f"How much was the {bus} fair?: "))
                        if fair > 0:
                            count = int(
                                input(f"How many times did you us the {bus}"))
                            if count > 0:
                                amount = fair * count
                                public_transport.append([
                                    bus,
                                    fair,
                                    count,
                                    amount,
                                ])
                                return amount
                            else:
                                print(
                                    "Your fair cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Your fair cannot be less than or equal to zero.")
                            continue

                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif mode == 2:
                    try:
                        taxi = transport[1]
                        fair = int(input(f"How much was the {taxi} fair?: "))
                        if fair > 0:
                            count = int(
                                input(f"How many times did you us the {taxi}"))
                            if count > 0:
                                amount = fair * count
                                public_transport.append([
                                    taxi,
                                    fair,
                                    count,
                                    amount,
                                ])
                                return amount
                            else:
                                print(
                                    "Your fair cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Your fair cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif mode == 3:
                    try:
                        train = transport[2]
                        fair = int(input(f"How much was the {train} fair?: "))
                        if fair > 0:
                            count = int(
                                input(f"How many times did you us the {train}"))
                            if count > 0:
                                amount = fair * count
                                public_transport.append([
                                    train,
                                    fair,
                                    count,
                                    amount,
                                ])
                                return amount
                            else:
                                print(
                                    "Your fair cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Your fair cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif mode == 4:
                    try:
                        e_hailing = transport[3]
                        fair = int(
                            input(f"How much was the {e_hailing} fair?: "))
                        if fair > 0:
                            count = int(
                                input(f"How many times did you us the {e_hailing}"))
                            if count > 0:
                                amount = fair * count
                                public_transport.append([
                                    e_hailing,
                                    fair,
                                    count,
                                    amount,
                                ])
                                return amount
                            else:
                                print(
                                    "Your fair cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Your fair cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif mode == 5:
                    try:
                        plane = transport[4]
                        fair = int(input(f"How much was the {plane} fair?: R"))
                        if fair > 0:
                            count = int(
                                input(f"How many times did you us the {plane}"))
                            if count > 0:
                                amount = fair * count
                                public_transport.append([
                                    plane,
                                    fair,
                                    count,
                                    amount,
                                ])
                                return amount
                            else:
                                print(
                                    "Your fair cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Your fair cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a numeric value.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
    return 0


def TollFees():
    is_running = True
    while is_running:
        print("Welcome to the Toll Gate Fees Calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        try:
            if option == "continue":
                price = float(input("How much were you toll gate fees?: R"))
                if price > 0:
                    print(f"Your total fees is : R{price:.2f}")
                    toll_fees.append([price])
                    return price
                else:
                   print("Your total fees cannot be less than or equal to zero.")
                   continue
            elif option == "quit":
                print("Goodbye!")
                is_running = False
            else:
                print("Please enter a valid option. 'continue' or 'quit'")
                continue
        except ValueError:
            print("Please enter a numeric value.")
            continue
    return 0


def CarInsurance():
    insurance = ["Roadside Assistance", "Scratch & Dent, Wheel & Tyre Cover",
                 "Comprehensive Coverage", "Uninsured/Underinsured Motorist Coverage"]
    is_running = True
    while is_running:
        print("Welcome to the Car Insurance Calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                coverage = int(input("Which car insurance would you like to pay?\n"
                                     "1. Roadside Assistance.\n"
                                     "2. Scratch & Dent, Wheel & Tyre Cover.\n"
                                     "3. Comprehensive Coverage.\n"
                                     "4. Uninsured Motorist Coverage.\n"
                                     "input: "))
                if coverage == 1:
                    cover = insurance[0]
                    try:
                        cost = float(input(f"How much was the {cover}: R"))
                        if cost > 0:
                            print(f"Your total cost is : R{cost:.2f}")
                            car_insurance.append([
                                cover,
                                cost
                            ])
                            return cost
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif coverage == 2:
                    cover = insurance[1]
                    try:
                        cost = float(input(f"How much was the {cover}: R"))
                        if cost > 0:
                            print(f"Your total cost is : R{cost:.2f}")
                            car_insurance.append([
                                cover,
                                cost
                            ])
                            return cost
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif coverage == 3:
                    cover = insurance[2]
                    try:
                        cost = float(input(f"How much was the {cover}: R"))
                        if cost > 0:
                            print(f"Your total cost is : R{cost:.2f}")
                            car_insurance.append([
                                cover,
                                cost
                            ])
                            return cost
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif coverage == 4:
                    cover = insurance[3]
                    try:
                        cost = float(input(f"How much was the {cover}: R"))
                        if cost > 0:
                            print(f"Your total cost is : R{cost:.2f}")
                            car_insurance.append([
                                cover,
                                cost
                            ])
                            return cost
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a numeric value.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
            continue
    return 0


def GasCosts():
    is_running = True
    fuel = ["Diesel", "Petrol 93", "Petrol 95"]
    while is_running:
        print("Welcome to the Gas Calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                gas = int(input("Which gas would you like to pay?\n"
                                "1. Diesel\n"
                                "2. Petrol 93\n"
                                "3. Petrol 95\n"
                                "input: "))
                if gas == 1:
                    fuel_range = fuel[0]
                    try:
                        price = float(
                            input(f"How much {fuel_range} did you pour: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {fuel_range} is : R{price:.2f}")
                            gas_costs.append([
                                fuel_range,
                                price
                            ])
                            return price
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif gas == 2:
                    fuel_range = fuel[1]
                    try:
                        price = float(
                            input(f"How much {fuel_range} did you pour: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {fuel_range} is : R{price:.2f}")
                            gas_costs.append([
                                fuel_range,
                                price
                            ])
                            return price
                        else:
                            print("Your total cannot be less than or equal to zero.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif gas == 3:
                    fuel_range = fuel[2]
                    try:
                        price = float(
                            input(f"How much {fuel_range} did you pour: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {fuel_range} is : R{price:.2f}")
                            gas_costs.append([
                                fuel_range,
                                price
                            ])
                            return price
                        else:
                            print("Your total cannot be less than or equal to zero.")
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
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
            continue
    return 0


def MaintenanceCosts():
    repairs = ["Brake Repairs", "Suspension Repairs",
               "Engine Repairs", "Electrical Repairs", "Tyre & Wheel Services"]
    maintenance = ["Oil Change", "Minor Service",
                   "Major Service", "Wheel Alignment", "Tyre Rotation"]
    is_running = True
    while is_running:
        print("Welcome to the Maintenance and Repairs Calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What did you do to your car?\n"
                                   "1.Repairs.\n"
                                   "2.Maintenance.\n"
                                   "input: "))
                if choice == 1:
                    service = int(input("Which repair did you pay? (1-5)\n"
                                        "1. Brake Repairs.\n"
                                        "2. Suspension Repairs.\n"
                                        "3. Engine Repairs.\n"
                                        "4. Electrical Repairs.\n"
                                        "5. Tyre & Wheel Services.\n"
                                        "input: "))
                    try:
                        if service == 1:
                            auto = repairs[0]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 2:
                            auto = repairs[1]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 3:
                            auto = repairs[2]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 4:
                            auto = repairs[3]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 5:
                            auto = repairs[4]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Please enter a valid option. (1-5)")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    service = int(input("Which maintenance did you pay? (1-5)\n"
                                        "1. Oil Change.\n"
                                        "2. Minor Service.\n"
                                        "3. Major Service.\n"
                                        "4. Wheel Alignment.\n"
                                        "5. Tyre & Wheel Services.\n"
                                        "input: "))
                    try:
                        if service == 1:
                            auto = maintenance[0]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 2:
                            auto = maintenance[1]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 3:
                            auto = maintenance[2]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 4:
                            auto = maintenance[3]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        elif service == 5:
                            auto = maintenance[4]
                            fees = float(input(f"How much was {auto}?\n"))
                            if fees > 0:
                                print(
                                    f"Your total cost for {auto} is : R{fees:.2f}")
                                maintenance_costs.append([
                                    auto,
                                    fees
                                ])
                                return fees
                            else:
                                print(
                                    "Your total cannot be less than or equal to zero.")
                                continue
                        else:
                            print("Please enter a valid option. (1-5)")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a valid option. (1-2)")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
            continue
    return 0


def RegistrationFees():
    is_running = True
    while is_running:
        print("Welcome to the Registration Fees Calculator.")
        option = input("Would you like to continue or quit: ").lower()
        if option == "continue":
            try:
                fees = float(input(f"How much was the registration fees?: R"))
                if fees > 0:
                    print(f"Your total cost for registration is : R{fees:.2f}")
                    registration_fees.append([fees])
                    return fees
                else:
                    print("Your total cannot be less than or equal to zero.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter a valid option. 'continue' or 'quit'")
            continue
    return 0
