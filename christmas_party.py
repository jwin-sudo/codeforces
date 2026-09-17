from sys import stdin, stdout

def main():
    n = int(stdin.readline().strip())
    MOD = 10**9 + 7

    if n == 1:
        return 0 
    else:
        d0 = 1  # D0
        d1 = 0  # D1

        for i in range(2, n + 1):
            d2 = (i - 1) * (d1 + d0) % MOD
            d0, d1 = d1, d2

    return d1

if __name__ == "__main__":
    print(main())