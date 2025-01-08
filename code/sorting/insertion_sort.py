def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        previous = i-1
        while previous >= 0 and item_to_insert < arr[previous]:
            arr[previous+1] = arr[previous]
            previous -= 1
        arr[previous+1] = item_to_insert

lst = [463, 54, 2, 11, 0, 57, 24, 4]
insertion_sort(lst)
print(lst)
