from unittest import result


class Result():
    def __init__(self,isSuccess,message,amount):
        self.isSuccess = isSuccess
        self.message = message  
        self.amount = amount

class bankAccount():
    def __init__(self, myBalance = 0):
        self.myBalance = myBalance
    def deposit(self, value):
        self.myBalance += value
        return Result(True,"Cash in:", value )
    def try_withdrawal(self, value):
        if(self.myBalance > value ):
            self.myBalance = value
            return Result(True,"Cash out:", value)
        return Result (False,"bomz,because try to withdrawal: ", value)
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
            return Result(False,"Cancel", value)
            