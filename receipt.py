from colorama import Fore

class Receipt:
    def print_receipt(self, name, age, address, email, payment_amount_cash, payment_amount_loan, payment_mode, selected_bike, bike_price, year_of_sale):
        print(Fore.GREEN + "Receipt:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Address: {address}")
        print(f"Email: {email}")
        print(f"Cash Payment: {payment_amount_cash}")
        print(f"Loan Payment: {payment_amount_loan}")
        print(f"Payment Mode: {payment_mode}")
        print(f"Bike: {selected_bike[0]}")
        print(f"Price: {bike_price}")
        print(f"Year of Sale: {year_of_sale}")
        print("Thank you for your purchase!" + Fore.RESET)
