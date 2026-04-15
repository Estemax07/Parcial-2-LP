grammar NoSQL;

programa  : sentencia+ EOF ;

sentencia : insertar | buscar | actualizar | eliminar ;

insertar  : 'INSERT' 'INTO' ID 'VALUES' documento ';' ;
buscar    : 'FIND' 'FROM' ID filtro? proyeccion? limite? ';' ;
actualizar: 'UPDATE' ID filtro 'SET' actualizacion ';' ;
eliminar  : 'DELETE' 'FROM' ID filtro ';' ;

filtro       : 'WHERE' condicion ;
proyeccion   : 'FIELDS' '{' ID (',' ID)* '}' ;
limite       : 'LIMIT' NUMERO ;
actualizacion: '{' asignacion (',' asignacion)* '}' ;
asignacion   : ID ':' valor ;

documento : '{' par (',' par)* '}' ;
par       : ID ':' valor ;

valor : STRING
      | NUMERO
      | BOOL
      | documento
      | '[' (valor (',' valor)*)? ']'
      | 'NULL' ;

condicion : condicion 'AND' condicion
          | condicion 'OR' condicion
          | 'NOT' condicion
          | campo op valor
          | '(' condicion ')' ;

campo : ID ('.' ID)* ;
op    : '==' | '!=' | '>' | '<' | '>=' | '<=' | 'IN' | 'EXISTS' ;

ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING : '"' ~["]* '"' ;
NUMERO : [0-9]+ ('.' [0-9]+)? ;
BOOL   : 'true' | 'false' ;
WS     : [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
