""" Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику """
values = [0, 2, 10, 6] 
def same_by(characteristic, objects):
    characteristic_etalon = characteristic(objects[0])
    for i in range(len(objects)):
        if characteristic(objects[i]) != characteristic_etalon:
           return 'Different'
    else: return True


print(same_by(lambda x: x % 2, values))