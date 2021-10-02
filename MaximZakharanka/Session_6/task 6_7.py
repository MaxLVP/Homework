
class Money:
    
    exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    "USD": 1,
    "JPY": 110.790480}
    
    class Money:

    exchange_rate = {
        'EUR': 0.85,
        'BYN': 2.5,
        'USD': 1,
        'JPY': 110.75
    }

    def __init__(self, value, currency = "USD"):
        self.value = value
        self.currency = currency
    
    def __str__(self):
        return f'{self.value:.2f} {self.currency}'
      
    def __repr__(self):
        return f'{self.__class__.__name__ }({self.value:.2f},{self.currency!r})'
    
    def __add__(self, other):
        k = Money.exchange_rate[self.currency]/Money.exchange_rate[other.currency]
        return Money(self.value + other.value*k, self.currency)
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __mul__(self, value):
        return Money(self.value * value, self.currency)

    def __rmul__(self, value):
        return Money(self.value * value, self.currency)

    def __sub__(self, other):
        return Money(self.value - other.value, self.currency)

    def __truediv__(self, other):
        return Money(self.value / other.value, self.currency)

    def __lt__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value < other.value / k

    def __le__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value <= other.value / k

    def __eq__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value == other.value / k

    def __ne__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value != other.value / k

    def __gt__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value > other.value / k

    def __ge__(self, other):
        k = Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        return self.value >= other.value / k
