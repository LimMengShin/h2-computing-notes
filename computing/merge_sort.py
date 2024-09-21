def merge_sort(arr, low, high):
    if low==high:
        return [arr[low]]
    mid = (low+high)//2
    left = merge_sort(arr, low, mid)
    right = merge_sort(arr, mid+1, high)
    return merge(left, right)

def merge(left, right):
    left_idx = right_idx = 0
    new_arr = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_arr.append(left[left_idx])
            left_idx += 1
        else:
            new_arr.append(right[right_idx])
            right_idx += 1
    new_arr.extend(left[left_idx:])
    new_arr.extend(right[right_idx:])
    return new_arr

lst = [463, 54, 2, 11, 0, 57, 24, 4]
lst = merge_sort(lst, 0, len(lst)-1)
print(lst)