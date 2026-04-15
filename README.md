# Parcial 2 - Lenguajes de Programacion 2026-1

## Descripcion

Este repositorio contiene la solucion completa del segundo parcial. Se implementaron los 5 puntos
cuales cubren diseno de gramaticas, parsing, ambiguedad y algoritmos.

---

## Punto 1 - Gramatica CRUD para BD No Relacional

Se diseno una gramatica formal en notacion EBNF para un lenguaje
que permite hacer las 4 operaciones basicas (CRUD) sobre una base
de datos no relacional estilo documento.

Operaciones cubiertas:
- INSERT INTO: crear documentos en una coleccion
- FIND FROM:  leer documentos con filtros, proyeccion y limite
- UPDATE:     modificar campos de documentos existentes
- DELETE FROM: eliminar documentos segun condicion

Archivos: punto1/gramatica_nosql.txt, punto1/ejemplos.nosql

---

## Punto 2 - Implementacion en ANTLR4

Se implemento la gramatica del punto 1 usando ANTLR4.
El archivo NoSQL.g4 define las reglas del lexer y parser.
Se realizaron pruebas con el comando grun mostrando el arbol
de derivacion para sentencias INSERT, FIND, UPDATE y DELETE.

Como ejecutar:
  cd punto2
  antlr4 NoSQL.g4
  javac *.java
  grun NoSQL programa -tree test.nosql

Archivos: punto2/NoSQL.g4, punto2/test.nosql

---

## Punto 3 - Ambiguedad en if-then-else

Se demostro que la gramatica propuesta en el enunciado sigue
siendo ambigua mediante el contraejemplo:

  if e1 then if e2 then otras else otras

Esta cadena produce dos arboles de derivacion distintos, lo que
prueba formalmente la ambiguedad. Se propuso una gramatica
corregida que separa las proposiciones en "emparejadas"
(cada if tiene su else) y "no emparejadas".

Como ejecutar:
  cd punto3
  python3 arboles.py

Archivos: punto3/ambiguedad.txt, punto3/arboles.py

---

## Punto 4 - Parser CYK vs Parser Predictivo LL

Se implemento el algoritmo CYK para parsear expresiones
de calculadora (suma, resta, multiplicacion, division).
La gramatica se convirtio primero a Forma Normal de Chomsky.

Se comparo el rendimiento de CYK (O(n^3)) contra un parser
predictivo LL (O(n)) mediante benchmark con 2000 repeticiones.
El resultado muestra que LL es significativamente mas rapido.

Como ejecutar:
  cd punto4
  python3 cyk_parser.py

Archivos: punto4/cyk_parser.py, punto4/resultados.txt

---

## Punto 5 - Parser Descendente Recursivo

Se diseno una gramatica y se implemento un parser descendente
recursivo en Python que soporta:
- Asignaciones: x = expr;
- Condicionales: if (cond) { } else { }
- Expresiones aritmeticas con precedencia correcta

Se incluye un interprete que evalua el arbol sintatico
y ejecuta las instrucciones mostrando el valor final
de cada variable.

Como ejecutar:
  cd punto5
  python3 parser_recursivo.py

Archivos: punto5/parser_recursivo.py, punto5/resultados_parser.txt

---

## Requisitos

- Python 3.x
- Java (openjdk)
- ANTLR4 4.13.1

