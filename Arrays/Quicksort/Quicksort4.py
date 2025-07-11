def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)

arr1 = quick_sort([4, 2, 7, 2, 1, 8, 4])
print(arr1[-1])




















