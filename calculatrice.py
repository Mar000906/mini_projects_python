import streamlit as st

st.title("🧮 Mini-calculatrice interactive")

st.write("Entrez deux nombres et choisissez une opération :")

# Champs pour entrer les nombres
a = st.number_input("Nombre 1", value=0.0, format="%.2f")
b = st.number_input("Nombre 2", value=0.0, format="%.2f")

# Boutons pour les opérations
if st.button("Addition (+)"):
    st.success(f"Résultat : {a + b}")

if st.button("Soustraction (-)"):
    st.success(f"Résultat : {a - b}")

if st.button("Multiplication (×)"):
    st.success(f"Résultat : {a * b}")

if st.button("Division (÷)"):
    if b != 0:
        st.success(f"Résultat : {a / b}")
    else:
        st.error("Erreur : division par zéro ❌")
