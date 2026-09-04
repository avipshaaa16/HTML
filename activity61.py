#Create a tuple with different data types
tuplex = ("tuple" , False , 3.2 , 1)
print(tuplex)

#create a tuple
tuplex = (4, 3 , 6 , 9 , 7)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create new tuple
tuplex = tuplex + (1,)
print(tuplex)

#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50 , 10 , 70 , 30 , 70)
print(tuple1.count(70))

#create a tuple
tuplex = (1 , 2 ,3 ,4 ,5 ,6 ,7 ,8)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:7]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)