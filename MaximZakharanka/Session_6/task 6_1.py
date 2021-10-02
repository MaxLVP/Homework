class Counter():
    
    def __init__(self, start = 0, stop=float("inf")):
        self.start = start
        self.stop = stop
    def increment(self):
        if self.start < self.stop:
            self.start += 1
        else:
            print("Maximal value is reached.")
    def get(self):
        return self.start
