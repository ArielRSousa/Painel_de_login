import customtkinter
import pymongo
from tkinter import messagebox

# Configurações
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

# Cria a janela
janela = customtkinter.CTk()
janela.geometry('500x300')  
janela.minsize(500, 300)
janela.maxsize(500,300)
janela.title("Projeto de Login")

# Funções   
def clique():
    global email, senha, janela
    if email.get() == "admin" and senha.get() == "admin":
            fg_color = "green"
            messagebox.showinfo("Login", "Login efetuado com sucesso!")
            janela.destroy()
            criar_nova_janela()
    else:
        messagebox.showerror("Login", "Usuario ou senha incorretos!", icon="warning")            


# Função para criar a nova janela ao efetuar o login
def criar_nova_janela():
    janela = customtkinter.CTk()
    janela.geometry('500x300')
    janela.minsize(500, 300)
    janela.maxsize(500, 300)
    janela.title("Projeto de Login")
    texto = customtkinter.CTkLabel(janela, text="Login efetuado com sucesso!", font=("Arial", 20))
    texto.pack(padx=10, pady=10)
    janela.mainloop()
    
# Função para ocultar a senha
def ocultar_senha(senha, botao_mostrar_senha): 
    senha.configure(show="*")
    botao_mostrar_senha.configure(text='MOSTRAR SENHA', command=mostrar_senha)

# Função para mostrar a senha
def mostrar_senha(): 
    global senha , botao_mostrar_senha
    senha.configure(show="")
    botao_mostrar_senha.configure(text='OCULTAR SENHA', command=ocultar_senha)

# Função para criar a janela de cadastro de novo usuário ao clicar no botão "Registrar" e salvar na db do MongoDB
def criar_novo_usuario():
    global nova_janela, entry_nome, entry_email, entry_senha
    nova_janela = customtkinter.CTk()
    nova_janela.geometry('400x200')
    nova_janela.minsize(400, 200)
    nova_janela.maxsize(400, 200)
    nova_janela.title("Registrar Novo Usuário")

    # Widgets para capturar informações do novo usuário
    label_nome = customtkinter.CTkLabel(nova_janela, text="Nome:")
    entry_nome = customtkinter.CTkEntry(nova_janela)
    label_email = customtkinter.CTkLabel(nova_janela, text="Email:")
    entry_email = customtkinter.CTkEntry(nova_janela)
    label_senha = customtkinter.CTkLabel(nova_janela, text="Senha:")
    entry_senha = customtkinter.CTkEntry(nova_janela, show='*')
    nova_janela.mainloop()

# Função para criar o novo usuário
def cadastrar():
    global entry_nome, entry_email, entry_senha
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    # Aqui você pode adicionar a lógica para inserir as informações do novo usuário no banco de dados
    messagebox.showinfo("Registro", "Novo usuário cadastrado com sucesso!")
    nova_janela.destroy()


# Widgets
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
email = customtkinter.CTkEntry(janela, placeholder_text="Usuario")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show='*')
botao_mostrar_senha = customtkinter.CTkButton(janela, text="MOSTRAR A SENHA", command=mostrar_senha)
botao_login = customtkinter.CTkButton(janela, text="Login", command=clique)
botao_registrar = customtkinter.CTkButton(janela, text="Registrar Novo Usuário", command=criar_novo_usuario)

# Posicionamento    
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)    
botao_login.pack(padx=60, pady=10)
botao_mostrar_senha.pack(padx=10, pady=10)
botao_registrar.pack(padx=60, pady=10)


# Inicia a janela
janela.mainloop() 