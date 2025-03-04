def solution(A):
    Available = set(A)
    smallest_no = 1
    while smallest_no in Available:
        smallest_no +=1
    return smallest_no
        