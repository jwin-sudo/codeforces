from sys import stdin, stdout

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a 
def main():
    T = int(stdin.readline().strip())
    
    while T > 0:
        A, B, C = list(map(int, stdin.readline().split()))
        
        g = gcd(A, B)
        
        if C % g == 0:
            print('Yes')
        else:
            print('No')
        T -= 1

if __name__ == "__main__":
    main()