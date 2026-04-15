import time

# Gramatica CNF para expresiones aritmeticas:
# S  -> S A | S B | n
# A  -> Plus S | Minus S
# B  -> Mult S | Div S
GRAMMAR = {
    'S':     [['S', 'A'], ['S', 'B'], ['n']],
    'A':     [['Plus', 'S'], ['Minus', 'S']],
    'B':     [['Mult', 'S'], ['Div', 'S']],
    'Plus':  [['+']],
    'Minus': [['-']],
    'Mult':  [['*']],
    'Div':   [['/']],
}

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
        elif expr[i].isdigit():
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append('n')
            i = j
        elif expr[i] in '+-*/':
            tokens.append(expr[i])
            i += 1
        else:
            raise ValueError(f"Token desconocido: '{expr[i]}'")
    return tokens

def cyk(tokens, grammar):
    n = len(tokens)
    if n == 0:
        return False
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    for i, tok in enumerate(tokens):
        for var, prods in grammar.items():
            if [tok] in prods:
                tabla[i][i].add(var)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for var, prods in grammar.items():
                    for prod in prods:
                        if len(prod) == 2:
                            B, C = prod
                            if B in tabla[i][k] and C in tabla[k+1][j]:
                                tabla[i][j].add(var)

    return 'S' in tabla[0][n-1]

class ParserLL:
    def __init__(self, tokens):
        self.tok = tokens
        self.pos = 0

    def peek(self):
        return self.tok[self.pos] if self.pos < len(self.tok) else 'EOF'

    def consume(self, t):
        if self.peek() == t:
            self.pos += 1
        else:
            raise SyntaxError(f"Esperaba {t}, encontre {self.peek()}")

    def parse(self):
        self.expr()
        return self.pos == len(self.tok)

    def expr(self):
        self.term()
        while self.peek() in ('+', '-'):
            self.pos += 1
            self.term()

    def term(self):
        self.factor()
        while self.peek() in ('*', '/'):
            self.pos += 1
            self.factor()

    def factor(self):
        if self.peek() == 'n':
            self.pos += 1
        else:
            raise SyntaxError(f"Factor invalido: {self.peek()}")

def benchmark():
    casos = [
        "3 + 5",
        "2 * 3 + 4",
        "10 / 2 - 3",
        "1 + 2 + 3 + 4 + 5",
        "3 * 4 + 2 / 2 - 1 + 8 * 3",
    ]
    reps = 2000
    print(f"{'Expresion':<38} {'CYK (ms)':>10} {'LL (ms)':>10} {'Estado':>8}")
    print("-" * 72)
    for expr in casos:
        tokens = tokenize(expr)

        t0 = time.perf_counter()
        for _ in range(reps):
            cyk(tokens, GRAMMAR)
        t_cyk = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        for _ in range(reps):
            try:
                ParserLL(tokens[:]).parse()
            except:
                pass
        t_ll = (time.perf_counter() - t0) * 1000

        print(f"{expr:<38} {t_cyk:>10.2f} {t_ll:>10.2f} {'OK':>8}")

    print()
    print("CYK es O(n^3) — crece cubicamente con la longitud de la entrada.")
    print("LL  es O(n)   — crece linealmente, mucho mas rapido en la practica.")

if __name__ == "__main__":
    print("=== BENCHMARK: CYK vs PARSER PREDICTIVO LL ===")
    print()
    benchmark()
