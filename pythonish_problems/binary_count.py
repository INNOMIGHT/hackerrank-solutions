n = int(input())
binary = ""
while n != 0:
    remainder = n % 2
    n = n // 2
    binary = binary + str(remainder)

one_list = max(binary.split('0'))
print(one_list.count('1'))




