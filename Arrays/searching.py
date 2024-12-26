def findlEement(arr, n, value):
    for i in range(n):
        if arr[i] == value:
            return i
        
    return -1

if __name__ == '__main__':
    LA = [1,2,3,4]
    n = len(LA)
    value = 3

    for x in range(0, len(LA)):
        print("LA", [x], "=", LA[x])

    
    index = findlEement(LA, n, value)

    if index != -1:
        print("Element", value, "Found at position =  " + str(index+1)) 
    else:
        print("Element not found")

    


















