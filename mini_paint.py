import streamlit as st

st.title("🎨 Mini-Paint avec Streamlit")
st.write("Choisis une couleur et clique sur les cases pour dessiner !")

# Choix de la couleur
couleur = st.color_picker("Choisis une couleur :", "#ff0000")

# Taille du tableau
taille = 5  # 5x5 cases

# Créer la grille de dessin
for i in range(taille):
    cols = st.columns(taille)
    for j, col in enumerate(cols):
        if col.button(" ", key=f"button_{i}_{j}"):  # clé unique pour chaque bouton
            col.markdown(
                f"<div style='width:50px;height:50px;background-color:{couleur};'></div>",
                unsafe_allow_html=True
            )
