import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
     page_title="Análise exploratória da previsão de renda",
     page_icon="💹",
     layout="wide",
)
def load_database():
    # Carregando dados
    database = pd.read_csv('./input/previsao_de_renda.csv')
    return database

# Verificando se database já está na base de dados,
# Se não estiver, carregue
if 'raw_database' not in st.session_state:
    st.session_state.raw_database = load_database()

# Salvando database em uma variável
renda = st.session_state['raw_database']

# Criando colunas para apresentação de dados
header = st.columns([0.5, 2, 0.5])
col_left, buff, col_right = st.columns([2,0.2,2])

# Exibindo título e criando padding
header[1].write('<h1 style="text-align:center;">Análise exploratória da previsão de renda</h1>',
                unsafe_allow_html = True)
header[1].write('<h3 style="text-align:center; color: rgba(255,255,255,0.75);">Gráficos bivariados</h3>',
                unsafe_allow_html = True)
header[1].markdown('<div style="padding: 40px 5px;"></div>', unsafe_allow_html = True)

# Abrindo coluna esquerda para escrita
with col_left:
    # Gráfico posse_de_imovel por renda
    avg_salary = renda.groupby('posse_de_imovel')['renda'].mean().reset_index()
    chart1 = alt.Chart(avg_salary).mark_bar().encode(
        x='posse_de_imovel',
        y='renda',
        tooltip=['posse_de_imovel', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'posse_de_imovel'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por status de posse de imóvel'
    ).interactive()

    st.write(chart1)

    # Gráfico posse_de_veiculo por renda
    avg_salary = renda.groupby('posse_de_veiculo')['renda'].mean().reset_index()
    chart2 = alt.Chart(avg_salary).mark_bar().encode(
        x='posse_de_veiculo',
        y='renda',
        tooltip=['posse_de_veiculo', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'posse_de_veiculo'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por status de posse de veículo'
    ).interactive()

    st.write(chart2)    

    # Gráfico qtd_filhos por renda
    avg_salary = renda.groupby('qtd_filhos')['renda'].mean().reset_index()
    chart3 = alt.Chart(avg_salary).mark_bar().encode(
        x='qtd_filhos',
        y='renda',
        tooltip=['qtd_filhos', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'qtd_filhos'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por quantidade de filhos'
    ).interactive()

    st.write(chart3)

    # Gráfico tipo_renda por renda
    avg_salary = renda.groupby('tipo_renda')['renda'].mean().reset_index()
    chart4 = alt.Chart(avg_salary).mark_bar().encode(
        x='tipo_renda',
        y='renda',
        tooltip=['tipo_renda', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'tipo_renda'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por tipo de renda'
    ).interactive()

    st.write(chart4)    

# Abrindo coluna direita para escrita
with col_right:
    # Gráfico educacao por renda
    avg_salary = renda.groupby('educacao')['renda'].mean().reset_index()
    chart5 = alt.Chart(avg_salary).mark_bar().encode(
        x='educacao',
        y='renda',
        tooltip=['educacao', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'educacao'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por nível de educação'
    ).interactive()

    st.write(chart5) 

    # Gráfico estado_civil por renda
    avg_salary = renda.groupby('estado_civil')['renda'].mean().reset_index()
    chart6 = alt.Chart(avg_salary).mark_bar().encode(
        x='estado_civil',
        y='renda',
        tooltip=['estado_civil', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'estado_civil'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por estado civil'
    ).interactive()

    st.write(chart6) 

    # Gráfico tipo_residencia por renda
    avg_salary = renda.groupby('tipo_residencia')['renda'].mean().reset_index()
    chart7 = alt.Chart(avg_salary).mark_bar().encode(
        x='tipo_residencia',
        y='renda',
        tooltip=['tipo_residencia', alt.Tooltip('mean(renda)', format = '.2f')],
        color = 'tipo_residencia'
    ).properties(
        width=600,
        height=400,
        title='Média salarial por tipo de residência'
    ).interactive()

    st.write(chart7) 

    avg_salary = renda.groupby('idade')['renda'].mean().reset_index()
    chart8 = alt.Chart(avg_salary).mark_bar().encode(
        x = alt.X('idade:O', title = 'Faixas de idade'),
        y = alt.Y('mean(renda):Q', title = 'Média salarial'),
        tooltip=['idade', alt.Tooltip('mean(renda)', format = '.2f')]
    ).properties(
        width=600,
        height=400,
        title='Média salarial por faixa de idade'
    )
    chart8 = chart8.configure_axisX(labelAngle = 90)

    st.write(chart8)
