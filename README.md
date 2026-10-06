# Automação e Análise de Relatórios de Pedidos

Projeto desenvolvido por **Julia do Nascimento Pereira** em Python para automatizar o fluxo de tratamento de dados de pedidos, cálculo de indicadores e geração de relatórios e visualizações de vendas.

O projeto simula um fluxo de **ETL (Extração, Transformação e Carga)**, partindo de uma base bruta com inconsistências até a geração de uma base tratada, indicadores e arquivos de análise.

---

## Visão Geral

O processo realiza as seguintes etapas:

**Base bruta → Limpeza e transformação → Cálculo de indicadores → Relatório → Gráficos**

A proposta é reproduzir um cenário prático de tratamento e análise de dados comerciais utilizando Python e bibliotecas voltadas para manipulação e visualização de dados.

---

## Funcionalidades

### Geração de Dados Sintéticos

O projeto cria uma base fictícia com problemas propositalmente inseridos, como:

- Espaços extras em nomes;
- Diferenças de capitalização;
- Regiões com formatos diferentes;
- Valores monetários em formatos textuais;
- Datas em formatos distintos;
- Valores ausentes;
- Registros duplicados.

Arquivo responsável:

`src/gerar_base.py`

---

### Limpeza e Tratamento de Dados

O tratamento é realizado com **Pandas** e inclui:

- Remoção de registros duplicados;
- Higienização dos nomes dos clientes;
- Padronização de nomes para *Title Case*;
- Conversão de valores monetários para `float`;
- Tratamento de valores ausentes na coluna de região;
- Padronização das regiões;
- Conversão e padronização das datas para `DD/MM/AAAA`;
- Criação da coluna de **Faturamento Total**, calculada a partir de quantidade × preço unitário.

Arquivo responsável:

`src/tratar_dados.py`

Resultado:

`output/base_pedidos_tratada.xlsx`

---

### Relatório de Vendas

O projeto calcula indicadores gerais e realiza análises por região e por cliente.

São calculados:

- Faturamento total;
- Total de pedidos;
- Ticket médio;
- Faturamento por região;
- Cinco principais clientes por faturamento.

Arquivo responsável:

`src/gerar_relatorio.py`

Resultado:

`output/relatorio_executivo.xlsx`

O relatório é exportado em formato **Excel**, com abas para análise por região e principais clientes.

---

### Visualização de Dados

O projeto gera gráficos automaticamente utilizando **Matplotlib** e **Seaborn**.

Visualizações disponíveis:

- Faturamento total por região em gráfico de barras;
- Cinco principais clientes por faturamento em gráfico de donut.

Arquivo responsável:

`src/gerar_graficos.py`

Arquivos gerados:

`output/grafico_faturamento_regiao.png`

`output/grafico_top_clientes.png`

---

## Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| **Python 3.12+** | Desenvolvimento do processo |
| **Pandas** | Tratamento e transformação dos dados |
| **OpenPyXL** | Leitura e escrita de arquivos Excel |
| **Matplotlib** | Geração de gráficos |
| **Seaborn** | Visualização de dados |
| **Git** | Controle de versão |
| **GitHub** | Hospedagem e versionamento |

---

## Estrutura do Projeto

```text
automacao-relatorio-pedidos/
│
├── data/
│   └── base_pedidos_bruta.xlsx
│       └── Base de dados bruta
│
├── src/
│   ├── gerar_base.py
│   │   └── Geração da base simulada
│   │
│   ├── tratar_dados.py
│   │   └── Limpeza e transformação dos dados
│   │
│   ├── gerar_relatorio.py
│   │   └── Cálculo dos indicadores e relatório em Excel
│   │
│   └── gerar_graficos.py
│       └── Geração das visualizações
│
├── output/
│   ├── base_pedidos_tratada.xlsx
│   ├── relatorio_executivo.xlsx
│   ├── grafico_faturamento_regiao.png
│   └── grafico_top_clientes.png
│
├── requirements.txt
└── README.md
```

---

## Como Executar

### 1. Clonar o repositório

```powershell
git clone https://github.com/julia-nascimento-dev/automacao-relatorio-pedidos.git
cd automacao-relatorio-pedidos
```

### 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 5. Gerar a base bruta

```powershell
python src/gerar_base.py
```

Esse comando cria:

`data/base_pedidos_bruta.xlsx`

### 6. Executar o tratamento dos dados

```powershell
python src/tratar_dados.py
```

Esse processo gera:

`output/base_pedidos_tratada.xlsx`

### 7. Gerar o relatório

```powershell
python src/gerar_relatorio.py
```

Esse processo calcula os indicadores e gera:

`output/relatorio_executivo.xlsx`

### 8. Gerar os gráficos

```powershell
python src/gerar_graficos.py
```

Esse processo gera:

`output/grafico_faturamento_regiao.png`

e

`output/grafico_top_clientes.png`

---

## Processo de Dados

```text
data/base_pedidos_bruta.xlsx
        ↓
src/tratar_dados.py
        ↓
output/base_pedidos_tratada.xlsx
        ↓
src/gerar_relatorio.py
        ↓
output/relatorio_executivo.xlsx

output/base_pedidos_tratada.xlsx
        ↓
src/gerar_graficos.py
        ↓
output/grafico_faturamento_regiao.png
output/grafico_top_clientes.png
```

---

## Indicadores

### Faturamento Total

Soma do faturamento calculado para os pedidos presentes na base tratada.

### Total de Pedidos

Quantidade de registros existentes após o processo de tratamento.

### Ticket Médio

Valor médio do faturamento por pedido.

### Faturamento por Região

Consolidação do faturamento e quantidade de pedidos por região.

### Cinco Principais Clientes

Ranking dos cinco clientes com maior faturamento na base analisada.

---

## Competências Aplicadas

- Python;
- Pandas;
- ETL;
- Limpeza e tratamento de dados;
- Manipulação de arquivos Excel;
- Cálculo de indicadores;
- Análise de dados;
- Visualização de dados;
- Matplotlib;
- Seaborn;
- Git;
- GitHub;
- Automação de processos.

---

## Autoria

Desenvolvido por **Julia do Nascimento Pereira**.

Projeto desenvolvido como parte do meu portfólio de **Engenharia de Software**, com foco em desenvolvimento, automação de processos e análise de dados.

---

## Status

**Em desenvolvimento / evolução contínua.**
