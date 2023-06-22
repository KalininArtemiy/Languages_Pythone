kilometers = int(input('Enter start km: '))
kilometers_per_day = int(input('Enter km per day: '))
days = int (kilometers/kilometers_per_day + (1 *(kilometers/kilometers_per_day % 1) > 0))
print(days)