import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class TabelaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Criador de Tabelas com Informação Cruzada")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        self.colunas_horizontais = []
        self.colunas_verticais = []
        self.dados = []  # Armazena os dados da tabela

        # Frame para adicionar colunas horizontais
        self.frame_colunas_horizontais = tk.Frame(root, bg="#f0f0f0")
        self.frame_colunas_horizontais.pack(pady=10)

        self.label_coluna_horizontal = tk.Label(self.frame_colunas_horizontais, text="Coluna Horizontal:", bg="#f0f0f0", font=("Arial", 10))
        self.label_coluna_horizontal.grid(row=0, column=0, padx=5)

        self.entry_coluna_horizontal = tk.Entry(self.frame_colunas_horizontais, font=("Arial", 10))
        self.entry_coluna_horizontal.grid(row=0, column=1, padx=5)

        self.botao_adicionar_coluna_horizontal = tk.Button(
            self.frame_colunas_horizontais, text="Adicionar Coluna Horizontal", command=lambda: self.adicionar_coluna("horizontal"),
            bg="#4CAF50", fg="white", font=("Arial", 10), relief=tk.FLAT
        )
        self.botao_adicionar_coluna_horizontal.grid(row=0, column=2, padx=10)

        # Frame para adicionar colunas verticais
        self.frame_colunas_verticais = tk.Frame(root, bg="#f0f0f0")
        self.frame_colunas_verticais.pack(pady=10)

        self.label_coluna_vertical = tk.Label(self.frame_colunas_verticais, text="Coluna Vertical:", bg="#f0f0f0", font=("Arial", 10))
        self.label_coluna_vertical.grid(row=0, column=0, padx=5)

        self.entry_coluna_vertical = tk.Entry(self.frame_colunas_verticais, font=("Arial", 10))
        self.entry_coluna_vertical.grid(row=0, column=1, padx=5)

        self.botao_adicionar_coluna_vertical = tk.Button(
            self.frame_colunas_verticais, text="Adicionar Coluna Vertical", command=lambda: self.adicionar_coluna("vertical"),
            bg="#2196F3", fg="white", font=("Arial", 10), relief=tk.FLAT
        )
        self.botao_adicionar_coluna_vertical.grid(row=0, column=2, padx=10)

        # Frame para adicionar dados
        self.frame_dados = tk.Frame(root, bg="#f0f0f0")
        self.frame_dados.pack(pady=10)

        self.botao_adicionar_dado = tk.Button(
            self.frame_dados, text="Adicionar Dado", command=self.adicionar_dado,
            bg="#FF9800", fg="white", font=("Arial", 10), relief=tk.FLAT
        )
        self.botao_adicionar_dado.grid(row=0, column=0, padx=10)

        # Frame para exibir a tabela
        self.frame_tabela = tk.Frame(root, bg="#f0f0f0")
        self.frame_tabela.pack(pady=10)

        # Botão para salvar em PDF
        self.botao_salvar_pdf = tk.Button(
            root, text="Salvar em PDF", command=self.salvar_pdf,
            bg="#9C27B0", fg="white", font=("Arial", 10), relief=tk.FLAT
        )
        self.botao_salvar_pdf.pack(pady=10)

    def adicionar_coluna(self, tipo):
        if tipo == "horizontal":
            coluna = self.entry_coluna_horizontal.get()
            if coluna:
                self.colunas_horizontais.append(coluna)
                self.entry_coluna_horizontal.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira um nome para a coluna horizontal.")
        elif tipo == "vertical":
            coluna = self.entry_coluna_vertical.get()
            if coluna:
                self.colunas_verticais.append(coluna)
                self.entry_coluna_vertical.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, insira um nome para a coluna vertical.")
        self.atualizar_tabela()

    def adicionar_dado(self):
        if not self.colunas_horizontais or not self.colunas_verticais:
            messagebox.showwarning("Aviso", "Adicione colunas horizontais e verticais antes de inserir dados.")
            return

        janela_dado = tk.Toplevel(self.root)
        janela_dado.title("Adicionar Dado")
        janela_dado.configure(bg="#f0f0f0")

        # Selecionar coluna vertical
        label_coluna_vertical = tk.Label(janela_dado, text="Selecione a Coluna Vertical:", bg="#f0f0f0", font=("Arial", 10))
        label_coluna_vertical.grid(row=0, column=0, padx=5, pady=5)

        combo_coluna_vertical = ttk.Combobox(janela_dado, values=self.colunas_verticais, font=("Arial", 10))
        combo_coluna_vertical.grid(row=0, column=1, padx=5, pady=5)

        # Selecionar coluna horizontal
        label_coluna_horizontal = tk.Label(janela_dado, text="Selecione a Coluna Horizontal:", bg="#f0f0f0", font=("Arial", 10))
        label_coluna_horizontal.grid(row=1, column=0, padx=5, pady=5)

        combo_coluna_horizontal = ttk.Combobox(janela_dado, values=self.colunas_horizontais, font=("Arial", 10))
        combo_coluna_horizontal.grid(row=1, column=1, padx=5, pady=5)

        # Valor do dado
        label_valor = tk.Label(janela_dado, text="Valor:", bg="#f0f0f0", font=("Arial", 10))
        label_valor.grid(row=2, column=0, padx=5, pady=5)

        entry_valor = tk.Entry(janela_dado, font=("Arial", 10))
        entry_valor.grid(row=2, column=1, padx=5, pady=5)

        def confirmar_dado():
            coluna_vertical = combo_coluna_vertical.get()
            coluna_horizontal = combo_coluna_horizontal.get()
            valor = entry_valor.get()

            if coluna_vertical and coluna_horizontal and valor:
                self.dados.append((coluna_vertical, coluna_horizontal, valor))
                self.atualizar_tabela()
                janela_dado.destroy()
            else:
                messagebox.showwarning("Aviso", "Preencha todos os campos.")

        botao_confirmar = tk.Button(
            janela_dado, text="Confirmar", command=confirmar_dado,
            bg="#4CAF50", fg="white", font=("Arial", 10), relief=tk.FLAT
        )
        botao_confirmar.grid(row=3, columnspan=2, pady=10)

    def atualizar_tabela(self):
        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        # Cria a tabela usando Treeview
        colunas = [""] + self.colunas_horizontais
        self.tree = ttk.Treeview(self.frame_tabela, columns=colunas, show="headings", style="Custom.Treeview")
        self.tree.pack()

        # Define o estilo da tabela
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 10), rowheight=25)
        style.configure("Custom.Treeview.Heading", font=("Arial", 10, "bold"))

        # Adiciona as colunas
        for coluna in colunas:
            self.tree.heading(coluna, text=coluna)

        # Adiciona as linhas
        for coluna_vertical in self.colunas_verticais:
            linha = [coluna_vertical] + [""] * len(self.colunas_horizontais)
            for dado in self.dados:
                if dado[0] == coluna_vertical:
                    idx = self.colunas_horizontais.index(dado[1])
                    linha[idx + 1] = dado[2]
            self.tree.insert("", tk.END, values=linha)

    def salvar_pdf(self):
        if not self.colunas_horizontais or not self.colunas_verticais or not self.dados:
            messagebox.showwarning("Aviso", "A tabela está vazia. Adicione colunas e dados antes de salvar.")
            return

        nome_arquivo = "tabela_cruzada.pdf"
        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, height - 50, "Tabela Cruzada")

        c.setFont("Helvetica", 12)
        y = height - 80

        # Cabeçalho horizontal
        cabecalho = [""] + self.colunas_horizontais
        x = 100
        for item in cabecalho:
            c.drawString(x, y, item)
            x += 120
        y -= 20

        # Dados
        for coluna_vertical in self.colunas_verticais:
            linha = [coluna_vertical] + [""] * len(self.colunas_horizontais)
            for dado in self.dados:
                if dado[0] == coluna_vertical:
                    idx = self.colunas_horizontais.index(dado[1])
                    linha[idx + 1] = dado[2]
            x = 100
            for item in linha:
                c.drawString(x, y, item)
                x += 120
            y -= 20

        c.save()
        messagebox.showinfo("Sucesso", f"Tabela salva como {nome_arquivo}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TabelaApp(root)
    root.mainloop()