#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую 
#степень B с помощью рекурсии
number = int(input("Enter number: "))
degree = int(input("Enter degree: "))
def recursion_degree(base, degree):
    if degree == 0:
        return 1
    else:
        return number * recursion_degree(base, degree - 1)

print(recursion_degree(number, degree))