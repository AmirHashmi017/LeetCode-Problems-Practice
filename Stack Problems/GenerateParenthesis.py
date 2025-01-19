def generateParenthesis(n):
        stack=[]
        result=[]
        def CombinationsBacktracking(openN,closedN):
            if(openN==closedN==n):
                result.append("".join(stack))
                return
            if(openN<n):
                stack.append('(')
                CombinationsBacktracking(openN+1,closedN)
                stack.pop()
            if(closedN<openN):
                stack.append(')')
                CombinationsBacktracking(openN,closedN+1)
                stack.pop()

        CombinationsBacktracking(0,0)
        return result

print(generateParenthesis(3))