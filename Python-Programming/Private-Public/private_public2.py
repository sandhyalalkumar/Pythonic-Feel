class SomeClass:
    def __init__(self):
        self.name = "sand"
        self.roll = 1234
        self.__aadhaar = "1234 5678 2345"

    def some_fun(self):
        self.add_data = 456

    def __some_fun(self):
        self.__add_data = 890

if __name__ == "__main__":

    o = SomeClass()
    print o.__dict__
    o.some_fun()
    print o.__dict__
    o._SomeClass__some_fun()
    print o.__dict__