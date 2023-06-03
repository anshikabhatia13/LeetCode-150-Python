def canConstruct(ransomNote: str, magazine: str) -> bool:
    #initialize two hashmaps for ransomnote and maganzine
    mag={}
    rn={}
    #in python hashmaps are constructed using dictionaries
    for rnchar in ransomNote:
        if rnchar not in rn:
            rn[rnchar]=1
        else:
            rn[rnchar]+=1
    for mgchar in magazine:
        if mgchar not in mag:
            mag[mgchar]=1
        else:
            mag[mgchar]+=1
            
    for char in ransomNote:
        if char not in mag or mag[char] < rn[char]:
            return False
    return True

ransomNote = "a"
magazine = "b"
ransomNote = "aa"
magazine = "ab"
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
        
        