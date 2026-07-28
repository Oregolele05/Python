ordering_costs = []
movie_tickets = []
event_tickets = []
recreational_hobby = []
travelling = []

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
                "5. Vacation or Trips."
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
    foods_type = ["Restaurant", "Fast food"]
    is_running = True
    while is_running:
        print("Welcome to the Ordering and Dining Expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which did you spend on?\n"
                                   "1. Restaurant.\n"
                                   "2. Fast food.\n"
                                   "choose an option (1-2): " ))
                if choice == 1:
                    food = foods_type[0]
                    try:
                        price = float(input(f"How much did you spend on {food}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {food}.")
                            ordering_costs.append([
                                food,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {food}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    food = foods_type[1]
                    try:
                        price = float(input(f"How much did you spend on {food}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {food}.")
                            ordering_costs.append([
                                food,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {food}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter 1 or 2.")
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
    return 0


def MovieAndRental():
    variety = ["movie tickets", "Movie rental"]
    is_running = True
    while is_running:
        print("Welcome to the Movie tickets and Rental Expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which did you spend on?\n"
                                   "1. Movie tickets.\n"
                                   "2. Movie Rental.\n"
                                   "choose an option (1-2): "))
                if choice == 1:
                    film = variety[0]
                    try:
                        price = float(input(f"How much did you spend on {film}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {film}.")
                            movie_tickets.append([
                                film,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {film}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    film = variety[1]
                    try:
                        price = float(input(f"How much did you spend on {film}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {film}.")
                            movie_tickets.append([
                                film,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {film}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter 1 or 2.")
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
    return 0

def EventAndConcert():
    outdoor = ["Event", "Festival", "Concert"]
    is_running = True
    while is_running:
        print("Welcome to the Event, Convert and Festival Expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which did you spend on?\n"
                                   "1. Event.\n"
                                   "2. Festival.\n"
                                   "3. Concert.\n"
                                   "choose an option (1-2): "))
                if choice == 1:
                    gig = outdoor[0]
                    try:
                        price = float(input(f"How much did you spend on {gig}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {gig}.")
                            event_tickets.append([
                                gig,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {gig}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    gig = outdoor[1]
                    try:
                        price = float(input(f"How much did you spend on {gig}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {gig}.")
                            event_tickets.append([
                                gig,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {gig}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    gig = outdoor[2]
                    try:
                        price = float(input(f"How much did you spend on {gig}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {gig}.")
                            event_tickets.append([
                                gig,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {gig}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter 1 or 2.")
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
    return 0


def RecreationalAndHobbies():
    variety = ["Recreational activities", "Hobbies"]
    is_running = True
    while is_running:
        print("Welcome to the Recreational activity and Hobby Expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which did you spend on?\n"
                                   "1. Recreational activity.\n"
                                   "2. Hobby.\n"
                                   "choose an option (1-2): "))
                if choice == 1:
                    act = variety[0]
                    try:
                        price = float(input(f"How much did you spend on {act}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {act}.")
                            recreational_hobby.append([
                                act,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {act}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    act = variety[1]
                    try:
                        price = float(input(f"How much did you spend on {act}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {act}.")
                            recreational_hobby.append([
                                act,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {act}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter 1 or 2.")
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
    return 0

def VacationAndTravel():
    variety = ["Vacation", "Traveling"]
    is_running = True
    while is_running:
        print("Welcome to the Vacation and Trip Expenses calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which did you spend on?\n"
                                   "1. Vacation.\n"
                                   "2. Trip.\n"
                                   "choose an option (1-2): "))
                if choice == 1:
                    road = variety[0]
                    try:
                        price = float(input(f"How much did you spend on {road}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {road}.")
                            travelling.append([
                                road,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {road}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    road = variety[1]
                    try:
                        price = float(input(f"How much did you spend on {road}?\n"))
                        if price > 0:
                            print(f"You spent R{price:.2f} on {road}.")
                            travelling.append([
                                road,
                                price
                            ])
                            return price
                        else:
                            print(f"You cannot spend R{price:.2f} on {road}.")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter 1 or 2.")
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
    return 0
