def evalRPN(tokens):
    stack=[]
    for char in tokens:
        if(char not in "+-*/"):
            stack.append(char)
        else:
            operand2=int(stack.pop())
            operand1=int(stack.pop())
            if(char=='+'):
                stack.append(operand1+operand2)
            elif(char=='-'):
                stack.append(operand1-operand2)
            elif(char=='*'):
                stack.append(operand1*operand2)
            elif(char=='/'):
                stack.append(int(float(operand1)/operand2))
    return int(stack[-1])

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))