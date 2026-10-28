# 🧮 Calculadora com Interface Gráfica em Python

Uma aplicação desktop simples e moderna de calculadora desenvolvida em **Python** utilizando a biblioteca gráfica nativa **Tkinter**. Realiza operações aritméticas básicas com interface estilizada e tratamento de erros.

---

## 🚀 Funcionalidades

- **4 Operações Básicas:**
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- **Expressões Compostas:** Suporte a parênteses `(` e `)` e números com ponto flutuante (decimais).
- **Tratamento de Exceções:**
  - Alerta visual caso o usuário tente realizar divisão por zero (`5 / 0`).
  - Alerta visual para expressões matemáticas com sintaxe inválida.
- **Interface Gráfica (GUI):**
  - Tema escuro (*Dark Mode*).
  - Janela com tamanho fixo para manter o alinhamento dos botões.
  - Visor numérico alinhado à direita.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Biblioteca GUI:** [Tkinter](https://docs.python.org/3/library/tkinter.html) *(integrada nativamente ao Python)*

---

## 💻 Como Instalar e Rodar no Windows

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

### 1. Instalar o Python no Windows

Caso ainda não possua o Python instalado:

1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Clique no botão de download para baixar o instalador mais recente para Windows.
3. Abra o instalador baixado.
4. ⚠️ **MUITO IMPORTANTE:** Na primeira tela de instalação, marque a opção:  
   👉 **"Add python.exe to PATH"** (Adicionar Python ao PATH).
5. Clique em **Install Now** e aguarde a finalização.
6. Ao concluir, clique em **Close**.

---

### 2. Baixar o Código do Projeto

Você pode clonar este repositório via terminal ou baixar diretamente:
- Clique no botão verde **Code** no topo desta página e selecione **Download ZIP**.
- Extraia a pasta baixada em qualquer local do seu computador (por exemplo, na Área de Trabalho).

---

### 3. Executar o Programa

1. Abra a pasta onde está o arquivo `calculadora.py`.
2. Clique na **barra de endereços** do Explorador de Arquivos (no topo da janela da pasta).
3. Digite `cmd` e aperte **Enter** (isso abrirá o Prompt de Comando direto na pasta).
4. No terminal, execute o seguinte comando:

```bash
python calculadora.py
(Se o comando python não for reconhecido, tente digitar py calculadora.py).
Atalho alternativo: Após instalar o Python, você também pode simplesmente dar dois cliques no arquivo calculadora.py para abrir a interface gráfica diretamente.
📂 Estrutura do Projeto
code
Text
├── calculadora.py   # Código-fonte da aplicação
└── README.md        # Documentação do projeto
👤 Autor
Desenvolvido por Cristiano
GitHub: @ChrisHT-Br