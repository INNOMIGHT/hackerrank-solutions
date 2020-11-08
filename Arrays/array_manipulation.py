def array_manipulation(n, queries):
    arr = [0] * (n + 2)

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
        print(arr)

    max_num = temp = 0
    for val in arr:
        temp += val
        print('temp =' + str(temp))
        max_num = max(max_num, temp)

    return max_num


print(array_manipulation(5,[[1, 2, 100], [2, 5, 100], [3, 4, 100]]))