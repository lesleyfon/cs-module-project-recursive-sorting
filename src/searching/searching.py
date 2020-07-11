# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1

    mid_point = (start + end) // 2

    if arr[mid_point] == target:
        return mid_point

    if target < arr[mid_point]:

        end = mid_point - 1
        return binary_search(arr, target, start, end)

    if target > arr[mid_point]:
        start = mid_point + 1
        #     # We want to recurse the left hand side of the array
        # Call binary_search with the left hand side of the array, excluding the mid point, target, start and the new end which is the mid_point - 1 of the array
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
