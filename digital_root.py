number = input("Enter the number: ")

while len(number) > 1:
    x = 0
    for n in number:
        x += int(n)
    number = str(x)

print(number)


