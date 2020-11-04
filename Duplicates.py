# Remove duplicates from a list

list = [4, 5, 7, 2, 5, 7, 23, 346, 1, 5, 7, 4, 23]
result_list = []

for i in range(len(list)):
    if list[i] not in result_list:
        result_list.append(list[i])
        
print(result_list)
