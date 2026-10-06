from sys import stdin, stdout

def main():
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split()))
    
    for num in nums:
        count = 0 
        for i in range(1, num+1, 1):
            if num % i == 0:
                count += 1

        if count == 3:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()