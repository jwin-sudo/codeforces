from sys import stdin, stdout 

def main():
    n = int(stdin.readline().strip())
    values = list(map(int, stdin.readline().strip().split()))
    
    min_value = min(values)
    max_value = max(values)
    
    max_diff = max_value - min_value
    
    min_ways = values.count(min_value)
    max_ways = values.count(max_value)
    
    if min_value == max_value:
        ways = n*(n-1) // 2
    else:
        ways = min_ways * max_ways
    print(max_diff)
    print(ways)

if __name__ == "__main__":
    main()