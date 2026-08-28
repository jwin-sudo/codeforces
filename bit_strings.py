from sys import stdin, stdout 

def main():
    n = int(stdin.readline().strip())
    
    result = pow(2, n, 10**9+7)
    print(result)
if __name__ == "__main__":
    main()