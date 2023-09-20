import operation as op
import utility
import validations as vld
import parentheses as par

def main():
    user_input = utility.get_equation()
    result = par.create_result(user_input)
    if result == 'Errore':
        print('Errore')
        main()
    else:
        response = input("Do you want to continue?  Y/N  ")
        control = utility.control_response(response)
        if control == True:
            main()
        else:
            print('GoodBye')






main()