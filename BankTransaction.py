is_running = True
balance = 0



def show_balance():
    print(f"You have R{balance} Balance")


def deposit():
    deposit = input("How much do you want to deposit: ")
    if deposit.isdigit():
        deposit = int(deposit)
        if deposit < 0:
            print("Deposit cannot be negative")
            return 0
        else:
            print(f"You have deposited R{deposit:.2f}")
            return deposit


def withdraw():
    amount = input("How much do you want to withdraw: ")
    if amount.isdigit():
        amount = float(amount)
        if amount < 0:
            print("Withdraw cannot be negative")
            return 0
        elif amount > balance:
            print("Withdraw cannot be greater than balance")
            return 0
        else:
            print(f"You have withdrew R{amount:.2f}")
            print(f"You available balance is R{balance -+ amount:.2f}")
            return amount


while is_running:
    print("Welcome to Bank Transaction")
    print("1. Show available balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = input("What do you want to do: ")

    if option == "1":
        show_balance()
    if option == "2":
        balance += deposit()
    if option == "3":
        balance -= withdraw()
    if option == "4":
        is_running = False
        print("Thank you for your time!")