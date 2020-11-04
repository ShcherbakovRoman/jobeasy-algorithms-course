list = [4, 5, 7, 2, 5, 7, 1, 5, 7, 4]
new_list = []
list_avg = sum(list) / len(list)
print("Average of the list:", list_avg)

for i in range(len(list)):
    if list[i] < list_avg:
        new_list.append(list[i])

print(new_list)