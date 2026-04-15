# Ambigüedad del if-then-else

Ejemplo:

if E1 then if E2 then S1 else S2

## Interpretación 1
if E1 then (if E2 then S1 else S2)

## Interpretación 2
(if E1 then if E2 then S1) else S2

Esto demuestra que la gramática es ambigua.

## Solución

prop → if expr then prop | prop_emparejada  
prop_emparejada → if expr then prop_emparejada else prop | otras  

Esta solución fuerza que el else se asocie al if más cercano
