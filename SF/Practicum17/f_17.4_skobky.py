# Функция проверяет парность скобок методом стека
def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент — открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит, возвращаем True, иначе — False
    return len(stack) == 0


string1 = '(()(())()())))'
print(par_checker(string1))
print(par_checker("(5+6)*(7+8)/(4+3)"))
