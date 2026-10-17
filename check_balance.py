import main

def check_balance(account_names, account_balances):
    print("\n Your Accounts: ")
    for i in range(len(account_names)):
        print("{}: {:.2f}".format(account_names[i], account_balances[i]))