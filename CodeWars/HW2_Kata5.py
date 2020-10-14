'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
'''


def areYouPlayingBanjo(name):
    y = " plays banjo"
    n = " does not play banjo"
    if name[0] == 'R' or name[0] == 'r':
        name = name + y
    else:
        name = name + n
    return name

'''
test.assert_equals(areYouPlayingBanjo("martin"), "martin does not play banjo");
test.assert_equals(areYouPlayingBanjo("Rikke"), "Rikke plays banjo");
'''