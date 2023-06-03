def intToRoman(num:int) ->str:
    #using a list instead of hashmap because order matters
    ListofSyms=[["M", 1000],["CM", 900],["D", 500],["CD", 400],
                ["C", 100],["XC", 90],["L", 50],["XL", 40],
                ["X", 10],["IX", 9],["V", 5],["IV", 4],["I", 1]]
    res=""
    for sym,val in ListofSyms:
        if num//val:
            count=num//val
            res=res+(sym * count)
            num=num%val
    return res
num = 3
num = 58
num = 1994
print(intToRoman(num))