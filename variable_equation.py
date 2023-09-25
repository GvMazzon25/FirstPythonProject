import resolution_equation as reseq

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


def variable_transport(left_part, right_part):
    alfabeto = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]

    for element in right_part:
        if element in alfabeto:
            print("c'è una variabile")
            break
        else:
            for element in left_part:
                for element in left_part:
                    if isinstance(element, (int, float)):
                        print('Numeri a sinistra')
                        break
                    else:
                        result_right = reseq.create_result(right_part)
                        return result_right










