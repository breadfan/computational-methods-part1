import numpy as np




def func(x):
    return np.sin(x) + x**2/2


def lagrange(table, n):
    poly = np.poly1d([0])      # giving a type of a polynomial
    for k in range(n):
        psi = np.poly1d([1])
        coeff = 1.0
        for i in range(n):
            if i != k:
                psi = psi * np.poly1d([1, -(table[i][0])])   # multiplication to (x - x_i)
                coeff *= table[k][0] - table[i][0]
        psi /= coeff
        poly += table[k][1] * psi   # poly = poly + f(x_k)*psi - MAIN FORM OF LAGRANGE-POLYNOMIAL INTERPOLATION
    return poly

def lagrangeValue(table, n, y):
    poly = 0.0  # giving a type of a polynomial
    for k in range(n):
        psi = 1.0
        coeff = 1.0
        for i in range(n):
            if i != k:
                psi *= (y - table[i][0])  # multiplication to (y - x_i)
                coeff *= table[k][0] - table[i][0]
        psi /= coeff
        poly += table[k][1] * psi  # poly = poly + f(x_k)*psi - MAIN FORM OF LAGRANGE-POLYNOMIAL INTERPOLATION
    return poly

def newton(table, n):
    poly = np.poly1d([table[0][1]])     # writing A_0
    ddTable = [[]]
    for i in range(n):
        ddTable[0].append(table[i][1])
    for k in range(1, n):       # on columns
        ddTable.append([])
        for i in range(n - k):      # n-k for the diagonal matrix
           ddTable[k].append((ddTable[k - 1][i + 1] - ddTable[k - 1][i]) / (table[i + k][0] - table[i][0]))
        dd = np.poly1d(1)
        for i in range(k):
            dd *= np.poly1d([1, -(table[i][0])])    # counting divide difference, (x - x_i)
        poly += ddTable[k][0] * dd
    return poly


def main():
    program = True
    while(program):

        try:
            print("Введите, пожалуйста, степень n(n < m + 1 =", m + 1, ')')
            n = int(input())
            while n > m:
                print("Введено число, большее m; либо недопустимое число. Пожалуйста, введите корректное n(n < m + 1 =  ", m+1, ')')
                n = int(input())
            y = np.float64(input("Введите, пожалуйста, точку интерполяции:"))
        except:
            print("Не могу понять введенное значение")
        program = False

        table.sort(key=lambda pair: abs(y - pair[0]))
        polynomial = lagrange(table, n + 1)
        errorL = abs(func(y) - lagrangeValue(table, n + 1, y))

        #вывод отсортированной таблицы:
        print("Отсортированная таблица для точки интерполяции y = ", y)
        for i in range(len(table)):
            print("x = ", '{:<30}'.format(table[i][0]), "f(x) = ", '{:>30}'.format(table[i][1]))
        print("Ваш полином в форме Лагранжа: \n", polynomial)
        print("Значение полинома в точке в форме Лагранжа: ", lagrangeValue(table, n + 1, y))
        print("Значение функции в точке: ", func(y))
        print("Погрешность полинома в форме Лагранжа: ", errorL)

        polynomial = newton(table, n + 1)
        errorN = abs(func(y) - polynomial(y))
        print("Ваш полином в форме Ньютона: \n", polynomial)
        print("Значение полинома в точке в форме Ньютона:", polynomial(y))
        print("Значение функции в точке:", func(y))
        print("Погрешность полинома в форме Ньютона:", errorN)
        #продолжение выполнения программы
        misspell = True
        while misspell:
            try:
                str = input("Хотите ли вы продолжать вычисления?(Да/Нет)")
                if (str.lower() == "да") | (str.lower == "y"):
                    program = True
                misspell = False
            except:
                print("Введено слово некорректного формата. Пожалуйста, ответьте \"Да\", либо \"Нет\" ")


print("Программа для вычисления многочлена с помощью метода интерполяции\n Вариант 11".center(30))
print("Подготовил Данил Кизеев, 222 группа \n 2019".center(30))
table = []
a = np.float64(input("Введите, пожалуйста, левую границу промежутка(a):"))
b = np.float64(input("Введите, пожалуйста, правую границу промежутка(b):"))
m = int(input("Введите, пожалуйста, степень разбиения(число m):"))
#table fullfilling
for j in range(m + 1):
    x = a + j * (b - a) / m
    table.append((x, func(x)))

#table printing
print("Таблица значений".center(60))
for i in range(len(table)):
    print("x = ", '{:<30}'.format(table[i][0]), "f(x) = ", '{:>30}'.format(table[i][1]))
main()
