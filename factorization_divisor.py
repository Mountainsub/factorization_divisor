def sample_code():
    n = 2**2 * 3**2 * 5**2

    print('# 素因数')
    fct = factorize(n)
    print(fct, num(fct))

    print('# 約数')
    for div in divisorize(fct):
        print(div, num(div))


def divisorize(fct):
    b, e = fct.pop() # base, exponen
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e+1)]
    return [pre + suf for pre in pre_div for suf in suf_div]

def factorize(n):
    fct = []
    b, e = 2,0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e += 1
        if e > 0:
            fct.append((b, e))
        b, e = b+ 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

if __name__== '__main__':
    sample_code()
