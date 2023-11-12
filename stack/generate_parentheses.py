class Solution:
    # I'm not sure how to do this iterative approach tbh
    def generateParenthesis(self, n: int) -> List[str]:
        # Using stack... generate different kinds of parenthesis
    
        result = []
    
        # n = 1 ()
        # n = 2 ()() (()) --> So basically the idea is for every left parantheses you either close it there or add an open
        # n = 3 ()()() or (())
        


        self.helper(n, "(", result, 1, 0)
        return result

    def helper(self, n, s, result, op, cl) :
        if op == n and cl == n: # when there are n amount of ( opening parantheses
            result.append(s)

        if cl < op:
            self.helper(n, s + ")" ,result, op, cl + 1)
        if op <= n :
            self.helper(n, s + "(", result, op + 1, cl)
        

        return result