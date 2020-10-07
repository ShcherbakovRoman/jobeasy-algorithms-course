Num_1 = int(input('Enter first random number: '))
Num_2 = int(input('Enter second random number: '))
Num_3 = int(input('Enter third random number: '))

result = 0

if Num_1 > Num_2 and Num_1 > Num_3:
    result = Num_1
elif Num_3 > Num_2 and Num_3 > Num_1:
    result = Num_3
else:
    result = Num_2

print("Max number is", result)