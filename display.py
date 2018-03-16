from __future__ import print_function


def hdr(h):
    print('\n*** {} ***'.format(h))


def table(f, xs):
    d = 5
    ds = str(d)
    row = '|  {:.' + ds + 'f} ' + \
          '|  {:.' + ds + 'f} |'
          
    print('|   {0}x |{0}f(x) |'\
    	    .format(d * ' '))
    print('+----{0}-+----{0}-+'\
    	    .format(d * '-'))
    for x in xs:
        print(row.format(x, f(x)))


def main():
    hdr('pretty table')
    table(lambda x: x**2, [0, 1, 3])


if __name__ == '__main__':
    main()