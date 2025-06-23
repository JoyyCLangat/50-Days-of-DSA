def quicksort(arr, low=0, high=None):
    """Sort array in-place from smallest to largest using QuickSort"""
    if high is None:
        high = len(arr) - 1
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:  # <= for ascending order
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, high)

    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(quicksort(arr))