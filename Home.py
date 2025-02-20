import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon="🏠",
    layout='wide'
)

#======================================================
# Sidebar
from scripts.page_sidebar import *
cia_logo(st)
#======================================================
# Contnent
st.write('# Beverage Bravus Company Dashboard')

st.markdown("""Dashboard to display key analyses and KPIs for a fictitious enterprise: Beverage Bravus Company, a B2B beverage resale business. """)
st.markdown("""The data presented here is synthetic.""")

st.markdown("""
            #### How to use this dashboard?
            * Home
                * Overview and introductory explanations
            * Business
            * Product
            * Clients
        """)

st.markdown("""
        ### Contact Me

        Feel free to reach out to me through any of the following channels:

        - **Email**: [matheus.salles_1994@hotmail.com](mailto:matheus.salles_1994@hotmail.com)
        - **LinkedIn**: [matheus-cordeiro-salles-06613022/](https://www.linkedin.com/in/matheus-cordeiro-salles-06613022/)
        - **GitHub**: [MSalles94](https://github.com/MSalles94)
        """)
