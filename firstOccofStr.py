# two wanys: O(nm) and O(n+m)
# O(nm) is brute force and O(n+m ) is KYM algo

# THIS IS A SOL OF O(nm) AND THE COMMENTED IS GOOD LOGIC BUT DOESN'T GET ACCEPTED DUE TO EXCEEDED TIME
def strStr(haystack: str, needle: str) -> int:
    if needle == " ":
        return 0
    for i in range(len(haystack)+1-len(needle)):
        # for j in range(len(needle)):
        #     if haystack[i+j]!=needle[j]:
        #         break 
        #     if j == len(needle)-1:
        #         return i 
        if haystack[i : i+len(needle)]==needle:
            return i
    return -1 
 
###########THIS IS O(n+m) KNUTH MORRIS PRATT ALGO
    

haystack = "sadbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
print(strStr(haystack, needle))

