from sys import stdin, stdout 

import math 
def main():
    n, m = list(map(int, stdin.readline().strip().split()))
    big_team = n - m + 1
    max_pairs = big_team * (big_team - 1) // 2
    
    small = n // m 
    extra = n % m 
    
    min_pairs = (
        (m-extra) * math.comb(small, 2)
        + extra * math.comb(small + 1, 2)
    )    
    
    print(min_pairs, max_pairs)
    
if __name__ == "__main__":
    main()