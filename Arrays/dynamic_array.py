def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for q, x, y in queries:
        if q == 1:
            idx = ((x ^ last_answer) % n)
            seq[idx].append(y)
        else:
            idx = ((x ^ last_answer) % n)
            v = y % len(seq[idx])
            print(v)
            last_answer = seq[idx][v]
            result.append(last_answer)

    return result

