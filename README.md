# 📊 Sales Intelligence & Data Pipeline Automation

Solução **end-to-end de automação de dados** desenvolvida por **Julia do Nascimento Pereira**, com foco no tratamento de dados de vendas, geração de indicadores de desempenho (KPIs), visualização interativa e criação de relatórios executivos.

O projeto simula um fluxo real de **ETL (Extract, Transform, Load)**, partindo de uma base de dados bruta com inconsistências até a geração de informações estruturadas para análise e tomada de decisão.

---

## 🎯 Visão Geral

O projeto automatiza o fluxo de tratamento e análise de uma base de pedidos de vendas.

**Base bruta → Tratamento → Padronização → Análise → Dashboard → Relatório Executivo**

A proposta é reproduzir um cenário próximo ao encontrado em aplicações reais de **automação de dados, análise comercial e geração de informações para apoio à tomada de decisão**.

---

## 🚀 Funcionalidades

### 🧪 Geração de Dados Sintéticos

Criação de uma base de dados simulada com inconsistências de formatação para reproduzir cenários semelhantes aos encontrados em bases reais.

Arquivo responsável:

`src/gerar_base.py`

### 🧹 Limpeza e Tratamento de Dados

Utilizando **Pandas**:

- Remoção de registros duplicados;
- Higienização de strings;
- Padronização de nomes de clientes;
- Padronização de regiões;
- Conversão de valores monetários como `R$ 3.500,00` para valores numéricos (`float`);
- Tratamento de valores ausentes (`null`, `None` e `NaN`);
- Preenchimento de datas ausentes com `Não informada`;
- Padronização das datas para `DD/MM/AAAA`.

Arquivo responsável:

`src/tratar_dados.py`

Resultado:

`output/base_pedidos_tratada.xlsx`

### 📈 Dashboard Web Interativo

O projeto gera um dashboard HTML para visualização dos principais indicadores, utilizando:

- Gráficos dinâmicos com Plotly;
- Busca textual por cliente;
- Filtros por região;
- Interação em tempo real;
- HTML5, CSS3 e JavaScript Vanilla.

Arquivo responsável:

`src/gerar_dashboard_interativo.py`

Resultado:

`output/dashboard_interativo.html`

### 📄 Relatório Executivo

Geração de relatório consolidado com:

- Faturamento total;
- Ticket médio;
- Volume de clientes.

Resultado:

`output/relatorio_executivo.pdf`

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| **Python 3.10+** | Desenvolvimento do pipeline |
| **Pandas** | Tratamento e transformação dos dados |
| **OpenPyXL** | Manipulação de arquivos Excel |
| **Plotly** | Gráficos e visualizações interativas |
| **Matplotlib** | Visualização de dados |
| **Seaborn** | Visualização e análise exploratória |
| **HTML5** | Estrutura do dashboard |
| **CSS3** | Estilização e layout |
| **JavaScript Vanilla** | Interações e filtros |
| **Git** | Controle de versão |
| **GitHub** | Hospedagem e versionamento |

---

## 📁 Estrutura do Projeto

```text
automacao-relatorio-pedidos/
├── .venv/
├── data/
│   └── base_pedidos_bruta.xlsx
├── output/
│   ├── base_pedidos_tratada.xlsx
│   ├── dashboard_interativo.html
│   └── relatorio_executivo.pdf
├── src/
│   ├── gerar_base.py
│   ├── tratar_dados.py
│   ├── gerar_dashboard_interativo.py
│   └── template_coupler.html
├── .gitignore
├── README.md
└── requirements.txt
```

> A pasta `.venv/` representa o ambiente virtual local do Python e não deve ser versionada no Git.

---

## 💻 Como Executar

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

Windows PowerShell:

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 5. Gerar a base bruta

Opcional caso a base já exista:

```powershell
python src/gerar_base.py
```

### 6. Executar o tratamento dos dados

```powershell
python src/tratar_dados.py
```

Gera:

`output/base_pedidos_tratada.xlsx`

### 7. Gerar o dashboard e o relatório executivo

```powershell
python src/gerar_dashboard_interativo.py
```

Gera:

``output/dashboard_interativo.html``
e
``output/relatorio_executivo.pdf``

### 8. Visualizar os resultados

Abra `output/dashboard_interativo.html` em um navegador como Chrome, Edge ou Firefox. O relatório pode ser acessado em `output/relatorio_executivo.pdf`.

---

## 🔁 Pipeline de Dados

```text
data/base_pedidos_bruta.xlsx
        ↓
src/tratar_dados.py
        ↓
output/base_pedidos_tratada.xlsx
        ↓
src/gerar_dashboard_interativo.py
        ↓
output/dashboard_interativo.html
output/relatorio_executivo.pdf
```

---

## 📊 Indicadores

### Faturamento Total
Valor total de faturamento obtido a partir dos pedidos processados.

### Ticket Médio
Indicador utilizado para acompanhar o valor médio das vendas.

### Volume de Clientes
Quantidade de clientes presente na base analisada.

---

## 🧠 Competências Aplicadas

- Python;
- Pandas;
- ETL;
- Tratamento e limpeza de dados;
- Manipulação de arquivos Excel;
- Análise de dados;
- Geração de indicadores;
- Visualização de dados;
- Criação de dashboards;
- HTML5;
- CSS3;
- JavaScript;
- Git;
- GitHub;
- Automação de processos.

---

## 👩🏻‍💻 Autoria

Desenvolvido por **Julia do Nascimento Pereira**.

Projeto desenvolvido como parte do meu portfólio de **Engenharia de Software**, com foco em desenvolvimento, automação de processos e análise de dados.

---

## 📌 Status

**Em desenvolvimento / evolução contínua.**
