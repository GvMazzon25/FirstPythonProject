import validations as val
import re


def create_array(equation):
    array = []
    regex = r'(\d+|[+\-*/()])'
    array = re.split(regex, equation)
    array = [item for item in array if item.strip()]
    print(array)
    return array

def parentheses_gestor(equation):
    return equation


def read_equation(equation):
    par_list = {')': '(', '}':'{', ']':'['}
    for i, element in equation:
        if element in '{[(':
            parenthesis = element[i]
            while True:
                if element == par_list[parenthesis]:
                    return False






def create_result(input):
    result = []
    result = create_array(input)
    return result