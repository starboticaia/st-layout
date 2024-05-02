import streamlit as st
import numpy as np
from PIL import Image

fichero = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if fichero is not None:
  original = Image.open(fichero)
  img_array = np.array(original)
  
  col1, col2 = st.columns(2)
  
  #original = Image.open(image)
  col1.header("Original")
  col1.image(original, use_column_width=True)
  
  gris = original.convert('LA')
  col2.header("Escala de grises")
  col2.image(gris, use_column_width=True)

  st.divider()
  
  for p in img_array:
    cols = st.columns(2)
    cols[0].write(p)
  #cols[1].write(importes[importes.index(c)])
