def quick_sort_ip(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_ip(arr, low, pi-1)
        quick_sort_ip(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [45,5735,756,64,546,46,464]
quick_sort_ip(arr, 0, 6)
print(arr)