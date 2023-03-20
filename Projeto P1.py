#Criar Um Algoritmo que seja capaz de ordenar de forma cresecente e descrente assim como imprimir de forma grafica a notação Big O do seu resultado
#Criar uma lista com todos os elementos da lista, e criar listas separadas para ordenar.

elementos = [['a','b','c','d'],['q','i','n','m'],['f','e','h','j'],['p','o','l','g']]
print('Todos Os Elementos Da Lista: ',elementos)

lista1 = ['a','b','c','d']

lista2 = ['q','i','n','m']

lista3 = ['f','e','h','j']

lista4 = ['p','o','l','g']

lista_cr = sorted(lista1+lista2+lista3+lista4)
print('\nElementos Em Ordem Crescente: \n',lista_cr)

lista_dc = sorted(lista1+lista2+lista3+lista4, reverse= True)
print('\nElementos Em Ordem Decrescente: \n',lista_dc)

#Big O-----------------------------------------------------------------------
import time
import matplotlib.pyplot as plt
 
# Função da sequência de Fibonacci:
def fib(n):
    if n <= 1:
        return n
    fib_n_menos_2 = 0
    fib_n_menos_1 = 1
    for i in range(2, n):
        fib_n = fib_n_menos_1 + fib_n_menos_2
        fib_n_menos_2 = fib_n_menos_1
        fib_n_menos_1 = fib_n
    return fib_n_menos_1 + fib_n_menos_2
 
# listas para armazenar os valores de n e o tempo de execução
ns = []
tempos = []
 
# testa a função para vários valores de n
for n in range(1, 31):
    start = time.perf_counter()
    result= fib(n)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(n)
    tempos.append(ms)
print(result)

# cria o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()