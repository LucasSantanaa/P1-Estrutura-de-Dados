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

#Big O --Resultado de O(n**2) 
import time
import matplotlib.pyplot as plt 

# Função da sequência de Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
 
#Listas para armazenar os valores de n e o tempo de execução
ns = []
tempos = []
 
#Testar a função para vários valores de N
for n in range(1, 31):
    start = time.perf_counter()
    result= fib(n)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(n)
    tempos.append(ms)
print(result) 

#Criar o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de N')
plt.ylabel('Tempo de execução(Micro segundos)')
plt.show()
