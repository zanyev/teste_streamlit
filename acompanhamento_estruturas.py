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
import openpyxl


# In[75]:


from functools import lru_cache


# In[82]:


@lru_cache
def get_data():
    return pd.read_excel('./operetas.xlsx',engine='openpyxl' )


# In[100]:


data = get_data()


# In[101]:


data = data.replace('-',0)


# In[102]:


st.set_page_config(layout="wide")

st.title("Operações Sob Custódia Prévia do Resultado")


# In[20]:



select = st.sidebar.selectbox('Show Clientes',(data['Código do Cliente']))


# In[21]:


#get the state selected in the selectbox

data_filtro = data[data['Código do Cliente'] == select]


st.subheader('Operações')
if data_filtro.empty:
    st.write('Nenhuma Fence Encontrada')
else:
    st.dataframe(data_filtro)



# In[ ]:


# In[ ]:




