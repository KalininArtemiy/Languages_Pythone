def is_lucky(number):
  if 99999 > number or number > 1000000:
    return ('Out of range')
  elif int(number/100000) + int((number/10000)%10) + int((number/1000)%10) == int((number/100)%10) + int((number/10)%10) + int(number%10):
    return ("You are lucky!")
  else:
    return ("You are lucky, but not this ticket :)")

number = int(input("Enter your ticker number "))
print (is_lucky (number))