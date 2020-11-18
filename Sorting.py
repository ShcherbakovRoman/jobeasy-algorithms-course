

array = [
    {'name': 'Aliza Hulme', 'job':'Speech therapist'},
    {'name': 'Emily-Jane Mejia', 'job':'Animal breeder'},
    {'name': 'Isaiah Mcgill', 'job':'Butler'},
    {'name': 'Jordon Rocha', 'job':'Unemployment'},
    {'name': 'Keiran Partridge', 'job':'Miner'},
    {'name': 'Lexi Bob', 'job':'Architect'},
    {'name': 'Michele Wilcox', 'job':'IT consultant'},
    {'name': 'Nimrah Regan', 'job':'Unemployment'},
    {'name': 'Scarlet Roberts', 'job':'Radio presenter'},
    {'name': 'Shakir Calhoun', 'job':'Police officer'},
    {'name': 'Zzz', 'job':'Police officer'},
]

array_2 = [1, 4, 7,-10, 9, 1, 2, 3, 0]

print(sorted(array, reverse=True, key=lambda x: x['job']))

# print(array_2.sort(reverse=True))
# print(array_2)

print('abc' > 'de')

# def function(array):
#     for item in array:
#         item['name']
#
#
# lambda x: x['name']