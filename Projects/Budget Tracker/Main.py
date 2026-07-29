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
import traceback

total_expenses = 0
salary = 0
is_running = True

def Payslip():
    while True:
        try:
            income = float(input("Please enter your monthly income: R"))
            if income > 0:
                return income
            else:
                print("Your income cannot be less than or equal to 0")
        except ValueError:
            print("Please enter a numeric value for your income.")

try:
    while is_running:
        print("Welcome to the Budget Tracker!")
        try:
            choice = int(input("Enter your choice (1-12)\n"
                               "1. Salary/Payslip. \n"
                               "2. Living Expenses. \n"
                               "3. Transportation Expenses. \n"
                               "4. Family Care. \n"
                               "5. Personal Care. \n"
                               "6. Health Care. \n"
                               "7. Technology expenses. \n"
                               "8. Debt Payments. \n"
                               "9. Savings & Investments. \n"
                               "10. Entertainment expenses. \n"
                               "11. Miscellaneous expenses. \n"
                               "12. Quit.\n"
                               "choice (1-12): "))
            if choice == 1:
                salary += Payslip()
            elif choice == 2:
                total_expenses += LE.Expenses()
            elif choice == 3:
                total_expenses += TE.Transportation()
            elif choice == 4:
                total_expenses += FC.FamCare()
            elif choice == 5:
                total_expenses += PC.SelfCare()
            elif choice == 6:
                total_expenses += HC.Medical()
            elif choice == 7:
                total_expenses += T.TechServices()
            elif choice == 8:
                total_expenses += DP.Debits()
            elif choice == 9:
                total_expenses += SAI.Funding()
            elif choice == 10:
                total_expenses += EE.Entertain()
            elif choice == 11:
                total_expenses += ME.Misc()
            elif choice == 12:
                is_running = False
            else:
                print("Invalid Choice.\nChoose 1-12")
                continue
        except ValueError:
            print("Please enter a numeric value")
            continue
    print("Thank you for using Budget Tracker")
    print(f"Total expenses: R{total_expenses:.2f}")
    print(f"Total income: R{salary:.2f}")
    print(f"Remaining: R{salary - total_expenses:.2f}")
except Exception as e:
    print("=" * 60)
    print("An unexpected error occurred:")
    traceback.print_exc()
    print("=" * 60)