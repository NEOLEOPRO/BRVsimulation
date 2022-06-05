from typing import Generator

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


def lcg(mod: int, a=1, c=1, seed=1, end=20) -> Generator[int, None, None]:
    """
    Linear congruential generator.
    If you set the function parameters incorrectly, the sequence will be much shorter.
    To display the first n elements set the parameter end.
    Usually prints the first 20.
    x(i) = (a * x(i-1) + c) mod m
    mod: m
    a: a
    c: c
    seed: x0
    end: number of last element needed to display
    """
    if a == 1:
        f = factor(mod)
        k = [i for i in f if i > 2]
        for l in range(len(k)):
            a = a * k[l]
        a = a * 4 + 1

    if c == 1:
        c = 2 * round(mod / 3)
        while gcd(mod, c) != 1:
            c = c + 1

    if seed == 1:
        seed = c + 2

    for i in range(end):
        yield seed
        seed = (a * seed + c) % mod


for a in lcg(3145728):
    print(a)
