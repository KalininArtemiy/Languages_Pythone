"""  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится c новой строки. """
    
arifm_prog_list = []
first_progr_elem = int(input("Enter the first elem of the progression: "))
progression_step = int(input("Enter progression step: "))
progression_elems = int(input("Enter amount of elements: "))
for elem in range (first_progr_elem, (first_progr_elem + (progression_elems - 1) * progression_step) + 1, 
        progression_step): arifm_prog_list.append(elem)
print(arifm_prog_list)


