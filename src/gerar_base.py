import os
import pandas as pd

# Garante que a pasta 'data' existe na raiz do projeto
os.makedirs('data', exist_ok=True)

# Criando uma base fictícia com problemas propositais para tratarmos depois
dados = {
    'ID_Pedido': [1001, 1002, 1003, 1004, 1005, 1005, 1006, 1007, 1008, 1009],
    'Cliente': [' Ana Silva ', 'Carlos Souza', 'ANA SILVA', 'Beatriz Lima', ' João Pedro ', ' João Pedro ', 'Maria Clara', 'Carlos Souza', '  Luciana Costa', 'Marcos Vinicius'],
    'Regiao': ['Sudeste', 'Sul', 'sudeste', None, 'Nordeste', 'Nordeste', 'Centro-Oeste', 'SUL', 'Sudeste', 'Norte'],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Cadeira Gamer', 'Cadeira Gamer', 'Fone Ouvido', 'Mouse', 'Notebook', 'Teclado'],
    'Quantidade': [1, 2, 1, 1, 1, 1, 3, 5, 1, 2],
    'Preco_Unitario': ['R$ 3500,00', '150.00', '250', 'R$ 1200.00', '1500.0', '1500.0', '80.0', '150.0', '3500.0', '250.0'],
    'Data_Pedido': ['2026-10-01', '01/10/2026', '2026-10-02', '2026-10-02', '2026-10-03', '2026-10-03', '2026-10-04', '2026-10-04', '2026-10-05', '2026-10-05'],
    'Status_Entrega': ['Entregue', 'Pendente', 'Entregue', 'Atrasado', 'Entregue', 'Entregue', 'Entregue', 'Atrasado', 'Entregue', 'Pendente']
}

# Transforma o dicionário em uma tabela do Pandas (DataFrame)
df = pd.DataFrame(dados)

# Salva em um arquivo Excel dentro da pasta data
caminho_arquivo = 'data/base_pedidos_bruta.xlsx'
df.to_excel(caminho_arquivo, index=False)

print(f"Base bruta gerada com sucesso em: {caminho_arquivo}")