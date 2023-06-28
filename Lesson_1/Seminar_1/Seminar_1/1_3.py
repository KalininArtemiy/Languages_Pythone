classroom_1 = int(input('First slass '))
classroom_2 = int(input('Second slass '))
classroom_3 = int(input('Third slass '))
tables1 = ((classroom_1/2) + 0.5) //1
tables2 = ((classroom_2/2) + 0.5) //1
tables3 = ((classroom_3/2) + 0.5) //1
print(f'you need: {int(tables1 + tables2 + tables3)} tables')