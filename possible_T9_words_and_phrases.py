def get_possible_words(words, digits):
    mapping = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    
    output = []
    
    def backtrack(path, i):
        if i == len(digits):
            output.append("".join(path[:]))
            return 
        
        for char in mapping[digits[i]]:
            path.append(char)
            backtrack(path, i+1)
            path.pop()
        
    backtrack([], 0)
    
    ans = []
    
    for word in output:
        if word in valid_words:
            ans.append(word)
            
    
    print(ans)
    
valid_words = ["act","bat","cat","acd","test"]
digits = [2, 2, 8]

get_possible_words(valid_words, digits)