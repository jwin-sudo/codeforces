from sys import stdin, stdout

def main():
    m = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Biggest A first
    A.sort(reverse=True)

    # Store B together with its original position
    B_with_index = []

    for i in range(m):
        B_with_index.append((B[i], i))

    # Smallest B first
    B_with_index.sort()

    answer = [0] * m

    # Pair biggest A with smallest B
    for i in range(m):
        b_value, original_index = B_with_index[i]
        answer[original_index] = A[i]

    print(*answer)

if __name__ == "__main__":
    main()