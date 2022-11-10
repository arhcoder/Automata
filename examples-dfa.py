from dfa import DFA

if __name__ == "__main__":

    # First example of DFA Automata instance:
    # Language of the Automata:
    # L(Automata) = {(b^n)a(w): n>=0, w in {a, b}*};
    # Any string with at least one "a";
    FirstAutomata = DFA()
    FirstAutomata.setStates({"q0", "q1"})
    FirstAutomata.setAlphabet({"a", "b"})
    FirstAutomata.setInitial("q0")
    FirstAutomata.setFinals({"q1"})
    FirstAutomata.addTransition(("q0", "a", "q1"))
    FirstAutomata.addTransition(("q0", "b", "q0"))
    FirstAutomata.addTransition(("q1", "a", "q1"))
    FirstAutomata.addTransition(("q1", "b", "q1"))


    # Second example of DFA Automata instance:
    # Language of the Automata:
    # L(Automata) = {(b^n)a(w): n>=0, w in {a, b}*};
    # Any string with at least one "a";
    #* States:
    Q = {"q0", "q1"}

    #* Alphabet:
    A = {"a", "b"}

    #* Transitions:
    T = []

    #* Starting state:
    S = "q0"

    #* Finals states:
    F = {"q1"}

    #* Transitions definition:
    T.append( ("q0", "a", "q1") )
    T.append( ("q0", "b", "q0") )
    T.append( ("q1", "a", "q1") )
    T.append( ("q1", "b", "q1") )

    #? Automata:
    SecondAutomata = DFA(Q, A, T, S, F)


    #/ Executes the probes:
    print()
    print("="*40)
    for _ in range(0, 2):
        print()
        word = input("Cadena: ")
        if FirstAutomata.accepts(word):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else: print(f"La cadena \"{word}\" NO es aceptada!")
    
    print()
    print("="*40)
    for _ in range(0, 2):
        print()
        word = input("Cadena: ")
        if SecondAutomata.accepts(word, stepByStep=True):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else: print(f"La cadena \"{word}\" NO es aceptada!")
    
    print()