def is_balaced(expression):
    stack=[]
    pair={')':'(','}':'{',']':'['}
    for ch in expr:
        if ch in "({[":
                 stack.append(ch)
        elif ch in ")}]':
        if not stack or stack.pop()
                 return False
    return not stack
