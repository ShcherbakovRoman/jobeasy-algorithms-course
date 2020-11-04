number_of_rows = int(input("Please enter a number of rows in triangle: "))

for r in range(1, number_of_rows + 1):
    result = 0
    counter = 1
    first_number_in_row = ((r - 1) ** 2) + (r - 1) + 1
    while counter <= r:
        result += first_number_in_row
        first_number_in_row += 2
        counter += 1
    print(f'The sum of odd numbers in row {r} is equal to {result}')


# OR THE EASY SOLUTION. I figured that was the "interesting patter" that you were talking about:


for r in range(1, number_of_rows + 1):
    print(f'The sum of odd numbers in row {r} is equal to {r ** 3}')



