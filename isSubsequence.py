def isSubsequence(s: str, t: str) -> bool:
    i,j=0,0
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            i=i+1
            j=j+1
        else:
            j=j+1
    return True if i==len(s) else False
            
s = "abc"
t = "ahbgdc"
# s="axc"
print(isSubsequence(s,t))
         