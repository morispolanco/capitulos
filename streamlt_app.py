import streamlit as st
import requests
import json

def generate_chapter(spell_id, indice, trama, capitulo_numero):
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": spell_id,
            "inputs": {
                "ndice": indice,
                "cap_tulo_n_mero": capitulo_numero,
                "trama": trama
            }
        })
    )
    
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return "Error en la generación del capítulo. Por favor, verifica tus datos."

def main():
    st.title("Generador de Capítulos de Novela")

    spell_id = "QW3t_KZR7urqy_BbUgxV7"  # ID del hechizo a utilizar
    
    indice = st.text_area("Introduce el índice de capítulos de tu novela:")
    trama = st.text_area("Introduce la trama de tu novela:")
    capitulo_numero = st.text_input("Introduce el número del capítulo que deseas generar:")
    
    if st.button("Generar Capítulo"):
        if indice and trama and capitulo_numero:
            chapter_content = generate_chapter(spell_id, indice, trama, capitulo_numero)
            st.subheader(f"Capítulo {capitulo_numero}")
            st.write(chapter_content)
        else:
            st.warning("Por favor, completa todos los campos.")

if __name__ == "__main__":
    main()
