import streamlit as st
import random

st.title("🎲 Jeu du Dé Amélioré")

st.write("Choisis combien de dés tu veux lancer et clique sur le bouton.")

# Sélection du nombre de dés
nb_des = st.slider("Nombre de dés :", 1, 3, 1)

if st.button("Lancer le(s) dé(s)"):
    resultats = []
    images = []
    
    for _ in range(nb_des):
        resultat = random.randint(1, 6)
        resultats.append(resultat)
        images.append(f"https://raw.githubusercontent.com/mahdimortafa/streamlit-dice-images/main/dice{resultat}.png")

    # Afficher les résultats
    st.success(f"Résultats : {resultats}")
    
    # Afficher la somme
    st.info(f"🎯 Somme totale = {sum(resultats)}")
    
    # Afficher les images des dés côte à côte
    cols = st.columns(nb_des)
    for i in range(nb_des):
        with cols[i]:
            st.image(images[i], width=100)
