def valid(bracket):
    s = []
    for b in bracket:
        if b == "(" or b == "[":
            s.append(b)
        elif b == ")":
            if not s:
                return False
            elif s[-1] == "(":
                s.pop()
            else:
                return False
        elif b == "]":
            if not s:
                return False
            elif s[-1] == "[":
                s.pop()
            else:
                return False
    return True if not s else False


def calc(n):
    total = 0
    while True:
        top = stack.pop()
        if top == "(" or top == "[":
            break
        total += top

    return total*n if total else n


bracket = list(input())

stack = []

if valid(bracket):
    for b in bracket:
        if b == "(" or b == "[":
            stack.append(b)
        elif b == ")":
            tmp = calc(2)
            stack.append(tmp)
        elif b == "]":
            tmp = calc(3)
            stack.append(tmp)
    print(sum(stack))

else:
    print(0)
