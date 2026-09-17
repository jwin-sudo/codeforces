from sys import stdin, stdout

def main():
    k = int(stdin.readline().strip())
    MOD = 10**9 + 7


    exponent = (pow(2, k, MOD - 1) - 2) % (MOD - 1)

    answer = 6 * pow(4, exponent, MOD) % MOD

    print(answer)

if __name__ == "__main__":
    main()