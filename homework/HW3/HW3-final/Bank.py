import numpy as np

from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():

    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('You should not be able to withdraw more money than the balance of the account.')
        if amount < 0:
            raise ValueError('You should not be able to withdraw a negative amount.')
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('You should not be able to deposit a negative amount.')
        self.balance += amount

    def __str__(self):
        return 'Bank account owner is ' + str(
            self.owner) + ' and the bank account type is ' + self.accountType.name + '.'

    def __len__(self):
        return self.balance


class BankUser():
    def __init__(self, owner):
        self.owner = owner
        self.account = [None, None]

    def addAccount(self, accountType):
        if self.account[accountType.value - 1] is None:
            self.account[accountType.value - 1] = BankAccount(self.owner, accountType)

        else:
            raise ValueError('Only one savings and checking account per user.')

    def getBalance(self, accountType):
        if self.account[accountType.value - 1] is None:
            raise ValueError("The account doesn't exist.")
        return len(self.account[accountType.value - 1])

    # your code

    def deposit(self, accountType, amount):
        if self.account[accountType.value - 1] is None:
            raise ValueError("The account doesn't exist.")
        self.account[accountType.value - 1].deposit(amount)

    # your code

    def withdraw(self, accountType, amount):
        if self.account[accountType.value - 1] is None:
            raise ValueError("The account doesn't exist.")
        self.account[accountType.value - 1].withdraw(amount)

    # your code

    def __str__(self):
        try:
            saving_balance = self.getBalance(AccountType.SAVINGS)
        except ValueError:
            saving_balance = None
        try:
            checking_balance = self.getBalance(AccountType.CHECKING)
        except ValueError:
            checking_balance = None

        return 'Owner ' + self.owner + ': \n --> saving account: ' + str(
            saving_balance) + '\n -->checking account: ' + str(checking_balance)


# your code
def ATMSession(bankUser):
    def interface():
        while True:
            option = int(
                input('Enter Option:\n 1)Exit \n 2)Create Account \n 3)Check Balance \n 4)Deposit \n 5)Withdraw'))
            if option == 1:
                break
            else:
                account = int(input('Enter Option:\n 1)Checking \n 2) Savings'))
                if option == 2:
                    bankUser.addAccount(AccountType.SAVINGS if account == 2 else AccountType.CHECKING)
                    print(
                        AccountType.SAVINGS.name if account == 2 else AccountType.CHECKING.name + ' account has been created!')
                elif option == 3:
                    print(bankUser.getBalance(AccountType.SAVINGS if account == 2 else AccountType.CHECKING))

                elif option in [4, 5]:
                    amount = int(input('Enter Integer Amount, Cannot Be Negative:'))
                    if option == 4:
                        bankUser.deposit(AccountType.SAVINGS if account == 2 else AccountType.CHECKING, amount)
                        print('Now you have ' + str(
                            bankUser.getBalance(AccountType.SAVINGS if account == 2 else AccountType.CHECKING))
                        + ' in this account.')

                    else:
                        bankUser.withdraw(AccountType.SAVINGS if account == 2 else AccountType.CHECKING, amount)
                        print('Now you have ' + str(
                            bankUser.getBalance(AccountType.SAVINGS if account == 2 else AccountType.CHECKING))
                        + ' in this account.')

    interface()
