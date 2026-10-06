import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual do Seaborn
sns.set_theme(style="whitegrid")

# 1. Carregar a base tratada
caminho_tratado = 'output/base_pedidos_tratada.xlsx'
df = pd.read_excel(caminho_tratado)

# 2. Gráfico 1: Faturamento por Região (Barras)
plt.figure(figsize=(8, 5))
faturamento_regiao = df.groupby('Regiao')['Faturamento_Total'].sum().reset_index()
faturamento_regiao = faturamento_regiao.sort_values(by='Faturamento_Total', ascending=False)

ax = sns.barplot(data=faturamento_regiao, x='Regiao', y='Faturamento_Total', palette='Blues_d')
plt.title('Faturamento Total por Região (R$)', fontsize=14, fontweight='bold')
plt.xlabel('Região', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)

# Adicionar valores no topo das barras
for p in ax.patches:
    ax.annotate(f'R$ {p.get_height():,.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=10, xytext=(0, 5), 
                textcoords='offset points')

plt.tight_layout()
plt.savefig('output/grafico_faturamento_regiao.png', dpi=300)
plt.close()

# 3. Gráfico 2: Top Clientes (Donut)
plt.figure(figsize=(7, 7))
top_clientes = df.groupby('Cliente')['Faturamento_Total'].sum().reset_index()
top_clientes = top_clientes.sort_values(by='Faturamento_Total', ascending=False).head(5)

plt.pie(top_clientes['Faturamento_Total'], labels=top_clientes['Cliente'], autopct='%1.1f%%', 
        startangle=140, colors=sns.color_palette('Set2'), wedgeprops=dict(width=0.4))

plt.title('Top 5 Clientes por Faturamento', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/grafico_top_clientes.png', dpi=300)
plt.close()

print("--- GRÁFICOS GERADOS COM SUCESSO! ---")
print("Imagens salvas na pasta 'output/':")
print("1. output/grafico_faturamento_regiao.png")
print("2. output/grafico_top_clientes.png")