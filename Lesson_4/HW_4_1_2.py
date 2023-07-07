""" Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы. """
def two_numbers_summ_with_recursion(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return two_numbers_summ_with_recursion(first_num + 1, second_num - 1)
    
fst_num = number = abs(int(input("Enter first number: ")))
snd_num = number = abs(int(input("Enter second number: ")))

print(two_numbers_summ_with_recursion(fst_num, snd_num))