
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

banner_image = Image.open('Pictures/Main_page/Banner.png').convert("RGBA")
txt_layer = Image.new("RGBA", banner_image.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(txt_layer)
text = "Livre de recettes Victorien"
font_size = int(banner_image.width / 15)  # Ajuste la taille du texte selon la largeur
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()
text_width, text_height = draw.textsize(text, font=font)
x = (banner_image.width - text_width) / 2
y = (banner_image.height - text_height) / 2    
draw.text((x+3, y+3), text, font=font, fill=(0, 0, 0, 160))  # ombre
draw.text((x, y), text, font=font, fill=(255, 255, 255, 230))  # texte principal    
combined = Image.alpha_composite(banner_image, txt_layer)
st.image(combined, use_container_width=True)    

#=======================
#|       Script        |
#=======================
st.markdown("# Livre de recettes de Victorien")
st.markdown(
    "Cette application regroupe un ensemble de recettes qu'elles soient de cuisine 🍔, pâtisserie 🧁, chocolaterie 🍫, confiserie 🍬, ... Mais aussi des conseils et astuces quand à la réalisation de ces dernières ou bien le choix de couleurs/ingrédients/accords."
)
st.markdown(
    "L'objectif de cette application est de rassembler les différentes recettes que j'ai pu trouver 🔎, tester 🧪, modifier 🥣 au cours du temps afin de pouvoir les centraliser et les partager."
)

