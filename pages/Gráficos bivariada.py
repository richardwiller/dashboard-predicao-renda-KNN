import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise exploratória da previsão de renda",
     page_icon="💹",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

st.write('## Gráficos bivariada')

fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])

sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])

sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])

sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])

sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])

sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])

sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])

sns.despine()
st.pyplot(plt)
