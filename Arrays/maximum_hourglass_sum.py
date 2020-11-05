def max_hourglass_sum(td_array):
    largest_hourglass = None
    for row in range(1, 5):
        for col in range(1, 5):
            hourglass_sum = td_array[row-1][col-1] + td_array[row-1][col] + td_array[row-1][col+1] + td_array[row][col] + td_array[row+1][col-1] + td_array[row+1][col] + td_array[row+1][col+1]
            if largest_hourglass is None:
                largest_hourglass = hourglass_sum
            elif hourglass_sum > largest_hourglass:
                largest_hourglass = hourglass_sum
    return largest_hourglass


print(max_hourglass_sum([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]))





