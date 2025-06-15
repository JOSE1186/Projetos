import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Lista para armazenar dados
usuarios = []
senhas = []

class SistemaCadastro:
    def __init__(self):
        # Configuração da janela principal
        self.janela = tk.Tk()
        self.janela.title("Sistema de Cadastro")
        self.janela.geometry("400x300")
        
        # Configuração da cor de fundo - CORRIGIDO
        self.janela.configure(bg='#4A90E2')  # Azul moderno correto
        
        # Criação da interface
        self.criar_widgets()
    
    def criar_widgets(self):
        # Frame principal com cor de fundo
        frame = ttk.Frame(self.janela, padding="10", style='Custom.TFrame')
        frame.pack(expand=True)
        
        # Configuração do estilo
        style = ttk.Style()
        style.configure('Custom.TFrame', background='#4A90E2')
        style.configure('Custom.TLabel', background='#4A90E2', foreground='black')
        
        # Campo do usuário - Label acima do campo
        ttk.Label(frame, text="Nome de Usuário:", style='Custom.TLabel').grid(row=0, column=0, pady=(5,0))
        self.entrada_usuario = ttk.Entry(frame, width=30, style='Custom.TEntry')
        self.entrada_usuario.grid(row=1, column=0, pady=(0,10))
        
        # Campo da senha - Label acima do campo
        ttk.Label(frame, text="Senha:", style='Custom.TLabel').grid(row=2, column=0, pady=(5,0))
        self.entrada_senha = ttk.Entry(frame, width=30, show="*", style='Custom.TEntry')
        self.entrada_senha.grid(row=3, column=0, pady=(0,10))
        
        # Botão de cadastro
        ttk.Button(frame, text="Cadastrar", command=self.cadastrar_usuario).grid(row=4, column=0, pady=20)
        
    def cadastrar_usuario(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        
        if len(senha) >= 8:
            usuarios.append(usuario)
            senhas.append(senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "A senha deve ter no mínimo 8 caracteres!")
    
    def limpar_campos(self):
        self.entrada_usuario.delete(0, tk.END)
        self.entrada_senha.delete(0, tk.END)
        self.entrada_usuario.focus()
    
    def iniciar(self):
        self.janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    app = SistemaCadastro()
    app.iniciar()

'''
CÓDIGO ORIGINAL SEM INTERFACE GRÁFICA:

# Lista para armazenar dados
usuarios = []
senhas = []

def cadastrar_usuario():
    while True:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha com no mínimo 8 caracteres: ")
        
        if len(senha) >= 8:
            usuarios.append(usuario)
            senhas.append(senha)
            print("Usuário cadastrado com sucesso!")
            return True
        else:
            print("Senha inválida!")
            print("Digite uma senha com no mínimo 8 caracteres")

# Executa a função de cadastro
cadastro_sucesso = cadastrar_usuario()
'''




