import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Título do Aplicativo Web
st.title("Análise Exploratória de Dados de Veículos")

# 2. Upload ou carregar dados reais do CSV
st.subheader("Carregamento de Dados")

# REMOVIDO o dado hardcoded. Agora o pandas lê diretamente o seu arquivo vehicles.csv
uploaded_file = "vehicles.csv" 
df = pd.read_csv(uploaded_file)

# 3. Mostrar a tabela de dados na tela
st.subheader("Visualização da Tabela de Dados")
st.dataframe(df)

# 4. Criar o gráfico de barras usando Plotly Express (Ajustado para as colunas do seu CSV)
st.subheader("Gráfico de Preço por Modelo")
fig = px.bar(
    df, 
    x="model",       # Nome exato da coluna no seu CSV
    y="price",       # Nome exato da coluna no seu CSV
    color="type",    # Nome exato da coluna no seu CSV
    title="Preço dos Veículos por Categoria"
)

# 5. Exibir o gráfico no Streamlit
st.plotly_chart(fig)

# 6. Seção do Histograma Interativo por Botão
st.subheader("Análise de Distribuição (Histograma)")

# Criando o botão na tela
meu_botao = st.button('Histograma de Preços')

# Verificando se o botão foi clicado
if meu_botao:
    # Exibindo mensagem de feedback
    st.write('Gerando a distribuição dos preços dos veículos com dados reais...')
    
    # Criando o histograma baseado na coluna real "price"
    fig_hist = px.histogram(
        df, 
        x="price",   # Nome exato da coluna no seu CSV
        title="Distribuição Geral de Preços (Dados do CSV)",
        nbins=20,    # Aumentado para 20 nbins para melhor visualização do volume do CSV
        color_discrete_sequence=['#636EFA'] 
    )
    
    # Renderizando o novo gráfico na tela
    st.plotly_chart(fig_hist)
