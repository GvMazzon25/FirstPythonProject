import utility
import validations as vld
import resolution_equation as resolve


def main():
    user_input = utility.get_equation()
    result = resolve.create_result(user_input)
    if result == 'Errore':
        print('Errore')
        main()
    else:
        print(result)
        response = input("Do you want to continue?  Y/N  ")
        control = utility.control_response(response)
        if control == True:
            main()
        else:
            print('GoodBye')






main()