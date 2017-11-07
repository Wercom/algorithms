#binary search

def binary_search(lst, x):
    low = 0
    up = len(lst)
    position = 0
    iteration = 0
    while low != up:
        iteration += 1
        compared_value = (low + up) // 2
        position = compared_value
        if x == lst[compared_value]:
            return [x, position+1, iteration]
        elif x < lst[compared_value]:
            up = compared_value
        else:
            low = compared_value + 1
    return None

lst = sorted([int(x) for x in input('Введите массив: ').split()])
x = int(input('Введите искомый элемент: '))
print(binary_search(lst, x)) #print x, position, inerations
