
# funtions
def make_withdrawal(balance):


    def new_balance(withdraw_amount):
        nonlocal balance

        balance = balance - withdraw_amount


        if balance < 0:
            raise ValueError
        return balance

    return new_balance


# demo
init_balance = 10000
withdrawal_amount = 200
new_withdrawal_amount = 500
wd = make_withdrawal(init_balance)
new_bal1 = wd(withdrawal_amount)
new_bal2 = wd(new_withdrawal_amount)
print("The new balance is {}".format(new_bal1))
print("The new balance is {}".format(new_bal2))