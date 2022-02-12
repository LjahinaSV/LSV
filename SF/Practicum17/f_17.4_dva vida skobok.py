# создаём словарь, в котором закрывающая скобка — ключ, открывающая — значение
pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_checker_mod('(([0123]))'))
