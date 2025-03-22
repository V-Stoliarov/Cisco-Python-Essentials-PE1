
my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 4, 1, 1, 4, 2, 6, 6, 2, 9, 9, 9]
i = 0
while i < len(my_list) :
    j = i+1
    temp_val = my_list[i]
    while j < len(my_list):
        if temp_val == my_list[j]:
            del my_list[j]
            continue
        else: j+=1
    i+=1;
print("The list with unique elements only:")
print(my_list)
