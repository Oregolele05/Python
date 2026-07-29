import csv
device_cost = []
internet_plan = []
computer_payments = []
streaming_payments = []
gaming_subscriptions = []
tech_parts = []


def TechServices():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the Technology Expenses Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Great! What would you like to do?\n"
                                   "1. Smart phone or devices.\n"
                                   "2. Internet services.\n"
                                   "3. Computer components.\n"
                                   "4. Streaming services.\n"
                                   "5. Gaming subscriptions.\n"
                                   "6. Tech accessories.\n"
                                   "choice (1-6): "))
                if choice == 1:
                    total_expenses += SmartphoneAndDevices()
                elif choice == 2:
                    total_expenses += InternetServices()
                elif choice == 3:
                    total_expenses += ComputerComponents()
                elif choice == 4:
                    total_expenses += StreamingServices()
                elif choice == 5:
                    total_expenses += GamingSubscriptions()
                elif choice == 6:
                    total_expenses += TechAccessories()
                else:
                    print("Please pick a number (1-6)")
                    continue
            except ValueError:
                print("Please enter a valid choice.")
                continue

        elif option == "quit":
            print("Goodbye!")
            filename = "technology_expenses.csv"
            with open(filename, 'w', newline=' ') as file:
                writer = csv.writer(file)

                writer.writerow(["Electronic device costs"])
                writer.writerow(["Electronic", "Amount"])
                writer.writerow(device_cost)
                writer.writerow([])

                writer.writerow(["Internet services"])
                writer.writerow(["Plan", "Amount"])
                writer.writerow(internet_plan)
                writer.writerow([])

                writer.writerow(["Computer components"])
                writer.writerow(["Component", "Amount"])
                writer.writerow(computer_payments)
                writer.writerow([])

                writer.writerow(["Streaming services"])
                writer.writerow(["Platform", "Amount"])
                writer.writerow(streaming_payments)
                writer.writerow([])

                writer.writerow(["Gaming subscriptions"])
                writer.writerow(["Plan", "Amount"])
                writer.writerow(gaming_subscriptions)
                writer.writerow([])

                writer.writerow(["Tech accessories"])
                writer.writerow(["Type", "Amount"])
                writer.writerow(tech_parts)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return total_expenses


def SmartphoneAndDevices():
    electronics = ["Cellphone", "TV, Audio & Media",
                   "Smart Home", "Laptop", "Wearable Tech"]
    is_running = True
    while is_running:
        print("Welcome to the Smartphone and Devices Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("What type of device did your purchase or pay?\n"
                                   "1. Cellphone\n"
                                   "2. TV, Audio & Media\n"
                                   "3. Smart Home\n"
                                   "4. Laptop\n"
                                   "5. Wearable Tech\n"
                                   "choice (1-5): "))
                if choice == 1:
                    elec = electronics[0]
                    try:
                        price = float(
                            input(f"How much did you pay for {elec}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {elec} is R{price:.2f}")
                            device_cost.append([
                                elec,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {elec} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    elec = electronics[1]
                    try:
                        price = float(
                            input(f"How much did you pay for {elec}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {elec} is R{price:.2f}")
                            device_cost.append([
                                elec,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {elec} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    elec = electronics[2]
                    try:
                        price = float(
                            input(f"How much did you pay for {elec}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {elec} is R{price:.2f}")
                            device_cost.append([
                                elec,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {elec} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 4:
                    elec = electronics[3]
                    try:
                        price = float(
                            input(f"How much did you pay for {elec}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {elec} is R{price:.2f}")
                            device_cost.append([
                                elec,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {elec} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 5:
                    elec = electronics[4]
                    try:
                        price = float(
                            input(f"How much did you pay for {elec}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {elec} is R{price:.2f}")
                            device_cost.append([
                                elec,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {elec} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between (1-5)")
                    continue

            except ValueError:
                print("Please enter a valid choice.")
                continue
        elif option == "quit":
            print("Goodbye!")
            is_running = False
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def InternetServices():
    plan = ["Data sim", "Wi-Fi"]
    is_running = True
    while is_running:
        print("Welcome to the Internet Services Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which one did you pay for?\n"
                                   "1. Data sim. \n"
                                   "2. Wi-fi.\n"
                                   "choice (1-2): "))
                if choice == 1:
                    internet = plan[0]
                    try:
                        price = float(
                            input(f"How much do you pay for {internet}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {internet} is R{price:.2f}")
                            internet_plan.append([
                                internet,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {internet} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    internet = plan[1]
                    try:
                        price = float(
                            input(f"How much do you pay for {internet}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {internet} is R{price:.2f}")
                            internet_plan.append([
                                internet,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {internet} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1 and 2")
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


def ComputerComponents():
    comp = ["Central processing unit (CPU)", "Memory (RAM)", "Storage Devices", "Motherboards",
            "Power supply unit (PSU)", "Cooling system", "Graphics processing unit (GPU)"]
    is_running = True
    while is_running:
        print("Welcome to the Computer Components Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which one did you pay for?\n"
                                   "1. Central processing unit (CPU).\n"
                                   "2. Memory (RAM).\n"
                                   "3. Storage Devices.\n"
                                   "4. Motherboards.\n"
                                   "5. Power supply unit (PSU).\n"
                                   "6. Cooling system.\n"
                                   "7. Graphics processing unit (GPU).\n"
                                   "choice (1-7): "))
                if choice == 1:
                    parts = comp[0]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    parts = comp[1]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    parts = comp[2]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 4:
                    parts = comp[3]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 5:
                    parts = comp[4]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 6:
                    parts = comp[5]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 7:
                    parts = comp[6]
                    try:
                        price = float(
                            input(f"How much do you pay for {parts}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {parts} is R{price:.2f}")
                            computer_payments.append([
                                parts,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {parts} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1-7")
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


def StreamingServices():
    streaming = ["Netflix", "Amazon Prime Video", "Disney+", "Showmax", "DStv"]
    is_running = True
    while is_running:
        print("Welcome to the Streaming Services Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which streaming service did you pay for?\n"
                                   "1. Netflix.\n"
                                   "2. Amazon Prime Video.\n"
                                   "3. Disney+\n"
                                   "4. Showmax.\n"
                                   "5. DStv.\n"
                                   "choice (1-5): "))
                if choice == 1:
                    stream = streaming[0]
                    try:
                        price = float(
                            input(f"How much do you pay for {stream}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {stream} is R{price:.2f}")
                            streaming_payments.append([
                                stream,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {stream} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    stream = streaming[1]
                    try:
                        price = float(
                            input(f"How much do you pay for {stream}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {stream} is R{price:.2f}")
                            streaming_payments.append([
                                stream,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {stream} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    stream = streaming[2]
                    try:
                        price = float(
                            input(f"How much do you pay for {stream}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {stream} is R{price:.2f}")
                            streaming_payments.append([
                                stream,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {stream} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 4:
                    stream = streaming[3]
                    try:
                        price = float(
                            input(f"How much do you pay for {stream}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {stream} is R{price:.2f}")
                            streaming_payments.append([
                                stream,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {stream} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 5:
                    stream = streaming[4]
                    try:
                        price = float(
                            input(f"How much do you pay for {stream}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {stream} is R{price:.2f}")
                            streaming_payments.append([
                                stream,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {stream} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please enter a choice between 1-5.")
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


def GamingSubscriptions():
    premiums = ["Xbox Game Pass",
                "Playstation Game Pass", "Nintendo Switch Online"]
    is_running = True
    while is_running:
        print("Welcome to the Gaming Subscriptions Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which subscription did you pay for?\n"
                                   "1. Xbox Game Pass\n"
                                   "2. Playstation Game Pass\n"
                                   "3. Nintendo Switch Online\n"
                                   "choice (1-3): "))
                if choice == 1:
                    subs = premiums[0]
                    try:
                        price = float(
                            input(f"How much do you pay for {subs}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {subs} is R{price:.2f}")
                            gaming_subscriptions.append([
                                subs,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {subs} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    subs = premiums[1]
                    try:
                        price = float(
                            input(f"How much do you pay for {subs}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {subs} is R{price:.2f}")
                            gaming_subscriptions.append([
                                subs,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {subs} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    subs = premiums[2]
                    try:
                        price = float(
                            input(f"How much do you pay for {subs}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {subs} is R{price:.2f}")
                            gaming_subscriptions.append([
                                subs,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {subs} cannot be R{price:.2f}")
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
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def TechAccessories():
    accessoriess = ["Mobile accessories",
                    "Gaming accessories", "Computer & Laptop accessories"]
    is_running = True
    while is_running:
        print("Welcome to the Tech assessories and Upgrades Calculator!")
        option = input("Would you like to continue or quit?: ").lower()
        if option == "continue":
            try:
                choice = int(input("Which accessory did you buy?\n"
                                   "1. Mobile accessories.\n"
                                   "2. Gaming accessories.\n"
                                   "3. Computer & Laptop accessories.\n"
                                   "choice (1-3): "))
                if choice == 1:
                    tech = accessoriess[0]
                    try:
                        price = float(
                            input(f"How much do you pay for {tech}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {tech} is R{price:.2f}")
                            tech_parts.append([
                                tech,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {tech} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 2:
                    tech = accessoriess[1]
                    try:
                        price = float(
                            input(f"How much do you pay for {tech}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {tech} is R{price:.2f}")
                            tech_parts.append([
                                tech,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {tech} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                elif choice == 3:
                    tech = accessoriess[2]
                    try:
                        price = float(
                            input(f"How much do you pay for {tech}?: R"))
                        if price > 0:
                            print(
                                f"Your total cost for {tech} is R{price:.2f}")
                            tech_parts.append([
                                tech,
                                price
                            ])
                            return price
                        else:
                            print(
                                f"Your total cost for {tech} cannot be R{price:.2f}")
                            continue
                    except ValueError:
                        print("Please enter a numeric value.")
                        continue
                else:
                    print("Please choose between 1-3")
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
