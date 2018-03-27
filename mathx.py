
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


def factorial(n):
    x = 1
    while n > 1:
        x *= n
        n -= 1
    return x

def over(n, k):
    if n < k:
        n, k = k, n
    return factorial(n) / \
    	      (factorial(k) * \
    	      	factorial(n - k))


if __name__ == '__main__':
    for x in list(linspace(0, 10, 10)):
        print(x)
    
    print('factorial')
    print(factorial(5), 120)
    print(factorial(0), 1)

    print('over(n, k)')
    print(over(52, 5), 2598960)