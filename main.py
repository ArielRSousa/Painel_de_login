import customtkinter
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
    global email, senha
    if email.get() == "admin" and senha.get() == "admin":
            fg_color = "green"
            messagebox.showinfo("Login", "Login efetuado com sucesso!")
            janela.destroy()
            criar_nova_janela()
    else:
        messagebox.showerror("Login", "Usuario ou senha incorretos!", icon="warning")
            

def ocultar_senha():
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
    

# Widgets
texto = customtkinter.CTkLabel(janela, text="Fazer Login")
email = customtkinter.CTkEntry(janela, placeholder_text="Usuario")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show='*')
botao_mostrar_senha = customtkinter.CTkButton(janela, text="MOSTRAR A SENHA", command=mostrar_senha)
botao_login = customtkinter.CTkButton(janela, text="Login", command=clique)

# Posicionamento
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)    
botao_login.pack(padx=60, pady=10)
botao_mostrar_senha.pack(padx=10, pady=10)


# Inicia a janela
janela.mainloop() 