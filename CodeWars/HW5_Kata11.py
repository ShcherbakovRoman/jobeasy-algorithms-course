'''
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.

For example:
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True
All inputs will be lowercase letters.
'''

def solve(st):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'y', 'z']
    list = []
    for char in st:
        list.append(char)
    list.sort()
    x = alphabet.index(list[0]) # in case list starts not with "a"
    for i in range(len(list)):
        if list[i] != alphabet[x + i]:
            return False
    return True


'''
Test.it("Basic tests") 
Test.assert_equals(solve("abc"),True)
Test.assert_equals(solve("abd"), False)
Test.assert_equals(solve("dabc"),True)
Test.assert_equals(solve("abbc"), False)
'''