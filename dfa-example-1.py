from dfa import DFA

if __name__ == "__main__":

    # First example of DFA Automata instance:
    # Language of the Automata:
    # L(Automata) = {(b^n)a(w): n>=0, w in {a, b}*};
    # Any string with at least one "a";
    Automata = DFA()
    Automata.setStates({"q0", "q1"})
    Automata.setAlphabet({"a", "b"})
    Automata.setInitial("q0")
    Automata.setFinals({"q1"})
    Automata.addTransition(("q0", "a", "q1"))
    Automata.addTransition(("q0", "b", "q0"))
    Automata.addTransition(("q1", "a", "q1"))
    Automata.addTransition(("q1", "b", "q1"))
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