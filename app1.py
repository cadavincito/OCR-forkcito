import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="OCR Dark Mode", layout="centered")

# CSS personalizado con gris oscuro
st.markdown("""
    <style>
        /* Tema principal - Gris oscuro */
        body {
            background-color: #1A1A1A;
            color: #FFFFFF;
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Contenedor principal */
        .stApp {
            background-color: #2D2D2D;
            padding: 2rem;
            border-radius: 10px;
        }
        
        /* Títulos */
        .stMarkdown h1 {
            color: #FFFFFF !important;
            text-align: center;
            border-bottom: 2px solid #444444;
            padding-bottom: 10px;
        }
        
        /* Sidebar */
        .stSidebar {
            background-color: #252525 !important;
            border-right: 1px solid #444444;
        }
        
        /* Radio buttons */
        .stRadio > div {
            background-color: #333333;
            padding: 10px;
            border-radius: 8px;
        }
        .stRadio label {
            color: #FFFFFF !important;
        }
        
        /* Cámara */
        .stCamera {
            border: 2px solid #444444;
            border-radius: 8px;
            overflow: hidden;
        }
        
        /* Texto resultante */
        .stCodeBlock {
            background-color: #333333 !important;
            border: 1px solid #444444;
            border-radius: 8px;
            padding: 15px !important;
        }
        
        /* Mensajes del sistema */
        .stAlert {
            background-color: #333333 !important;
            border: 1px solid #444444 !important;
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
    
    # Mostrar resultado con estilo
    st.markdown("### Resultado del reconocimiento:")
    st.code(text, language='text')
