def simplifyPath(path: str) -> str:
    stack=[]# creating a stack for this problem as if .. is encountered we pop
    cur=""# the character currently read
    
    for c in path + "/": # / is already read
        if c=="/": #the next / encountered i.e. // case
            if cur==".." :# the prev read charecter is this
                if stack: stack.pop()# if stack is not empty pop
            elif cur!="" and cur!=".": # if prev element is not . or empty
                stack.append(cur)# add that to stack if not . or end
            cur = ""
        else:
            cur+=c # keep reading
    return "/"+"/".join(stack)# join all elements of stack put a / in between and put / in start
path = "/../"
path="/home/"
path = "/home//foo/"
print(simplifyPath(path))