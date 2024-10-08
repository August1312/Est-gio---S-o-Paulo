def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Digite o número de termos da sequência Fibonacci: "))

fibonacci(n)
