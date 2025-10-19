
#=======================
#|      Packages       |
#=======================
import streamlit as st
from PIL import Image

#=======================
#|        Setup        |
#=======================
with open('Styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

background = Image.open('Pictures/Main_page/Banner.png')
st.image(background)


#=======================
#|       Script        |
#=======================
st.markdown("# Livre de recettes de Victorien 🍰")
st.markdown(
    "Cette application regroupe un ensemble de recettes qu'elles soient de cuisine 🍔, pâtisserie 🧁, chocolaterie 🍫, confiserie 🍬, ... Mais aussi des conseils et astuces quand à la réalisation de ces dernières ou bien le choix de couleurs/ingrédients/accords."
)
st.markdown(
    "L'objectif de cette application est de rassembler les différentes recettes que j'ai pu trouver 🔎, tester 🧪, modifier 🥣 au cours du temps afin de pouvoir les centraliser et les partager."
)

