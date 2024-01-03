# from colorama import Fore
# from bikes_and_banks import RoyalEnfieldShowroom

# class LoanProcess:
#     def process_loan(self, bike_price, selected_bike, name, age, address, email, financial_proof, want_loan):
#         showroom = RoyalEnfieldShowroom()
#         payment_mode = ""
#         payment_amount_cash = 0
#         payment_amount_loan = 0
        
#         if want_loan.lower() == 'yes':
#             print("Choose a bank for a loan:")
#             for bank, interest_rate in showroom.banks.items():
#                 print(f"{bank} - Interest Rate: {interest_rate}%")

#             loan_bank = input("Enter the bank name for a loan: ").upper()
#             interest_rate = showroom.banks.get(loan_bank)
#             if not interest_rate:
#                 print("Invalid bank choice!")
#                 return None

#             loan_amount = int(input("Enter the loan amount: "))
#             if loan_amount >= bike_price:
#                 print("Loan amount should be less than the bike price.")
#                 return None

#             total_loan_amount = loan_amount + (loan_amount * (interest_rate / 100))
#             payment_amount_cash = bike_price - total_loan_amount
#             payment_amount_loan = total_loan_amount

#             print("Loan approved by the bank!")
#             payment_mode = f"Loan (Bank: {loan_bank}, Amount: {total_loan_amount})"
#         else:
#             payment_mode = "Cash"
#             payment_amount_cash = int(input("Enter the amount paid (in cash): "))
#             if payment_amount_cash < bike_price:
#                 remaining_amount = bike_price - payment_amount_cash
#                 print(f"The amount paid is less than the bike price. Please pay the remaining {remaining_amount} amount.")
#                 return None

#         return {
#             "payment_amount_cash": payment_amount_cash,
#             "payment_amount_loan": payment_amount_loan,
#             "payment_mode": payment_mode
#         }

from colorama import Fore
from bikes_and_banks import RoyalEnfieldShowroom

class LoanProcess:
    def process_loan(self, bike_price, selected_bike, name, age, address, email, financial_proof, want_loan):
        showroom = RoyalEnfieldShowroom()
        payment_mode = ""
        payment_amount_cash = 0
        payment_amount_loan = 0
        
        if want_loan.lower() == 'yes':
            print("Choose a bank for a loan:")
            for bank, interest_rate in showroom.banks.items():
                print(f"{bank} - Interest Rate: {interest_rate}%")

            loan_bank = input("Enter the bank name for a loan: ").upper()
            interest_rate = showroom.banks.get(loan_bank)
            if not interest_rate:
                print("Invalid bank choice!")
                return None

            loan_amount = int(input("Enter the loan amount: "))
            if loan_amount >= bike_price:
                print("Loan amount should be less than the bike price.")
                return None

            total_loan_amount = loan_amount + (loan_amount * (interest_rate / 100))
            payment_amount_cash = bike_price - total_loan_amount
            payment_amount_loan = total_loan_amount

            print("Loan approved by the bank!")
            payment_mode = f"Loan (Bank: {loan_bank}, Amount: {total_loan_amount})"
        else:
            payment_mode = "Cash"
            payment_amount_cash = int(input("Enter the amount paid (in cash): "))
            remaining_amount = bike_price - payment_amount_cash
            if payment_amount_cash < bike_price:
                print(f"The amount paid is less than the bike price. Please pay the remaining {remaining_amount} amount.")
                return None

        return {
            "payment_amount_cash": payment_amount_cash,
            "payment_amount_loan": payment_amount_loan,
            "payment_mode": payment_mode
        }
