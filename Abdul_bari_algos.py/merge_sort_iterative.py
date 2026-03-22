

# merge sort iterative method 

"""
THis is Merge sort iterative method, we simply take smallest elements and then we sort it, and then we keeping on merging the arrays
In this solution we are doing in place merge sort, so we do not need extra space for it.
T.C -> O(n log n)
S.C -> O(1) since no recusive stack and no final result array.
"""

def merge_sort(arr):
    n = len(arr)
    curr_size = 1

    while curr_size < n:
        left_start = 0

        while left_start < n - 1:    # check why -1 ?
            mid = min(left_start + curr_size - 1, n - 1)
            right_end = min(left_start + 2 * curr_size - 1, n - 1)         # we need the min fucntion for the odd number of length, since the mid and right can go out of bounds in that case we restrict it to n - 1

            merge(arr, left_start, mid, right_end)

            left_start += 2 * curr_size
        
        curr_size *= 2
    
    return arr


def merge(arr, left_start, mid, right_end):

    left = arr[left_start: mid + 1]
    right = arr[mid + 1: right_end + 1]
    i, j, k = 0, 0, left_start             # k is supposed to start from left_start because we are supposed to change those numbers where left_start is starting from

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    


arr = [9, 3, 7, 5, 6, 4, 8]
result = merge_sort(arr)
print(result)
