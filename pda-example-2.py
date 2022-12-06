from pda import PDA

if __name__ == "__main__":

    # Second example of PDA Automata instance:
    # Language of the Automata:
    # L(Automata) = { w c (w)^R: w in {a, b}* };
    # Any "a" and "b" combination string (also empty),
    # with then a "c", and then his reverse:

    #* States:
    Q = {"qw", "qc", "qf"}

    #* Alphabet:
    A = {"a", "b", "c"}

    #* Transitions:
    T = []

    #* Starting state:
    S = "qw"

    #* Finals states:
    F = {"qf"}

    #* Stack alphabet:
    X = {"Z", "1", "2"}

    #* Initial stack:
    I = ["Z"]

    #* Transitions definition:
    T.append( ("qw", "a", "Z", "1Z", "qw") )
    T.append( ("qw", "b", "Z", "2Z", "qw") )
    T.append( ("qw", "a", "1", "11", "qw") )
    T.append( ("qw", "a", "2", "12", "qw") )
    T.append( ("qw", "b", "1", "21", "qw") )
    T.append( ("qw", "b", "2", "22", "qw") )

    T.append( ("qw", "c", "1", "1", "qc") )
    T.append( ("qw", "c", "2", "2", "qc") )
    T.append( ("qw", "c", "Z", "Z", "qc") )

    T.append( ("qc", "a", "1", "", "qc") )
    T.append( ("qc", "b", "2", "", "qc") )

    T.append( ("qc", "", "Z", "", "qf") )

    #? Automata:
    Automata = PDA(Q, A, T, S, F, X, I)
    Automata.show()

    #/ Executes the Automata:
    while True:
        print()
        word = input("Cadena: ")
        if Automata.accepts(word, stepByStep=True):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else:
            print(f"La cadena \"{word}\" NO es aceptada!")
        print()
        print("═"*40)