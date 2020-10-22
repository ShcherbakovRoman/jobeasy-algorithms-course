'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.'''



def find_short(s):
    counter = 0
    result = []
    for i in range(len(s)):
        if s[i] != ' ':
            counter += 1
        else:
            result.append(counter)
            counter = 0
    result.append(counter)
    l = min(result)
    return l # l: shortest word length


'''
test.describe("Basic Tests")
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
'''