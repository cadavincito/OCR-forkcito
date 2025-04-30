import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="OCR Dark Mode", layout="centered")

# CSS personalizado con gris oscuro y texto blanco
st.markdown("""
    <style>
        /* Tema principal - Gris oscuro */
        :root {
            --primary-bg: #2D2D2D;
            --secondary-bg: #252525;
            --element-bg: #333333;
            --border-color: #444444;
            --text-color: #FFFFFF;
        }
        
        /* Todos los textos en blanco */
        * {
            color: var(--text-color) !important;
        }
        
        body {
            background-color: var(--primary-bg);
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Contenedor principal */
        .stApp {
            background-color: var(--primary-bg);
            padding: 2rem;
            border-radius: 10px;
        }
        
        /* Títulos */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            text-align: center;
        }
        
        /* Sidebar */
        .stSidebar {
            background-color: var(--secondary-bg) !important;
            border-right: 1px solid var(--border-color);
        }
        
        /* Radio buttons */
        .stRadio > div {
            background-color: var(--element-bg);
            padding: 10px;
            border-radius: 8px;
        }
        
        /* Cámara */
        .stCamera {
            border: 2px solid var(--border-color);
            border-radius: 8px;
            overflow: hidden;
        }
        
        /* Texto resultante */
        .stCodeBlock {
            background-color: var(--element-bg) !important;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 15px !important;
        }
        
        /* Selectores y controles */
        .stRadio, .stCheckbox, .stSelectbox, .stTextInput, .stSlider {
            color: var(--text-color) !important;
        }
        
        /* Placeholders */
        ::placeholder {
            color: #AAAAAA !important;
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)

# Interfaz de usuario
st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    st.markdown("### Configuración de procesamiento")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'), index=1)

if img_file_buffer is not None:
    # Procesamiento de imagen
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar resultado
    st.markdown("### Resultado del reconocimiento:")
    st.code(text, language='text')
