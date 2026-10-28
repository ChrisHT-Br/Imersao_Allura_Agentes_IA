import tkinter as tk
from tkinter import messagebox

def clicar_botao(valor):
    """Adiciona o caractere clicado ao visor."""
    texto_atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(tk.END, texto_atual + str(valor))

def limpar():
    """Limpa o visor."""
    visor.delete(0, tk.END)

def calcular():
    """Calcula a expressão matemática no visor."""
    expressao = visor.get()
    try:
        # Avalia a expressão matemática
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não é possível dividir por zero!")
        limpar()
    except Exception:
        messagebox.showerror("Erro", "Expressão inválida!")
        limpar()

# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x420")
janela.resizable(False, False)
janela.configure(bg="#2b2b2b")

# 2. Visor da Calculadora
visor = tk.Entry(
    janela, 
    font=("Arial", 22), 
    bg="#1e1e1e", 
    fg="#ffffff", 
    bd=0, 
    justify="right"
)
visor.grid(row=0, column=0, columnspan=4, padx=12, pady=(20, 15), ipady=12, sticky="nsew")

# 3. Lista de botões: (Texto, Linha, Coluna, Cor de Fundo, Cor do Texto)
botoes = [
    ('C', 1, 0, '#d9534f', '#ffffff'), 
    ('(', 1, 1, '#4a4a4a', '#ffffff'), 
    (')', 1, 2, '#4a4a4a', '#ffffff'), 
    ('/', 1, 3, '#f0ad4e', '#ffffff'),
    
    ('7', 2, 0, '#3a3a3a', '#ffffff'), 
    ('8', 2, 1, '#3a3a3a', '#ffffff'), 
    ('9', 2, 2, '#3a3a3a', '#ffffff'), 
    ('*', 2, 3, '#f0ad4e', '#ffffff'),
    
    ('4', 3, 0, '#3a3a3a', '#ffffff'), 
    ('5', 3, 1, '#3a3a3a', '#ffffff'), 
    ('6', 3, 2, '#3a3a3a', '#ffffff'), 
    ('-', 3, 3, '#f0ad4e', '#ffffff'),
    
    ('1', 4, 0, '#3a3a3a', '#ffffff'), 
    ('2', 4, 1, '#3a3a3a', '#ffffff'), 
    ('3', 4, 2, '#3a3a3a', '#ffffff'), 
    ('+', 4, 3, '#f0ad4e', '#ffffff'),
    
    ('0', 5, 0, '#3a3a3a', '#ffffff'), 
    ('.', 5, 1, '#3a3a3a', '#ffffff'), 
    ('=', 5, 2, '#5cb85c', '#ffffff'),
]

# 4. Criando e posicionando os botões na tela
for item in botoes:
    texto, linha, coluna, cor_bg, cor_fg = item
    
    if texto == '=':
        comando = calcular
        colspan = 2  # O botão de igual ocupa 2 colunas para fechar a grade
    elif texto == 'C':
        comando = limpar
        colspan = 1
    else:
        comando = lambda t=texto: clicar_botao(t)
        colspan = 1

    btn = tk.Button(
        janela, 
        text=texto, 
        font=("Arial", 14, "bold"),
        bg=cor_bg, 
        fg=cor_fg, 
        bd=0, 
        activebackground="#555555",
        command=comando
    )
    btn.grid(row=linha, column=coluna, columnspan=colspan, padx=4, pady=4, sticky="nsew")

# Ajuste automático das proporções das linhas e colunas
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    janela.grid_rowconfigure(i, weight=1)

# Iniciar o loop da interface gráfica
janela.mainloop()