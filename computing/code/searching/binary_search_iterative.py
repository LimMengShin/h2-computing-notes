def binary_search_iterative(arr, low, high, value):
    while low <= high:
        mid = (low+high)//2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            low = mid + 1
        else:
            high = mid -1
    return -1

lst = [1, 6, 9, 34, 56, 233, 983, 1234, 5645]
print(binary_search_iterative(lst, 0, len(lst)-1, 34))