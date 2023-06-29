def word_cost ():
  number = int(input("Enter language 0 for English, 1 for Russian: "))
  eng = {1: 'AEIOULNSTR',
        2:'DG',
        3:'BCMP',
        4:'FHVWY',
        5:'K',
        8:'JZ',
        10:'QZ'}
  rus = {1:'АВЕИНОРСТ',
      2:'ДКЛМПУ',
      3:'БГЁЬЯ',
      4:'ЙЫ',
      5:'ЖЗХЦЧ',
      8:'ШЭЮ',
      10:'ФЩЪ'}
  result = 0
  if number == 0:
    word = input("English language\nEnter your word: ").upper()
    print(f'''You've got {sum(k for i in word for k, v in eng.items() if i in v)} scores!''')
  elif number == 1:
    word = input("Russian language\nEnter your word: ").upper()
    print(f'''You've got {sum(k for i in word for k, v in rus.items() if i in v)} scores!''')
  else:
    print(f'''ERROR''')

word_cost()