from sys import stdin

MOD = 10**9

def main():
    dp = [[0] * 1000 for _ in range(1000)]

    dp[0][0] = 1

    for n in range(1, 1000):
        dp[n][0] = 1
        dp[n][n] = 1

        for r in range(1, n):
            dp[n][r] = (dp[n - 1][r - 1] + dp[n - 1][r]) % MOD

    T = int(stdin.readline())

    while T > 0:
        n = int(stdin.readline())

        print(*dp[n][:n + 1])

        T -= 1

if __name__ == "__main__":
    main()