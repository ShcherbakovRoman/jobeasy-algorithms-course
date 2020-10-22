string = input('Please enter a string: ')
substr = input('Enter char or substring to find and calculate: ')

def substr_counter(substr, string):
    x = len(substr)
    y = len(string)
    res = 0

    for i in range(y - x + 1):
        j = 0
        while j < x:
            if (string[i + j] != substr[j]):
                break
            j += 1
        if (j == x):
            res += 1
            j = 0
    return res


print(substr_counter(substr, string))

# cat caterpillar catastrophicat