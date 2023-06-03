def lengthOfLastWord( s: str) -> int:
     
    length=0
    i=len(s)-1
    print(i)
    for j in range(len(s)):
        if s[i]==" ":
            i=i-1
    for j in range(len(s)):
        if i>=0 and s[i]!=" ":
            length+=1
            i=i-1
        else:
            return length
    return length
        

    
    # while s[i]==" ":
    #     i-=1
    # while i>=0 and s[i]!=" ":
    #     length =length+1 
    #     i=i-1     
    # return length
            
        

s = "Hello World"
# s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))