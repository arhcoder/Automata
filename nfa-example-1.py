from nfa import NFA

if __name__ == "__main__":

    # First example of NFA Automata instance:
    # Language of the Automata:
    # L(Automata) = {aba(b^n): n>0} U
    # {ab(a^n): n>=0};
    #* States:
    Q = {"q0", "qa", "qab", "qf", "qabf"}

    #* Alphabet:
    A = {"a", "b"}

    #* Transitions:
    T = []

    #* Starting state:
    S = "q0"

    #* Finals states:
    F = {"qf", "qabf"}

    #* Transitions definition:
    T.append( ("q0", "a", "qa") )
    T.append( ("qa", "b", "qab") )
    T.append( ("qab", "a", "qf") )
    T.append( ("qf", "b", "qf") )
    T.append( ("qab", "", "qabf") )
    T.append( ("qabf", "a", "qabf") )

    #? Automata:
    Automata = NFA(Q, A, T, S, F)

    #/ Executes the Automata:
    while True:
        print()
        word = input("Cadena: ")
        if Automata.accepts(word, stepByStep=True):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else:
            print(f"La cadena \"{word}\" NO es aceptada!")