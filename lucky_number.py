from sys import stdin, stdout


def main():
    n = int(stdin.readline().strip())

    result = pow(2, n + 1) - 2

    print(result)


if __name__ == "__main__":
    main()
