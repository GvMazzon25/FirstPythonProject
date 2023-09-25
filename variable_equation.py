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
            print(result_right)
        else:
            counter +=1

    return


def variable_transport(left_part, right_part):
    alfabeto = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]

    for element in right_part:
        if right_part in alfabeto:
            print("c'è una variabile")
        else:
            result_right = reseq.risolvi_equazione(right_part)



