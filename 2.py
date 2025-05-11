def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci(n):
    fib_sequence = fibonacci(n)
    if n in fib_sequence:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

n = int(input("Informe um número: "))
check_fibonacci(n)
