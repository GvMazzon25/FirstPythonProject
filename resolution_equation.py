import validations as val
import utility
import mathematics as math

def risolvi_equazione(espressione):
    # Funzione di supporto per valutare un'operazione tra due operandi e un operatore
    def calcola(operatore, operandi):
        if operatore == '+':
            return math.sum_variables(operandi[0], operandi[1])
        elif operatore == '-':
            return math.sub_variables(operandi[0], operandi[1])
        elif operatore == '*':
            return math.mult_variables(operandi[0], operandi[1])
        elif operatore == '/':
            return math.diff_variables(operandi[0], operandi[1])
        elif operatore == '^':
            return math.exponentiation(operandi[0], operandi[1])

    # Inizializza uno stack per operandi e operatori
    operandi_stack = []
    operatori_stack = []
    parentesi_stack = []  # Aggiunto uno stack per il controllo dell'ordine delle parentesi

    # Definisci la precedenza degli operatori
    precedenza = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Mappa parentesi di apertura e chiusura
    parentesi_apertura = "([{"
    parentesi_chiusura = ")]}"

    # Dividi l'espressione in token (operandi, operatori e parentesi)
    tokenized_expression = espressione.replace(" ", "")
    tokenized_expression = [char for char in tokenized_expression]

    for token in tokenized_expression:
        if token.isdigit():
            operandi_stack.append(float(token))
        elif token in parentesi_apertura:
            operatori_stack.append(token)
            parentesi_stack.append(token)  # Aggiungi la parentesi aperta allo stack
        elif token in parentesi_chiusura:
            parentesi_aperta_corrispondente = parentesi_apertura[parentesi_chiusura.index(token)]
            while operatori_stack and operatori_stack[-1] != parentesi_aperta_corrispondente:
                operatore = operatori_stack.pop()
                operandi2 = operandi_stack.pop()
                operandi1 = operandi_stack.pop()
                risultato_operazione = calcola(operatore, [operandi1, operandi2])
                operandi_stack.append(risultato_operazione)
            operatori_stack.pop()  # Rimuovi la parentesi aperta corrispondente
            parentesi_stack.pop()  # Rimuovi la parentesi aperta dallo stack
        elif token in "+-*/^":
            while (
                operatori_stack
                and operatori_stack[-1] in "+-*/^"
                and precedenza[token] <= precedenza[operatori_stack[-1]]
            ):
                operatore = operatori_stack.pop()
                operandi2 = operandi_stack.pop()
                operandi1 = operandi_stack.pop()
                risultato_operazione = calcola(operatore, [operandi1, operandi2])
                operandi_stack.append(risultato_operazione)
            operatori_stack.append(token)

    # Controlla se ci sono parentesi rimaste aperte
    if parentesi_stack:
        return 'Error: Le parentesi non sono bilanciate'

    # Esegui tutte le operazioni rimanenti
    while operatori_stack:
        operatore = operatori_stack.pop()
        operandi2 = operandi_stack.pop()
        operandi1 = operandi_stack.pop()
        risultato_operazione = calcola(operatore, [operandi1, operandi2])
        operandi_stack.append(risultato_operazione)

    # Il risultato finale dovrebbe essere sull'unico elemento rimasto nello stack degli operandi
    return operandi_stack[0]



def create_result(espressione):
    print(espressione)
    array_espression = utility.create_array(espressione)
    print(array_espression)
    par_detector = utility.parentheses_detector(array_espression)
    if par_detector == False:
        result = risolvi_equazione(espressione)
        return result
    else:
        val_result = val.parentheses_validation(espressione)
        if val_result == False:
            return 'Error'
        else:
            result = risolvi_equazione(espressione)
            return result

