if __name__ == '__main__':
    LA =[0,0,0]
    x = 0

    print("Array Before Insertion: ")
    for x in range(0, len(LA)):
        print("LA", [x], "=", LA[x])

    print("Inserting Elements....")
    for x in range(0, len(LA)):
        LA[x] = x + 2

    LA.append(5)
    print("After Insertion: ")
    for x in range(0, len(LA)):
        print("LA", [x], "=", LA[x])
    





















