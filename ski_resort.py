from sys import stdin, stdout 


def main():
    t = int(stdin.readline().strip())
    
    while t > 0:
        n, k, q = list(map(int, stdin.readline().strip().split()))
        
        a = list(map(int, stdin.readline().strip().split()))
        
        ans = 0 
        length = 0 
        for temp in a: 
            if temp <= q:
                length += 1 
                
                if length >= k:
                    ans += length - k + 1 
            
            else:
                length = 0 
        
        print(ans)
        
        t -= 1
        
if __name__ == "__main__":
    main()