from sys import stdin, stdout

def main():
    s1 = list(stdin.readline().strip())
    score_s1 = 0
    good = 0 
    unrecognize = 0 
    score_s2 = 0 
    
    probability = 0 
    
    s2 = list(stdin.readline().strip())
    
    for dir in s1:
        if dir == "+":
            score_s1 += 1
        elif dir == "-":
            score_s1 -= 1
    
    for dir in s2:
        if dir == "+":
            score_s2 += 1
        elif dir == "-":
            score_s2 -= 1
        elif dir == "?":
            unrecognize += 1 
            
    def backtrack(index, current_score):
        nonlocal good 
        if index == unrecognize:
            if current_score == score_s1:
                good += 1 
            
            return 
        backtrack(index + 1, current_score + 1)
        backtrack(index + 1, current_score - 1)    
    backtrack(0, score_s2)
    print(f"{good / pow(2, unrecognize):.12f}")  
if __name__ == "__main__":
    main()