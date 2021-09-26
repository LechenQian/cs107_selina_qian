
# functions
def make_withdrawal(balance):

    def new_balance(withdraw_amount):
        remaining = balance-withdraw_amount
        if remaining < 0:
            raise ValueError
        return remaining

    return new_balance

# demo
print("The algorithm doesn't behave correctly because the balance values used by the inner function hasn't been updated" )
init_balance = 10000
withdrawal_amount = 200
new_withdrawal_amount = 50000
wd = make_withdrawal(init_balance)
new_bal1 = wd(withdrawal_amount)
new_bal2 = wd(new_withdrawal_amount)
print("The new balance is {}".format(new_bal1))
print("The new balance is {}".format(new_bal2))

