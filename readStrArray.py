from extender import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    plantNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак прямоугольника
            i += 1
            plant = Tree()
            i = plant.ReadStrArray(strArray, i)  # чтение прямоугольника с возвратом позиции за ним
        elif key == 2:  # признак треугольника
            i += 1
            plant = Bush()
            i = plant.ReadStrArray(strArray, i)  # чтение треугольника с возвратом позиции за ним
        elif key == 3:  # признак треугольника
            i += 1
            plant = Flower()
            i = plant.ReadStrArray(strArray, i)  # чтение треугольника с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return plantNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return plantNum
        plantNum += 1
        container.store.append(plant)
    return plantNum


def RandomRead(container, arrayLen):
    plantNum = 0
    for i in range(arrayLen):
        key = generate() % 3 + 1
        if key == 1:
            plant = Tree()
            plant.RandomRead()
        elif key == 2:
            plant = Bush()
            plant.RandomRead()
        elif key == 3:
            plant = Flower()
            plant.RandomRead()
        else:
            return plantNum
        plantNum += 1
        container.store.append(plant)
    return plantNum