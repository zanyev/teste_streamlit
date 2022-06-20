#!/usr/bin/env python
# coding: utf-8

# In[18]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import openpyxl


# In[19]:


from functools import lru_cache


# In[20]:


@lru_cache
def get_data():
    return pd.read_excel('operetas.xlsx',engine='openpyxl')


# In[21]:


data = get_data()


# In[22]:


data['Maximo no Periodo'] = data['Maximo no Periodo'].replace('-',0)


# In[23]:



# In[24]:


st.set_page_config(layout="wide")

st.title("Operações Sob Custódia Disponíveis")


# In[20]:
limpar_clientes = st.sidebar.checkbox('Limpar Filtro Clientes')
buscar_cliente = st.sidebar.checkbox('Buscar Por Nome ?')

if buscar_cliente:
    select = st.sidebar.selectbox('Show Clientes',(data['Nome'].unique()))
else:
    select = st.sidebar.selectbox('Show Clientes',(data['Código do Cliente'].unique()))

limpar_assessores = st.sidebar.checkbox('Limpar Filtro Assessores')

select2 = st.sidebar.selectbox('Show Assessores',(data['Código do Assessor'].unique()))






# In[21]:


#get the state selected in the selectbox
if limpar_clientes:
    data_filtro = data[data['Código do Cliente'].isin(data['Código do Cliente'].unique())]
else:
    if buscar_cliente:
        data_filtro = data[data['Nome'] == select]
    else:
        data_filtro = data[data['Código do Cliente'] == select]

if limpar_assessores:
    data_filtro = data[data['Código do Cliente'].isin(data['Código do Cliente'].unique())]
else:
    data_filtro = data[(data['Código do Assessor'] == select2)] 






st.subheader('Fence')
if data_filtro.empty:
    st.write('Nenhuma Estrutura Encontrada')
else:
    st.dataframe(data_filtro)



# In[ ]:


# In[ ]:




