# -*- coding: utf-8 -*-
"""Projeto Mod01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bzlVHVlPiVidprYCawab7omDOlE1T-Zx
"""

nome = input("Nome do Aluno ")
nota = input("Nota do Aluno ")

nota = int(nota)
if nota >= 7:
  print("Parabéns, você passou!")
else:
  print("Não foi dessa vez, tente novamente")

Nome = input("Nome do Aluno: ")
nota_prova_1 = input("Nota da Prova 1: ")
nota_prova_2 = input("Nota da Prova 2: ")
nota_atividades = input("Nota das Atividades Extras: ")

nota_prova_1 = int(nota_prova_1)
nota_prova_2 = int(nota_prova_2)
nota_atividades = int(nota_atividades)

nota_final = (nota_prova_1 + nota_prova_2 + nota_atividades) / 3

print(f"A nota final de {Nome} é {nota_final}")
if nota_final >= 7:
  print("Parabéns, você passou!")
else:
  print("Não foi dessa vez, tente novamente")