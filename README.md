# Automação e Análise de Relatórios de Pedidos

Projeto desenvolvido por **Julia do Nascimento Pereira** em Python para gerar uma base de pedidos, realizar o tratamento dos dados, calcular indicadores de vendas, gerar um relatório em Excel e criar visualizações.

O projeto foi construído como uma simulação de um fluxo de tratamento e análise de dados comerciais. A base inicial contém inconsistências propositalmente inseridas para que o processo de limpeza e padronização possa ser demonstrado.

---

## Visão Geral

O fluxo atual do projeto é:

**Geração da base → Tratamento dos dados → Cálculo dos indicadores e relatório → Geração dos gráficos**

A execução é feita por quatro scripts Python, cada um responsável por uma etapa específica.

---

## Funcionalidades

### 1. Geração da base de pedidos

O arquivo `src/gerar_base.py` cria uma base fictícia com 10 registros e salva o resultado em Excel.

A base contém as seguintes colunas:

- `ID_Pedido`: identificador do pedido;
- `Cliente`: nome do cliente;
- `Regiao`: região do cliente;
- `Produto`: produto vendido;
- `Quantidade`: quantidade de unidades do pedido;
- `Preco_Unitario`: preço unitário do produto;
- `Data_Pedido`: data do pedido;
- `Status_Entrega`: situação da entrega.

A base também contém inconsistências propositalmente inseridas, como:

- Espaços extras nos nomes dos clientes;
- Diferenças de capitalização;
- Regiões escritas em formatos diferentes;
- Região ausente;
- Valores monetários em formatos diferentes;
- Datas em formatos diferentes;
- Um registro duplicado.

Arquivo gerado:

`data/base_pedidos_bruta.xlsx`

---

### 2. Tratamento dos dados

O arquivo `src/tratar_dados.py` lê a base bruta e realiza as seguintes operações:

- Remove registros duplicados;
- Remove espaços extras dos nomes dos clientes;
- Padroniza os nomes dos clientes utilizando formato de título;
- Converte os preços unitários para números do tipo `float`;
- Preenche regiões ausentes com `Não Informado`;
- Remove espaços extras e padroniza as regiões;
- Converte as datas para o formato `DD/MM/AAAA`;
- Cria a coluna `Faturamento_Total`.

O faturamento é calculado pela multiplicação:

`Quantidade × Preco_Unitario`

O resultado é salvo em:

`output/base_pedidos_tratada.xlsx`

---

### 3. Cálculo dos indicadores e geração do relatório

O arquivo `src/gerar_relatorio.py` utiliza a base tratada para calcular:

- **Faturamento Total**;
- **Total de Pedidos**;
- **Ticket Médio**;
- **Faturamento por Região**;
- **Cinco principais clientes por faturamento**.

O Faturamento por Região é calculado considerando:

- Soma do faturamento;
- Quantidade de pedidos.

Os cinco principais clientes são ordenados pelo faturamento e limitados aos cinco maiores resultados.

O script também exibe os indicadores gerais no terminal.

O resultado analítico é exportado para:

`output/relatorio_executivo.xlsx`

O arquivo Excel possui duas abas:

- `Por Regiao`;
- `Top Clientes`.

Observação: os indicadores gerais de Faturamento Total, Total de Pedidos e Ticket Médio são exibidos no terminal pelo script. Eles não são gravados em uma aba própria no arquivo Excel atual.

---

### 4. Geração de gráficos

O arquivo `src/gerar_graficos.py` utiliza **Matplotlib** e **Seaborn** para criar duas visualizações a partir da base tratada:

#### Faturamento por Região

Gráfico de barras com o faturamento total de cada região.

Arquivo:

`output/grafico_faturamento_regiao.png`

#### Cinco principais clientes

Gráfico de donut com a participação dos cinco clientes com maior faturamento.

Arquivo:

`output/grafico_top_clientes.png`

Os gráficos são salvos em formato PNG com resolução de 300 DPI.

---

## Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| **Python 3.12+** | Desenvolvimento dos scripts de processamento |
| **Pandas** | Leitura, tratamento, transformação e análise dos dados |
| **OpenPyXL** | Leitura e escrita dos arquivos Excel |
| **Matplotlib** | Geração dos gráficos |
| **Seaborn** | Construção e estilização das visualizações |
| **Git** | Controle de versão |
| **GitHub** | Hospedagem do código |

As versões das principais bibliotecas utilizadas estão definidas no arquivo `requirements.txt`.

---

## Estrutura do Projeto

```text
automacao-relatorio-pedidos/
│
├── data/
│   └── base_pedidos_bruta.xlsx
│
├── src/
│   ├── gerar_base.py
│   ├── tratar_dados.py
│   ├── gerar_relatorio.py
│   └── gerar_graficos.py
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

### 5. Gerar a base de pedidos

```powershell
python src/gerar_base.py
```

Esse comando gera:

`data/base_pedidos_bruta.xlsx`

### 6. Tratar os dados

```powershell
python src/tratar_dados.py
```

Esse comando gera:

`output/base_pedidos_tratada.xlsx`

### 7. Calcular os indicadores e gerar o relatório

```powershell
python src/gerar_relatorio.py
```

Esse comando:

- Calcula os indicadores gerais;
- Exibe os resultados no terminal;
- Calcula o faturamento por região;
- Identifica os cinco principais clientes;
- Gera o arquivo `output/relatorio_executivo.xlsx`.

### 8. Gerar os gráficos

```powershell
python src/gerar_graficos.py
```

Esse comando gera:

- `output/grafico_faturamento_regiao.png`;
- `output/grafico_top_clientes.png`.

---

## Fluxo de Execução

Os scripts devem ser executados na seguinte ordem:

```text
src/gerar_base.py
        ↓
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

Soma da coluna `Faturamento_Total` da base tratada.

### Total de Pedidos

Quantidade de registros existentes na base tratada após a remoção de duplicidades.

### Ticket Médio

Média da coluna `Faturamento_Total` da base tratada.

### Faturamento por Região

Agrupamento dos pedidos por região, considerando a soma do faturamento e a quantidade de pedidos.

### Cinco principais clientes

Ranking dos cinco clientes com maior faturamento na base tratada.

---

## Competências Aplicadas

- Python;
- Pandas;
- Tratamento e transformação de dados;
- Manipulação de arquivos Excel;
- Cálculo de indicadores;
- Análise de dados;
- Visualização de dados;
- Matplotlib;
- Seaborn;
- Automação de processos;
- Git;
- GitHub.

---

## Autoria

Desenvolvido por **Julia do Nascimento Pereira**.

Projeto desenvolvido como parte do portfólio de **Engenharia de Software**, com foco em desenvolvimento, automação de processos e análise de dados.

---

## Status

**Em desenvolvimento e evolução contínua.**
