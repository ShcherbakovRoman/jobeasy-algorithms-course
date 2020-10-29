# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string, and words may be separated by several spaces).
# Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

def make_regular_string(string):
    while string[0] == ' ':   # delete space(s) in the beginning of the string
        string = string[1:]
    while string[-1] == ' ':   # delete space(s) in the end of the string
        string = string[:-1]
    while '  ' in string:  # leave only 1 space between words
        string = string.replace('  ', ' ')
    return string

print(make_regular_string(' gfdfs   skjdhfjk s   dshfkjdfhk sdjk  k'))