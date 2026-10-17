import main
import valid

def make_withdraw(account_names, account_balances):
    account_choice_val = 0
    account_balance_input = 0.0

    while True:
        account_choice_val = valid.get_integer("\nPlease select which account to make a withdraw for: ")
        if account_choice_val <= (len(account_names) - 1):
            account_balance_input = valid.get_float("Please enter the amount to be withdrawn: ")
            account_balances[account_choice_val] = account_balances[account_choice_val] - account_balance_input
            break