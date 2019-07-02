list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

# Update an element
list1[2] = 2001

# Delete an element
del list1[1]

# Get size
len(list1)

# Concatenate lists
list1 + list2

# Repetition
list1 * 4

# check if an element exists in the list
"x" in list1

# Iteration
for i in list1:
    print(list1[i])
