import resolution_equation as reseq
import ClassVariable as variable

def resolve_variable_equation(input):
    left_part = []
    right_part = []
    counter = 0
    for element in input:
        if element == '=':
            left_part = input[:counter]
            right_part = input[counter+1:]
            result_right = variable_transport(left_part,right_part)
            break
        else:
            counter +=1

    return result_right


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






def variable_transport(left_part, right_part):
    left_index, right_index = search_variable(left_part, right_part)
    if right_index == []:
        result_right = reseq.create_result(right_part)


    return result_right













