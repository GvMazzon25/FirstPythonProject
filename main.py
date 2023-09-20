import operation as op
import utility
import validations as vld
import parentheses as par


def main():

    while True:
        user_input = utility.get_equation()
        result = par.create_result(user_input)
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