from sys import stdin, stdout 

def main():
    n = int(stdin.readline().strip())
    res = 0
    MOD = 10 ** 9 + 7
    while n > 0:
        a, b = map(int, stdin.readline().strip().split())
        res =+ pow(a, b, MOD)
        print(res)
        
        n -= 1
    
if __name__ == "__main__":
    main()