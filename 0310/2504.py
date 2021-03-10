def check(arr):
    stack = []
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack: return False
            elif stack[-1] == '(':
                stack.pop()
            else: return False
        elif i == ']':
            if not stack: return False
            elif stack[-1] == "[": stack.pop()
            else: return False
            
    if len(stack) != 0:
        return False
    else:
        return True


def num_sum(n):
    tmp = 0
    while True:
        top = stack.pop()
        if top == '(' or top == '[':
            break
        tmp += top

    if tmp != 0:
        return tmp * n
    else:
        return n


arr = list(input())

if not check(arr):
    print(0)
else:
    stack = []
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            stack.append(num_sum(2))
        elif i == ']':
            stack.append(num_sum(3))        

    print(sum(stack))         