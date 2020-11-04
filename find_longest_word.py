# Enter a string of words separated by spaces. Find the longest word. (split / join methods)

string = input("Please enter a regular random string with words separated by spaces: ")

# Tried to do it without split / join methods

# word = ''
# length = 0
# result = ''
# list_result = []
# new_string = string + ' ' # To check the last word
# for char in new_string:
#     word += char
#     if char == ' ':
#         word = word[:-1] # remove space (last char) from word
#         if len(word) > length:
#             length = len(word)
#             list_result = [] # remove previously added temporary longest word
#             list_result.append(word)
#         elif len(word) == length:
#             list_result.append(word)
#         word = ''
#
# result = ' '.join(list_result)
#
# print(result)


def find_longest_word(string):
    list_max_words = []
    all_words = string.split(' ')
    length = 0
    for word in all_words:
        if len(word) > length:
            length = len(word)
    for i in all_words:
        if len(i) == length:
            list_max_words.append(i)
    result = ' '.join(list_max_words)
    return result

print(find_longest_word(string))
