import streamlit as st
import time

# 1. SAYFA AYARLARI (Hata almamak için en üstte olmalı)
st.set_page_config(page_title="TEKNO GENÇ AI - NEXUS", page_icon="🛰️", layout="wide")

# 2. NEXUS V5 GÖRSEL TASARIM (CSS)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

.stApp {
    background: radial-gradient(circle at top, #1a1f25 0%, #05070a 100%);
    color: #e0e6ed;
    font-family: 'Rajdhani', sans-serif;
}

.nexus-header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(90deg, transparent, rgba(0,209,178,0.1), transparent);
    border-bottom: 1px solid rgba(0,255,255,0.1);
    margin-bottom: 30px;
}

.nexus-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(24px, 8vw, 45px);
    font-weight: 700;
    letter-spacing: 5px;
    background: linear-gradient(180deg, #00f2fe 0%, #4facfe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(0,242,254,0.5));
}

.chat-container { display: flex; flex-direction: column; gap: 20px; }

.chat-row { display: flex; width: 100%; margin: 10px 0; }
.chat-row.user { justify-content: flex-end; }
.chat-row.ai { justify-content: flex-start; }

.bubble {
    padding: 12px 20px;
    border-radius: 18px;
    max-width: 80%;
    font-size: 16px;
    backdrop-filter: blur(10px);
}

.user .bubble {
    background: linear-gradient(135deg, #ff4b4b 0%, #b30000 100%);
    color: white;
    border-bottom-right-radius: 2px;
    box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
}

.ai .bubble {
    background: rgba(30, 41, 59, 0.8);
    color: #00f2fe;
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-bottom-left-radius: 2px;
}

.stChatInput {
    border-radius: 50px !important;
    border: 1px solid rgba(0, 242, 254, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

# 3. SİSTEM BELLEĞİ
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. ANA BAŞLIK
st.markdown('<div class="nexus-header"><div class="nexus-title">TEKNO GENÇ AI</div></div>', unsafe_allow_html=True)

# 5. MESAJLARI GÖSTER
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "ai"
    st.markdown(f'<div class="chat-row {role_class}"><div class="bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

# 6. GİRİŞ VE ZEKA
if prompt := st.chat_input("NEXUS'a bir komut ver..."):
    # Kullanıcı mesajı
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # AI Yanıt Mantığı
    p = prompt.lower()
    if any(x in p for x in ["selam", "merhaba"]):
        cevap = "NEXUS Çekirdeği aktif. Hoş geldin CEO Kağan Alp. Tüm sistemler emrinde."
    elif any(x in p for x in ["nasılsın", "durum"]):
        cevap = "Sistem sıcaklığı stabil, muhakeme motoru %100 kapasitede. Seninle çalışmak harika!"
    else:
        cevap = f"'{prompt}' verisi analiz edildi. Stratejik olarak bu konuyu derinleştirebiliriz."

    st.session_state.messages.append({"role": "assistant", "content": cevap})
    st.rerun()
