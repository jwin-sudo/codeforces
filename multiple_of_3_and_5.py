from sys import stdin, stdout

def main():
    T = int(stdin.readline().strip())
    
    while T > 0:
        N = int(stdin.readline().strip())
        ans = 0 
        
        for i in range(N):
            if i % 3 == 0 or i % 5 == 0:
                ans += i
        print(ans)
        
        T -= 1
    

if __name__ == "__main__":
    main()