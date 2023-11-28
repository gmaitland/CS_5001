'''
    Lab 8: Stack for Postfix Calculator
'''

from Stack import Stack

def postfix_eval(postfix_expr):
    stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = do_math(token, operand1, operand2)
            stack.push(result)
    return stack.pop()

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def main():
    print(postfix_eval('4 2 /')) # 2.0
    print(postfix_eval('7 8 *')) # 56
    print(postfix_eval('7 8 +')) # 15
    print(postfix_eval('7 8 + 3 2 + /')) # 3.0
    print(postfix_eval('7 8 + 3 4 2 + +')) # 9
    print(postfix_eval('7 8 + 3 4 2 + + +')) # 24

main()
