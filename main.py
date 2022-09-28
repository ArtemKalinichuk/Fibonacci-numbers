def Fibonaci(n, arr: list):
    for index in range(n):
        arr.append(arr[index] + arr[index + 1])


def main():
    result = [0, 1]
    Fibonaci(9,result)
    print(result)

if __name__ == "__main__":
    main()
