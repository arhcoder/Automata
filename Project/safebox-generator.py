from Automata.dfa import DFA
import os

'''
    EXAMPLE PROJECT WITH DFA
    SAFEBOX-AUTOMATA-GENERATOR

    This algorithm designs an automaton set to the password of a Safebox;
    Safebox passwords can be represented as a string of movements to the
    Left ("L") and Right ("R"). Grouping them as a word; for example
    "LLLLRRRLLRRRRRR" where each "L" or "R" represents a movement, a
    password is built, and automata theory can be applied, where a DFA
    could act as a safebox, accepting the strings that contains in some
    part, the password; the knob can be moved any number of times, and if
    in between those movements the password is ever formed, the safe opens
    (The string is accepted), and whatever comes after it will still allow
    the password to be accepted string. SO THIS ALGORITHM DESIGNS THE DFA
    ADJUSTED TO THE PASSWORD INDICATED BY THE USER.
'''

def generateDFA(password: str):
    
    #? DFA:
    #* This implementation is to generate an auotomaton,
    #* that represents a safebox, and depending on the,
    #* password (string of movements of "L" and "R":
    #* Left and Right), the automaton is generated;
    #* The automaton is expected to accept:
    #* { wxv:  w, v ∈ {L, R}*,  x is the password };
    Automata = DFA()
    Automata.setAlphabet({"L", "R"})

    #* Start with the drawing of the automaton:
    # print(f"\nGenerated Automaton for \"{password}\":\n")


    #? INITIAL STRUCTURE ?#
    '''
    The automaton is expected to accept the password from
    the safe regardless of what comes before it (v in {L, R}*);
    therefore, it is necessary to create a particular structure
    for the first group password characters:

    * If the password begins with movements to the
    left "L"; this fact is "recorded".

    * If the password begins with movements to the
    right "R"; this fact is "recorded".

    This first symbol is taken as the transition that
    the initial state has to transite to subsequent states,
    and the complement of the symbol (the other), to
    generate a loop in which it does not leave the initial
    state. That is, when the beggining of the string is
    being read, it it is expected that when it reads the
    symbol with which the password starts, it starts moving
    forward assuming the password is already being typed,
    in case other symbols are read, it will continiue to
    waiting for this first symbol to arrive, to assume
    again that it is starting to type the password.

    This first structure has "x" states; where "x"
    represents the number of movements of the first
    digit of the password (number of symbols of the
    initial structure, before starting with another
    letter).

    The "x" states of this structure return to the initial
    state when they read a symbol that is not equal to the
    initial of the password, and advance until the last
    state of this structure (the number "x"), should start
    reading other letters, in that case, it will loop itself
    as long as it continues to read the initial symbol; This
    is because it is expected that if that symbol came "a
    thousand" times before the password, it will register
    all of them in an equally valid way as if only "x" came.
    '''
    #? Initial state:
    Automata.setInitial("q0")
    #? Initial symbol:
    initialSymbol = password[0]
    #? First transitions:
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

    #? First "x" states:
    index = 1

    #? Read the "x" repetitions of the first symbol;
    #? and create states for each one; under the rules
    #? of the first structure, definded above:
    while initialSymbol == password[index]:

        #/ New state "x":
        Automata.addState(str(f"q{index}"))

        #/ Transition from this state to the next;
        #/ Moving forward because you found the initial symbol:
        Automata.addTransition((str(f"q{index}"), initialSymbol, str(f"q{index+1}")))
        # print(f"(\'q{index}\', \'{initialSymbol}\', \'q{index+1}\')")

        #/ Transition in which it returns to the initial state:
        #/ This because it found a different symbol than the initial one:
        Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
        # print(f"(\'q{index}\', \'{notInitialSymbol}\', \'q0\')")

        index += 1

    #? Create the described loop for the last state "x":
    #/ Transition for itself:
    Automata.addState(str(f"q{index+1}"))
    Automata.addTransition((str(f"q{index}"), initialSymbol, str(f"q{index}")))
    # print(f"(\'q{index}\', \'{initialSymbol}\', \'q{index}\')")

    #/ Transition to advance with the following type of symbol:
    Automata.addTransition((str(f"q{index}"), notInitialSymbol, str(f"q{index+1}")))
    # print(f"(\'q{index}\', \'{notInitialSymbol}\', \'q{index+1}\')")


    #? GENERAL STRUCTURE:
    '''
    This structure is used for the rest of the digits of the password;
    For each following symbol it will follow the rules:

        * A state is created for each next move (symbol):
            - Creates a transition to advance to the next state,
            based on the current symbol of the password.
            - When you are reading the initial symbol; the other
            transition goes to "q0"; that is, it starts over because
            reading something in the password was incorrect.
            - When you are reading the non-initial symbol, the other
            transition goes to "q1", because it assumes that you made
            a mistake, but that this error could mean that it is the correct
            first symbol of the password.
    '''
    print()
    #* If it is necessary to change direction to the next move;
    #* This is because the next symbol is different from the current one:
    if index != len(password)-1 and password[index] != password[index+1]:
        change = True
    else:
        change = False
    index += 1
    
    while index < len(password):

        #* A new state is created for the current symbol:
        Automata.addState(str(f"q{index}"))

        #* A forward transition is created:
        Automata.addTransition((str(f"q{index}"), password[index], str(f"q{index+1}")))
        # print((str(f"q{index}"), password[index], str(f"q{index+1}")))

        #? If the initial symbol is being read:
        if password[index-1] == initialSymbol:
            #/ Back transition:
            if not change:
                Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
                # print((str(f"q{index}"), notInitialSymbol, "q0"))
            else:
                Automata.addTransition((str(f"q{index}"), initialSymbol, "q1"))
                # print((str(f"q{index}"), initialSymbol, "q1"))
        
        #? If the non-initial symbol is being read:
        else:
            #/ Back transition:
            if not change:
                Automata.addTransition((str(f"q{index}"), initialSymbol, "q1"))
                # print((str(f"q{index}"), initialSymbol, "q1"))
            else:
                Automata.addTransition((str(f"q{index}"), notInitialSymbol, "q0"))
                # print((str(f"q{index}"), notInitialSymbol, "q0"))
        
        #* If it is necessary to switch direction to the next move;
        #* This is because the next symbol is different from the current one:
        if index != len(password)-1 and password[index] != password[index+1]:
            change = True
        else:
            change = False
        index += 1

    print()

    #? FINAL STRUCTURE:
    '''
    This structure consists of the final state, reached ONLY if
    the password was correct; in that case, he will cycle himself
    regardless of what he receives afterwards; since the safebox
    is already open.
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
        word = input("String: ")
        if Automata.accepts(word, stepByStep=False):
            # print(f"The string \"{word}\" IS accepted!")
        else:
            # print(f"The string \"{word}\" IS NOT accepted!")
    '''
    
    Automata.show()
    return Automata


#! Main execution point:
if __name__ == "__main__":

    while True:
        print("\n")
        os.system("cls")
        print(f"\n"+("═"*40))
        print(f"\nSAFEBOX AUTOMATA GENERATION\n\n"+("═"*40))
        print("\nCreate a password for a safebox based on movements to\n"+
              "Left and Right; The password has to be a string of\nmovements; where each symbol of "+
              "\"L\" and \"R\" represents\na movement; for example, \"LLLLRRRLLRR\" represents:\n" +
              " * 4 movements to Left;\n * 3 movements to Right;\n * 2 movements to Left;\n * 2 movements to Right;\n")
        password = str(input("Password: ")).upper()
        generateDFA(password)
        print("\n")
        os.system("pause")