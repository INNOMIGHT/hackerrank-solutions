def decodeHuff(root, s):
    temp = root
    result = []

    for char in s:
        if char == '0':
            temp = temp.left
        elif char == '1':
            temp = temp.right
        if temp.left is None and temp.right is None:
            result.append(temp.data)
            temp = root

    print("".join(result))
