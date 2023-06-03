def wordPattern( pattern: str, s: str) -> bool:
    words=s.split(" ")
    if len(pattern)!=len(words):
        return False
    patterntoS={}
    Stopattern={}
    
    for i,j  in zip(pattern, words):
        if ((i in patterntoS and patterntoS[i]!=j) or (j in Stopattern and Stopattern[j]!=i)):
            return False
        patterntoS[i]=j
        Stopattern[j]=i
        
    return True


pattern = "abba"

s = "dog cat cat dog"
pattern = "abba"
s = "dog cat cat fish"
pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))