def isIsomorphic( s: str, t: str) -> bool:
    StoT={}
    TtoS={}
    for i in range(len(s)):
        char1=s[i]
        char2=t[i]
        if ((char1 in StoT and StoT[char1]!=char2) or (char2 in TtoS and TtoS[char2]!=char1)):
            return False
        StoT[char1]=char2
        TtoS[char2]=char1
        
    return True

s = "egg"
t = "add"
s = "foo"
t = "bar"
s = "paper"
t = "title"
print(isIsomorphic(s,t))
