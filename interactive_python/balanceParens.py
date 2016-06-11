def balanceParens(parensString):
    parensItems = list(parensString)
    stack = []
    for i in range(len(parensItems)):
        item = parensItems[i]
        if item == "(":
            stack.append(item)
        elif item == ")":
            if len(stack) == 0:
                return False
            elif stack.pop() != "(":
                return False
    return len(stack) == 0

print balanceParens("((()())())")


