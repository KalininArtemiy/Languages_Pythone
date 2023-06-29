numbers_amount = int(input('Enter your number '))
my_list = []
for i in range(numbers_amount):
    new_number = int(input('Enter new number '))
    my_list.append(new_number)
print(my_list)
searching_number = int(input('Enter searching number '))
count = 0
for element in range(numbers_amount):
    if my_list[element] == searching_number:
        count += 1
print (count)