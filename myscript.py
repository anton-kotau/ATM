#from bank_account import bankAccount
from bank_account import MinimumBalanceAccount

"""
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
"""
accountMin = MinimumBalanceAccount(myBalance=1500, minimumBalance=1000)
result = accountMin.try_withdrawal(990)

accountMin.deposit(500)
print(result.message, result.amount, "$")

