import re

def get_equation():

    equation = input("Inserisci l'equazione: ")
    return equation

def extract_parentheses(equation):
    parStr = re.findall(r'[(){}\[\]]', equation)
    return parStr

def control_response(response):
    if response in 'Yy':
        return True
    elif response in 'Nn':
        return False
    else:
        return False

def create_array(equation):
    array = []
    regex = r'(\d+|[+\-*/()])'
    array = re.split(regex, equation)
    array = [item for item in array if item.strip()]
    return array

def parentheses_detector(array):
    for element in array:
        if element in '{[()]}':
            return True
        else:
            return False

def classifier_elements(input_str):

    results = {
        'numbers': [],
        'parentheses': [],
        'letters': [],
        'signs': []
    }

    # Regex per le diverse categorie
    regex_patterns = {
        'numbers': r'\d+',
        'parentheses': r'[(){}\[\]]',
        'letters': r'[a-zA-Z]',
        'signs': r'[+\-*/]'
    }

    for category, regex_pattern in regex_patterns.items():
        elements = re.findall(regex_pattern, input_str)
        for element in elements:
            results[category].extend(list(element))

    return results



def selection_mode(input_str):
    results = classifier_elements(input_str)
    numbers = results['numbers']
    parentheses = results['parentheses']
    letters = results['letters']
    signs = results['signs']

    if not numbers or not signs:
        print('Error')
        return 'Error'
    elif not parentheses and not letters:
        print('M-OP')
        return 'M-OP'
    elif letters and numbers and signs:
        print('M-EQ')
        return 'M-EQ'
    elif parentheses and signs and numbers:
        print('M-PAR')
        return 'M-PAR'





