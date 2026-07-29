import csv
emergency_fund = []
retirement_fund = []
investment_contributions = []
education_fund = []
financial_goals = []


def Funding():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the savings and investments calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would you like to do?\n"
                                   "1. Emergency fund.\n"
                                   "2. Retirement fund.\n"
                                   "3. Investment contributions.\n"
                                   "4. Education fund.\n"
                                   "5. Financial goals.\n"
                                   "choice (1-5)"))
                if choice == 1:
                    total_expenses += EmergencyFund()
                elif choice == 2:
                    total_expenses += RetirementFund()
                elif choice == 3:
                    total_expenses += InvestmentContributions()
                elif choice == 4:
                    total_expenses += EducationFund()
                elif choice == 5:
                    total_expenses += FinancialGoals()
                else:
                    print("Invalid choice. Please choose from 1-5.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            is_running = False
            print("Goodbye!")
            filename = "savings_and_investments.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # child expenses
                writer.writerow(["Emergency fund"])
                writer.writerow(["Amount"])
                writer.writerows(emergency_fund)
                writer.writerow([])

                writer.writerow(["Retirement fund"])
                writer.writerow(["Amount"])
                writer.writerows(retirement_fund)
                writer.writerow([])

                writer.writerow(["Investment portfolio"])
                writer.writerow(["Amount"])
                writer.writerows(investment_contributions)
                writer.writerow([])

                writer.writerow(["Education fund"])
                writer.writerow(["Amount"])
                writer.writerows(education_fund)
                writer.writerow([])

                writer.writerow(["Financial goals"])
                writer.writerow(["Amount"])
                writer.writerows(financial_goals)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses


def EmergencyFund():
    is_running = True
    while is_running:
        print("Welcome to the Emergency fund calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you contribute?: R"))
                if price > 0:
                    print(
                        f"You have contributed R{price:.2f} towards Emergency fund.")
                    emergency_fund.append([price])
                    return price
                else:
                    print(
                        f"You cannot contribute R{price:.2f} to Emergency fund.")
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


def RetirementFund():
    is_running = True
    while is_running:
        print("Welcome to the Retirement fund calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you contribute?: R"))
                if price > 0:
                    print(
                        f"You have contributed R{price:.2f} towards Retirement fund.")
                    retirement_fund.append([price])
                    return price
                else:
                    print(
                        f"You cannot contribute R{price:.2f} to Retirement fund.")
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


def InvestmentContributions():
    is_running = True
    while is_running:
        print("Welcome to the Investments calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you contribute?: R"))
                if price > 0:
                    print(
                        f"You have contributed R{price:.2f} towards investments.")
                    investment_contributions.append([price])
                    return price
                else:
                    print(
                        f"You cannot contribute R{price:.2f} towards investments.")
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


def EducationFund():
    is_running = True
    while is_running:
        print("Welcome to the Education fund calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you contribute?: R"))
                if price > 0:
                    print(
                        f"You have contributed R{price:.2f} towards Education fund.")
                    education_fund.append([price])
                    return price
                else:
                    print(
                        f"You cannot contribute R{price:.2f} to Education fund.")
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


def FinancialGoals():
    is_running = True
    while is_running:
        print("Welcome to the Financial goals calculator.")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                price = float(input("How much did you contribute?: R"))
                if price > 0:
                    print(
                        f"You have contributed R{price:.2f} towards financial goals.")
                    financial_goals.append([price])
                    return price
                else:
                    print(
                        f"You cannot contribute R{price:.2f} to financial goals.")
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
