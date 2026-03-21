


# merge sort recusive approach
"""
Merge sort falls under divide and conquer stratergy, we divid ethe array into smaller array and then we just sort
then while merging them back into the full array.
T.C -> Theta of nlogn
S.C -> O(nlogn)
"""
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

    

arr = [4, 9, 7, 6, 4, 2]
import random
arr = [random.randint(-1000, 1000) for _ in range(1000)]

print(merge_sort(arr))