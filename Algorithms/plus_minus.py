def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    zeroes = 0
    for i in arr:
        if i > 0:
            positive += 1
        if i < 0:
            negative += 1
        if i == 0:
            zeroes += 1
    print("{:.6f}\n{:.6f}\n{:.6f}".format(positive/length, negative/length, zeroes/length))
