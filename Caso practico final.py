# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 20:23:41 2023

@author: JOSE
"""

import random

def generar_matriz(tamano):
    """Genera una matriz cuadrada de tamaño tamano con números aleatorios entre 0 y 9."""
    return [[random.randint(0, 9) for _ in range(tamano)] for _ in range(tamano)]

def imprimir_matriz(matriz):
    """Imprime la matriz en la consola."""
    for fila in matriz:
        print(fila)

def calcular_sumas(matriz):
    """Calcula las sumas de las filas y columnas de la matriz."""
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(columna) for columna in zip(*matriz)]
    return sumas_filas, sumas_columnas

def imprimir_sumas(sumas_filas, sumas_columnas):
    """Imprime las sumas de las filas y columnas."""
    print("Suma de cada fila:")
    for suma in sumas_filas:
        print(suma)
    
    print("\nSuma de cada columna:")
    for suma in sumas_columnas:
        print(suma)

try:
    tamano = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    
    matriz = generar_matriz(tamano)
    print("\nMatriz generada:")
    imprimir_matriz(matriz)
    
    sumas_filas, sumas_columnas = calcular_sumas(matriz)
    print("\nSumas:")
    imprimir_sumas(sumas_filas, sumas_columnas)

except ValueError:
    print("Error: Por favor, ingrese un número entero válido para el tamaño de la matriz.")
