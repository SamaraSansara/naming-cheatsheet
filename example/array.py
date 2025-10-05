N_MAX = 15

def read_array():
    n = int(input("Enter number of elements:"))
    if n > N_MAX:
        print(f"Error: Maximum {N_MAX} elements allowed.")
        return None
    print("Enter elements:")
    arr = []
    for _ in range(n):
        tmp = int(input(""))
        arr.append(tmp)
    return arr

def print_array(arr):
    print("Array:")
    for x in arr:
        print(x, end=" ")
    print("")

# main
arr = read_array()
if arr is not None:
    print_array(arr)

