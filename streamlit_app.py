import streamlit as st
from PIL import Image

col1, col2 = st.columns(2)

original = Image.open(image)
col1.header("Original")
col1.image(original, use_column_width=True)

gris = original.convert('LA')
col2.header("Escala de grises")
col2.image(grayscale, use_column_width=True)
