



def resolve_variable_equation(input):
    left_part = []
    right_part = []
    counter = 0
    for element in input:
        if element == '=':
            left_part = input[:counter]
            right_part = input[counter+1:]
            print(left_part,'  ',right_part)
        else:
            counter +=1

    return

