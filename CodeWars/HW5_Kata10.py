'''
Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"
'''



def even_or_odd(s):
    sum_of_even = 0
    sum_of_odd = 0
    for char in s:
        if int(char) % 2 == 0:
            sum_of_even += int(char)
        else:
            sum_of_odd += int(char)
    if sum_of_even > sum_of_odd:
        return 'Even is greater than Odd'
    elif sum_of_even < sum_of_odd:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'


'''
@test.it("Sample tests")
def tests():
    test.assert_equals(even_or_odd('12'), 'Even is greater than Odd')
    test.assert_equals(even_or_odd('123'), 'Odd is greater than Even')
    test.assert_equals(even_or_odd('112'), 'Even and Odd are the same')
'''