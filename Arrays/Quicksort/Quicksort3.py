def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1  # Start right after the pivot

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:  # Allow duplicates to go left
            arr[i], arr[j] = arr[j], arr[i]
            i += 1


    return i - 1

# Test the function
arr = [4, 2, 7, 2, 1, 8, 4]
print(f"Original: {arr}")
pivot_index = partition(arr, 0, len(arr) - 1)
print(f"After partition: {arr}")
print(f"Pivot index: {pivot_index}, Pivot value: {arr[pivot_index]}")









