from Bank import BankAccount, BankUser, AccountType, ATMSession


def test_over_withdrawal():  # this test function should throw an Exception or Error
    user = BankUser("Joeh");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.withdraw(AccountType.SAVINGS, 1000);  # this will cause an Exception or Error
    except Exception as e:
        print(e);  # print the message for the Exeption

def test_over_dup_account():  # this test function should throw an Exception or Error
    user = BankUser("Joeh");
    user.addAccount(AccountType.SAVINGS);

    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.addAccount(AccountType.SAVINGS);
    except Exception as e:
        print(e);  # print the message for the Exeption


def test_over_neg_deposit():  # this test function should throw an Exception or Error
    user = BankUser("emma");
    user.addAccount(AccountType.CHECKING);
    try:
        user.deposit(AccountType.CHECKING, -10);
    except Exception as e:
        print(e);  # print the message for the Exeption

def test_over_getbalance():  # this test function should throw an Exception or Error
    user = BankUser("Joeh");
    user.addAccount(AccountType.SAVINGS);

    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.getBalance(AccountType.CHECKING);
    except Exception as e:
        print(e);  # print the message for the Exeption
# tests
test_over_withdrawal();
test_over_dup_account()
test_over_neg_deposit()
test_over_getbalance()

# test one user
user = BankUser("Adam")
user.addAccount(AccountType.CHECKING)
user.deposit(AccountType.CHECKING, 1000)
user.withdraw(AccountType.CHECKING, 10)
print(user.getBalance(AccountType.CHECKING))
print(user)

# test interface
Selina = BankUser("Selina")
a = ATMSession(Selina)

