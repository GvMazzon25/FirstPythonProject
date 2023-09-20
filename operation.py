import re
import mathematics as mat
import  validations as val



def operations(x, y, sign):
    if sign == "*":
        result = mat.mult_variables(x,y)
    elif sign == "/":
        result = mat.diff_variables(x,y)
    elif sign == "+":
        result = mat.sum_variables(x,y)
    elif sign == "-":
        result = mat.sub_variables(x,y)
    return result


def get_operator(element, equation, index):
    x = int(equation.pop(index - 1))
    sign = equation.pop(index - 1)
    y = int(equation.pop(index -1))
    print(x,sign,y)
    return x, y

def operation_cicle(equation, operator_list, index):
    for i, element in enumerate(equation):
        if element == operator_list[index]:
            x, y = get_operator(element, equation, i)
            result = operations(x, y, operator_list[index])
            equation.insert(i - 1, result)
            break
        else:
            continue

def read_equation(equation):
    operator_list = ["*", "/", "-", "+"]
    indxOp = 0
    while True:
        operation_cicle(equation, operator_list, indxOp)

        indxOp +=1
        operation_cicle(equation, operator_list, indxOp)

        indxOp += 1
        operation_cicle(equation, operator_list, indxOp)

        indxOp += 1
        operation_cicle(equation, operator_list, indxOp)
        indxOp = 0
        if len(equation) == 1:
            break
    return equation


def create_result(input):
    result = read_equation(input)
    print(result)
    return result


