import re

def parentheses_array_generator(equation):
    parArray = []
    parStr =  re.findall(r'[(){}\[\]]', equation)
    parArray.extend(list(parStr))

    print(parArray)
    return parArray

def parentheses_validation(equation):
    array = parentheses_array_generator(equation)
    stack = []

    parenthesis = {')': '(', '}':'{', ']':'['}
    if not array:
        return False
    else:
        for element in array:
            if element in '({[':
                stack.append(element)
            elif element in ')}]':
                if not stack:
                    return False

                if stack[-1] == parenthesis[element]:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0



