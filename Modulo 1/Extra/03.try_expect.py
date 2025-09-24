# Crie uma função chamada calculadora que receba tres parametros
# dois numeros e uma operação(+, -, *, /
# funçãio deve retornar o resultado da operação, mas precisa
# tratar as seguintes exeções:
# divisão por zero(ZeroDivisionError)
# Tipo de dado inválido(ValueError)

def calculadora():
    try:
        n = input('Digite um numero(ou x para sair do sistema): ')
        if  n.lower() == 'x':
            print('Até breve.')
            return
        n1=input('Digite um numero ou x para sair do sistema')
        if n1.lower() == 'x':
            print('Até breve.')
        operador = input('informe um operador matematico (+,=,*,/) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            return
        n2=input('Digite um numero ou x para sair do sistema')
        if n2.lower() =='x':
            print('Até breve.')
            return
        n = float(n)
        n1 = float(n1)

        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            resultado = n / n1
            if n1 == 0:
                raise ZeroDivisionError('Não é possivel dividir por zero')
            resultado =n /n1
        else:
            print('Voce não escolheu um operador ou escolheu um comando invalido')
            return
        print(f'Operação: {n}{operador}{n1}= {resultado}.')
    except ValueError:
        print('Voce digitou um caracter invalido, digite somente numeros')
    except ZeroDivisionError as zero:
        print(zero)
calculadora()