'''
Arpa's hard exam and Mehrdad's naive cheat
'''
from sys import stdin, stdout 

def main():
    n = int(stdin.readline().strip())
    
    res = pow(1378, n, 10)
    print(res)
if __name__ == "__main__":
    main()