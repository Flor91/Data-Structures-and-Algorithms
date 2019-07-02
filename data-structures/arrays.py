from array import *


"""
Typecode	Value
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 byte
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytes
d	Represents floating point of size 8 bytes
"""
arr = array(typecode='i', [10, 20, 30, 40])


# Array iteration
for x in arr:
    print(arr[x])

# Insert value 60 at index 1
arr.insert(1, 60)

# Remove first occurrence of a value
arr.remove(20)

# Search for index of first occurence of a value
arr.index(30)

# Update a value
arr[2] = 20