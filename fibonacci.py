n=int(input('Digite um número: '))
n1, n2 = 0, 1
n3 = n1 + n2
if n==0 or n==1:
    print('Número informado pertence à sequencia de Fibonacci')
else:
    cont=3
    while n3 <= n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        cont += 1
    if n == n3 or n == n2 or n==n1: 
        print('Número informado pertence à sequencia de Fibonacci')
    else:
        print('Número informado NÃO pertence à sequencia de Fibonacci')