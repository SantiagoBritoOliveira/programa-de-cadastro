#1 importa as bibliotecas

import tkinter as tk
import datetime  as dt
from tkinter import ttk

#2 criar a interface grafica
lista_tipos = ['galao', 'caixa', 'saco', 'unidade']
janela = tk.Tk()
#titulo da janela

lista_de_codigos = []


#criação da função
def inserir_codigo():
    descrição = entry_descrição.get()
    tipo = combo_box.get()
    quant = entry_quantidade.get()
    data_criada = dt.datetime.now()
    data_criada = dt.datetime.now().strftime("%d/%m/%y %H:%M")
    codigo = len(lista_de_codigos) + 1
    codigo_str = f'cod-{codigo}'
    lista_de_codigos.append((codigo_str, descrição, tipo, quant, data_criada))






janela.title('Ferramenta de cadastro de Material')

label_descricao = tk.Label(text='descrição do material')

label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descrição = tk.Entry()

entry_descrição.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text='tipo da unidade do material')

label_tipo_unidade.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combo_box = ttk.Combobox(values=lista_tipos) 

combo_box.grid(row=5, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text='Quantiade da unidade do material')
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)


botao_criar_codigo = tk.Button(text='Criar codigo', command=inserir_codigo)
botao_criar_codigo.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=4 )


janela.mainloop()


print(lista_de_codigos)

#  - descrição do material
#  - Unidade
#  - tipo da unidade
#  - quantidade do tipo da Unidade

#4 inteligencia da interface grafica
#  -função 
