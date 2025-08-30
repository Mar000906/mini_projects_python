import streamlit as st

st.title("💱 Convertisseur de devises")
st.write("Convertis un montant en euros vers une autre devise.")

# Entrée du montant en euros
euros = st.number_input("Montant en euros :", min_value=0.0, value=10.0, step=1.0)

# Choix de la devise
devise = st.selectbox("Convertir en :", ["Dollar ($)", "Livre (£)", "Yen (¥)"])

# Taux de conversion (exemple simplifié)
taux = {"Dollar ($)": 1.1, "Livre (£)": 0.88, "Yen (¥)": 150.0}

# Conversion
if st.button("Convertir"):
    resultat = euros * taux[devise]
    st.success(f"{euros} € = {resultat:.2f} {devise}")
