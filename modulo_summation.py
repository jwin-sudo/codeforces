from sys import stdin, stdout 

def main():
    n = int(stdin.readline().strip())
    
    values = list(map(int, stdin.readline().strip().split()))
    
    total = 0 
    
    for num in values:
        total += num - 1
    print(total)
            
    
if __name__ == "__main__":
    main()