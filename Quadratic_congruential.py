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


def qcg(m=2 ** 20, k1=random.randint(0, 2 ** 32), k2=random.randint(0, 2 ** 32), seed1=1, seed2=1,
        C=random.randint(0, 2 ** 32), end=20):
    """
    A(i) = (k2 * A(i-1)^2 + k1 * A(i-2) + C) mod m, i = 1,2,3...

    m: m модуль

    k1: k1 первый коэффициент

    k2: k2 второй коэффициент

    seed1: A1 первое стартовое значение(возводится во 2ю степень)

    seed2: A2 второе стартовое значение

    end: количество первых чисел которые нужно отобразить
    """
    if seed1 == 1:
        seed1 = random.randint(0, m)
    if seed2 == 1:
        seed2 = random.randint(0, m)
    print('Seeds:', seed1 / m, seed2 / m)
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
res = qcg(end=2 ** 20)
z = res[2]

print('Если коэф. корреляции близок к нулю, это признак хорошего качества входных параметров рекурентной фунции \n'
      'для генерации последовательности максимальной длинны, соотвественно мат ожидание и дисперсия должны быть \n'
      'близко равны 0.5 и 1/12(0.083)')
print()
print('Мат ожидание:', res[0])
print('Дисперсия:', res[1])
print()

fig = plt.figure()
plt.hist(z, bins=10, density=True, log=True)
plt.title(
    'Гистограмма квадратичного конгруэнтного метода площадь\nстолбца - вероятность что z(i) попадёт в T(k) интервал')
plt.ylabel('Вес каждого интервала')
plt.xlabel('Интервалы T(k) и входящие в них значения z(i)')
plt.subplots_adjust(left=.23)
plt.grid(True)

plt.show()

fig = plt.figure()

s = 5  # задать шаг корреляции двух Z
e = 0
for i in range(s, len(z)):
    e += z[i]*z[i-s]
corr = 12 * e / (len(z) - s) - 3
print('Коэффициент корреляции:', corr)

for i in range(s, len(z), len(z)//1024): # отображает 1024 точки на графике взятых из массива
    plt.scatter(z[i], z[i - s], s=3)
plt.ylabel('Z(i)')
plt.xlabel('Z(i-s)')
plt.grid(True)

plt.show()
