import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.neighbors import KNeighborsRegressor

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise exploratória da previsão de renda",
     page_icon="💹",
     layout="wide",
)

def runRegr(sexo, posse_de_veiculo, posse_de_imovel, tipo_renda, educacao, qt_pessoas_residencia,idade, tempo_emprego):

     columns_to_encode = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 'tipo_renda', 'educacao']

     # Criando dummies com colunas categóricas
     dummies = pd.get_dummies(renda[columns_to_encode])
     
     # Concatenando colunas dummies com dataframe
     df_encoded = pd.concat([renda, dummies], axis=1)

     # Deletando colunas prévias
     df_encoded.drop(columns_to_encode, axis=1, inplace=True)

     # Separando dados
     X,y = df_encoded.drop('renda', axis = 1), df_encoded['renda']
     
     # Recriando dados de usuário no mesmo formato do que será usado no modelo
     user = pd.DataFrame({'sexo': sexo, 'posse_de_veiculo': posse_de_veiculo , 'posse_de_imovel': posse_de_imovel, 
                          'tipo_renda' : tipo_renda, 'educacao' : educacao, 'qt_pessoas_residencia': qt_pessoas_residencia, 
                          'idade' : idade, 'tempo_emprego' : tempo_emprego},
                          index = [0])
     dummies_user = pd.get_dummies(user[columns_to_encode])
     df_user_encoded = pd.concat([user, dummies_user], axis = 1)
     df_user_encoded.drop(columns_to_encode, axis = 1, inplace = True)
     df_user_encoded = df_user_encoded.reindex(columns=X.columns, fill_value = 0)

     # Treinando modelo
     KNN_model = KNeighborsRegressor(n_neighbors=3).fit(X,y)

     # Executando previsão
     pred = KNN_model.predict(df_user_encoded)

     # Exibindo previsão
     st.sidebar.markdown('<div style="padding: 80px 5px;"></div>', unsafe_allow_html = True)
     st.sidebar.success(f'R$ {pred[0]:.2f}')
     st.toast('Previsão concluída!')

st.write('# Análise exploratória da previsão de renda')

# Limpando dados
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda.drop(['Unnamed: 0', 'id_cliente', 'data_ref', 'tipo_residencia', 'qtd_filhos', 'estado_civil'], axis = 1, inplace = True)
renda.dropna(subset = 'tempo_emprego', inplace = True)
renda['qt_pessoas_residencia'] = renda['qt_pessoas_residencia'].astype('int')

# Criando colunas para organizar app
header = st.columns([0.5, 2, 0.5])
col_top_left, buff, col_top_right = st.columns([2,0.3,2])
col_bot_left, buff, col_bot_right = st.columns([2,0.3,2])

header[1].markdown('<div style="padding: 40px 5px;"></div>', unsafe_allow_html = True)

# Criando formulários para inserção de dados
sexo = col_top_left.selectbox(
    'Selecione seu sexo:',
    ['F', 'M'],
    index = None,
    placeholder = "Escolha F para sexo feminino ou M para masculino"
)

posse_de_veiculo = col_top_left.selectbox(
    'Possui veículo?',
    ['Sim', 'Não'],
    index = None,
    placeholder = "Escolha Sim ou Não"
)
if posse_de_veiculo:
     posse_de_veiculo = True if posse_de_veiculo == "Sim" else False

posse_de_imovel = col_top_left.selectbox(
    'Possui imóvel?',
    ['Sim', 'Não'],
    index = None,
    placeholder = "Escolha Sim ou Não"
)
if posse_de_imovel:
     posse_de_imovel = True if posse_de_imovel == "Sim" else False

tipo_renda = col_bot_left.selectbox(
    'Qual categoria mais se aproxima de classificar seu emprego ?',
    ['Assalariado', 'Empresário', 'Pensionista', 'Servidor público', 'Bolsista'],
    index = None,
    placeholder = "Escolha entre as opções disponíveis"
)

educacao = col_bot_left.selectbox(
    'Qual seu nível de estudo?',
    ['Secundário', 'Superior completo', 'Superior incompleto', 'Primário', 'Pós graduação'],
    index = None,
    placeholder = "Escolha entre as opções disponíveis"
)

qt_pessoas_residencia = col_top_right.slider('Quantas pessoas moram em sua residência?', 0, 15, 0)

idade = col_top_right.slider('Qual a sua idade?', 20, 100, 30)

tempo_emprego = col_top_right.slider('Quantos anos está em seu emprego?', 0, 45, 0)

# Criando botão de execução do algoritmo KNN

col_bot_right.markdown('<div style="padding: 40px 5px;"></div>', unsafe_allow_html = True)

exec_dis = col_bot_right.button("Executar", 
                                type = "primary", 
                                on_click = runRegr, 
                                args = (sexo, posse_de_veiculo, posse_de_imovel,
                                        tipo_renda, educacao, qt_pessoas_residencia,
                                        idade, tempo_emprego),
                                use_container_width = True)

