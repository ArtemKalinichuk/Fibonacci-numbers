def Fibonaci(n, arr: list):
    for index in range(n):
        arr.append(arr[index] + arr[index + 1])


def Fibonacci_Rec(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci_Rec(n - 1) + Fibonacci_Rec(n - 2)


def main():
    print(Fibonacci_Rec(9))


if __name__ == "__main__":
    main()
