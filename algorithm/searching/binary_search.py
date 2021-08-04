# Binary Search in python


def binarySearch(array, x):

    low = 0
    high = len(array)-1

    while low <= high:

        mid = (low + high)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")