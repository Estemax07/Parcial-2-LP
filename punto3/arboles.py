cadena = "if e1 then if e2 then otras else otras"

def mostrar_arbol1():
    print("ARBOL 1: el else va con el if e2 (mas cercano)")
    print("  prop")
    print("  --> if e1 then prop")
    print("                 --> prop_emparejada")
    print("                       --> if e2 then prop_emp else prop")
    print("                                      --> otras")
    print("                       --> otras")
    print()

def mostrar_arbol2():
    print("ARBOL 2: el else va con el if e1 (mas lejano)")
    print("  prop")
    print("  --> prop_emparejada")
    print("        --> if e1 then prop_emp else prop")
    print("                       --> if e2 then otras")
    print("                   --> otras")
    print()

def gramatica_corregida():
    print("GRAMATICA CORREGIDA (no ambigua):")
    print("  prop        --> prop_emp | prop_no_emp")
    print("  prop_emp    --> if expr then prop_emp else prop_emp | otras")
    print("  prop_no_emp --> if expr then prop")
    print("              |  if expr then prop_emp else prop_no_emp")
    print()

if __name__ == "__main__":
    print("=" * 55)
    print(f"Cadena analizada: {cadena}")
    print("=" * 55)
    print()
    print("La gramatica propuesta produce 2 arboles distintos:")
    print()
    mostrar_arbol1()
    mostrar_arbol2()
    gramatica_corregida()
    print("Con la gramatica corregida, cada cadena tiene exactamente un arbol.")
