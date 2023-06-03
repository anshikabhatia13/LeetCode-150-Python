def isPalindrome( s: str) -> bool:
#This one takes more time
    left=0
    right = len(s)-1
    while left < right:
        while left < right and not alphanum(s[left]):
            left=left+1
        while right > left and not alphanum(s[right]):
            right=right-1
        if s[left].lower()!=s[right].lower():
            return False
        left=left+1
        right=right-1
    return True

def alphanum(c):
    return(ord('A') <= ord(c) <= ord('Z') or
           ord('a') <= ord(c) <= ord('z') or
           ord('0') <= ord(c) <= ord('9') )
                 
        
    
        
        




# def isPalindrome( s: str) -> bool:
#     #This is O(n) space solution
#         new=""
#         for c in s:
#             if c.isalnum():
#                 new+=c.lower()
#         return new==new[::-1]

s = "A man, a plan, a canal: Panama"
# s = "race a car"
print(isPalindrome(s))