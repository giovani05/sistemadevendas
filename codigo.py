# TITULO - SISTEMAS DE VENDAS
# comando execução:
    # python -m streamlit run codigo.py

# SEÇÃO CADASTRO DE VENDAS
    # CAMPO DATA
    # CAMPO VENDEDOR
    # CAMPO PRODUTO
    # CAMPO QUANTIDADE
    # CAMPO VALOR
    # BOTÃO CADASTRAR
        # quando clicar no botão -> add venda na tabela

# SEÇÃO VENDAS CADASTRADAS
    # TABELA COM AS VENDAS

# DASHBOARD FATURAMENTO
    # CARD/MÉTRICA -> FATURAMENTO TOTAL
    # GRÁFICO DE BARRA/COLUNA -> VENDA POR VENDEDOR
    # GRÁFICO DE PIZZA -> VENDA POR PRODUTO

# uso de 3 ferramentas de Python:
    # streamlit, pandas, plotly
# importação das ferramentas
import streamlit as st
import pandas as pd
import plotly.express as px

# CARREGAR A BASE DE DADOS
tabela_vendas = pd.read_csv('vendas.csv')

# SISTEMA DE CADASTRO DE VENDAS
st.write('# SISTEMA DE VENDAS')

# SEÇÃO DE CADASTRO DE VENDAS
st.sidebar.write('## CADASTRO DE VENDAS')

# CAMPO DATA
data = st.sidebar.date_input(
    'Data da Venda',
    max_value = pd.to_datetime('today')
)

# CAMPO VENDEDOR
vendedores = ['Ana', 'Bruno', 'Carla', 'Giovani']
vendedor = st.sidebar.selectbox('Vendedor', vendedores)

# CAMPO PRODUTO
produtos = ['Celular', 'Notebook', 'Fone']
produto = st.sidebar.selectbox('Produto', produtos)

# CAMPO QUANTIDADE
quantidade = st.sidebar.number_input('Quantidade', min_value=1, max_value=100, value=1)

# CAMPO VALOR
valor = st.sidebar.number_input('Valor', min_value=0.0, max_value=100000.0, value=0.0, step=0.01)
# FIM CAD VENDAS



# BOTÃO CADASTRAR
    # lógica de cadastro de venda
botao_cadastrar = st.sidebar.button('Cadastrar Venda')
if botao_cadastrar:
    if valor <= 0:
        st.sidebar.error('O valor da venda deve ser maior que zero!')
    else:
        nova_venda = [
            str(data), 
            vendedor, 
            produto, 
            quantidade,
            valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv('vendas.csv', index=False)
        st.sidebar.success('Venda cadastrada com sucesso!')
    
# SEÇÃO DE VIZUALIZAÇÃO DE VENDAS
st.write('## VENDAS CADASTRADAS')
st.dataframe(tabela_vendas)

# SEÇÃO DE DASHBOARD DE FATURAMENTO
st.write('## DASHBOARD DE FATURAMENTO')

# CARD/MÉTRICA -> FATURAMENTO TOTAL
faturamento_total = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R$ {faturamento_total:,.2f}')

# GRÁFICO DE BARRA/COLUNA -> VENDA POR VENDEDOR
    # primeiro cria o gráfico e depois exibe ele
grafico_barra = px.bar(
    tabela_vendas,
    x='vendedor',
    y='valor',
    color='produto'    
)
st.plotly_chart(grafico_barra)

# GRÁFICO DE PIZZA -> VENDA POR PRODUTO
grafico_pizza = px.pie(
    tabela_vendas,
    names='produto',
    values='valor'
)
st.plotly_chart(grafico_pizza)
