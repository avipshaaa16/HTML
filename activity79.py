#Part 1 : create the parent class with shared family traits
class FamilyMember:
    def __init__(self , eye_color , height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Height (cm):", self.height_cm)

#Part 2 : Create the child class that inherits from familymember
class Kid(FamilyMember):

    #Part 3: Give Kid its own details, plus the inherited traits
    def __init__(self, name , age , eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

        #Part 4: Override show_traits to add the kid's own details too
    def show_traits(self):
          print("Name:", self.name)
          print("Age:", self.age)
          super().show_traits()

        #PArt 5 : Add a brand new method that only Kid has
    def favorite_hobby(self,hobby):
         print(self.name , "loves" , hobby)

#Part 6: Create a Kid object with real family trait values
child = Kid("Maya" , 10 , "brown" , 140)

#Part 7: Call the overridden method and the new method
child.show_traits()
child.favorite_hobby("painting")

#Part 8: Check whether Kid is really a subclass of FamilyMember
print("Is Kid a subclass of FamilyMember?", issubclass(Kid, FamilyMember))