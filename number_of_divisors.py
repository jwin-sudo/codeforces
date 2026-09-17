from sys import stdin, stdout
import math 

def main():
    T = int(stdin.readline().strip())
    
    while T > 0:
        N = int(stdin.readline().strip())
        count = 0 
        
        for i in range(1, int(math.sqrt(N)) + 1, 1):
            if N % i == 0:
                if i * i == N:
                    count += 1
                else:   
                    count += 2
        print(count)
        
        T -= 1

if __name__ == "__main__":
    main()