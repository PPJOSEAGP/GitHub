# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:09:53 2023

@author: JOSE
"""

import random
import unittest

def generar_matriz(tamano):
    return [[random.randint(0, 9) for _ in range(tamano)] for _ in range(tamano)]

def calcular_sumas(matriz):
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(columna) for columna in zip(*matriz)]
    return sumas_filas, sumas_columnas

class TestGenerarMatriz(unittest.TestCase):
    def test_generar_matriz_tamano_0(self):
        matriz = generar_matriz(0)
        self.assertEqual(matriz, [])

    def test_generar_matriz_tamano_3(self):
        matriz = generar_matriz(3)
        self.assertEqual(len(matriz), 3)
        for fila in matriz:
            self.assertEqual(len(fila), 3)

class TestCalcularSumas(unittest.TestCase):
    def test_calcular_sumas_matriz_vacia(self):
        matriz = []
        sumas_filas, sumas_columnas = calcular_sumas(matriz)
        self.assertEqual(sumas_filas, [])
        self.assertEqual(sumas_columnas, [])

    def test_calcular_sumas_matriz_3x3(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sumas_filas_esperadas = [6, 15, 24]
        sumas_columnas_esperadas = [12, 15, 18]
        sumas_filas, sumas_columnas = calcular_sumas(matriz)
        self.assertEqual(sumas_filas, sumas_filas_esperadas)
        self.assertEqual(sumas_columnas, sumas_columnas_esperadas)

if __name__ == "__main__":
    unittest.main()
