import streamlit as st

# =================================================================
# 1. TG KAĞAN - ULTRA MİNİMALİST BEYAZ TASARIM (CSS)
# =================================================================
st.set_page_config(page_title="TG KAĞAN", page_icon="🚀", layout="wide")

st.markdown("""
<style>
/* Arka Plan: Saf Beyaz */
.stApp {
    background-color: #ffffff;
    color: #000000;
}

/* ÜST PANEL: (+) Butonu ve TG KAĞAN Başlık */
.header-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #f2f2f7;
    margin-bottom: 20px;
}

.brand-section {
    display: flex;
    align-items: center;
    gap: 10px;
}

.brand-text {
    font-size: 18px;
    font-weight: 600;
    color: #1c1c1e;
    letter-spacing: -0.5px;
}

/* Ana Selamlama */
.welcome-box {
    margin-top: 50px;
    margin-bottom: 30px;
}

.welcome-title {
    font-size: 26px;
    font-weight: 500;
    color: #1c1c1e;
}

.welcome-sub {
    font-size: 15px;
    color: #8e8e93;
    margin-top: 5px;
}

/* Chat Balonları */
.chat-row { display: flex; width: 100%; margin: 10px 0; }
.chat-row.user { justify-content: flex-end; }
.chat-row.ai { justify-content: flex-start; }

.bubble {
    padding: 10px 16px;
    border-radius: 18px;
    max-width: 85%;
    font-size: 15px;
}

.user .bubble {
    background-color: #007aff;
    color: white;
    border-bottom-right-radius: 4px;
}

.ai .bubble {
    background-color: #f2f2f7;
    color: #1c1c1e;
    border-bottom-left-radius: 4px;
}

/* Input Alanı Düzeltme */
div[data-testid="stChatInput"] {
    background-color: transparent !important;
}

div[data-testid="stChatInput"] textarea {
    border: 1px solid #d1d1d6 !important;
    border-radius: 20px !important;
}

/* Gizlemeler */
[data-testid="stSidebar"] { display: none; }
header { visibility: hidden; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. SİSTEM BELLEĞİ
# =================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =================================================================
# 3. ÜST BAR (Roket + TG KAĞAN + Artı Butonu)
# =================================================================
col_left, col_right = st.columns([5, 1])

with col_left:
    st.markdown("""
        <div class="brand-section">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Teknofest_logo.png" width="30">
            <div class="brand-text">TG KAĞAN</div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # (+) Butonu - Yeni Sohbet Başlatır
    if st.button("➕", help="Yeni Sohbet"):
        st.session_state.messages = []
        st.rerun()

# =================================================================
# 4. ANA EKRAN İÇERİĞİ
# =================================================================
if not st.session_state.messages:
    st.markdown("""
        <div class="welcome-box">
            <div class="welcome-title">Merhaba</div>
            <div class="welcome-sub">Size nasıl yardımcı olabilirim?</div>
        </div>
    """, unsafe_allow_html=True)

# Mesajları listele
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "ai"
    st.markdown(f'<div class="chat-row {role_class}"><div class="bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

# =================================================================
# 5. GİRİŞ ALANI
# =================================================================
if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Basit Yanıt Modeli
    cevap = "Seni dinliyorum. Bu konuyu detaylandırabiliriz."
    if "selam" in prompt.lower():
        cevap = "Merhaba, seni dinliyorum. Bugün ne üzerine çalışıyoruz?"
        
    st.session_state.messages.append({"role": "assistant", "content": cevap})
    st.rerun()
