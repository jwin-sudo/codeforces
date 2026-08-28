'''
Arpa's hard exam and Mehrdad's naive cheat
'''
from sys import stdin, stdout 

def main():
    T = int(stdin.readline().strip())
    while T > 0:
        A, B, C, P = list(map(int, stdin.readline().strip().split()))
        
        exponent = pow(B, C, P-1)
        res = pow(A, exponent, P)
        print(res)

        T -= 1
    
if __name__ == "__main__":
    main()