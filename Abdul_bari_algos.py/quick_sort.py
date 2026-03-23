
import random

# quick sort


"""
This is is quick sort which is also divide and conquer, this is done therough recusion as well.
The whole idea is that you take a rnadom number and place it in its correct position and then
you divide and repeat the ones before it and the ones after it. 
T.C -> O(n log n)
worst case -> O(n^2)
S.C -> O(logn)
worst case -> O(n) if array is already sorted, the binary tree will be equal the length of the array, when you divide it
"""


def partition(l, h, arr):

    random_index = random.randint(l, h)
    arr[random_index], arr[h] = arr[h], arr[random_index]
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


def quick_sort(l, h, arr):

    if l < h:
        pivot = partition(l, h, arr)
        quick_sort(l, pivot - 1, arr)
        quick_sort(pivot + 1, h, arr)


arr = [4, 9, 7, 6, 8, 7, 1244, -1, 4, 2]
quick_sort(0, len(arr) - 1, arr)
print(arr)