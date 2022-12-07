from pda import PDA
import os

def validatePassword(password: str):

    '''
        Recibe una contraseña y valida si es
        correcta para el contexto de la caja
        fuerte, utilizando una autómata de
        pila que valida el siguiente formato:

        L = { (L^n)(R^m)(L^o)(R^p):
        (4  <=  n + m + o + p  <=  40) };

        Es decir; contraseñas con grupos de
        L's, luego R's, luego L's, luego R's,
        en donde cada grupo tenga por lo menos
        un caracter, y en conjunto no sumen más
        de 4 caracteres como longitud.

        Esta propuesta no está implementada en
        la aplicación, por lo que es agena a esta,
        se propone como propuesta interesante
        tener constraseñas con el lenguaje:
        L' = { L = { (L^n)(R^m)(L^o)(R^p):
        (1 <= n, m, o, p <= 10 };

        Es decir; contraseñas de cuatro grupos
        alternados (iguales a la propuesta anterior,
        pero en los cuales cada uno sólo admite un
        máximo de 10 símbolos).

        También se propone a futuro extender el
        lenguaje que acepte contraseñas que comienzen
        con grupos de R's, no de sólo L's.

        Retorna verdadero o falso según acepte o no
        acepte la contraseña de parámetro.
    '''

    #? Se crea instancia del autómata (de pila):
    Estados = {"q0", "q1", "q2", "q3", "q4", "q5"}
    Alfabeto = {"L", "R"}
    Inicial = "q0"
    Finales = {"q4"}
    Alfapila = {"1", "Z"}
    Pila = ["Z"]
    Transiciones = [
        ("q0", "L", "Z", "1111111111111111111111111111111111111111Z", "q1"),
        ("q1", "L", "1", "", "q1"),
        ("q1", "R", "1", "", "q2"),
        ("q2", "R", "1", "", "q2"),
        ("q2", "L", "1", "", "q3"),
        ("q3", "L", "1", "", "q3"),
        ("q3", "L", "1", "", "q3"),
        ("q3", "R", "1", "", "q4"),
        ("q4", "R", "1", "", "q4"),
        ("q4", "", "Z", "Z", "q5")
    ]
    Automata = PDA(Estados, Alfabeto, Transiciones, Inicial, Finales, Alfapila, Pila)
    Automata.show()
    print()
    return True if Automata.accepts(password, stepByStep=True) else False


#* Punto de ejecución:
if __name__ == "__main__":
    while True:
        os.system("cls")
        print()
        password = input("Contraseña: ")
        if validatePassword(password):
            print(f"\nLa contraseña \"{password}\" SÍ es válida")
        else:
            print(f"\nLa contraseña \"{password}\" NO es válida")
        print()
        print("═"*40)
        print("\n")
        os.system("pause")