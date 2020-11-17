def palindromic(sequence):
    return "".join(list(sequence) + list(reversed(sequence)))


print(palindromic('Innomight'))
