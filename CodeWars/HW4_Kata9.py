'''
"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"
'''


def remove_consecutive_duplicates(s):
    list = s.split(' ')
    list_result = []
    for i in range(len(list) - 1):
        if list[i] != list[i + 1]:
            list_result.append(list[i])
    list_result.append(list[-1])
    result = ' '.join(list_result)
    return result

'''
import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');


'''