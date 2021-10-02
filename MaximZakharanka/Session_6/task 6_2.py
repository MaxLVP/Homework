class HistoryDict():
    
    def __init__(self,dict):
        self.dict = dict
        self.keys = []
    
    def set_value(self, key, value):
        self.dict[key] = value
        self.keys.append(key)
    def get_history(self):
        return self.keys[:-11:-1]
