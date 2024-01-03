from colorama import Fore
from user_input import UserInput
from loan_process import LoanProcess
from receipt import Receipt
Receipt.print_receipt(**input_data, **loan_data)

class RunProgram:
    def start(self):
        user_input = UserInput()
        input_data = user_input.get_user_input()

        if input_data:
            loan_process = LoanProcess()
            loan_data = loan_process.process_loan(**input_data)

            if loan_data:
                receipt = Receipt()
                receipt.print_receipt(**input_data, **loan_data)

run = RunProgram()
run.start()
