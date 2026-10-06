import os
import pandas as pd

# 1. Carregar a base bruta
caminho_bruto = 'data/base_pedidos_bruta.xlsx'
df = pd.read_excel(caminho_bruto)

print("--- BASE BRUTA ORIGINAL ---")
print(df.info())
print("\nPrimeiras linhas:")
print(df.head())

# 2. Remover duplicatas exatas
df = df.drop_duplicates()

# 3. Limpeza do Nome dos Clientes (Remove espaços extras e padroniza para formato Título: 'Ana Silva')
df['Cliente'] = df['Cliente'].astype(str).str.strip().str.title()

# 4. Tratamento do Preço Unitário (Transformar texto 'R$ 3500,00' em número float 3500.00)
df['Preco_Unitario'] = (
    df['Preco_Unitario']
    .astype(str)
    .str.replace('R$', '', regex=False)
    .str.replace(' ', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

# 5. Criar coluna de Faturamento Total (Quantidade * Preco_Unitario)
df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']

# 6. Tratar valores ausentes na coluna Regiao
df['Regiao'] = df['Regiao'].fillna('Não Informado').str.strip().str.title()

# 7. Padronizar Datas para o formato DD/MM/AAAA
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], dayfirst=True, errors='coerce').dt.strftime('%d/%m/%Y')

# 8. Salvar base limpa na pasta output
os.makedirs('output', exist_ok=True)
caminho_limpo = 'output/base_pedidos_tratada.xlsx'
df.to_excel(caminho_limpo, index=False)

print("\n--- TRATAMENTO CONCLUÍDO COM SUCESSO! ---")
print(f"Base tratada salva em: {caminho_limpo}")
print("\nBase Limpa:")
print(df[['Cliente', 'Regiao', 'Preco_Unitario', 'Faturamento_Total']])