import utility
import resolution_equation as resolve
import variable_equation as veq
def base_function():
    user_input = utility.get_equation()
    user_input = user_input.replace(" ", "")
    mode = utility.chose_mode(user_input)
    if not mode:
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
        if control:
            base_function()
        else:
            print('GoodBye')