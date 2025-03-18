import sys

preanalisis = ''
flag = 0
limite_cadena = 0
cadena = ""

def exp():
    term_t, infijo_t, prefijo_t, posfijo_t = term()
    Resto_exp_t, infijo_r, prefijo_r, posfijo_r = Resto_exp(term_t, infijo_t, prefijo_t, posfijo_t)
    return Resto_exp_t, infijo_r, prefijo_r, posfijo_r

def Resto_exp(her, infijo, prefijo, posfijo):
    global preanalisis
    if preanalisis == '+':
        coincidir('+')
        term_t, infijo_t, prefijo_t, posfijo_t = term()
        return Resto_exp(her + term_t, f"{infijo} + {infijo_t}", f"+ {prefijo} {prefijo_t}", f"{posfijo} {posfijo_t} +")
    elif preanalisis == '-':
        coincidir('-')
        term_t, infijo_t, prefijo_t, posfijo_t = term()
        return Resto_exp(her - term_t, f"{infijo} - {infijo_t}", f"- {prefijo} {prefijo_t}", f"{posfijo} {posfijo_t} -")
    else:
        return her, infijo, prefijo, posfijo

def term():
    factor_t, infijo_t, prefijo_t, posfijo_t = factor()
    return Resto_term(factor_t, infijo_t, prefijo_t, posfijo_t)

def Resto_term(her, infijo, prefijo, posfijo):
    global preanalisis
    if preanalisis == '*':
        coincidir('*')
        factor_t, infijo_t, prefijo_t, posfijo_t = factor()
        return Resto_term(her * factor_t, f"{infijo} * {infijo_t}", f"* {prefijo} {prefijo_t}", f"{posfijo} {posfijo_t} *")
    elif preanalisis == '/':
        coincidir('/')
        factor_t, infijo_t, prefijo_t, posfijo_t = factor()
        return Resto_term(her / factor_t, f"{infijo} / {infijo_t}", f"/ {prefijo} {prefijo_t}", f"{posfijo} {posfijo_t} /")
    else:
        return her, infijo, prefijo, posfijo

def factor():
    global preanalisis
    if preanalisis == '(':
        coincidir('(')
        Resto_exp_result, infijo, prefijo, posfijo = exp()
        if preanalisis == ')':
            coincidir(')')
            return Resto_exp_result, f"({infijo})", prefijo, posfijo
        else:
            print("Error: Se esperaba ')'")
            return None, "", "", ""
    else:
        return digito()

def digito():
    global preanalisis
    if preanalisis in '0123456789':
        valor = int(preanalisis)
        num_str = preanalisis
        coincidir(preanalisis)
        return valor, num_str, num_str, num_str
    else:
        print("La cadena no es valida, el programa terminara")
        sys.exit()
        return 0, "", "", ""

def coincidir(caracter):
    global preanalisis, cadena, flag, limite_cadena
    flag += 1
    if flag <= limite_cadena:
        print(f"El caracter '{caracter}' es válido")
        preanalisis = cadena[flag]
    else:
        print(f"El caracter '{caracter}' es válido")
        print("Cadena Terminada")

def main():
    global limite_cadena, preanalisis, cadena
    cadena = input("Ingresa una cadena: ")
    limite_cadena = len(cadena) - 1
    preanalisis = cadena[0]
    resultado, infijo, prefijo, posfijo = exp()
    print("Resultado es:", resultado)
    print("\nNotación Infija:", infijo)
    print("Notación Prefija:", prefijo)
    print("Notación Posfija:", posfijo)

preanalisis = ''
flag = 0
limite_cadena = 0
cadena = ""
main()