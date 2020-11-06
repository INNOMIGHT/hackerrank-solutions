import hashlib

n = int(input())
input_line = input()
input_list = input_line.split()
integer_list = []

for i in range(0, n):
    integer_list.append(int(input_list[i]))

integer_list = tuple(integer_list)
print(hash(integer_list))

