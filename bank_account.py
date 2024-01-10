from mimetypes import init
from unittest import result
from Result import Ok,Error

myBalance = 0
class bankAccount():
    def __init__(self, initial_balance = 0):
        self.myBalance = initial_balance
    def deposit(self, value):
        if value > 0:
            self.myBalance += value
            return Ok (self.myBalance)
        else:
            return Error("Invalid deposit")
    def get_balance(self):
        return self.myBalance
    def try_withdrawal(self, value):
        if self.myBalance >= value :
            self.myBalance -= value
            return Ok("Cash out", value)
        return Error ("Error!", value)
        time.s

    def screenATM(self):
        print("Your balance:", self.myBalance ,"$")
    def __str__(self):
        return str(myBalance)
    
class MinimumBalanceAccount(bankAccount):
    def __init__(self,myBalance=0, minimumBalance=50):
        super().__init__ (myBalance)
        self.minimumBalance = minimumBalance
    def try_withdrawal(self, value):
        if self.myBalance - value >= self.minimumBalance:
            self.myBalance -= value
            return super().try_withdrawal(value)
        else:
            return Error("Cancel, you have minimum balance and you can't withdrawal", value)
            