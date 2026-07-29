import csv
prescription_meds = []
prepaid_meds = []
doctor_visits = []
specialist_visit = []
memberships = []


def Medical():
    total_expenses = 0
    is_running = True
    while is_running:
        print("Welcome to the Health Care Calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                choice = int(input("Would you like to do?\n"
                                   "1. Prescription Meds\n"
                                   "2. Prepaid Meds\n"
                                   "3. Doctor Visits\n"
                                   "4. Specialist Visits\n"
                                   "5. Memberships\n"
                                   "choice"))
                if choice == 1:
                    total_expenses += PrescriptionMeds()
                elif choice == 2:
                    total_expenses += PrepaidMeds()
                elif choice == 3:
                    total_expenses += DoctorVisits()
                elif choice == 4:
                    total_expenses += SpecialistVisits()
                elif choice == 5:
                    total_expenses += Memberships()
                else:
                    print("Please enter a valid choice (1-5).")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
            filename = "health_expenses.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                
                writer.writerow(["Prescription medication costs"])
                writer.writerow(["Amount"])
                writer.writerows(prescription_meds)
                writer.writerow([])

                writer.writerow(["Over the counter medication costs"])
                writer.writerow(["Amount"])
                writer.writerows(prepaid_meds)
                writer.writerow([])

                writer.writerow(["Doctor visits"])
                writer.writerow(["Amount"])
                writer.writerows(doctor_visits)
                writer.writerow([])

                writer.writerow(["Specialist visit"])
                writer.writerow(["Amount"])
                writer.writerows(specialist_visit)
                writer.writerow([])

                writer.writerow(["Medical aid"])
                writer.writerow(["Amount"])
                writer.writerows(memberships)
                writer.writerow([])

                writer.writerow(["Total Expenses", total_expenses])
        else:
            print("Please enter either 'continue' or 'quit'")
            continue
    return total_expenses


def PrescriptionMeds():
    is_running = True
    while is_running:
        print("Welcome to prescription meds calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                price = float(input("Please enter your prescription price: "))
                if price > 0:
                    print(f"Your prescription price is R{price:.2f}")
                    prescription_meds.append([price])
                    return price
                elif price == 0:
                    print("Your medical aid paid for your prescription!")
                    prescription_meds.append([price])
                    return price
                else:
                    print(f"Your prescription price cannot be R{price:.2f}")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def PrepaidMeds():
    is_running = True
    while is_running:
        print("Welcome to prepaid meds calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                price = float(input("Please enter your prepaid price: "))
                if price > 0:
                    print(f"Your prepaid price is R{price:.2f}")
                    prepaid_meds.append([price])
                    return price
                elif price == 0:
                    print("Your medical aid paid for your medication!")
                    prepaid_meds.append([price])
                    return price
                else:
                    print(f"Your prepaid price cannot be R{price:.2f}")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def DoctorVisits():
    is_running = True
    while is_running:
        print("Welcome to Doctor visit calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                price = float(input("Please enter your visit cost: "))
                if price > 0:
                    print(f"Your visit price is R{price:.2f}")
                    doctor_visits.append([price])
                    return price
                elif price == 0:
                    print("Your medical aid paid for your visit!")
                    doctor_visits.append([price])
                    return price
                else:
                    print(f"Your visit cannot be R{price:.2f}")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def SpecialistVisits():
    is_running = True
    while is_running:
        print("Welcome to specialist visit calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                price = float(input("Please enter your visit price: "))
                if price > 0:
                    print(f"Your visit price is R{price:.2f}")
                    specialist_visit.append([price])
                    return price
                elif price == 0:
                    print("Your medical aid paid for your visit!")
                    specialist_visit.append([price])
                    return price
                else:
                    print(f"Your visit price cannot be R{price:.2f}")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0


def Memberships():
    is_running = True
    while is_running:
        print("Welcome to medical aid calculator!")
        option = input("Would you like to continue or quit").lower()
        if option == "continue":
            try:
                price = float(input("Please enter your membership price: "))
                if price > 0:
                    print("Your membership price is R{price:.2f}")
                    memberships.append([price])
                    return price
                else:
                    print(f"Your membership cannot be R{price:.2f}")
                    continue
            except ValueError:
                print("Please enter a numeric value")
                continue
        elif option == "quit":
            is_running = False
            print("Thank you for your time")
        else:
            print("Please enter either 'continue' or 'quit'.")
            continue
    return 0
