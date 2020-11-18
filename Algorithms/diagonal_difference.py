def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for size in range(n):
        diagonal1 += arr[size][size]
        diagonal2 += arr[size][n - 1 - size]
    return abs(diagonal1 - diagonal2)