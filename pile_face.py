import random
import streamlit as st

st.title("🎲 Jeu : Pile ou Face")

# L'utilisateur choisit
choix = st.radio("Choisis ton camp :", ["Pile", "Face"])

if st.button("Lancer la pièce"):
    # Tirage au hasard
    resultat = random.choice(["Pile", "Face"])

    st.write(f"💡 La pièce est tombée sur **{resultat}**")

    # Vérifier si le joueur a gagné
    if choix == resultat:
        st.success("🎉 Bravo, tu as gagné !")
    else:
        st.error("😢 Dommage, essaie encore !")
