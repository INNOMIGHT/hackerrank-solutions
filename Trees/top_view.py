def topView(root):
    d = {}

    def traverse(root, key, level):
        if root:
            if key not in d:
                d[key] = [root, level]
            elif d[key][1] > level:
                d[key] = [root, level]

            traverse(root.left, key - 1, level + 1)
            traverse(root.right, key + 1, level + 1)

    traverse(root, 0, 0)

    for key in sorted(d):
        print(d[key][0], end=" ")