import customtkinter
import pymongo
from tkinter import messagebox
from config.funcoes import clique, mostrar_senha, criar_nova_janela, criar_novo_usuario, cadastrar

# Configurações
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

# Cria a janela
janela = customtkinter.CTk()
janela.geometry('500x300')  
janela.minsize(500, 300)
janela.maxsize(500,300)
janela.title("Projeto de Login")



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