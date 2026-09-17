from sys import stdin, stdout 

def main():
    MOD = 998244353
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()
    
    left = 0 
    
    while s[left] == s[0] and left < n:
        left += 1
        
    right = 0 
    
    while s[n-1 - right] == s[-1] and right < n:
        right += 1
        
    if s[0] != s[-1]:
        return (left + right + 1) % MOD
    if s[0] == s[-1]:
        return (left+1) * (right+1) % MOD
        
if __name__ == "__main__":
    print(main())