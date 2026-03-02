import streamlit as st

# 1. KAPAK VE SAYFA AYARLARI (İkon ve Başlık burada değişiyor)
st.set_page_config(
    page_title="Tekno Genç Universal V1",
    page_icon="🚀",
    layout="centered"
)

# 2. HAVALI BİR GİRİŞ (Banner yerine emoji ve büyük başlık)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛰️ TEKNO GENÇ UNIVERSAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>Milli Teknoloji Hamlesi Mühendislik Motoru</b></p>", unsafe_allow_html=True)

# 3. ÜST KAPAK GÖRSELİ (Teknoloji temalı)
st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")

st.divider()

# Yan Menü Tasarımı
with st.sidebar:
    st.title("⚙️ Kontrol Paneli")
    mod = st.radio("Laboratuvar Seç:", ["Fizik Motoru", "Kimya & Atom"])
    st.info("Sürüm: V1.0.0\nCEO: Kağan Alp")

if mod == "Fizik Motoru":
    st.header("⚡ Fiziksel Analiz Sistemi")
    
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input("Kütle (kg):", value=1.0)
    with col2:
        a = st.number_input("İvme (m/s²):", value=0.0)
    
    if st.button("HESAPLA 🔥"):
        f = m * a
        st.balloons() # Başarıyı balonlarla kutla!
        st.success(f"Hesaplanan Kuvvet: {f:,.2f} Newton")
        st.metric(label="Kuvvet Çıkışı (F)", value=f"{f:,.2f} N", delta="Aktif")

elif mod == "Kimya & Atom":
    st.header("⚛️ Atomik Veri Merkezi")
    element = st.selectbox("Elementi Seç:", ["Hidrojen", "Helyum", "Lityum"])
    # Burayı ileride seninle dev bir kütüphaneye çevireceğiz.
    st.write(f"{element} elementi için veriler analiz ediliyor...")

st.divider()
st.write("🇹🇷 *Gelecek, onu bugünden kodlayanlarındır.*")
