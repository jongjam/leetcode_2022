def evalRPN(tokens):
    # find first operation
    # S is stack... when first operation is found use the last two spots
    # Add result to the stack

    # When further operations are found use the previous item plus the top of stack
    s = []

    for op in tokens :
        if op == '+' or op == '-' or op == '*' or op == '/' :
            a = s.pop()
            b = s.pop()
            result = eq_eval(a, b, op)
            s.append(result)
        else :
            # it's not an op
            s.append(int(op))
    
    return s[0]


def eq_eval(a, b, op) :
    if op == '+' :
        return a + b
    elif op == '-':
        return b - a
    elif op == '*':
        return a * b
    elif op == '/':
        return int(b / a)
    
def main() :
    print(evalRPN(["4","13","5","/","+"]))
main()
        