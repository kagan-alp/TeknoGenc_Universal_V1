import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="Tekno Genç AI Asistan", page_icon="🤖")

# Robot Karakteri ve Başlık
st.markdown("<h1 style='text-align: center;'>🤖 TEKNO GENÇ AI V1</h1>", unsafe_allow_html=True)
st.write("---")

# Yapay Zeka Hafızası (Sohbet Geçmişi)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski mesajları ekrana bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan Soru Al (Chat Input)
if prompt := st.chat_input("Bana bir bilimsel soru sor..."):
    # Kullanıcı mesajını göster ve kaydet
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Robotun Cevap Hazırlama Alanı
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Burası Robotun 'Düşünme' simülasyonu
        if "kuvvet" in prompt.lower() or "fizik" in prompt.lower():
            robot_cevap = "Fizik analizi yapılıyor... Girdiğin verilere göre evrensel çekim yasalarını kontrol ettim. Sorun üzerinde derinlemesine çalışıyorum!"
        elif "atom" in prompt.lower() or "kimya" in prompt.lower():
            robot_cevap = "Atomik yapıyı inceliyorum. Çekirdek ve elektron dizilimlerine bakılırsa, sorduğun element oldukça enerjik görünüyor."
        else:
            robot_cevap = f"'{prompt}' konusunu veri tabanımda analiz ettim. Ben Tekno Genç AI olarak bu konuda sana rehberlik edebilirim. Ne öğrenmek istersin?"

        # Cevabı kelime kelime yazdır (Yapay zeka yazıyor hissi)
        for chunk in robot_cevap.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Robotun cevabını hafızaya kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})

