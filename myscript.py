from bank_account import bankAccount


ATM = bankAccount()
result = ATM.deposit(4)
if(result.isSuccess):
    print(result.message, result.amount, "$")
ATM.screenATM()
result = ATM.deposit(110)
if(result.isSuccess):
    print(result.message, result.amount, "$")
ATM.screenATM()
result = ATM.try_withdrawal(22210)
if(result.isSuccess):
    print(result.message, result.amount, "$")
else:
    print(result.message, result.amount, "$")

ATM.screenATM()