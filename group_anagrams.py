from collections import Counter
def group_anagrams(arr):
    sorted_words = ["".join(sorted(word)) for word in arr]
    mp = Counter(sorted_words)
    
    most_common = mp.most_common(2)
    if len(most_common) >= 2:
        if most_common[0][1] == most_common[1][1]:
            return "not good"
        else:
            return mp.most_common(1)
    else:
        return mp.most_common(1)
   
    

             
            

arr = ["cart", "crab", "barc", "ract", "actr"] 
print(group_anagrams(arr))

arr = ["bar"]
print(group_anagrams(arr))

arr = ["bar", "car"]
print(group_anagrams(arr))