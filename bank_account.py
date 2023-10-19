from unittest import result


class Result():
    def __init__(self,isSuccess,message,amount):
        self.isSuccess = isSuccess
        self.message = message  
        self.amount = amount

class bankAccount():
    def __init__(self):
        self.myBalance = 0
    def deposit(self, value):
        self.myBalance += value
        return Result(True,"Cash in:", value )
    def try_withdrawal(self, value):
        if(self.myBalance > value ):
            self.myBalance -= value
            return Result(True,"Cash out:", value)
        return Result (False,"bomz,because try to withdrawal: ", value)
    def screenATM(self):
        print("Your Balance:", self.myBalance ,"$")
    """test"""