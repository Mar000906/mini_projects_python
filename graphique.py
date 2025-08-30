import streamlit as st
import pandas as pd

st.title("📊 Graphique interactif de la semaine")

st.write("Entrez vos données (par exemple : heures d'étude ou dépenses) et voyez le graphique.")

# Saisie des données par l'utilisateur
lundi = st.number_input("Lundi", min_value=0, value=2)
mardi = st.number_input("Mardi", min_value=0, value=3)
mercredi = st.number_input("Mercredi", min_value=0, value=1)
jeudi = st.number_input("Jeudi", min_value=0, value=4)
vendredi = st.number_input("Vendredi", min_value=0, value=2)
samedi = st.number_input("Samedi", min_value=0, value=5)
dimanche = st.number_input("Dimanche", min_value=0, value=3)

# Création du DataFrame
data = pd.DataFrame({
    "Jour": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
    "Valeur": [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]
})

# Afficher le tableau
st.write("### Données saisies")
st.dataframe(data)

# Afficher le graphique
st.write("### Graphique en barres")
st.bar_chart(data.set_index("Jour"))
