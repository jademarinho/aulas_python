def fibonacci(limite):
    result = [0, 1]
    while result[-1] < limite:
        result.append(result[-2] + result[-1])
    return result

if __name__ == '__main__':
    for fib in fibonacci(20000):
        print(fib)