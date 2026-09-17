from sys import stdin, stdout 

def gcd(a, b):
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b 
    return a 
def main():
    T = int(stdin.readline().strip())
    
    while T > 0:
                    
        N = int(stdin.readline().strip())
        
        A = list(map(int,stdin.readline().strip().split()))
        
        curr_gcd = A[0]

        for i in range(1, N, 1):
            curr_gcd = gcd(curr_gcd, A[i])
            
        if curr_gcd >= 2:
            print('Yes')
        else:
            print('No')
        
        
        T -= 1
        
    

    
    
if __name__ == "__main__":
    main() 