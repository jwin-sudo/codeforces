from sys import stdin, stdout 

def main():
    T = int(stdin.readline().strip())
    while T > 0:
        line = stdin.readline().strip()
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        
        parts = line.split()
        
        parts.remove("(")
        parts.remove(")")
        
        a, op1, b, op2, c, mod, p = list(parts)
        
        def calculate(op, a, b):
            a = int(a)
            b = int(b)
            if op == "+":
                return a + b 
            elif op == "-":
                return a - b 
            elif op == "*":
                return a * b 
            elif op == "/":
                return a // b 
            elif op == "mod":
                return a % b 
        total = 0 
        if op1 in ("+", "-") and op2 in ("*", "/"):
            right = calculate(op2, b, c)
            total = calculate(op1, a, right)
        else:
            left = calculate(op1, a, b)
            total = calculate(op2, left, c)
        final = calculate(mod, total, p)
        print(final)
        
        T-= 1   
if __name__ == "__main__":
    main()