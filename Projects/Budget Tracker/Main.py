import LivingExpenses as LE
import TransportationExpenses as TE
import FamilyCare as FC
import PersonalCare as PC
import HealthCare as HC
import TechnologyExpenses as T
import DebtPayments as DP
import SavingsAndInvestments as SAI
import EntertainmentExpenses as EE
import MiscellaneousExpenses as ME


total_expenses = 0
is_running = True

while is_running:
    try:
        choice = int(input("Enter your choice (1-11)\n"
                           "1. Living Expenses. \n"
                           "2. Transportation Expenses. \n"
                           "3. Family Care. \n"
                           "4. Personal Care. \n"
                           "5. Health Care. \n"
                           "6. Technology expenses. \n"
                           "7. Debt Payments. \n"
                           "8. Savings & Investments. \n"
                           "9. Entertainment expenses. \n"
                           "10. Miscellaneous expenses. \n"
                           "11. Quit.\n"
                           "choice (1-11): "))
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
            total_expenses += EE.Entertain()
        elif choice == 10:
            total_expenses += ME.Misc()
        elif choice == 11:
            is_running = False
        else:
            print("Invalid Choice.\nChoose 1-11")
            continue
    except ValueError:
        print("Invalid Choice.\nChoose 1-11")
        continue
print("Thank you for using Budget Tracker")
print(f"Total expenses: R{total_expenses:.2f}")
