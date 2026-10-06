import pandas as pd

# 1. Carregar a base de dados tratada
caminho_tratado = 'output/base_pedidos_tratada.xlsx'
df = pd.read_excel(caminho_tratado)

# 2. Cálculos dos KPIs Gerais
faturamento_total = df['Faturamento_Total'].sum()
total_pedidos = len(df)
ticket_medio = df['Faturamento_Total'].mean()

print("=" * 40)
print("      RELATÓRIO EXECUTIVO DE VENDAS     ")
print("=" * 40)
print(f"Faturamento Total: R$ {faturamento_total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
print(f"Total de Pedidos:  {total_pedidos}")
print(f"Ticket Médio:      R$ {ticket_medio:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
print("=" * 40)

# 3. Análise por Região
print("\n--- FATURAMENTO POR REGIÃO ---")
faturamento_regiao = (
    df.groupby('Regiao')['Faturamento_Total']
    .agg(['sum', 'count'])
    .rename(columns={'sum': 'Faturamento (R$)', 'count': 'Nº Pedidos'})
    .sort_values(by='Faturamento (R$)', ascending=False)
)
print(faturamento_regiao)

# 4. Top Clientes
print("\n--- TOP CLIENTES ---")
top_clientes = (
    df.groupby('Cliente')['Faturamento_Total']
    .sum()
    .reset_index()
    .sort_values(by='Faturamento_Total', ascending=False)
    .head(5)
)
print(top_clientes.to_string(index=False))

# 5. Exportar o resumo executivo para Excel
with pd.ExcelWriter('output/relatorio_executivo.xlsx') as writer:
    faturamento_regiao.to_excel(writer, sheet_name='Por Regiao')
    top_clientes.to_excel(writer, sheet_name='Top Clientes', index=False)

print("\nRelatório exportado com sucesso para: output/relatorio_executivo.xlsx")