#Two Sum – Find two numbers that add up to a target.
def two_sum(A, T):
    dict = {}
    for i, num in enumerate(A):
        num1 = T - num
        if num1 in dict:
            return [dict[num1], i]
        dict[num] = i
    return []
    
A = [2, 7, 11, 15]
T = 9
print(two_sum(A, T))