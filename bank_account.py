from unittest import result
from Result import Ok,Error


class bankAccount():
    def __init__(self, myBalance = 0):
        self.myBalance = myBalance
    def deposit(self, value):
        self.myBalance += value
        return Ok ("Cash in:", value )
    def try_withdrawal(self, value):
        if(self.myBalance > value ):
            self.myBalance = value
            return Ok("Cash out", value)
        return Error ("bomz,because try to withdrawal: ", value)
    def screenATM(self):
        print("Your Balance:", self.myBalance ,"$")
    def __str__(self):
        return str(self.myBalance)
    
class MinimumBalanceAccount(bankAccount):
    def __init__(self,myBalance=0, minimumBalance=500):
        super().__init__ (myBalance)
        self.minimumBalance = minimumBalance
    def try_withdrawal(self, value):
        if self.myBalance - value >= self.minimumBalance:
            return super().try_withdrawal(value)
        else:
            return Error("Cancel", value)
            