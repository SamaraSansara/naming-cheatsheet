NU nano 7.2                           

def read_array():
    arr = list()
    n = int(input("Enter number of elements:"))
    print("Enter elements:")
    i = 0
    while i < n:
        tmp = int(input(""))
        arr.append(tmp)
        i += 1
    return arr

def print_array(arr):
    print("Array:")
    for x in arr:
        print(x, end=" ")
    print("")

# main
arr = read_array()
print_array(arr)

