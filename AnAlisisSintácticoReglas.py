preanalisis = ''
flag=0
limite_cadena = 0
cadena = ""


def exp():
    term_t=term()
    Resto_exp_t=Resto_exp(term_t)
    return Resto_exp_t

def Resto_exp(her):
    global preanalisis
    if preanalisis == '+':
        coincidir('+')
        term_t=term()
        Resto_exp_t= Resto_exp(her + term_t)
        return Resto_exp_t
    elif preanalisis == '-':
        coincidir('-')
        term_t=term()
        Resto_exp_t= Resto_exp(term_t-her)
        return Resto_exp_t
    else:
        return her
    
def term():
    factor_t= factor()
    Resto_term_t=Resto_term(factor_t)
    return Resto_term_t

def Resto_term(her):
    global preanalisis
    if preanalisis == '/':
        coincidir('/')
        factor_t=factor()
        Resto_exp_t= Resto_exp(her * factor_t)
        return Resto_exp_t
    elif preanalisis == '*':
        coincidir('*')
        factor_t=factor()
        Resto_term_t= Resto_term(factor_t/her)
        return Resto_term_t
    else:
        return her
    
def factor():
    global preanalisis
    if preanalisis == '(':
        Resto_exp=exp()
        return Resto_exp
    elif preanalisis == digito():
        return preanalisis
    else:
        print("No valido")


def digito():
    global preanalisis  # Declaración global xd
    if preanalisis == '0':
        coincidir('0')
        return preanalisis
    elif preanalisis == '1':
        coincidir('1')
        return preanalisis
    elif preanalisis == '2':
        coincidir('2')
        return preanalisis
    elif preanalisis == '3':
        coincidir('3')
        return preanalisis
    elif preanalisis == '4':
        coincidir('4')
        return preanalisis
    elif preanalisis == '5':
        coincidir('5')
        return preanalisis
    elif preanalisis == '6':
        coincidir('6')
        return preanalisis
    elif preanalisis == '7':
        coincidir('7')
        return preanalisis
    elif preanalisis == '8':
        coincidir('8')
        return preanalisis
    elif preanalisis == '9':
        coincidir('9')
        return preanalisis
    else:
        print("no coincide la cadena")

def coincidir(caracter):
    global preanalisis
    global cadena
    global flag
    global limite_cadena
    flag+=1
    if flag <= limite_cadena:
        print("El caracter", caracter, "es válido")
        preanalisis= cadena[flag]
    else:
        print("El caracter", caracter, "es válido")
        print("la cadena es valida")

    


def main():
    global limite_cadena
    global preanalisis
    global cadena
    resultado = 0
    cadena = input("Ingresa una cadena: ")
    limite_cadena=len(cadena)-1
    preanalisis = cadena[0]
    resultado=exp()
    print("Resultado es:",resultado)


preanalisis = ''
flag = 0
limite_cadena = 0
cadena = ""  
main()