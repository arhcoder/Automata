from nfa import NFA

if __name__ == "__main__":

    # Second example of NFA Automata instance:
    # Language of the Automata:
    # L(Automata) = {(a^n): n>=0} U {(b^n)a: n>=1};
    Automata = NFA()
    Automata.setStates({"q0", "qb", "qa", "qba"})
    Automata.setAlphabet({"a", "b"})
    Automata.setInitial("q0")
    Automata.setFinals({"qa", "qba"})
    Automata.addTransition(("q0", "", "qa"))
    Automata.addTransition(("q0", "b", "qb"))
    Automata.addTransition(("qa", "a", "qa"))
    Automata.addTransition(("qb", "a", "qba"))
    Automata.addTransition(("qb", "b", "qb"))

    #/ Executes the Automata:
    while True:
        print()
        word = input("Cadena: ")
        if Automata.accepts(word, stepByStep=True):
            print(f"La cadena \"{word}\" SÍ es aceptada!")
        else:
            print(f"La cadena \"{word}\" NO es aceptada!")