def isValid(s):
    if(s=="" or len(s)%2!=0):
        return False
    stack=[]
    for char in s:
        if(char in ")}]"):
            if(stack):
                opening=stack.pop()
            else:
                return False
            while(opening not in "({["):
                opening=stack.pop()
            if((char==')' and opening!='(') or (char=='}' and opening!='{')or(char==']' and opening!='[')):
                return False
        else:
            stack.append(char)
    if(stack==[]):
        return True
    return False

print(isValid("()[]{}"))
