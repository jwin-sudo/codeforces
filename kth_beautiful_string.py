from sys import stdin

def main():
    t = int(stdin.readline())

    while t > 0:
        n, k = map(int, stdin.readline().split())

        block = 1

        while k > block:
            k -= block
            block += 1

        ans = ['a'] * n

        first_b = n - block - 1
        second_b = n - k

        ans[first_b] = 'b'
        ans[second_b] = 'b'

        print(''.join(ans))

        t -= 1

if __name__ == "__main__":
    main()