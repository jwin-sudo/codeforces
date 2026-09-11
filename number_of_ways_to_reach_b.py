from sys import stdin

MOD = 10**9 + 7

def main():
    T = int(stdin.readline())

    while T > 0:
        n = int(stdin.readline())

        ans = n * (n - 3) // 2

        print(ans % MOD)

        T -= 1

if __name__ == "__main__":
    main()