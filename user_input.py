from colorama import Fore
from bikes_and_banks import RoyalEnfieldShowroom

class UserInput:
    def get_user_input(self):
        showroom = RoyalEnfieldShowroom()
        print(f"{Fore.GREEN}{'-'*20}Welcome to Royal Enfield Showroom!{'-'*20}{Fore.RESET}")
        want_bike = input("\n\nWelcome to Royal Enfield Showroom! Do you want to buy a bike? (yes/no): ")
        if want_bike.lower() != 'yes':
            print("Thanks for visiting!")
            return

        print("Choose a bike:")
        for key, value in showroom.bikes.items():
            print(f"{key}: {value[0]} - Price: {value[1]}")

        bike_choice = int(input("Enter the number corresponding to the bike you want: "))
        selected_bike = showroom.bikes.get(bike_choice)
        if not selected_bike:
            print("Invalid choice!")
            return

        print(f"Please fill this form to confirm the order of your {selected_bike[0]}:")
        name = input("Name: ")
        age = int(input("Age: "))
        if age < 21:
            print("Underage to buy a bike")
            return

        address = input("Address: ")
        email = input("Email Address: ")
        financial_proof = input("Financial Proof (e.g., bank statement, salary slip): ")

        bike_price = selected_bike[1]
        want_loan = input("Do you want a loan? (yes/no): ")

        user_input_data = {
            "bike_price": bike_price,
            "selected_bike": selected_bike,
            "name": name,
            "age": age,
            "address": address,
            "email": email,
            "financial_proof": financial_proof,
            "want_loan": want_loan
        }

        return user_input_data
