def read_file():
  action = int(input(f'''Enter 1 to show all telephone directory, enter 2 to find Surname, Name, patronymic or number: '''))
  if action == 1:
     with open('my_file.txt', 'r',  encoding='utf-8') as f:
        contacts = f.read()
        print(*(contacts.split(';')))
  elif action == 2: 
     find_contact = str(input("Enter searching information: ")).upper().strip()
     with open('my_file.txt', 'r',  encoding='utf-8') as f:
        contacts = f.readlines()
        for contact in contacts:
           if find_contact in contact.upper().split(';'):
              print(*contact.split(';'), end = "")
           else: 
              print("There is no this contact: ")
              next_command = int(input("Enter 1 to ad contact, enter any key to - skip: "))
              if next_command == 1:
                 add_to_file()
              else:
                 return          
  # another elif - How variant we could add searhing S+N+P, using code from changing.
  #  I think it would be better to split every function into parts
  else: print('Unknown command')
  return
 
     


def add_to_file():
    surname = str(input('Enter surname: ')).lower().strip()
    name = str(input('Enter name: ').lower()).strip()
    patronymic = str(input('Enter patronymic: ')).lower().strip()
    number = str(input('Enter number: ').replace('+', "")).strip()
    if number[0] == '7':
       number = '8' + number[1:]
    new_contact = surname.capitalize() + ';' + name.capitalize() + ';' + patronymic.capitalize() + ';' + number
    with open('my_file.txt', 'a',  encoding='utf-8') as f:
       f.write('\n')
       f.write(new_contact)
    return


def change_file():
    changing_contact = str(input("Enter contact's information: " )).upper().strip()
    with open('my_file.txt', 'r',  encoding='utf-8') as f:
        contacts = f.readlines()
        for _ in range(len(contacts)):
          if changing_contact in contacts[_].upper().split(';'):
               print(f'''contacts id: {_}''')
               print(*contacts[_].split(';'))
          else: print('Not in contacts')
    changing_id = int(input("enter id of the contact you'd like to change: "))
    changing_command = int(input("enter 0 to change surname, enter 1 to change name, enter 2 to change patronymic, enter 3 to change number, enter 4 to rewrite contact: "))
    changed_contact = contacts[changing_id].split(';')
    if changing_command == 0:
       new_surname = str(input('Enter surname: ')).lower().strip() 
       changed_contact[0] = new_surname.capitalize()
    elif changing_command == 1:
       new_name = str(input('Enter name: ')).lower().strip()
       changed_contact[1] = new_name.capitalize()
    elif changing_command == 2:
       new_patronymic = str(input('Enter patronymic: ')).lower().strip()
       changed_contact[2] = new_patronymic.capitalize()
    elif changing_command == 3:
       new_number = str(input('Enter number: ').replace('+', "")).strip()
       if new_number[0] == '7':
          new_number = '8' + new_number[1:]
       changed_contact[3] = new_number
    elif changing_command == 4:
       new_surname = str(input('Enter surname: ')).lower().strip() 
       changed_contact[0] = new_surname.capitalize()
       new_name = str(input('Enter name: ')).lower().strip()
       changed_contact[1] = new_name.capitalize()
       new_patronymic = str(input('Enter patronymic: ')).lower().strip()
       changed_contact[2] = new_patronymic.capitalize()
       new_number = str(input('Enter number: ').replace('+', "")).strip()
       if new_number[0] == '7':
          new_number = '8' + new_number[1:]
       changed_contact[3] = new_number
    else: print("Unknow command")
    changed_contact = ";".join(changed_contact)
    contacts[changing_id] = changed_contact
    with open('my_file.txt', 'w',  encoding='utf-8') as f:
       f.writelines(contacts)
    return

           
           
           
           
         









def menu():
    command_menu = int(input("Enter 1 for reading phone number, 2 for adding new number, 3 for changing "))
    if command_menu == 1:
        read_file()
    elif command_menu == 2:
        add_to_file()
    elif command_menu == 3:
       change_file()

menu()