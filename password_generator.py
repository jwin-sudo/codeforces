from sys import stdin, stdout

def main():
    chars = list(stdin.readline().strip().split())
    print(chars)
    min_length = 2
    max_length = 4
    output = []
    
    def permutations(path, start):
        if len(path) == max_length:
            return 
        if len(path) >= min_length:
            output.append(path)
        
        for i in range(start, len(chars), 1):
            permutations(path + chars[i], i)

    permutations("", 0)
    print(output)
        
        
if __name__ == "__main__":
    main()