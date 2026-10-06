# 📊 Automação e Análise de Relatórios de Pedidos

Projeto desenvolvido em Python para automação do fluxo de tratamento de dados, geração de indicadores executivos (KPIs) e criação de relatórios visuais de vendas.

---

## 🚀 Funcionalidades

- **Geração de Dados Sintéticos:** Criação de base bruta simulando cenários reais com inconsistências de formatação.
- **Limpeza e Tratamento de Dados (Pandas):**
  - Remoção de registos duplicados.
  - Padronização de nomes de clientes e regiões (remoção de espaços e formatação em *Title Case*).
  - Conversão de valores monetários em formato texto (`R$ 3.500,00`) para numéricos (`float`).
  - Tratamento de valores ausentes (*null/None*).
  - Padronização de datas para o formato `DD/MM/AAAA`.
- **Geração de Relatório Executivo:** Cálculo automático de Faturamento Total, Ticket Médio e consolidação de dados por Região e Top Clientes.
- **Visualização de Dados (Matplotlib & Seaborn):** Geração automática de gráficos de barras e de setores (donut) exportados diretamente em formato `.png`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Manipulação de Dados:** Pandas, OpenPyXL
- **Visualização de Dados:** Matplotlib, Seaborn
- **Controlo de Versão:** Git e GitHub

---

## 📁 Estrutura do Projeto

```text
automacao-relatorio-pedidos/
├── data/
│   └── base_pedidos_bruta.xlsx
├── src/
│   ├── gerar_base.py
│   ├── tratar_dados.py
│   ├── gerar_relatorio.py
│   └── gerar_graficos.py
├── output/
│   ├── base_pedidos_tratada.xlsx
│   ├── relatorio_executivo.xlsx
│   ├── grafico_faturamento_regiao.png
│   └── grafico_top_clientes.png
├── .gitignore
├── requirements.txt
└── README.md
