import streamlit as st
import random
import string

st.title("Générateur de mots de passe")
st.write("Cliquez sur le bouton pour générer un mot de passe sécurisé.")

# Longueur du mot de passe
length = st.number_input("Longueur du mot de passe", min_value=6, max_value=20, value=12)

# Bouton pour générer
if st.button("Générer"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    st.success(f"Voici votre mot de passe : {password}")
