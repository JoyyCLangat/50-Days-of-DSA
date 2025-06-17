if __name__ == '__main__':
    LA = [0,0,0]
    n = len(LA)
    print("Array Before Deletion:")
    for x in range(len(LA)):
        LA[x] = x + 3
        print("LA", [x],"=", LA[x])

    del LA[1]

    print("Array After Deletion: ")
    for x in range(len(LA)):
        print("LA", [x], "=", LA[x])























