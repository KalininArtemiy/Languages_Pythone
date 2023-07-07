""" Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума) """

Users_mass = list(map(int, input("Enter your mass, use spase to separate them: ").split()))
min_diaops = int(input("Enter min: "))
max_diaops = int(input("Enter max: "))
new_diapos = list()
for i in range(len(Users_mass)):
    if min_diaops < Users_mass[i] < max_diaops:
        new_diapos.append(i)
print(new_diapos)