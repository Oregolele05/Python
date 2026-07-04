def expenses():
    cost = 0
    while True:
        print("1. Utilities.\n"
              "2. Rent.\n"
              "3. Insurance.\n"
              "4. Exit.")
        expense = input("Which expense would you like: ")
        if expense == "1":
            cost = float(input("How much are your utilities: "))
            return cost
        elif expense == "2":
            cost =  float(input("How much is your rent: "))
            return cost
        elif expense == "3":
            cost = float(input("How much is your insurance: "))
            return cost
        elif expense == "4":
            print(f"Total expenses: R{cost}")
            return cost
        else:
            print("Please enter a valid option")


def budget():
    allocation = input("Enter your budget allocation: ")
    if allocation.isdigit():
        allocation = float(allocation)
        if allocation < 0:
            print("Please enter a positive number")
            return 0
        else:
            budgetAllocation = allocation
            return budgetAllocation
    else:
        print("Please enter a valid budget allocation")
        return 0

def balance():
    print(f"Your current balance is {budgetAllocation}")


budgetAllocation = 0
is_running = True

while is_running:
    print("1. Add Budget. \n"
          "2. Add expenses.\n"
          "3. View Balance")
    option = input("What would you like to do: ")
    if option == "1":
        budgetAllocation += budget()
    elif option == "2":
        budgetAllocation -= expenses()
    elif option == "3":
        balance()

