from sys import stdin, stdout

def main():
    n, k = list(map(int, stdin.readline().strip().split()))
    
    s = stdin.readline().strip()
    
    valid_chars = list(stdin.readline().strip().split())
    
    ans = 0 
    length = 0 
    for char in s:
        if char in valid_chars:
            length += 1
        
        else:
            ans += (length * (length + 1)) // 2 
            length = 0 
    
    ans += (length * (length + 1)) // 2 
    print(ans)
    
    
if __name__ == "__main__":
    main()