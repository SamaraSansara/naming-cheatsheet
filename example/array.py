N_MAX = 15

arr = list()
n = int(input("Enter number of elements:"))
if n > N_MAX:
    print(f"Error: Maximum {N_MAX} elements allowed.")
else:
    print("Enter elements:")
    i = 0
    while i < n:
        tmp = int(input(""))
        arr.append(tmp)
        i += 1

    print("Array:")
    i = 0
    while i < n:
        print(arr[i], end=" ")
        i += 1
    print("")

