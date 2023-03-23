def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result = result * i
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    num = 7
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
    print(f"{result})