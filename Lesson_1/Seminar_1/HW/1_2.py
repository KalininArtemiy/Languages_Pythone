all_origamis = int(input('Enter number '))
one_origami_for_each_boy = all_origamis / 6
if all_origamis > 5 and all_origamis % 2 == 0:
  print(f''' Peter and Sergey each made {int(one_origami_for_each_boy)} and Kate made {int(one_origami_for_each_boy*4)} origamis''')
else: print ('That\'s impossible ')