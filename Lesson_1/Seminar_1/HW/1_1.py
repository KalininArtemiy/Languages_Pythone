number = int(input('Enter your Number from 100 to 999 '))
if number < 100 or number > 999:
    print("Error enter another number ") 
else:
    print(int(int(number % 10) + int(number / 100)+ int((number % 100) / 10)))