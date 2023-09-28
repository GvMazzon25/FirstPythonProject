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
                print(expression[i])
                list_num.insert(0, expression[i])

        variable_number = "".join(list_num)

    variable = Variable.Variable(variable_sign, variable_number, variable_base)
    return variable


def create_variable_arr(indexes, expression):
    variable_arr = []
    for i in indexes:
        variable = generate_variable(i, expression)
        variable_arr.append(variable)

    print(variable_arr)
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
    print(do_operation(variable_left))
    print(do_operation(right_arr))
    return variable_left, right_arr


def do_operation(array):
    first_var = array[0]
    second_var = array[1]
    print(array[1].sign)
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

    print(operation)
    return operation


def variable_operation(left_part, right_part):
    left_index, right_index = search_variable(left_part, right_part)
    if not right_index:
        result_right = reseq.create_result(right_part)
        result = str(left_part) + ' = ' + str(result_right)
    else:
        result = variable_transport(left_part, right_part, left_index, right_index);
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
            result = variable_operation(left_part, right_part)
            break
        else:
            counter += 1

    return result
