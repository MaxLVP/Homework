class Sun:
    
    instance = None

    def __new__(cls):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance

    @classmethod
    def inst(cls):
        return cls.__new__(cls)
