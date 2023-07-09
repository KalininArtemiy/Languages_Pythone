def read_file():
  action = int(input(f'''Enter 1 to show all telephone directory, enter 2 to find Surname, Name, patronymic or number: '''))
  if action == 1:
     with open('my_file.txt', 'r',  encoding='utf-8') as f:
        contacts = f.read()
        print(*(contacts.split(';')))
  elif action == 2: 
     find_contact = str(input("Enter surname: ")).upper()
     with open('my_file.txt', 'r',  encoding='utf-8') as f:
        contacts = f.readlines()
        for contact in contacts:
           if find_contact in contact.upper().split(';'):
              print(*contact.split(';'), end = "")
  else: print('Unknown command')
  return()
           
     


def write_file():
   pass


def menu():
    command_menu = int(input("Enter 1 for reading phone number, 2 for writing new number, 3 for changing "))
    if command_menu == 1:
        read_file()

menu()