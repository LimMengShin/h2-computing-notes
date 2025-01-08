def binary_search_recursive(arr, low, high, value):
    if low > high:
        return -1
    mid = (low+high)//2
    if value == arr[mid]:
        return mid
    elif value > arr[mid]:
        return binary_search_recursive(arr, mid+1, high, value)
    else:
        return binary_search_recursive(arr, low, mid-1, value)
    
lst = [1, 6, 9, 34, 56, 233, 983, 1234, 5645]
print(binary_search_recursive(lst, 0, len(lst)-1, 34))
