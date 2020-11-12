"""
There are two lists that have different length. First has keys and the second has values.
Create a function, which creates a dictionary of keys and values.
If there is not enough values to match each key, this key should have value equal to None.
If there is not enough keys to match each value, this value should be ignored.
"""


# keys_list = ['a', 'd', 't', 'c', 'h', 'y', 'v', 'u', 's', 'r']
keys_list = ['a', 'd', 't', 'c', 'h', 'y', 'v', 'u', 's', 'w', 'q', 'z', 'p']
values_list = [1, 2, 345, 23, 2, 65, 11, 3, 5, 10]
dict = {}

def create_dictionary(keys_list, values_list):
    if len(keys_list) > len(values_list):
        for i in range(len(values_list)):
            dict[keys_list[i]] = values_list[i]
        for x in keys_list[len(values_list):]:
            dict[x] = None
        return dict
    elif len(keys_list) <= len(values_list):
        for i in range(len(keys_list)):
            dict[keys_list[i]] = values_list[i]
        return dict

print(create_dictionary(keys_list, values_list))