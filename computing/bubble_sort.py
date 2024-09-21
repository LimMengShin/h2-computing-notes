def bubble_sort(arr):
    x = len(arr)-1
    for i in range(x):
        swapped = False
        for j in range(x-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return

lst = [463, 54, 2, 11, 0, 57, 24, 4]
bubble_sort(lst)
print(lst)