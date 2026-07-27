ordering_costs = []
movie_tickets = []
event_tickets = []
recreational_activities = []
vacation_funds = []

def Entertain():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome To ther Entertainment expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What would youy like to calculate?\n" 
                "1. Ordering and Dining costs.\n" 
                "2. Movie expenses.\n" 
                "3. Events/Concerts.\n" 
                "4. Recreational activities or hobbies.\n" 
                "5. Vacation or Trips"
                "choose an option (1-5): "))
                if choice == 1:
                    total_expenses += OrderingAndDining()
                elif choice ==2:
                    total_expenses += MovieAndRental()
                elif choice ==3:
                    total_expenses += EventAndConcert()
                elif choice ==4:
                    total_expenses =+ RecreationalAndHobbies()
                elif choice ==5:
                    total_expenses += VacationAndTravel()
                else:
                    print("Invalid choice. Please choose between 1-5.")
                    continue
            except ValueError:
                print("Please enter a numeric value.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses

def OrderingAndDining():
    pass


def MovieAndRental():
    pass


def EventAndConcert():
    pass


def RecreationalAndHobbies():
    pass


def VacationAndTravel():
    pass