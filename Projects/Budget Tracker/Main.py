import LivingExpenses as LE, TransportationExpenses as TE, FamilyCare as FC, PersonalCare as PC, HealthCare as HC
import Technology as T, DebtPayments as DP, SavingsAndInvestments as SAI, Entertainment as E, Miscellaneous as M
total_expenses = 0
is_running = True

while is_running:
    try:
        choice = int(input("Enter your choice (1-11): "))
        if choice == 1:
            total_expenses += LE.Expenses()
        elif choice == 2:
            total_expenses += TE.Transportation()
        elif choice == 3:
            total_expenses += FC.FamCare()
        elif choice == 4:
            total_expenses += PC.SelfCare()
        elif choice == 5:
            total_expenses += HC.Medical()
        elif choice == 6:
            total_expenses += T.TechServices()
        elif choice == 7:
            total_expenses += DP.Debits()
        elif choice == 8:
            total_expenses += SAI.Funding()
        elif choice == 9:
            total_expenses += E.Entertain()
        elif choice == 10:
            total_expenses += M.Misc()
        elif choice == 11:
            is_running = False
        else:
            print("Invalid Choice.\nChoose 1-10")
            continue
    except ValueError:
        print("Invalid Choice.\nChoose 1-10")
        continue
print("Thank you for using Budget Tracker")
print(f"Total expenses: R{total_expenses:.2f}")