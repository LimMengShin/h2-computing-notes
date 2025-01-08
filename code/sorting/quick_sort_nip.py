def quick_sort_nip(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quick_sort_nip(left) + mid + quick_sort_nip(right)

lst = [463, 54, 2, 11, 0, 57, 24, 4]
lst = quick_sort_nip(lst)
print(lst)