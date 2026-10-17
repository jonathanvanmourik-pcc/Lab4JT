#******************************************************************************
# Author:           Jonathan van Mourik
# Lab:              Lab 4
# Date:             10/15/26
# Description:      Basic ATM
# Input:            int: options selection, str: naming account, float: Changing Balance of account
# Output:           Str: account name, Floats: account balance
# Sources:          Lab 4
#******************************************************************************
"""
Welcome to Basic Banking ATM
1: Check Balance
2: Make a Deposit
3: Make a Withdraw
4: Create an Account
5: Quit

What would you like to do today?: 4

What would you like to name your account?: Savings
How much would you like to deposit in Savings?: 100


Welcome to Basic Banking ATM
1: Check Balance
2: Make a Deposit
3: Make a Withdraw
4: Create an Account
5: Quit

What would you like to do today?: 1

 Your Accounts:
Checking: 50.20
Savings: 100.00
"""

import valid
import check_balance
import make_deposit
import make_withdraw
import create_account

def main():
    #main
    account_names = ["Checking"]
    account_balances = [50.2]
    option_val = 0


    while True:
        print_menu()
        option_val = valid.get_integer("\nWhat would you like to do today?: ")
        if option_val == 1:
            check_balance.check_balance(account_names, account_balances)
        elif option_val == 2:
            print_account_list(account_names)
            make_deposit.make_deposit(account_names, account_balances)
        elif option_val == 3:
            print_account_list(account_names)
            make_withdraw.make_withdraw(account_names, account_balances)
        elif option_val == 4:
            create_account.create_account(account_names, account_balances)
        elif option_val == 5:
            break


def print_menu():
    #print the main menu
    print("\n\nWelcome to Basic Banking ATM")
    print("1: Check Balance")
    print("2: Make a Deposit")
    print("3: Make a Withdraw")
    print("4: Create an Account")
    print("5: Quit")

def print_account_list(account_names):
    #Prints out the list of accounts
    print("\nYour Accounts: ")
    for i in range(len(account_names)):
        print("{}: {}".format(i, account_names[i]))

if __name__ == "__main__":
    main()