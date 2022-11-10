from dfa import DFA

if __name__ == "__main__":

    # Second example of DFA Automata instance:
    # Language of the Automata:
    # L(Automata) = All strings with at least one "a",
    # and exactly two b's:
    #* States:
    Q = {"q0", "qa", "q1", "qb", "q2", "qf", "qx"}

    #* Alphabet:
    A = {"a", "b"}

    #* Transitions:
    T = []

    #* Starting state:
    S = "q0"

    #* Finals states:
    F = {"qf"}

    #* Transitions definition:
    T.append( ("q0", "a", "qa") )
    T.append( ("q0", "b", "q1") )

    T.append( ("qa", "a", "qa") )
    T.append( ("qa", "b", "qb") )

    T.append( ("q1", "a", "qb") )
    T.append( ("q1", "b", "q2") )

    T.append( ("qb", "a", "qb") )
    T.append( ("qb", "b", "qf") )

    T.append( ("q2", "a", "qf") )
    T.append( ("q2", "b", "qx") )
    
    T.append( ("qf", "a", "qf") )
    T.append( ("qf", "b", "qx") )

    T.append( ("qx", "a", "qx") )
    T.append( ("qx", "b", "qx") )

    #? Automata:
    Automata = DFA(Q, A, T, S, F)

    #/ Executes the Automata:
    while True:
        print()
        word = input("Cadena: ")
        if Automata.accepts(word, stepByStep=True):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else:
            print(f"La cadena \"{word}\" NO es aceptada!")