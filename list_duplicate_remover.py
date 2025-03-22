# This is a primitive program to remove duplicates from current list
# without a usage of list comprehension or dict.fromkeys()
my_list = []

# Prompting a user to fill the list with elements he wants:
a = int(input("Enter the amount of elements you want to add to list: "))
for x in range(a):
    my_list.append(input("Enter the element want to add to list: "))\

i = 0
while i < len(my_list) :
    j = i+1
    temp_val = my_list[i] # setting a value
    while j < len(my_list):
        if temp_val == my_list[j]:
            del my_list[j]
            continue
        else: j+=1
    i+=1;
# the efficiency must be really bad for large lists

print("The list with unique elements only:")
print(my_list)
