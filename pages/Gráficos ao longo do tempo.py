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
header[1].write('<h3 style="text-align:center; color: rgba(255,255,255,0.75);">Gráficos ao longo do tempo</h3>',
                unsafe_allow_html = True)
header[1].markdown('<div style="padding: 40px 5px;"></div>', unsafe_allow_html = True)

# Abrindo coluna esquerda para escrita
with col_left:
    # Gráfico contagem de posse_de_imovel por renda(organizado em bins)
    chart1 = alt.Chart(renda).mark_bar().encode(
        x=alt.X('renda:O', bin = alt.Bin(maxbins = 20), title = "Renda"),
        y=alt.Y('count(posse_de_imovel):Q', title = "Contagem"),
        color = 'count(posse_de_imovel)'
    ).properties(
        width=600,
        height=400,
        title='Quantidade de pessoas que possuem imóvel por faixa de renda'
    ).interactive()

    st.write(chart1)

    # Gráfico posse_de_imovel por média salarial ao longo do tempo
    chart2 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = "Média salarial"),
        color = 'posse_de_imovel'
    ).properties(
        width=600,
        height=400,
        title='Posse de imóvel por média salarial ao longo do tempo'
    )
    
    st.write(chart2)

    # Gráfico posse_de_veiculo por média salarial ao longo do tempo
    chart3 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = "Média salarial"),
        color = 'posse_de_veiculo'
    ).properties(
        width=600,
        height=400,
        title='Posse de veículo por média salarial ao longo do tempo'
    )

    st.write(chart3)

    # Gráfico qtd_filhos por média salarial ao longo do tempo
    chart4 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title='Média salarial'),
        color = 'qtd_filhos'
    ).properties(
        width=600,
        height=400,
        title = 'Quantidade de filhos por média salarial ao longo do tempo'
    )

    st.write(chart4)

# Abrindo coluna direita para escrita
with col_right:
    # Gráfico tipo_renda por média salarial ao longo do tempo
    chart5 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = 'Média salarial'),
        color = 'tipo_renda'
    ).properties(
        width=600,
        height=400,
        title = 'Tipo de renda por média salarial ao longo do tempo'
    )

    st.write(chart5)

    # Gráfico educacao por média salarial ao longo do tempo
    chart6 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = "Média salarial"),
        color = 'educacao'
    ).properties(
        width=600,
        height=400,
        title = 'Nível de educação por média salarial ao longo do tempo'
    )

    st.write(chart6)

    # Gráfico estado_civil por média salarial ao longo do tempo
    chart7 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = "Média salarial"),
        color = 'estado_civil'
    ).properties(
        width=600,
        height=400,
        title = 'Estado civil por média salarial ao longo do tempo'
    )

    st.write(chart7)

    # Gráfico tipo_residencia por média salarial ao longo do tempo
    chart8 = alt.Chart(renda).mark_line().encode(
        x = 'data_ref',
        y = alt.Y('mean(renda):Q', title = "Média salarial"),
        color = 'tipo_residencia'
    ).properties(
        width=600,
        height=400,
        title = 'Tipo residencial por média salarial ao longo do tempo'
    )

    st.write(chart8)
