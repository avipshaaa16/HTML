#Class 1
class Nepal():
    def capital(self):
        print("Kathmandu is the capital of Nepal")

    def language(self):
        print("Nepali is the most widely spoken language of Nepal")

    def type(self):
        print("Nepal is a developing country")

#Class 2
class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a developing country")

#common creation
obj_nep = Nepal()
obj_ind = India()

#Common interface
for country in(obj_nep, obj_ind):
    country.capital()
    country.language()
    country.type()