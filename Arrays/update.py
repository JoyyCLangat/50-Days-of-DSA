#Initializing the array
LA = [1,2,3,4,5,6,7,8,9]

#printing the original array
print("The original array elements are:")
for i in range(len(LA)):
    print("LA",[i], "=", LA[i])

LA[2] = 10
print("Elements after update are:")
for i in range(len(LA)):
    print("LA",[i], "=", LA[i])