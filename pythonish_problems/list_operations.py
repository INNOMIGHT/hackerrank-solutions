n = int(input())
a_list = []

for _ in range(n):
    s_operation = input().split()
    cmd = s_operation[0]
    rest = s_operation[1:]
    eval('a_list.{0}{1}'.format(cmd, tuple(map(int, rest))))
    print(a_list)
