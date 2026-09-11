from sys import stdin

MOD = 10**9 + 7
MAX = 10**6

def main():
    fact = [1] * (MAX + 1)

    for i in range(1, MAX + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (MAX + 1)

    inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)

    for i in range(MAX, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    n = int(stdin.readline())

    while n > 0:
        a, b = map(int, stdin.readline().split())

        ans = fact[a]
        ans = ans * inv_fact[b] % MOD
        ans = ans * inv_fact[a - b] % MOD

        print(ans)

        n -= 1

if __name__ == "__main__":
    main()