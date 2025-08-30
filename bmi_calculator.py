import streamlit as st

st.title("🧍‍♀️ Calculatrice d'IMC (BMI)")
st.write("Cette application calcule ton Indice de Masse Corporelle.")

# Entrées utilisateur
poids = st.number_input("Entre ton poids (kg) :", min_value=1.0, step=0.5)
taille = st.number_input("Entre ta taille (m) :", min_value=0.5, step=0.01)

# Bouton de calcul
if st.button("Calculer l'IMC"):
    if taille > 0:
        bmi = poids / (taille ** 2)
        st.success(f"Ton IMC est : {bmi:.2f}")

        # Interprétation
        if bmi < 18.5:
            st.warning("➡️ Tu es considéré comme **maigre**.")
        elif 18.5 <= bmi < 24.9:
            st.success("➡️ Tu as un **poids normal** 🎉.")
        elif 25 <= bmi < 29.9:
            st.info("➡️ Tu es en **surpoids**.")
        else:
            st.error("➡️ Tu es en **obésité**.")
    else:
        st.error("⚠️ La taille doit être supérieure à 0 !")
