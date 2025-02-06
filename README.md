🖥️ Aplicativo de Criação de Tabelas

Este é um aplicativo simples e moderno para criar tabelas com colunas horizontais e verticais, permitindo a inserção de dados de forma cruzada. O aplicativo também oferece a funcionalidade de salvar a tabela em PDF.
🚀 Como Usar
Pré-requisitos

    Python 3.x instalado.
    Bibliotecas necessárias: tkinter, pandas, reportlab.

Instalação

    Clone o repositório:

git clone https://github.com/seu-usuario/criar-tabela-app.git

Navegue até a pasta do projeto:

cd criar-tabela-app

Instale as dependências:

    pip install pandas reportlab

Executando o Aplicativo

    Execute o arquivo principal:

    python criar_tabela_gui.py

    A interface gráfica será aberta.

🛠️ Funcionalidades

    Adicionar Colunas Horizontais
        No campo "Coluna Horizontal", digite o nome da coluna.
        Clique em "Adicionar Coluna Horizontal".

    Adicionar Colunas Verticais
        No campo "Coluna Vertical", digite o nome da coluna.
        Clique em "Adicionar Coluna Vertical".

    Adicionar Dados
        Clique em "Adicionar Dado".
        Selecione a coluna vertical e a coluna horizontal.
        Insira o valor no campo correspondente.
        Clique em "Confirmar".

    Visualizar Tabela
        A tabela será exibida automaticamente na interface, com as colunas horizontais e verticais cruzadas.

    Salvar em PDF
        Clique em "Salvar em PDF".
        A tabela será salva como tabela_cruzada.pdf no diretório do projeto.

📊 Exemplo de Uso
Passo a Passo

    Adicione colunas horizontais: "Produto A", "Produto B".

    Adicione colunas verticais: "Jan", "Fev", "Mar".

    Adicione dados:
        ("Jan", "Produto A", "100")
        ("Fev", "Produto B", "200")

    Visualize a tabela:
    	Produto A	Produto B
    Jan	100	
    Fev		200
    Mar		

    Salve a tabela em PDF.

🖼️ Capturas de Tela
Interface Principal

Exemplo de como a interface do aplicativo se apresenta.
Adicionar Dado

Interface para adicionar novos dados cruzados.
Tabela Gerada

A tabela gerada diretamente na interface.
PDF Gerado

Exemplo do arquivo PDF gerado com a tabela.
📂 Estrutura do Projeto

criar-tabela-app/
├── criar_tabela_gui.py  # Código principal do aplicativo
├── README.md            # Este arquivo
├── requirements.txt     # Lista de dependências
└── screenshots/         # Pasta para capturas de tela

📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

    Faça um fork do projeto.
    Crie uma branch para sua feature:

git checkout -b feature/nova-feature

Commit suas mudanças:

git commit -m 'Adicionando nova feature'

Envie para a branch:

git push origin feature/nova-feature

Abra um Pull Request.
