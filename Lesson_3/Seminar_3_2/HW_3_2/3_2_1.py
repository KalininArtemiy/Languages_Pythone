set_1 = set()
set_2 = set()
set_1_amount = int(input('Enter first set numbers amount '))
set_2_amount = int(input('Enter second set numbers amount '))
for number in range(set_1_amount):
    set_1.add(int(input(f'''Enter first set {number+1} number ''')))
for number in range(set_2_amount):
    set_2.add(int(input(f'''Enter second set {number+1} number ''')))
print(set_1)
print(set_2)
set_3 = set_1 & set_2
my_list = list(set_3)
my_list.sort()
for i in my_list: 
    print(i, end = ' ')

