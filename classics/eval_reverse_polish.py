valid_operators = ["+", "-", "/", "*"]

def eval_reverse_polish(operators_operands_arr):
    result = None
    stack = [] # stack in python - push and pop elements from the front?
    for op in operators_operands_arr:
        try:
            # if op is operand, push it to the stack
            v = int(op)
            stack.insert(0, v)
        except ValueError:
            if op in valid_operators:
                v1 = stack.pop(0)
                v2 = stack.pop(0)                
                if op == '+':
                    stack.insert(0, v2 + v1)
                elif op == '-':
                    stack.insert(0, v2 - v1)
                elif op == '*':
                    stack.insert(0, v2 * v1)
                elif op == '/':
                    stack.insert(0, v2 / v1)
            else:
                raise ValueError("Bad argument: " + op + " is not a valid operator or operand.")
    if len(stack) > 1:
        raise ValueError("Bad arguments: invalid operator operand combination")
    return stack[0]
