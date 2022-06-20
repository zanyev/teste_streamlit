#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt



# In[3]:


path_filtro = r'C:\Users\rlima\FAROS AAI\Faros - Documentos\MESA RV\Business Inteligence\Relatórios Faros\Produtos Estruturados\Planilhas Operações Gerais\DEBUG saves_ass\operacoes_email_oportunidades.xlsx'


list_excel = pd.read_excel('./operacoes_email_oportunidades.xlsx',sheet_name = [0,1,2,3,4])


# In[11]:


series_clientes = [list_excel[0].Conta,list_excel[1].Conta,list_excel[2].Conta,list_excel[3].Conta,list_excel[4].Conta]


# In[14]:


clientes_unicos = pd.concat(series_clientes).unique()


# In[15]:


for i in range(len(list_excel)):
    if list_excel[i].Estrutura.iloc[0] == 'FENCE':
        fence = list_excel[i]
        

    elif list_excel[i].Estrutura.iloc[0] == 'Booster Vanilla':                
        booster = list_excel[i]
        
    elif list_excel[i].Estrutura.iloc[0] == 'Collar UI':
        collar_ui = list_excel[i]
    
    elif list_excel[i].Estrutura.iloc[0] == 'BoosterShield':
        booster_shield = list_excel[i]
        
    elif list_excel[i].Estrutura.iloc[0] == 'BoosterKO':
        boosterko = list_excel[i]


# In[16]:
st.set_page_config(layout="wide")

st.title("Operações Sob Custódia Disponíveis")


# In[20]:



select = st.sidebar.selectbox('Show Clientes',pd.Series(clientes_unicos))


# In[21]:


#get the state selected in the selectbox

fence_filtro = fence[fence['Conta'] == select]
booster_filtro = booster[booster['Conta'] == select]


st.subheader('Fence')
if fence_filtro.empty:
    st.write('Nenhuma Fence Encontrada')
else:
    st.dataframe(fence_filtro)

st.subheader('Booster')

if booster_filtro.empty:
    st.write('Nenhuma Booster Encontrada')
else:
    st.dataframe(booster_filtro)


# In[ ]:




