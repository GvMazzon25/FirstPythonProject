import resolution_equation as reseq
import ClassVariable as Variable
import re


def search_variable(left_part, right_part):
    left_variables_position = []
    right_variables_position = []
    left_index = 0
    right_index = 0
    alfabeto = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
    for element in right_part:
        if element in alfabeto:
            right_variables_position.append(right_index)
            right_index += 1
        else:
            right_index += 1
    for element in left_part:
        if element in alfabeto:
            left_variables_position.append(left_index)
            left_index += 1
        else:
            left_index += 1
    return left_variables_position, right_variables_position


def generate_variable(index, expression):
    variable_base = expression[index]
    variable_sign = '+'
    variable_number = '1'
    list_num = []
    if index == 0:
        variable = Variable.Variable(variable_sign, variable_number, variable_base)
    else:
        for i in range(index, - 1, -1):
            if expression[i] in ['+', '-', '*', '/']:
                variable_sign = expression[i]
                if expression[i + 1] == variable_base:
                    variable_number = '1'
                    variable = Variable.Variable(variable_sign, variable_number, variable_base)
                    return variable
                break
            elif expression[i].isdigit():
                list_num.insert(0, expression[i])

        variable_number = "".join(list_num)

    variable = Variable.Variable(variable_sign, variable_number, variable_base)
    return variable


def create_variable_arr(indexes, expression):
    variable_arr = []
    for i in indexes:
        variable = generate_variable(i, expression)
        variable_arr.append(variable)

    return variable_arr


def variable_transport(left_part, right_part, left_index, right_index):
    variable_left = create_variable_arr(left_index, left_part)
    variable_right = create_variable_arr(right_index, right_part)
    left_arr = []
    right_arr = []
    for element in variable_right:
        variable = element
        right_arr.append(variable)
        sign = variable.sign
        if sign == '+':
            variable2 = Variable.Variable('-', variable.mult, variable.variable)
            right_arr.append(variable2)
            variable_left.append(variable2)
        elif sign == '-':
            variable2 = Variable.Variable('+', variable.mult, variable.variable)
            right_arr.append(variable2)
            variable_left.append(variable2)
        elif sign == '*':
            variable2 = Variable.Variable('/', variable.mult, variable.variable)
            right_arr.append(variable2)
            variable_left.append(variable2)
        elif sign == '/':
            variable2 = Variable.Variable('*', variable.mult, variable.variable)
            right_arr.append(variable2)
            variable_left.append(variable2)
    left = do_operation(variable_left)
    right = do_operation(right_arr)
    return left, right


def search_number(left_part, right_part):
    left_indices = []
    right_indices = []
    left_index = 0
    right_index = 0

    for element in right_part:
        if element.isdigit():
            if (right_index == 0 or not right_part[right_index - 1].isalpha()) and \
                    (right_index == len(right_part) - 1 or not right_part[right_index + 1].isalpha()):
                right_indices.append(right_index)
            right_index += 1
        else:
            right_index += 1

    for element in left_part:
        if element.isdigit():
            if (left_index == 0 or not left_part[left_index - 1].isalpha()) and \
                    (left_index == len(left_part) - 1 or not left_part[left_index + 1].isalpha()):
                left_indices.append(left_index)
            left_index += 1
        else:
            left_index += 1

    return left_indices, right_indices

def create_number_array(indexes, array):
    number_array = []
    return number_array

def number_transport(left_part, right_part, left_index, right_index):
    number_left = ''
    number_right = ''
    result = ''
    return result


def do_operation(array):
    first_var = array[0]
    second_var = array[1]
    if second_var is not []:
        sign1 = first_var.sign
        sign2 = second_var.sign
        if sign1 == '+' and sign2 == '-':
            array[1].sign = '+'
        elif sign1 == '-' and sign2 == '+':
            array[1].sign = '-'
        elif sign1 == '-' and sign2 == '-':
            array[1].sign = '+'

    operation = ''
    for indice, variable in enumerate(array):
        if indice == 0:
            number = variable.mult
            operation = operation + str(number)
        else:
            sign = variable.sign
            number = variable.mult
            operation = operation + sign + str(number)

    result = reseq.create_result(operation)
    return result


def variable_operation(left_part, right_part):
    left_index, right_index = search_variable(left_part, right_part)
    if not right_index:
        result_right = reseq.create_result(right_part)
        result = str(left_part) + ' = ' + str(result_right)
    else:
        left, right = variable_transport(left_part, right_part, left_index, right_index);
        result = str(left) + '=' + str(right)
    return result


def resolve_variable_equation(user_input):
    result = []
    left_part = []
    right_part = []
    counter = 0
    for element in user_input:
        if element == '=':
            left_part = user_input[:counter]
            right_part = user_input[counter + 1:]
            left, right = variable_operation(left_part, right_part)
            result = str(left) + '=' + str(right)
            break
        else:
            counter += 1

    return result
