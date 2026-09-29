#create class
class Employee:

    #initializing
    def _init_(self):
        print("Employee created")

    #calling destructor 
    def _del_(self) :
        print("destructor called")

def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("program end...")