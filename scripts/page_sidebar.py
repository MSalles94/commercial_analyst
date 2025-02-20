

def cia_logo(st):
    from PIL import Image
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

def sidebar_products(st,data):
    cia_logo(st)