from sys import stdin, stdout 

def main():
    MOD = 10**9 + 7

    n = int(input())

    total = pow(3, 3 * n, MOD)
    bad = pow(7, n, MOD)

    answer = (total - bad) % MOD

    print(answer)
if __name__ == "__main__":
    main()