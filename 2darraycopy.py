def copy2dArray(array):
    cp = []
    for row in array:
        cp.append(row.copy())
    return cp

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr_copy = copy2dArray(arr)

arr_copy[0][0] = 0

print(arr)