import re

PATRONES = [
    ('NUMERO', r'\d+(\.\d+)?'),
    ('ID',     r'[a-zA-Z_]\w*'),
    ('OP_REL', r'==|!=|<=|>=|<|>'),
    ('OP',     r'[+\-*/]'),
    ('ASIGN',  r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMI',   r';'),
    ('WS',     r'\s+'),
]

def tokenizar(codigo):
    pos, tokens = 0, []
    while pos < len(codigo):
        for tipo, patron in PATRONES:
            m = re.match(patron, codigo[pos:])
            if m:
                if tipo != 'WS':
                    tokens.append((tipo, m.group()))
                pos += len(m.group())
                break
        else:
            raise SyntaxError(f"Caracter desconocido en pos {pos}: '{codigo[pos]}'")
    tokens.append(('EOF', ''))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def consume(self, tipo=None):
        tok = self.tokens[self.pos]
        if tipo and tok[0] != tipo:
            raise SyntaxError(f"Se esperaba '{tipo}', se encontro '{tok[1]}' ({tok[0]})")
        self.pos += 1
        return tok

    def programa(self):
        stmts = []
        while self.peek()[0] != 'EOF':
            stmts.append(self.sentencia())
        return ('programa', stmts)

    def sentencia(self):
        tk = self.peek()
        if tk[0] == 'ID' and self.tokens[self.pos+1][0] == 'ASIGN':
            return self.asignacion()
        elif tk == ('ID', 'if'):
            return self.condicional()
        else:
            raise SyntaxError(f"Sentencia invalida: '{tk[1]}'")

    def asignacion(self):
        nombre = self.consume('ID')[1]
        self.consume('ASIGN')
        expresion = self.expr()
        self.consume('SEMI')
        return ('asignacion', nombre, expresion)

    def condicional(self):
        self.consume('ID')
        self.consume('LPAREN')
        cond = self.condicion()
        self.consume('RPAREN')
        then_b = self.bloque()
        if self.peek() == ('ID', 'else'):
            self.consume('ID')
            else_b = self.bloque()
            return ('if_else', cond, then_b, else_b)
        return ('if', cond, then_b)

    def bloque(self):
        self.consume('LBRACE')
        stmts = []
        while self.peek()[0] != 'RBRACE':
            stmts.append(self.sentencia())
        self.consume('RBRACE')
        return ('bloque', stmts)

    def condicion(self):
        iz = self.expr()
        op = self.consume('OP_REL')[1]
        de = self.expr()
        return ('condicion', iz, op, de)

    def expr(self):
        nodo = self.termino()
        while self.peek()[0] == 'OP' and self.peek()[1] in '+-':
            op = self.consume('OP')[1]
            nodo = ('binop', op, nodo, self.termino())
        return nodo

    def termino(self):
        nodo = self.factor()
        while self.peek()[0] == 'OP' and self.peek()[1] in '*/':
            op = self.consume('OP')[1]
            nodo = ('binop', op, nodo, self.factor())
        return nodo

    def factor(self):
        tk = self.peek()
        if tk[0] == 'LPAREN':
            self.consume('LPAREN')
            e = self.expr()
            self.consume('RPAREN')
            return e
        elif tk[0] == 'NUMERO':
            return ('num', float(self.consume()[1]))
        elif tk[0] == 'ID':
            return ('id', self.consume()[1])
        raise SyntaxError(f"Factor invalido: '{tk[1]}'")

def evaluar(nodo, env):
    t = nodo[0]
    if t == 'programa':
        for s in nodo[1]: evaluar(s, env)
    elif t == 'asignacion':
        env[nodo[1]] = evaluar(nodo[2], env)
        print(f"  {nodo[1]} = {env[nodo[1]]}")
    elif t == 'if':
        if evaluar(nodo[1], env): evaluar(nodo[2], env)
    elif t == 'if_else':
        if evaluar(nodo[1], env): evaluar(nodo[2], env)
        else: evaluar(nodo[3], env)
    elif t == 'bloque':
        for s in nodo[1]: evaluar(s, env)
    elif t == 'condicion':
        a = evaluar(nodo[1], env); b = evaluar(nodo[3], env)
        return {'==':a==b,'!=':a!=b,'>':a>b,'<':a=':a>=b,'<=':a<=b}[nodo[2]]
    elif t == 'binop':
        a = evaluar(nodo[2], env); b = evaluar(nodo[3], env)
        return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}[nodo[1]]
    elif t == 'num': return nodo[1]
    elif t == 'id': return env.get(nodo[1], 0)

PRUEBAS = [
    ("Asignacion simple",
     "x = 10;"),
    ("Expresion aritmetica",
     "y = 3 * 4 + 2;"),
    ("If sin else",
     "z = 5; if (z > 3) { z = z + 1; }"),
    ("If con else",
     "a = 8; if (a > 10) { a = 100; } else { a = 0; }"),
    ("Anidado",
     "n = 15; if (n > 10) { n = n - 5; if (n > 5) { n = 0; } }"),
]

if __name__ == "__main__":
    print("=== PARSER DESCENDENTE RECURSIVO ===")
    print()
    for nombre, codigo in PRUEBAS:
        print(f"Prueba: {nombre}")
        print(f"Codigo: {codigo}")
        try:
            tokens = tokenizar(codigo)
            arbol  = Parser(tokens).programa()
            env    = {}
            print("Resultado:")
            evaluar(arbol, env)
            print(f"Variables finales: {env}")
        except SyntaxError as e:
            print(f"Error de sintaxis: {e}")
        print("-" * 45)
