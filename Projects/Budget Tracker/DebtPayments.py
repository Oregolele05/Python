import csv
credit_card = []
student_loan = []
personal_loan = []
medical_debt = []

def Debits():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the Debt payments calculator")
        choice = input("Would you like to continue or quit?").lower()
        if choice == "continue":
            try:
                option = int(input("Would you like to pay off?\n"
                                   "1. Credit card.\n"
                                   "2. Student Loan.\n"
                                   "3. Personal Loan.\n"
                                   "4. Medical Debt.\n"
                                   "choice (1-4): "))
                if option == 1:
                    total_expenses += CreditPayments()
                elif option == 2:
                    total_expenses += StudentLoan()
                elif option == 3:
                    total_expenses += PersonalLoan()
                elif option == 4:
                    total_expenses += MedicalDebt()
                else:
                    print("Please choose between 1-4.")

            except ValueError:
                print("Please enter a numeric value")
                continue
        elif choice == "quit":
            is_running = False
            print("Thank you for your time!")
            filename = "debt_payments.csv"
            with open(filename, 'w', newline=' ') as file:
                writer = csv.writer(file)

                #Credit card payments
                writer.writerow(["Credit card payment"])
                writer.writerow(["Amount"])
                writer.writerow(credit_card)
                writer.writerow([])

                #student loan paymemts
                writer.writerow(["Student loan payments"])
                writer.writerow(["Amount"])
                writer.writerow(student_loan)
                writer.writerow([])

                #personal loan payments
                writer.writerow(["Personal loan payments"])
                writer.writerow(["Amount"])
                writer.writerow(personal_loan)
                writer.writerow([])

                #medical debts payment
                writer.writerow(["Medical debt payments"])
                writer.writerow(["Amount"])
                writer.writerow(medical_debt)
                writer.writerow([])
                
                writer.writerow(["Total Expenses", total_expenses])

        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return total_expenses

def CreditPayments():
    is_running = True
    while is_running:
        print("Welcome to the Credit card payments calculator")
        option = input("Would you like to continue or quit?").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay off?: R"))
                if price > 0:
                    print(f"You payed off R{price:.2f}")
                    credit_card.append([price])
                    return price
                else:
                    print(f"You cannot have payed R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def StudentLoan():
    is_running = True
    while is_running:
        print("Welcome to the Student loan payments calculator")
        option = input("Would you like to continue or quit?").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay off?: R"))
                if price > 0:
                    print(f"You payed off R{price:.2f}")
                    student_loan.append([price])
                    return price
                else:
                    print(f"You cannot have payed R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0

def PersonalLoan():
    is_running = True
    while is_running:
        print("Welcome to the Personal loan payments calculator")
        option = input("Would you like to continue or quit?").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay off?: R"))
                if price > 0:
                    print(f"You payed off R{price:.2f}")
                    personal_loan.append([price])
                    return price
                else:
                    print(f"You cannot have payed R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def MedicalDebt():
    is_running = True
    while is_running:
        print("Welcome to the Medical debts payments calculator")
        option = input("Would you like to continue or quit?").lower()
        if option == "continue":
            try:
                price = float(input("How much did you pay off?: R"))
                if price > 0:
                    print(f"You payed off R{price:.2f}")
                    medical_debt.append([price])
                    return price
                else:
                    print(f"You cannot have payed R{price:.2f}.")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time!")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0
