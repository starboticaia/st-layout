import streamlit as st
import numpy as np
from PIL import Image

fichero = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if fichero is not None:
  original = Image.open(fichero)
  #img_array = np.array(original)
  
  col1, col2 = st.columns(2)
    
  col1.header("Original")
  col1.image(original, use_column_width=True)
  
  gris = original.convert('LA')
  col2.header("Escala de grises")
  col2.image(gris, use_column_width=True)

  st.divider()
  #ancho, alto = img_array.size
  angulo = st.slider('ángulo',0,360)
  original = original.rotate(angulo)
  
