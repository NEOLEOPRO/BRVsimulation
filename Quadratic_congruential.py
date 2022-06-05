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


def qcg(m: int, k1=1, k2=1, seed1=1, seed2=1, C=1, end=20):
    """
    A(i) = (k2 * A(i-1)^2 + k1 * A(i-2) + C) mod m, i = 1,2,3...
    m: m
    k1: k1
    k2: k2
    seed1: A1
    seed2: A2
    end: number of last element needed to display
    To display the first n elements set the parameter end.
    Usually prints the first 20.
    Если по формуле вместо A(i-2) - A(i-1), то чтобы период был наибольшим:
    1) (c, m) = 1 т.е c и m – взаимно простые числа;
    2) k2 и k1−1 – кратны q, где q – любой нечетный простой делитель модуля m;
    3) k2 – четное число, причем
    k2 = (k1 − 1) mod 4, если m кратно 4,
    k2 = (k1 − 1) mod 2, если m кратно 2;
    4) если модуль m кратен 9, то d != 3c mod 9.
    """
    if k2 == 1 and k1 == 1:
        f = factor(m)
        k = [i for i in f if i > 2]
        for l in range(len(k)):
            k2 = k2 * k[l]
        for l in range(len(k)):
            k1 = k1 * k[l]
        k2 *= 2
        k1 *= 2


    if C == 1:
        C = 2 * round(m / 3)
        while gcd(m, C) != 1:
            C = C + 1

    if seed1 == 1:
        seed1 = C + 2
    if seed2 == 1:
        seed2 = C - 2

    seeds = [0] * m
    for i in range(m):
        seeds[i] = seed1
        seed1, seed2 = seed2, (k2 * (seed2 ** 2) + k1 * seed1 + C) % m

    return seeds[0:end], sorted(seeds)[0:end]


print(qcg(3145728))
