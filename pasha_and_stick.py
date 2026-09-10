from sys import stdin, stdout


def main():
    n = int(stdin.readline().strip())

    if n % 2 == 0:
        print((n - 2) // 4)
    else:
        print(0)


if __name__ == "__main__":
    main()
