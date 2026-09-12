# Análise Exploratória de Dados de Veículos

## Descrição do Projeto

Este é um aplicativo web interativo desenvolvido com **Streamlit** que realiza análises exploratórias de dados de veículos. O aplicativo processa dados de um arquivo CSV e apresenta visualizações interativas para facilitar a compreensão dos padrões e tendências nos dados dos veículos.

## Para que Serve

O aplicativo foi desenvolvido para explorar e analisar conjuntos de dados sobre veículos, permitindo que usuários visualizem informações sobre modelos, tipos, preços e outras características de forma intuitiva e interativa.

## Funcionalidades

- **📊 Carregamento de Dados**: Lê automaticamente o arquivo `vehicles.csv` contendo informações sobre veículos
  
- **📋 Visualização em Tabela**: Exibe os dados completos em formato de tabela interativa para fácil consulta

- **📈 Gráfico de Preços por Modelo**: Apresenta um gráfico de barras que mostra o preço de cada modelo de veículo, com cores diferenciadas por tipo de veículo (Hatch, Sedan, SUV, etc.)

- **📉 Histograma Interativo**: Oferece uma análise de distribuição dos preços através de um histograma com:
  - Botão para ativar/desativar a visualização
  - Análise de frequência de preços em 20 faixas (bins)
  - Insights sobre a distribuição geral de valores no mercado

## Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Streamlit**: Framework para criar aplicativos web interativos
- **Pandas**: Manipulação e análise de dados
- **Plotly Express**: Criação de gráficos interativos

## Como Usar

1. Certifique-se de ter as dependências instaladas (veja `requirement.txt`)
2. Execute o aplicativo com: `streamlit run app.py`
3. O navegador abrirá automaticamente com a interface do aplicativo
4. Explore os gráficos e interaja com os dados

## Estrutura do Projeto

```
Sprint5/
├── app.py              # Código principal do aplicativo Streamlit
├── vehicles.csv        # Dados dos veículos para análise
├── requirement.txt     # Dependências do projeto
├── README.md          # Documentação do projeto
└── notebooks/
    └── EDA.ipynb      # Análise Exploratória de Dados em Jupyter Notebook
```
