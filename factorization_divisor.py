import manup
    n = 2**2 * 3**2 * 5**2

    print('# 素因数')
    fct = factorize(n)
    print(fct, num(fct))

    print('# 約数')
    for div in divisorize(fct):
        print(div, num(div))
