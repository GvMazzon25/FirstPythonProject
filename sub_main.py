import utility
import resolution_equation as resolve
import variable_equation as veq
def base_function():
    user_input = utility.get_equation()
    mode = utility.chose_mode(user_input)
    if mode == False:
        result = resolve.create_result(user_input)
    else:
        result = veq.resolve_variable_equation(user_input)

    if result == 'Errore':
        print('Errore')
        base_function()
    else:
        print(result)
        response = input("Do you want to continue?  Y/N  ")
        control = utility.control_response(response)
        if control == True:
            base_function()
        else:
            print('GoodBye')