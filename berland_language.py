from sys import stdin, stdout 


def main():
    
    word = stdin.readline().strip()
    
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    
    isUsed = [False] * len(alphabet)
    output = []
    def permutation(path, isUsed):
        if len(path) == 2:
            output.append("".join(path[:]))
            return 
        
        for i in range(0, len(alphabet), 1):
            if isUsed[i]:
                continue 
            
            isUsed[i] = True 
            path.append(alphabet[i])
            permutation(path, isUsed)
            path.pop()
            
            isUsed[i] = False 
            
    permutation([], isUsed)
            
    output = sorted(output)

    dictionary = {}
    
    for i in range(0, len(output)):
        dictionary[i+1] = output[i]
        

    for key, value in dictionary.items():
        if word == value:
            print(key)
            
if __name__ == "__main__":
    t = int(stdin.readline().strip())
    while t > 0:
        main()
        t -= 1