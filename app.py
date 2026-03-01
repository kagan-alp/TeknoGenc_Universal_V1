import streamlit as st

# Uygulama Başlığı ve Konsepti
st.set_page_config(page_title="Tekno Genç Universal V1", page_icon="⚛️")

st.title("🚀 Tekno Genç Universal V1")
st.subheader("Evrensel Bilim ve Mühendislik Motoru")

# Yan Menü (Sidebar)
st.sidebar.header("🔬 Laboratuvar Seçimi")
mod = st.sidebar.selectbox("Hangi alanda çalışacaksın?", ["Fizik Motoru", "Kimya & Atom"])

if mod == "Fizik Motoru":
    st.header("⚡ Fiziksel Analiz")
    st.write("Kuvvet, kütle ve ivme hesaplamaları yapabilirsin.")
    
    m = st.number_input("Kütle (kg):", min_value=0.0, value=1.0)
    a = st.number_input("İvme (m/s²):", min_value=0.0, value=0.0)
    
    if st.button("Hesapla"):
        f = m * a
        st.success(f"Hesaplanan Kuvvet (F): {f} Newton")
        st.info("Formül: F = m * a")

elif mod == "Kimya & Atom":
    st.header("⚛️ Atomik Laboratuvar")
    st.write("Elementleri ve atomik yapıları tanı.")
    
    element = st.selectbox("Bir element seç:", ["Hidrojen (H)", "Helyum (He)", "Lityum (Li)"])
    
    if element == "Hidrojen (H)":
        st.write("**Atom Numarası:** 1")
        st.write("**Özellik:** Evrendeki en hafif ve en çok bulunan element.")
    elif element == "Helyum (He)":
        st.write("**Atom Numarası:** 2")
        st.write("**Özellik:** Soygazdır, yanıcı değildir.")
    elif element == "Lityum (Li)":
        st.write("**Atom Numarası:** 3")
        st.write("**Özellik:** En hafif metaldir, pillerde kullanılır.")

st.divider()
st.caption("Tekno Genç V1 - Geleceği Kodlayan Gençlik")
