L = [1,6,23,12,10,4,2,3]
print("original list:",L)

#Variable to store the sum of
#the list
count = 0

#finding the sum
for i in L :
    count += 1

#dividing the total number of elements
#by number of elements
avg = count/len(L)

print("sum =", count)
print("average =", avg)

#sorting the elements of the list
L.sort()

#printing the smallest element
print("the smallest element is :", L[0])
#print the largest element
print("the largest element is :", L[-1])




