class Result():
    def __init__(self,message,amount=None):
        self.isSuccess = None
        self.message = message  
        self.amount = amount
    def is_ok(self):
        return(self.isSuccess)
        
class Ok(Result):
    def __init__(self,message,amount=None):
        super().__init__(message,amount)
        self.isSuccess = True
class Error(Result):
    def __init__(self,message,amount=None):
        super().__init__ (message,amount)
        self.isSuccess = False
        