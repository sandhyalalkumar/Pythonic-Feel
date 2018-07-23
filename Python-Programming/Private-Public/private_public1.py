# private atttributes and methods can't be access outside the class
# In Python, the private is not very strict, they mangeled and ungandled at run time on name.
# So a private attribute and method can be accessed like:
#         obj = class_name()
#         obj._class_name__attribute_name
#         obj._class_name__method_name()

class HelloWorld:
    def __init__(self, data, __data):
        self.data = data
        self.__data = __data

    def some_fun(self):
        print "This is some function"

    def __some_fun(self):
        print "This is __some function"


if __name__ == "__main__":

    h = HelloWorld(10, 20)
    print h.data
    print h.__data # not accessible out the class
    print h._HelloWorld__data # this way private attribute can be accessed

    h.some_fun()
    h.__some_fun() # private method not accessible outside the class
    h._HelloWorld__some_fun() # this way private attribute is accessible outside the class