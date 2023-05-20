import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry('500x300')
janela.minsize(500, 300)
janela.maxsize(500,300)

def clique():
    print("Login feito com sucesso! [💚]")


def ocultar_senha():
    global senha, botao_mostrar_senha
    senha.configure(show="*")
    botao_mostrar_senha.configure(text='MOSTRAR SENHA', command=mostar_senha)


def mostar_senha():
    global senha, botao_mostrar_senha
    senha.configure(show="")
    botao_mostrar_senha.configure(text='OCULTAR SENHA', command=ocultar_senha)


texto = customtkinter.CTkLabel(janela, text="Fazer Login")
email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show='*')
botao_mostrar_senha = customtkinter.CTkButton(janela, text="MOSTRAR A SENHA", command=mostar_senha)
botao_login = customtkinter.CTkButton(janela, text="Login", command=clique)

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao_login.pack(padx=60, pady=10)
botao_mostrar_senha.pack(padx=10, pady=10)


janela.mainloop()
 