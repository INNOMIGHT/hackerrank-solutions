string = "abcdefghijklmno"
max_width = 4
for i in range(1, len(string)+1):
    print(string[i-1], end="")
    if i % max_width == 0:
        print()
