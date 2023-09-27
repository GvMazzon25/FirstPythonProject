import resolution_equation as reseq
import ClassVariable as Variable
import re

def resolve_variable_equation(input):
    left_part = []
    right_part = []
    counter = 0
    for element in input:
        if element == '=':
            left_part = input[:counter]
            right_part = input[counter+1:]
            result = variable_operation(left_part,right_part)
            break
        else:
            counter +=1

    return result


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
            right_index+=1

    for element in left_part:
        if element in alfabeto:
            left_variables_position.append(left_index)
            left_index += 1
        else:
            left_index+=1


    return left_variables_position,right_variables_position

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
                break
            elif expression[i].isdigit():
                list_num.insert(0, expression[i])

        variable_number = str(list_num)
        variable = Variable.Variable(variable_sign, variable_number, variable_base)

    return variable







def create_variable_arr(indexes, expression):
    variable_arr = []
    for i in indexes:
        variable = generate_variable(i,expression)
        variable_arr.append(variable.sign + variable.mult + variable.variable)

    print(variable_arr)
    return variable_arr




def variable_transport(left_part, right_part, left_index, right_index):
    variable_left = create_variable_arr(left_index, left_part)
    variable_right = create_variable_arr(right_index,right_part)
    return variable_left, variable_right






def  variable_operation(left_part, right_part):
    left_index, right_index = search_variable(left_part, right_part)
    if right_index == []:
        result_right = reseq.create_result(right_part)
        result = str(left_part) + ' = ' + str(result_right)
    else:
        result = variable_transport(left_part, right_part, left_index, right_index);


    return result













