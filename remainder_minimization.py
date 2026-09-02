from sys import stdin, stdout 

def main():    
    L, R= list(map(int, stdin.readline().strip().split()))
    
    minimum = float('inf')    
    for i in range(L, R+1, 1):
        for j in range(L, R+1, 1):
            smallest = (i * j) % 2019
            if smallest < minimum and i < j:
                minimum = smallest
    
    print(minimum)
            
    
if __name__ == "__main__":
    main()