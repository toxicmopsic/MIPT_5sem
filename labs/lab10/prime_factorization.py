import sys
import multiprocessing

def factor(n):
    num = n
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)

    print('{}:'.format(num), ' '.join(map(str, result)))
    return result

def multiprocessing_factor(numbers):
    pool = multiprocessing.Pool(processes=8)
    pool.map(factor, numbers)

if __name__ == '__main__':
    numbers = [int(arg) for arg in sys.argv[1:]]
    multiprocessing_factor(numbers)
