from collections import Counter 

def group_anagram(arr):
    sorted_word = ["".join(sorted(word)) for word in arr]
    mp = Counter(sorted_word)
    
    for key, value in list(mp.items()):
        if value > 1:
            del mp[key]
    output = []
    for word in arr:
        if "".join(sorted(word)) in mp:
            output.append(word)
            
    return output 

arr = ["cart", "crab", "barc", "ract", "actr"]
print(group_anagram(arr))