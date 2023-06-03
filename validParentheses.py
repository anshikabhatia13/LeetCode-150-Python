def isValid( s: str) -> bool:
    stack=[] # stack sata structure
    mappingctoo={")": "(" , "}": "{" , "]": "["    } # mapping using hash map
    # poping if lhs matches rhs
    opening=set(["(", "{", "["])
    for c in s:
        if c in opening: # if c is LHS of mapingctoo
            stack.append(c)
        elif stack and stack[-1]==mappingctoo[c]:
            stack.pop()
        else:
            return False
        
    if stack: 
        return False
    else :
        return True
            
    
    
    
s = "()"
print(isValid(s))