
def linspace(a, b, n):
    a = float(a)
    b = float(b)
    if b < a:
        a, b = b, a
    d = float(b - a)
    d /= n
    while a < b:
        yield a
        a += d
    yield b

if __name__ == '__main__':
    for x in list(linspace(0, 10, 10)):
        print(x)
