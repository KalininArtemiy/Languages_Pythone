numbers_amount = int(input('Enter your number '))
my_list = []
for i in range(numbers_amount):
    new_number = int(input('Enter new number '))
    my_list.append(new_number)
print(my_list)
searching_number = int(input('Enter searching number '))
min_diff = 100 ** 100
min_number = 0
for i in range(numbers_amount):
    if abs(searching_number - my_list[i]) < min_diff:
        min_diff = abs(searching_number - my_list[i])
        min_number = my_list[i]
print(f'''the nearest number is {min_number} and the difference is {min_diff}''')