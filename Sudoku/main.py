import copy

basic_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Клетка поля, хранящая свои коорданаты, цифру и возможные значения цифры
class square:
    data = 0
    possible = set()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.possible


def print_delta(L_old, L_new):
    for i in range(9):
        for j in range(9):
            if L_new[i][j].data != L_old[i][j].data:
                print('\x1b[6;30;42m' + str(L_new[i][j].data) + '\x1b[0m', end=" ")
            else:
                print(L_new[i][j].data, end=" ")
        print()
    print()


def print_data(L):
    for i in L:
        for j in i:
            print(j.data, end=" ")
        print()


# Возвращает мн-во клеток с неизвестной цифрой в ряду n
def get_zeroes_row(L, n):
    res = set()
    for i in range(9):
        if L[n][i].data == 0:
            res.add(L[n][i])
    return res


# Возвращает мн-во клеток с неизвестной цифрой в столбце n
def get_zeroes_column(L, n):
    res = set()
    for i in range(9):
        if L[i][n].data == 0:
            res.add(L[i][n])
    return res


# Возвращает мн-во клеток с неизвестной цифрой в квадрате n
def get_zeroes_square(L, n):
    res = set()
    a = n // 3
    b = n % 3
    for i in range(3 * a, 3 * a + 3):
        for j in range(3 * b, 3 * b + 3):
            if L[i][j].data == 0:
                res.add(L[i][j])
    return res


# Есть ли в n-ом ряду клетка с цифрой digit
def is_in_row(L, digit, n):
    for i in range(9):
        if L[n][i].data == digit:
            return True
    return False


# Есть ли в n-ом столбце клетка с цифрой digit
def is_in_column(L, digit, n):
    for i in range(9):
        if L[i][n].data == digit:
            return True
    return False


# Есть ли в n-ом квадрате клетка с цифрой digit
def is_in_square(L, digit, n):
    a = n // 3
    b = n % 3
    for i in range(3 * a, 3 * a + 3):
        for j in range(3 * b, 3 * b + 3):
            if L[i][j].data == digit:
                return True
    return False


# Возвращает мн-во отсутствующих цифр в n-ой строке
def absent_row(L, n):
    res = set()
    for i in basic_set:
        if not is_in_row(L, i, n):
            res.add(i)
    return res


# Возвращает мн-во отсутствующих цифр в n-ом столбце
def absent_column(L, n):
    res = set()
    for i in basic_set:
        if not is_in_column(L, i, n):
            res.add(i)
    return res


# Возвращает мн-во отсутствующих цифр в n-ом квадрате
def absent_square(L, n):
    res = set()
    for i in basic_set:
        if not is_in_square(L, i, n):
            res.add(i)
    return res


# Возвращает идентификатор квадрата, в котором находится клетка sqr
def get_square_id(sqr):
    return 3 * (sqr.y // 3) + sqr.x // 3


# Возвращает мн-во цифр в n-ой строке
def get_row(L, n):
    return basic_set - absent_row(L, n)


# Возвращает мн-во цифр в n-ом столбце
def get_column(L, n):
    return basic_set - absent_column(L, n)


# Возвращает мн-во цифр в n-ом квадрате
def get_square(L, n):
    return basic_set - absent_square(L, n)


# Завершена ли n-ая строка
def row_done(L, n):
    if absent_row(L, n) == set():
        return True
    else:
        return False


# Завершён ли n-ый столбец
def column_done(L, n):
    if absent_column(L, n) == set():
        return True
    else:
        return False


# Завершён ли n-ый квадрат
def square_done(L, n):
    if absent_square(L, n) == set():
        return True
    else:
        return False


# Выставляет на поле цифру, если существует всего один возможный вариант для клетки (обрабатывает всё поле)
def confirm(L):
    res = False
    for i in range(9):
        for j in range(9):
            if len(L[i][j].possible) == 1:
                L[i][j].data = L[i][j].possible.pop()
                res = True
    return res


# Обрабатывает n-ую строку
def do_row(L, n):
    changed = False
    absent = absent_row(field, n)
    zero_squares = get_zeroes_row(field, n)
    exist = get_row(L, n)
    for i in range(9):  # В ряду нет повторений
        L[n][i].possible.difference_update(exist)
    for i in absent:  # Перебираем отсутствующие цифры в n-ом ряду
        for j in zero_squares:  # Ищем в колоннах с нулями в n-ом ряду
            if is_in_column(field, i, j.x) or is_in_square(field, i, get_square_id(j)):
                if i in field[n][j.x].possible:  # Отмечаем, что в клетке [n][j.x] не может быть цифры i
                    field[n][j.x].possible.discard(i)
                    changed = True
    return changed


# Обрабатывает n-ый столбец
def do_column(L, n):
    changed = False
    absent = absent_column(field, n)
    zero_squares = get_zeroes_column(field, n)
    exist = get_column(L, n)
    for i in range(9):  # В столбце нет повторений
        L[i][n].possible.difference_update(exist)
    for i in absent:  # Перебираем отсутствующие цифры в n-ой колонне
        for j in zero_squares:  # Ищем в строках с нулями в n-ой колонне
            if is_in_row(field, i, j.y) or is_in_square(field, i, get_square_id(j)):
                if i in field[j.y][n].possible:  # Отмечаем, что в клетке [j.y][n] не может быть цифры i
                    field[j.y][n].possible.discard(i)
                    changed = True
    return changed


# Обрабатывает n-ый квадрат
def do_square(L, n):
    changed = False
    absent = absent_square(L, n)
    zero_squares = get_zeroes_square(L, n)
    exist = get_square(L, n)
    a = n // 3
    b = n % 3  # В квадрате нет повторений
    for i in range(3 * a, 3 * a + 3):
        for j in range(3 * b, 3 * b + 3):
            L[i][j].possible.difference_update(exist)
    for i in absent:  # Перебираем отсутствующие цифры в n-ом квадрате
        for j in zero_squares:  # Ищем в строках и столбцах
            if is_in_row(field, i, j.y) or is_in_column(field, i, j.x):
                if i in field[j.y][j.x].possible:
                    field[j.y][j.x].possible.discard(i)
                    changed = True
    return changed


# Ввод данных
existing = set()
field = [[square(i, j) for i in range(9)] for j in range(9)]  # Создаём клетки, одновременно заполняя их поля
for i in range(9):
    existing.clear()
    row = input().split()
    for j in range(9):
        field[i][j].data = int(row[j])
        if field[i][j].data != 0:
            existing.add(field[i][j].data)  # Теперь в existing находятся цифры, существующие в ряду
    for j in range(9):
        if field[i][j].data == 0:  # Клеткам с неизвестной цифрой создаём поле possible
            field[i][j].possible = basic_set - existing

# Решение судоку
proceed1 = True
proceed2 = True
while proceed1 or proceed2:
    old = copy.deepcopy(field)
    proceed1 = False
    proceed2 = False
    for k in range(9):  # Перебираем ряды [0; 8]
        if not row_done(field, k):
            proceed1 = do_row(field, k) or proceed1
    proceed2 = confirm(field) or proceed2
    for k in range(9):  # Перебираем столбцы [0;8]
        if not column_done(field, k):
            proceed1 = do_column(field, k) or proceed1
    proceed2 = confirm(field) or proceed2
    for k in range(9):  # Перебираем квадраты [0; 8]
        if not square_done(field, k):
            proceed1 = do_square(field, k) or proceed1
    proceed2 = confirm(field) or proceed2
    print_delta(old, field)
# print_data(field)
