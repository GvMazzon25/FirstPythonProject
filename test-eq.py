import re
import validations as val

def get_equation():
    equation = input("Inserisci l'equazione: ")
    return equation

def sum_variables(x,y):
    sum = x + y
    return sum

def sub_variables(x,y):
    sub = x - y
    return sub

def mult_variables(x,y):
    mult = x * y
    return mult

def diff_variables(x,y):
    diff = x / y
    return diff

def operations(x, y, sign):
    if sign == "*":
        result = mult_variables(x,y)
    elif sign == "/":
        result = diff_variables(x,y)
    elif sign == "+":
        result = sum_variables(x,y)
    elif sign == "-":
        result = sub_variables(x,y)
    return result


def built_array_equation(equation):
    array = []
    regex = r'(\s+|[-+*/()\[\]{}])'
    array = re.split(regex,equation)
    array = [item for item in array if item.strip()]
    if val.parentheses_validation(equation) == False:
       return "Parentesi non valide"
    print(array)
    return array


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




def main():
    while True:
        equation = get_equation()
        array_equation = built_array_equation(equation)
        if array_equation == False:
            break

        print(read_equation(array_equation))
        response = input("Do you want to continue?  Y/N  ")
        print(response)
        if response == "Y" or response == "y":
            continue
        if response == "N" or response == "n":
            break
        else:
            response = input("Please enter a valid value  ")
            continue





main()
