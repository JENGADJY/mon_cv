import streamlit as st
from PIL import Image
import pandas as pd
from pathlib import Path


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "cv" / "CVLUIDJYMONGORINSEMEDOBRITO.pdf"
css_file = current_dir / "styles" / "main.css"


with open(css_file) as f:
    css = f.read()

image = Image.open('photo.jpg')
st.set_page_config(page_title="CV de Luidjy MONGORIN SEMEDO BRITO")
data = {
    "Langues" : ["French","English"],
    "Scale on 10" : ["9","7"]
}



df = pd.DataFrame(data)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



col1,col2= st.columns(2, gap="small")


with col1:
    st.image(image)


with col2:
    st.title("MONGORIN SEMEDO BRITO Luidjy")
    st.write("📧Main mail : LUIDJYMSB2301@gmail.com")
    st.write("living at Saint Michel sur Orge ")
    st.write("got my driver's license")
    st.download_button(
        label="telecharge",
        data=PDFbyte,
        key="pdf_download",
        file_name=resume_file.name,
        mime="application\pdf")   



st.write("-------------------------")
st.write("My name is Luidjy et I'm a student at Ynov campus Paris,currently in B1 IT.")
st.write("I hope become a data analyst later.")
st.write("-------------------------")
st.subheader("🎓FORMATION:")

st.markdown("• Septembre 2023 - Maintenant : Paris Ynov Campus")
st.write("B1 Informatique")

st.markdown("• 2021-2023 : Baccalauréat Générale ")
st.write("Lycée Albert Einstein , Saint-Geneviève-des-Bois")
st.write("Spécialité 1:Numériques et sciences de l'informatique")
st.write("Spécialité 2:Langues, littératures et civilisations étrangères et régionales Anglais")
st.write("Spécialité de première:Sciences économique et sociales")

st.markdown("• 2020-2021 Seconde Général et Technologique")
st.write("Lycée Léonard de Vinci,Saint-Michel-Sur-Orge")

st.write("-------------------------")

st.subheader("💼PARCOURS PROFESSIONNEL:")

st.markdown("• Septembre 2023 - Maintenant : AMAZON")
st.markdown("Préparateur de commande , placement des produits ")

st.markdown("• Juin 2022 à Juillet 2023 technicien de maintenance Laverie 3000")
st.write("91100 Évry-Courcouronnes")
st.write("Entretien et nettoyage des stores,rideaux et tapis draps pour les professionnels")
st.write("(mairie, banque , ambassade,palais de justice)")
st.write("Pose des films solaires (banque, école, commissariat etc...)")

st.markdown("• Décembre 2019 Stage de 3éme découverte métier")
st.write("DSI VIAPOST 94270 Le Kremlin Bicêtre")
st.write("Assistant chef projet (rédaction compte rendu des réunions)")
st.write("Découverte du réseau")
st.write("support informatique")
st.write("découverte des différents autres métiers chez Viapost")
st.write("-------------------------")

st.subheader("🗣️LANGUES:")

st.dataframe(df)

st.subheader("COMPÉTENCES:")

st.write("Montage pc complet ")
st.write("Installation système d’exploitation")
st.write("Installation Logiciels")
st.write("Apprentissage des languages (python, HTML, GO)")

st.subheader("CENTRES D’INTERET:")

st.write("Musique")
st.write("Jeux vidéo")





    
    

