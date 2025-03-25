import streamlit as st
from PIL import Image
import pandas as pd
from pathlib import Path


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "cv" / "cv_alternance_data.pdf"
css_file = current_dir / "styles" / "main.css"




image = Image.open("C:/Users/JENGO/B2_projet/cv_streamlit/mon_cv/photo.jpg")
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
    st.write("📧Main mail : luidjy.msb@gmail.com")
    st.write("living at La Garenne-Colombes")
    st.write("got my driver's license")
    st.download_button(
        label="Mon CV",
        data=PDFbyte,
        key="pdf_download",
        file_name=resume_file.name,
        mime="application\pdf")
    st.markdown('<a href="https://github.com/JENGADJY" target="_self">Mon Github</a>', unsafe_allow_html=True)   



st.write("-------------------------")
st.write("My name is Luidjy et I'm a student at Ynov campus Paris,currently in B2 IT.")
st.write("I hope become a data analyst later.")
st.write("-------------------------")




col3,col4= st.columns(2, gap="small")



with col3:
    st.subheader("Langages:")

    st.write("Python,Golang,PHP,C#,SQL")
    st.subheader("Bases de Données:")
    st.write("PhpMyAdmin,MongoDB,MySQL")


with col4:
    st.subheader("Framework & Outils:")
    st.write("Scrapping(BeautifulSoup,Selenium)")
    st.write("Visualisation(Pandas,Matplotlib,Streamlit)")
    st.write("Scrapping(BeautifulSoup,Selenium)")


st.subheader("🎓FORMATION:")

st.markdown("• September 2023 - Now : Paris Ynov Campus")
st.write("B2 Informatique")

st.markdown("• 2021-2023 : Baccalauréat Générale ")
st.write("Lycée Albert Einstein , Saint-Geneviève-des-Bois")
st.write("Spécialité 1:Numériques et sciences de l'informatique")
st.write("Spécialité 2:Langues, littératures et civilisations étrangères et régionales Anglais")
st.write("Spécialité de première:Sciences économique et sociales")

st.markdown("• 2020-2021 Seconde Général et Technologique")
st.write("Lycée Léonard de Vinci,Saint-Michel-Sur-Orge")

st.write("-------------------------")

st.subheader("💼PARCOURS PROFESSIONNEL:")

st.markdown("• April 2024 - August 2024 : Viaposte(Crit)")
st.write("91380 Chilly-Mazarin")
st.markdown("Injecteur de colis  , Gestion de zone ")

st.markdown("• Septembre 2023 - January 2024 : AMAZON")
st.write("91220 Brétigny-sur-Orge")
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

st.subheader("CENTRES D’INTERET:")

st.write("Musique")

