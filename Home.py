import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon="🏠",
    layout='wide'
)

# Sidebar
#======================================================
#image
image_path='assets/Beer-Logo-Graphics-39523999-1.jpg'
image=Image.open(image_path)
st.sidebar.image(image,width=120)
#title
st.sidebar.markdown('# Beverage Bravus Company')
st.sidebar.markdown('## Strength and flavor in every sip.')
st.sidebar.markdown("""---""")
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
