import streamlit as st

st.title("📝 Quiz interactif")
st.write("Réponds à la question ci-dessous !")

# Question
st.subheader("Quelle est la capitale de la France ?")
reponse = st.radio("Choisis une réponse :", ["Paris", "Londres", "Berlin", "Madrid"])

# Vérification
if st.button("Vérifier la réponse"):
    if reponse == "Paris":
        st.success("🎉 Correct ! Bravo !")
    else:
        st.error("❌ Incorrect ! Essaie encore.")
