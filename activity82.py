# Class creation
class MyClass:

    # Private variable
    __privateVar = 27

    # Private method
    def __privMeth(self):
        print("I'm inside class MyClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value:", MyClass.__privateVar)


# Object creation and method call
foo = MyClass()

foo.hello()