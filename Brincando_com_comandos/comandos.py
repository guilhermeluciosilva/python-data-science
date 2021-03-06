# -*- coding: utf-8 -*-
"""analisando_randint.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10sALnIAsPyA2yy0fu-5ChvZcGL8fKk5X

#Analisando Python Data science
"""

import pandas as pd
from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Parte dos códigos abaixo foram tirados do site: https://paulovasconcellos.com.br/28-comandos-%C3%BAteis-de-pandas-que-talvez-voc%C3%AA-n%C3%A3o-conhe%C3%A7a-6ab64beefa93


list0 = []

#gerando nossos dados
for x in range(0, 10000):
  list0.append(randint(0, 100))


dados = pd.DataFrame(list0, columns = ["numeros_aleatorios"]) #criando nossa planilha

dados.head(10) #mostra os 10 primeiros

dados.min() #O menor número
dados.max() #O maior número
dados.shape #linhas e colunas
dados.index #começa no 0, termina no 10000 com uma coluna
dados.columns #mostra as colunas, posso até alterar
dados.count #conta os dados não nulos
dados.columns = ['dados_aleatorios']
dados.sum() #soma todos os meus dados
dados.idxmin() #o primeiro index que corresponde ao menor valor 
dados[dados["dados_aleatorios"] == 0] #Aqui estamos selecionando todos os index com o valor 0
dados.idxmax() #o primeiro index que corresponde ao maior valor
dados[dados["dados_aleatorios"] == 100] #Aqui estamos selecionando todos os index com o valor 100
dados.describe() 
"""DataFrame.count
Contar o número de observações não-NA / nulas.

DataFrame.max
Máximo dos valores no objeto.

DataFrame.min
Mínimo dos valores no objeto.

DataFrame.mean
Média dos valores.

DataFrame.std
Desvio padrão das observações.

DataFrame.select_dtypes
Subconjunto de um DataFrame incluindo / excluindo colunas com base em seu tipo."""
dados.mean() #Media dos valores
dados.median() #mediana dos valores
"""A média é a média aritmética de um conjunto de números.
A mediana é um valor numérico que separa a metade superior de um conjunto da metade inferior."""
dados.sort_values("dados_aleatorios") #Classifica os valores da coluna do menor ao maior, mas não por aparição. 
dados.sort_values("dados_aleatorios", ignore_index=True) #aqui ignoramos os index e ordenamos todos os valores
dados.sort_values("dados_aleatorios", ascending=True) #Aqui já classificamos na ordem crescente por aparição, mantendo seu index
dados.sort_values("dados_aleatorios", ascending=False) #Classificamos do maior para o menor, mas não por aparição
dados.add(2)#Somamos todos os valores na série por 2
dados.sub(2)#subtraimos todos os valores da série por 2
dados.div(2)#dividimos todos os valores da série por 2
dados[dados["dados_aleatorios"] % 2 == 0] #Aqui vamos trabalhar só com os valores pares
dados[dados["dados_aleatorios"] % 2 != 0] #Aqui vamos trabalhar só com valores impares 
dados.loc[0, "dados_aleatorios"] #Aqui selecionamos a primeira linha de nosso projeto
dados.loc[9995, "dados_aleatorios"] #Aqui selecionamos a linha 9995 do nosso projeto

dados.plot() # no eixo X temos a quantidade de dados e no eixo Y temos as opçoes de dados

dados.plot.box() #Aqui conseguimos analisar as partes dos nossos dados, sendo o risco verde onde divide a metade dos nossos dados. 
#Esse modelo trabalha em 25% em 25%

dados.plot.area(figsize=(20, 6), subplots = True) 

#Esse é outro metodo de plotagem, o "subplots" vamos usar mais para frente quando formos trabalhar com mais dados
#o "figsize" é para aumentar o tamanho do nosso gráfico, ele funciona em x em y como o exemplo:
#figsize=(x,y)

#comece a olhar: https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

fig = plt.figure()  # uma figura vazia sem eixos
fig, ax = plt.subplots()  # uma figura com um único eixo
fig, axs = plt.subplots(2, 2)  # uma figura com uma grade 2x2 de eixos

x = np.linspace(0, 2, 100) #Retornar números espaçados uniformemente em um intervalo especificado
#Observe que, mesmo no estilo OO, usamos `.pyplot.figure` para criar a figura.
fig, ax = plt.subplots() #Criei uma figura e eixos
ax.plot(x, x, label='linear')   #Traçar alguns dados nos eixos
ax.plot(x,x**2, label='quadratic') # Traçar mais dados sobre os eixos
ax.plot(x, x**3, label='cubic') #trançando mais
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple plot")
ax.legend()

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()