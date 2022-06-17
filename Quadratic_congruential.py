import random
import matplotlib.pyplot as plt
import numpy


def factor(n):
    """
    Prime factor decomposition
    """
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


def gcd(x: int, y: int):
    """
    Greatest common divisor
    """
    s = 0
    if x > y:
        temp = y
    else:
        temp = x
    for i in range(1, temp + 1):
        if (x % i == 0) and (y % i == 0):
            s = i
    return s


def qcg(m, k1, k2, seed1, seed2, C, end):
    """
    A(i) = (k2 * A(i-1)^2 + k1 * A(i-2) + C) mod m, i = 1,2,3...

    m: m модуль

    k1: k1 первый коэффициент

    k2: k2 второй коэффициент

    seed1: A1 первое стартовое значение(возводится во 2ю степень)

    seed2: A2 второе стартовое значение

    end: количество первых чисел которые нужно отобразить
    """
    print('Использованные значения: Стартовые значения:', seed1, seed2, 'Коэффициенты:', k1, k2, 'C:', C, 'm:', m)
    if not (C % 2):
        C = C + 1
    seeds = [0] * end
    for i in range(end):
        seeds[i] = seed1 / m
        seed1, seed2 = seed2, (k2 * (seed2 ** 2) + k1 * seed1 + C) % m
    M = numpy.average(seeds)
    D = numpy.var(seeds)
    return M, D, seeds


# можно задать значения к функции чтобы упростить вычисления, увеличивать числа не рекомендуется:
print('Если коэф. корреляции близок к нулю, это признак хорошего качества входных параметров рекурентной фунции \n'
      'для генерации последовательности максимальной длинны, соотвественно мат ожидание и дисперсия должны быть \n'
      'близко равны 0.5 и 1/12(0.083)')
y = input('Ввести значения? Enter - использовать оптимальные:')
if y=='':
    m = 2 ** 32
    k1 = random.randint(0, m)
    while (k1 - 1) % 4 != 0:
        k1 += 1
    k2 = random.randint(0, m)
    while (k2 - 1) % 4 != 0:
        k2 += 1
    seed1 = random.randint(0, m)
    seed2 = random.randint(0, m)
    C = 1013904223
    end = 2 ** 20
    res = qcg(m=int(m), k1=int(k1), k2=int(k2), seed1=int(seed1), seed2=int(seed2), C=int(C), end=int(end))
else:
    m = input('Введите модуль m, Enter - использовать стандартное:')
    if m == '':
        m = 2 ** 32
    k1 = input('Введите коэффициент k1, Enter - использовать стандартное:')
    if k1 == '':
        k1 = random.randint(0, m)
        while (k1-1)%4!=0:
            k1 +=1
    k2 = input('Введите коэффициент k2, Enter - использовать стандартное:')
    if k2 == '':
        k2 = random.randint(0, m)
        while (k2-1)%4!=0:
            k2 +=1
    seed1 = input('Введите seed1, Enter - использовать стандартное:')
    if seed1 == 1:
        seed1 = random.randint(0, m)
    seed2 = input('Введите seed2, Enter - использовать стандартное:')
    if seed2 == 1:
        seed2 = random.randint(0, m)
    C = input('Введите константу C, Enter - использовать стандартное:')
    if C == 1:
        C = 1013904223
    end = input('Введите длину последовательности end, Enter - использовать стандартное:')
    if end == 1:
        end = 2 ** 20
    res = qcg(m=int(m), k1=int(k1), k2=int(k2), seed1=int(seed1), seed2=int(seed2), C=int(C), end=int(end))

z = res[2]

print('Мат ожидание:', res[0])
print('Дисперсия:', res[1])
print()

fig = plt.figure()
bins = input('Введите кол-во интервалов для гистограммы, Enter - стандартное:')
if bins=='':
    bins = 30
else:
    bins = int(bins)
d = input('Выберите накоплением или нормированная, Enter - первое:')
if d=='':
    d = False
    log = True
else:
    d = True
    log = False
plt.hist(z, bins=bins, log=log, density=d)
plt.title(
    'Гистограмма квадратичного конгруэнтного метода площадь\nстолбца - вероятность что z(i) попадёт в T(k) интервал')
if d == False:
    plt.ylabel(f'Кол-во точек в интервале длинной {"%.2f" % (1/bins)}')
else:
    plt.ylabel('Вес интервала T(k)')
plt.xlabel('Интервалы T(k) и входящие в них значения z(i)')
plt.subplots_adjust(left=.23)
plt.grid(True)

plt.show()

fig = plt.figure()

s = input('Задать шаг корреляции двух Z, Enter - стандартное:')
if s=='':
    s = 5  # задать шаг корреляции двух Z
else:
    s = int(s)
e = 0
for i in range(s, len(z)):
    e += z[i]*z[i-s]
corr = 12 * e / (len(z) - s) - 3
print('Коэффициент корреляции:', corr)

n = input('Введите кол-во точек для графика корреляции, Enter - стандартное:')
if n=='':
    n = 1000
for i in range(s, len(z), len(z)//int(n)): # отображает 1024 точки на графике взятых из массива
    plt.scatter(z[i], z[i - s], s=3)
plt.ylabel('Z(i)')
plt.xlabel('Z(i-s)')
plt.grid(True)

plt.show()
