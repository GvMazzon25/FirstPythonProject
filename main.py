import operation as op
import utility
import validations as vld
import parentheses as par


def main():

    while True:
        user_input = op.get_equation()
        mode = utility.selection_mode(user_input)
        if mode == 'M-OP':
            op.create_result(user_input)
        elif mode == 'M-PAR':
            par.create_result(user_input)
        elif mode == "M-EQ":
            print('Work in progress')
            continue
        elif mode == "Error":
            print('Work in progress')
            continue


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