import customtkinter
import pymongo
from tkinter import messagebox


# Funções
def clique():
    if email.get() == "admin" and senha.get() == "admin":
            fg_color = "green"
            messagebox.showinfo("Login", "Login efetuado com sucesso!")
            janela.destroy()
            criar_nova_janela()
    else:
        messagebox.showerror("Login", "Usuario ou senha incorretos!", icon="warning")            

def ocultar_senha():
    global senha, botao_mostrar_senha
    senha.configure(show="*")
    botao_mostrar_senha.configure(text='MOSTRAR SENHA', command=mostrar_senha)

def mostrar_senha():
    senha.configure(show="")
    botao_mostrar_senha.configure(text='OCULTAR SENHA', command=ocultar_senha)

def criar_nova_janela():
    janela = customtkinter.CTk()
    janela.geometry('500x300')
    janela.minsize(500, 300)
    janela.maxsize(500, 300)
    janela.title("Projeto de Login")
    texto = customtkinter.CTkLabel(janela, text="Login efetuado com sucesso!", font=("Arial", 20))
    texto.pack(padx=10, pady=10)
    janela.mainloop()
    
def criar_novo_usuario():
    global nova_janela, entry_nome, entry_email, entry_senha
    nova_janela = customtkinter.CTk()
    nova_janela.geometry('400x200')
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