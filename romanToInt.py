def romanToInt( s: str) -> int:
    #add if largest to smallest
    #subtract if smaller to larger
    #hashmap 
    roman ={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000 }
    output=0
    
    for i in range(len(s)):
        if i<len(s)-1 and roman[s[i]]<roman[s[i+1]]:
            output=output-roman[s[i]]
        else:
            output=output+roman[s[i]]
    print(output)
s = "III"
s = "LVIII"
s = "MCMXCIV"
romanToInt(s)