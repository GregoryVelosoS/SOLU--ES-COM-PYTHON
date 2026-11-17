import customtkinter as ctk


#Cores e fonte
cor_principal = '#FFFFFF'
cor_secundaria = '#FF0000'
cor_texto = '#000000'
cor_sucesso = "#00A100"
cor_erro = '#FF0000'
fonte_texto = ("Arial", 20, "bold")

# Criando tela
janela = ctk.CTk()
# Título
janela.title("Sistema Escolar")
# Definindo tamanho
janela.geometry("500x350")
# Definindo cor de fundo
janela.configure(fg_color = cor_principal)
# Define tema do app
ctk.set_appearance_mode("light")

# Criando título
titulo = ctk.CTkLabel( janela, text="Faça seu login 😁",font=("Segoe UI", 40, "bold"), text_color = cor_texto, justify= "right")
# Anexa o título a tela
titulo.pack(pady='20') 
# titulo.pack(anchor="w") 

# Texto usuário
txt_usuario = ctk.CTkLabel( janela, text="🧑‍💻Usuário",font=fonte_texto, text_color = cor_texto )
txt_usuario.pack(pady='10')

# Input usuário
cx_usuario = ctk.CTkEntry(janela, placeholder_text="Digite seu usuário", justify="center")
cx_usuario.pack(pady='10')

# Texto senha
txt_senha = ctk.CTkLabel( janela, text="🧑Senha",font=fonte_texto, text_color = cor_texto )
txt_senha.pack(pady='10')

# Input usuário
cx_senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha", justify="center", show="*")
cx_senha.pack(pady='10')

# Função para verificar o login
def verificar_login():
    # Pega as informações preenchidas
    usuario = cx_usuario.get()
    senha = cx_senha.get()
    # Compara os valores
    if(usuario == "Cristiano" and senha == "cr7"):
      txt_final.configure(text="LOGIN REALIZADO", text_color = cor_sucesso)        
    else:
      txt_final.configure(text="USUÁRIO OU SENHA INCORRETOS", text_color = cor_erro)        

# Botão login
botao_login = ctk.CTkButton( janela, text="Login",command = verificar_login, fg_color= cor_secundaria, hover_color= cor_texto)
botao_login.pack()

# Texto resposta
txt_final= ctk.CTkLabel( janela, text="",font= ("Arial", 25, "bold"), text_color = cor_texto )
txt_final.pack(pady='10')


janela.mainloop()
