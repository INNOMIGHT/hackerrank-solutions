strings = ['abc', 'bc', 'bc']
queries = ['ab', 'bc', 'abc']
result = []
count = 0

for query in queries:
    for string in strings:
        if query == string:
            count += 1
    result.append(count)
    count = 0

print(result)



