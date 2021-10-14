
# funtions
def make_withdrawal(balance):
    def new_balance(withdraw_amount):
        balance = balance - withdraw_amount

        if balance < 0:
            raise ValueError
        return balance

    return new_balance

print("Updated balance name is bound in a block, it is a local variable within the inner function "
      "of that block, unless declared as nonlocal or global, so the way I wrote the algorithm cannot make the function run properly.")

# demo
init_balance = 10000
withdrawal_amount = 200
new_withdrawal_amount = 500
wd = make_withdrawal(init_balance)
new_bal1 = wd(withdrawal_amount)
new_bal2 = wd(new_withdrawal_amount)
print("The new balance is {}".format(new_bal1))
print("The new balance is {}".format(new_bal2))

