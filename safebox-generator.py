from dfa import DFA
import os

def generateDFA(password: str):
    
    #? DFA:
    #* Se espera que el autómata acepte:
    #* { wxv:  w, v en {L, R}*,  x es la contraseña };
    Automata = DFA()
    Automata.setAlphabet({"L", "R"})

    #* Se comienza con el dibujo del autómata:
    # print(f"\nAutómata generado para \"{password}\":\n")


    #? ESTRUCTURA INICIAL ?#
    '''
    Se espera que el autómata acepte la contraseña de
    la caja fuerte independientemente de lo que venga
    antes de esta (v en {L, R}*); por ente, es necesario
    crear una estructura particular para el primer grupo
    de caracteres de la contraseña:

    * Si la contraseña comienza con movimientos a la
    izquierda "L"; se "registra" este hecho.

    * Si la contraseña comienza con movimientos a la
    derecha "R"; se "registra" este hecho.

    Se toma este primer símbolo como la transición que
    el estado inicial tiene para avanzar a estados
    siguientes, y el complemento del símbolo (el otro),
    para generar un ciclo en el que no sale del estado
    inicial. Es decir, cuando se esté leyendo el inicio
    de la cadena, se espera que cuando lea el símbolo
    con el que inicia la contraseña, comience a avanzar
    suponiendo que ya se está tecleando la contraseña,
    en caso de que se lean otros símbolos, seguirá a la
    espera de que este primer símbolo llegue.

    Esta primer estructura tiene "x" estados; en donde
    "x" representa la cantidad de movimientos del primer
    dígito de la contraseña (cantidad de símbolos de la
    estructura inicial, antes de comenzar con otra letra).

    Los "x" estados de esta estructura regresan al estado
    inicial cuando encuentran un símbolo que no es igual al
    inicial de la contraseña, y avanzan hasta que el último
    estado de esta estructura (el número "x"), debe comenzar
    a leer otras letras, en ese caso, se ciclará a sí mismo
    mientras siga leyendo el símbolo inicial; esto porque se
    espera que si antes de la contraseña vinieron "mil" veces
    ese símbolo, los registre todos de manera igualmente válida
    que si sólo vinieron "x".
    '''
    #? Estado incial:
    Automata.setInitial("q0")
    #? Símbolo inicial:
    initialSymbol = password[0]
    #? Primeras transiciones:
    if initialSymbol == "L":
        Automata.addTransition(("q0", "R", "q0"))
        # print(f"(\'q0\', \'R\', \'q0\')")
        Automata.addTransition(("q0", "L", "q1"))
        # print(f"(\'q0\', \'L\', \'q1\')")
        notInitialSymbol = "R"
    else:
        Automata.addTransition(("q0", "L", "q0"))
        # print(f"(\'q0\', \'L\', \'q0\')")
        Automata.addTransition(("q0", "R", "q1"))
        # print(f"(\'q0\', \'R\', \'q1\')")
        notInitialSymbol = "L"

    #? Primeros "x" estados:
    index = 1

    #? Le las "x" repeticiones del primer símbolo;
    #? y crea estados para cada uno; bajo las reglas
    #? de la primer estructura:
    while initialSymbol == password[index]:

        #/ Nuevo estado x:
        Automata.addState(str(f"q{index}"))

        #/ Transición de este estado hacia le siguiente;
        #/ Avanzando porque encontró el símbolo inicial:
        Automata.addTransition((str(f"q{index}"), initialSymbol, str(f"q{index+1}")))
        # print(f"(\'q{index}\', \'{initialSymbol}\', \'q{index+1}\')")

        #/ Transición en el que regresa al estado inicial:
        #/ Esto porque encontró un símbolo diferente al inicial:
        Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
        # print(f"(\'q{index}\', \'{notInitialSymbol}\', \'q0\')")

        index += 1

    #? Crea el ciclo descrito para el último estado "x":
    #/ Transición para sí mismo:
    Automata.addState(str(f"q{index+1}"))
    Automata.addTransition((str(f"q{index}"), initialSymbol, str(f"q{index}")))
    # print(f"(\'q{index}\', \'{initialSymbol}\', \'q{index}\')")

    #/ Transición para avanzar con el siguiente tipo de símbolo:
    Automata.addTransition((str(f"q{index}"), notInitialSymbol, str(f"q{index+1}")))
    # print(f"(\'q{index}\', \'{notInitialSymbol}\', \'q{index+1}\')")


    #? ESTRUCTURA GENERAL:
    '''
    Esta estructura sirve para el resto de dígitos de la contraseña;
    Para cada símbolo siguiente seguirá las reglas:

        * Se crea un estado para cada siguiente movimiento (caracter):
            - Crea una transición para avanzar al siguiente estado,
            según el símbolo actual de la contraseña.
            - Cuando estás leyendo el símbolo inicial; la otra transición
            va a "q0"; es decir, vuelve a empezar porque al estar leyendo
            algo en la contraseña fue incorrecto.
            - Cuando estás leyendo el símbolo no-inicial, la otra transición
            va a "q1", porque supone que te equivocaste, pero que este error
            podría significar que es el primer símbolo correcto de la contraseña.
    '''
    print()
    #* Si toca cambiar de dirección al siguiente movimiento;
    #* Esto porque el siguiente caracter es diferente al actual:
    if index != len(password)-1 and password[index] != password[index+1]:
        change = True
    else:
        change = False
    index += 1
    
    while index < len(password):

        #* Se crea el estado para el símbolo actual:
        Automata.addState(str(f"q{index}"))

        #* Se crea una transición de avance:
        Automata.addTransition((str(f"q{index}"), password[index], str(f"q{index+1}")))
        # print((str(f"q{index}"), password[index], str(f"q{index+1}")))

        #? Si se está leyendo el caracter inicial:
        if password[index-1] == initialSymbol:
            #/ Transición de retroceso:
            if not change:
                Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
                # print((str(f"q{index}"), notInitialSymbol, "q0"))
            else:
                Automata.addTransition((str(f"q{index}"), initialSymbol, "q1"))
                # print((str(f"q{index}"), initialSymbol, "q1"))
        
        #? Si se está leyendo el caracter no-inicial:
        else:
            #/ Transición de retroceso:
            if not change:
                Automata.addTransition((str(f"q{index}"), initialSymbol, "q1"))
                # print((str(f"q{index}"), initialSymbol, "q1"))
            else:
                Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
                # print((str(f"q{index}"), notInitialSymbol, "q0"))
        
        #* Si toca cambiar de dirección al siguiente movimiento;
        #* Esto porque el siguiente caracter es diferente al actual:
        if index != len(password)-1 and password[index] != password[index+1]:
            change = True
        else:
            change = False
        index += 1

    print()
    #? ESTRUCTURA FINAL:
    '''
    Esta estructura consiste en el estado final, al que se llegó
    SÓLO si la contraseña fue correcta; en ese caso, se ciclará
    a sí mismo independientemente de lo que reciba después; ya
    que la caja ya está abierta.
    '''
    Automata.addState(str(f"q{index}"))
    Automata.addTransition((str(f"q{index}"), "L", str(f"q{index}")))
    # print(f"(\'q{index}\', \'L\', \'q{index}\')")
    Automata.addTransition((str(f"q{index}"), "R", str(f"q{index}")))
    # print(f"(\'q{index}\', \'R\', \'q{index}\')")
    Automata.setFinals({str(f"q{index}")})


    #/ Executes the Automata:
    '''
    while True:
        word = input("Cadena: ")
        if Automata.accepts(word, stepByStep=False):
            # print(f"La cadena \"{word}\" SÍ es aceptada!")
        else:
            # print(f"La cadena \"{word}\" NO es aceptada!")
    '''
    
    Automata.show()
    return Automata


#? Punto de ejecución:
if __name__ == "__main__":

    while True:
        print("\n")
        os.system("cls")
        password = input("Contraseña: ")
        generateDFA(password)
        print("\n")
        os.system("pause")