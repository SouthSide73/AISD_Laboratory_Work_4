"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Формируется матрица F следующим образом:
если в Е количество нулей в нечетных столбцах в области 4 больше, чем сумма чисел в нечетных строках в области 1,
то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А
не меняется. После чего вычисляется выражение: К*(A*F)–K*A^T. Выводятся по мере формирования А, F
и все матричные операции последовательно.
"""
import random
import time


def print_matrix(M, matr_name, tt):
    print("Матрица " + matr_name + " промежуточное время = " + str(tt) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()


print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input("\nВы ввели неверное число"
                          "\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, AF, AT = [], [], [], []    # Задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)
    for i in range(row_q):      # Заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    E = []     # Задаем матрицу Е
    size = row_q // 2
    for i in range(size):
        E.append([0] * size)

    for i in range(size):  # Формируем подматрицу E
        for j in range(size):
            E[i][j] = F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(E, "E", time_next - time_prev)

    amount = 0
    summa = 0
    for i in range(size):  # Обрабатываем подматрицу E
        for j in range(size):
            if i > j and j % 2 != 1 and j < size - 1 - i and E[i][j] == 0:
                amount += 1
    for i in range(size):  # Обрабатываем подматрицу E
        for j in range(size):
            if i > j and i % 2 != 1 and j < size - 1 - i:
                summa += E[i][j]
    if amount > summa:
        for i in range(size):    # Меняем подматрицу Е
            for j in range(size):
                if (i == 0) and (j < size - 1 - i) and (j > 0):
                    E[i][j], E[j][size - 1] = E[j][size - 1], E[i][j]
                if (i < j) and (j < size - 1 - i) and (i > 0):
                    E[i][j], E[j][size - 1 - i] = E[j][size - 1 - i], E[i][j]
        print_matrix(E, "E", time_next - time_prev)
        for i in range(size):    # Формируем матрицу F
            for j in range(size):
                F[i][j] = E[i][j]
        print_matrix(F, "F!", time_next - time_prev)
    else:
        for j in range(row_q // 2):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j] \
                    = F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # A*F
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A*F", time_next - time_prev)

    for i in range(row_q):  # K*(A*F)
        for j in range(row_q):
            AF[i][j] = K * AF[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "K*A*F", time_next - time_prev)

    for i in range(row_q):  # A^T
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):  # K*A^T
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K*A^T", time_next - time_prev)

    for i in range(row_q):  # K*(A*F)-K*A^T
        for j in range(row_q):
            AF[i][j] = AF[i][j] - AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "К*(A*F)–K*A^T", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
    print("\nЭто не число. Введите число без сторонних символов.")
