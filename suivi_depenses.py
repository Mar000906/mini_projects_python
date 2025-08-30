import streamlit as st
import pandas as pd

st.title("💰 Suivi des Dépenses Personnelles")

# Créer une session pour garder les données
if "depenses" not in st.session_state:
    st.session_state.depenses = []

# Entrée utilisateur
categorie = st.text_input("Catégorie :")
montant = st.number_input("Montant (€) :", min_value=0.0, step=0.5)

# Ajouter une dépense
if st.button("Ajouter dépense"):
    if categorie and montant > 0:
        st.session_state.depenses.append({"Catégorie": categorie, "Montant": montant})
        st.success("✅ Dépense ajoutée !")
    else:
        st.error("⚠️ Veuillez remplir correctement les champs.")

# Afficher les dépenses
if st.session_state.depenses:
    df = pd.DataFrame(st.session_state.depenses)
    st.write("### Tableau des dépenses")
    st.dataframe(df)

    # Graphique
    st.write("### Graphique des dépenses par catégorie")
    st.bar_chart(df.groupby("Catégorie")["Montant"].sum())
