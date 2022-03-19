# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:40:04 2022

@author: edwin
"""
# Bibliotecas usadas
import timeit
import numpy as np   
import threading

# Función que calcula la multiplicación de dos matrices;
# esta función es usada por los hilos.
def hilosMatMul(N,t,m):
    for i in range(N):
        for j in range(t,m):
            for k in range(N):
                D[i][j] += A[i][k] * B[k][j]

# Parámetros
N = 1024 # Tamaño de la matriz: es el unico valor a cambiar.
A = np.random.randint(1,6, size=(N,N)) # Matriz aleatoria A (valores entre 1 y 6)
B = np.random.randint(1,6, size=(N,N)) # Matriz aleatoria B (valores entre 1 y 6)

# Código de multiplicación de matrices con dos hilos
D=np.zeros((N,N), int)

print("2 hilos")
start_time = timeit.default_timer()
hilo1 = threading.Thread(target=hilosMatMul,args=(N,0,int(N/2),))
hilo2 = threading.Thread(target=hilosMatMul,args=(N,int(N/2),N,))
hilo1.start()
hilo2.start()
print(timeit.default_timer() - start_time)

# Código de multiplicación de matrices con cuatro hilos
D=np.zeros((N,N), int)

print("4 hilos")
start_time = timeit.default_timer()
hilo1 = threading.Thread(target=hilosMatMul,args=(N,0,int(N/4),))
hilo2 = threading.Thread(target=hilosMatMul,args=(N,int(N/4),2*int(N/4),))
hilo3 = threading.Thread(target=hilosMatMul,args=(N,2*int(N/4),3*int(N/4),))
hilo4 = threading.Thread(target=hilosMatMul,args=(N,3*int(N/4),N,))
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
print(timeit.default_timer() - start_time)

# Código de multiplicación de matrices con ocho hilos
D=np.zeros((N,N), int)

print("8 hilos")
start_time = timeit.default_timer()
hilo1 = threading.Thread(target=hilosMatMul,args=(N,0,int(N/8),))
hilo1.start()
hilo2 = threading.Thread(target=hilosMatMul,args=(N,int(N/8),2*int(N/8),))
hilo2.start()
hilo3 = threading.Thread(target=hilosMatMul,args=(N,2*int(N/8),3*int(N/8),))
hilo3.start()
hilo4 = threading.Thread(target=hilosMatMul,args=(N,3*int(N/8),4*int(N/8),))
hilo4.start()
hilo5 = threading.Thread(target=hilosMatMul,args=(N,4*int(N/8),5*int(N/8),))
hilo5.start()
hilo6 = threading.Thread(target=hilosMatMul,args=(N,5*int(N/8),6*int(N/8),))
hilo6.start()
hilo7 = threading.Thread(target=hilosMatMul,args=(N,6*int(N/8),7*int(N/8),))
hilo7.start()
hilo8 = threading.Thread(target=hilosMatMul,args=(N,7*int(N/8),N,))
hilo8.start()
print(timeit.default_timer() - start_time)

# Código de multiplicación de matrices con 16 hilos
D=np.zeros((N,N), int)

print("16 hilos")
start_time = timeit.default_timer()
hilo1 = threading.Thread(target=hilosMatMul,args=(N,0,int(N/16),))
hilo1.start()
hilo2 = threading.Thread(target=hilosMatMul,args=(N,int(N/16),2*int(N/16),))
hilo2.start()
hilo3 = threading.Thread(target=hilosMatMul,args=(N,2*int(N/16),3*int(N/16),))
hilo3.start()
hilo4 = threading.Thread(target=hilosMatMul,args=(N,3*int(N/16),4*int(N/16),))
hilo4.start()
hilo5 = threading.Thread(target=hilosMatMul,args=(N,4*int(N/16),5*int(N/16),))
hilo5.start()
hilo6 = threading.Thread(target=hilosMatMul,args=(N,5*int(N/16),6*int(N/16),))
hilo6.start()
hilo7 = threading.Thread(target=hilosMatMul,args=(N,6*int(N/16),7*int(N/16),))
hilo7.start()
hilo8 = threading.Thread(target=hilosMatMul,args=(N,7*int(N/16),8*int(N/16),))
hilo8.start()
hilo9 = threading.Thread(target=hilosMatMul,args=(N,8*int(N/16),9*int(N/16),))
hilo9.start()
hilo10 = threading.Thread(target=hilosMatMul,args=(N,9*int(N/16),10*int(N/16),))
hilo10.start()
hilo11 = threading.Thread(target=hilosMatMul,args=(N,10*int(N/16),11*int(N/16),))
hilo11.start()
hilo12 = threading.Thread(target=hilosMatMul,args=(N,11*int(N/16),12*int(N/16),))
hilo12.start()
hilo13 = threading.Thread(target=hilosMatMul,args=(N,12*int(N/16),13*int(N/16),))
hilo13.start()
hilo14 = threading.Thread(target=hilosMatMul,args=(N,13*int(N/16),14*int(N/16),))
hilo14.start()
hilo15 = threading.Thread(target=hilosMatMul,args=(N,14*int(N/16),15*int(N/16),))
hilo15.start()
hilo16 = threading.Thread(target=hilosMatMul,args=(N,15*int(N/16),N,))
hilo16.start()
print(timeit.default_timer() - start_time)

# Código de multiplicación de matrices tradicional
C=np.zeros((N,N), int)

print("Algoritmo Tradicional")
start_time = timeit.default_timer()
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j] += A[i][k] * B[k][j]
print(timeit.default_timer() - start_time)