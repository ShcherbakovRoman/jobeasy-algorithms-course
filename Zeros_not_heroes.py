input_number = input("Please enter a number ending with 0: ")
number = 0
if input_number == '0':
    print("Zero alone is fine, don't worry about it. Poor guy anyway")
else:
    while input_number[-1] == '0':
        number = int(input_number) // 10
        input_number = str(number)
    print(input_number)