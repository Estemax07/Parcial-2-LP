# Punto 2 - ANTLR4 NoSQL Parser

## Como compilar
antlr4 NoSQL.g4
javac *.java

## Como ejecutar
grun NoSQL programa -tree test.nosql

## Resultados esperados
- INSERT INTO: arbol de derivacion correcto
- FIND con WHERE y LIMIT: arbol de derivacion correcto
- UPDATE con SET: arbol de derivacion correcto
- DELETE con WHERE: arbol de derivacion correcto
