def array_rotation(array, d, n):
    """
    array: Input array
    n: [INT] number elements in array
    b: [INT] number of places to rotate array
    
    Function that given an array of n elements, rotates by d elements.
    Returns: rotated array
    """

    for i in range(d):
        rotate_one(array, n)

def rotate_one(array, n):
    element = array[0]

    for i in range(n-1):
        array[i] = array[i + 1]
    array[n-1] = element

def print_array(array, n):
    for i in range(n):
        print(" %d " % array[i], end=" ")

    
arr = [1, 2, 3, 4, 5, 6, 7]
array_rotation(arr, 3, 7)
print_array(arr, 7)