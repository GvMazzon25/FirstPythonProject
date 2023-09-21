import validations as val
import re
import operation as op


parenthesis = {')': '(', '}':'{', ']':'['}

def create_array(equation):
    array = []
    regex = r'(\d+|[+\-*/()])'
    array = re.split(regex, equation)
    array = [item for item in array if item.strip()]
    print(array)
    return array

def parentheses_detector(array):
    for element in array:
        if element in '{[()]}':
            print('true')
            return True
        else:
            print('false')
            return False


def do_equation(equation):
    for element in equation:

    return equation


def read_equation(equation):
    par_ceck = parentheses_detector(equation)
    if par_ceck == False:
        result = op.create_result(equation)
    else:
        str_eq = ''.join(equation)
        par_val = val.parentheses_validation(str_eq)
        if par_val == True:
            result = do_equation(equation)
            return result
        else:
            message = "Error"
            return message



def create_result(input):
    result = []
    input_array = create_array(input)
    result = read_equation(input_array)
    return result