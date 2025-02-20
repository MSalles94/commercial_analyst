

data=''

#========================================
#Libs
import streamlit as st
from PIL import Image
#========================================
#layout
st.set_page_config(page_title='Produtos',page_icon="🍺",layout='wide')
#======================================================
# Sidebar
from scripts.page_sidebar import *
sidebar_products(st,data)
#======================================================