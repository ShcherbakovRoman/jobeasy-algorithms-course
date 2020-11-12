'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''


def solution(string, ending):
    if ending == '':
        return True
    if ending in string:
        l = len(ending)
        end_string = string[-l:]
        for i in range(len(end_string)):
            if end_string[i] != ending[i]:
                return False
            else:
                return True
    else:
        return False

'''
test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
'''