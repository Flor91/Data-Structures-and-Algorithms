"""
In binary search we take a sorted list of elements and start looking for an element at the middle of the list. 
If the search value matches with the middle value in the list we complete the search. 
Otherwise we eleminate half of the list of elements by choosing whether to procees with the right or left half of the list depending on the value of the item searched. 
This is possible as the list is sorted and it is much quicker than linear search. 
Here we divide the given list and conquer by choosing the proper half of the list. 
We repeat this approach till we find the element or conclude about it's absence in the list.
"""

# Recursive Implemetation
# Returns index of x in arr if present, else -1
def binarySearchRec(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) / 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearchRec(arr, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binarySearchRec(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Iterative
def binarySearchIt(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) / 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearchRec(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")