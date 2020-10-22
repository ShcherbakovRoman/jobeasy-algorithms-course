# a4b3c2d

str = input("Please enter a string: ")

def decomp_str(string):
    result = ''
    for index in range(len(string)):
        if string[index].isnumeric() == True:
            result += (string[index-1] * (int(string[index]) - 1))
        else:
            result += string[index]
    return result

print(decomp_str(str))

