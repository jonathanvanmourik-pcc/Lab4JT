import valid
import main

def create_account(account_names, account_balances):
    #creates a new account
    account_name_val = ""
    account_balance_val = 0

    account_name_val = valid.get_string("\nWhat would you like to name your account?: ")
    account_balance_val = valid.get_integer("How much would you like to deposit in {}?: ".format(account_name_val))
    account_names.append(account_name_val)
    account_balances.append(account_balance_val)
