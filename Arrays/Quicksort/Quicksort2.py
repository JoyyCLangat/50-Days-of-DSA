def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)

print(quick_sort([6, 3, 8, 1, 5]))
