a = [1, 1, 2, 3, 4, 5, 6, 7]
b = set(a)
print (len(b))

#OR 
print ('or')

setty = set(int(a) for a in input().split())
print(len(setty))

#OR

my_list = [1, 1, 2, 3, 4, 5, 6, 7]
my_list_2 = [0]
count = 0
for i in my_list:
    if i not in my_list_2:
        my_list_2.append(i)
        count += 1
print(count)