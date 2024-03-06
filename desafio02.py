
def verifica_fibonacci(numero):
    a = 0
    b = 1
    while b < numero:
       a, b = b, a + b

    if b == numero:
        return f'{numero} pertence à sequência de Fibonacci.'
    else:
        return f'{numero} não pertence à sequência de Fibonacci.'
    
num = int(input('Qual número você quer verificar se pertence à sequência de Fibonacci: '))

print(verifica_fibonacci(num))