import streamlit as st

# Crear tres columnas vacías, usamos solo la central
col1, col2, col3 = st.columns([1, 2, 1])  # col2 es más ancha

with col2:
    st.markdown("### KASPA")
    st.markdown("## **0.07 usd**")
    st.markdown("### 7.20 %")


col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    st.markdown("### KASPA")
    st.markdown("## **0.07 usd**")
    st.markdown("### 7.20 %")
