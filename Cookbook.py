
#=======================
#|      Packages       |
#=======================
import streamlit as st
from PIL import Image, ImageDraw, ImageFont



#=======================
#|        Setup        |
#=======================
st.set_page_config(layout="wide")

with open('Styles.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



#=======================
#|       Script        |
#=======================
st.markdown(    
	"""
    <section id="Banner_main">
		<div class="content">
			<h1>Livre de recettes de Victorien</h2>
		</div>
	</section>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    Cette application regroupe un ensemble de recettes qu'elles soient de cuisine 🍔, pâtisserie 🧁, chocolaterie 🍫, confiserie 🍬, ... Mais aussi des conseils et astuces quand à la réalisation de ces dernières ou bien le choix de couleurs/ingrédients/accords.
    
    L'objectif de cette application est de rassembler les différentes recettes que j'ai pu trouver 🔎, tester 🧪, modifier 🥣 au cours du temps afin de pouvoir les centraliser et les partager.
    """
)

