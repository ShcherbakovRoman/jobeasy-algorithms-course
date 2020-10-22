# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE

string = input('Please enter a string: ')
substr1 = input('Enter a substring to find: ')
substr2 = input("Enter a substring to replace with: ")

# index = 0
#
# for char in string:
#     if char == substr1:
#         string[index::] = substr2
#     index += 1
#
# print(string)

def replace_substr(string, substr1, substr2):
    x = len(substr1)
    y = len(substr2)
    result = ''
    subresult = ''
    for index in range(len(string)):
        if string[index] != substr1[0]:
            result += string[index]
        else:
            counter = 1
            for z in range(x):
                if substr1[counter] == string[index + counter]:
                    counter += 1

    return result


print(replace_substr(string, substr1, substr2))



