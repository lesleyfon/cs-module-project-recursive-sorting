# TO-DO: complete the helper function below to merge 2 sorted arrays
import random


def merge(arrA, arrB):
    '''
        Takes two sorted arrays arrays
        Create a result variable to hold results of sorted numbers

        while there are still numbers in arrA and arrB:
            if the first element of arrA is less than the first element of arrB, remove that element and add it to the result arr
            else remove the first element from arrB and add it to the results array because it is smaller than the first element in arrA
        next if there are anny elements in arrA or arrB, append them to the results array. 
    '''
    result = []
    while len(arrA) and len(arrB):
        if (arrA[0] < arrB[0]):
            res = arrA.pop(0)
            result.append(res)
        else:
            result.append(arrB.pop(0))

    result.extend(arrA)
    result.extend(arrB)

    return result

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    '''
        1. Takes an array and divides it into small a chunk as possible
        2. The smallest we can divide an array into is an array on length 1
        3. We divide the array into halves and keep calling the merge_sort function until it is is of length 1
        4. So when the get to the point where the array length is 1, we can't sub divide the array any more so we call the merge function with arrays on length 1
    '''
    # Your code here
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr

    mid_point = len(arr) // 2
    print(arr)
    return merge(merge_sort(arr[:mid_point]),  merge_sort(arr[mid_point:]))
    # return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort(arr1)
# def test_merge_sort():
#     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#     arr2 = []
#     arr3 = [2]
#     arr4 = [0, 1, 2, 3, 4, 5]
#     arr5 = random.sample(range(200), 50)

#     print(merge_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     print(merge_sort(arr2), [])
#     print(merge_sort(arr3), [2])
#     print(merge_sort(arr4), [0, 1, 2, 3, 4, 5])
#     # print(merge_sort(arr5), sorted(arr5))


# test_merge_sort()
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
# Your code here
