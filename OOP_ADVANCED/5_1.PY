
class Money:
    def __init__ (self, amount: int, currency: int, str = 'VNd'):
        self.amount = amount
        self.currency = currency
        pass 
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    