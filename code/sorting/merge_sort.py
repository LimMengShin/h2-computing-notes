def merge_sort(arr, low, high):
    if low == high:
        return [arr[low]]
    mid = (low+high)//2
    left_arr = merge_sort(arr, low, mid)
    right_arr = merge_sort(arr, mid+1, high)
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    merged_arr = []
    left_idx = right_idx = 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
    merged_arr += left_arr[left_idx:]
    merged_arr += right_arr[right_idx:]
    return merged_arr

lst = [463, 54, 2, 11, 0, 57, 24, 4]
lst = merge_sort(lst, 0, len(lst)-1)
print(lst)
