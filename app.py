import streamlit as st
import time

# =================================================================
# 1. TG KAĞAN - SAF VE PROFESYONEL TASARIM (CSS)
# =================================================================
st.set_page_config(page_title="TG KAĞAN", page_icon="🚀", layout="wide")

st.markdown("""
<style>
/* Saf Beyaz Ana Ekran */
.stApp {
    background-color: #ffffff;
    color: #1a1a1a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* Teknofest Roketi ve TG KAĞAN Başlık */
.header-container {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 10px 0;
    border-bottom: 1px solid #f0f0f0;
    margin-bottom: 30px;
}
.rocket-icon { width: 40px; height: 40px; }
.brand-name {
    font-size: 20px;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: 1px;
}

/* Merhaba ve Alt Başlık */
.welcome-section {
    text-align: left;
    margin-bottom: 40px;
}
.welcome-text {
    font-size: 28px;
    font-weight: 400;
    color: #1a1a1a;
    margin-bottom: 5px;
}
.sub-text {
    font-size: 16px;
    color: #666;
}

/* Chat Kutuları - Profesyonel Mesafe */
.chat-row { display: flex; width: 100%; margin: 12px 0; }
.chat-row.user { justify-content: flex-end; }
.chat-row.ai { justify-content: flex-start; }

.bubble {
    padding: 12px 18px;
    border-radius: 15px;
    max-width: 80%;
    font-size: 15px;
    line-height: 1.5;
}

.user .bubble {
    background-color: #007aff; /* Apple Blue */
    color: white;
    border-bottom-right-radius: 2px;
}

.ai .bubble {
    background-color: #f2f2f7;
    color: #1c1c1e;
    border-bottom-left-radius: 2px;
}

/* Input Alanı (Çift kutu hatası düzeltildi) */
div[data-testid="stChatInput"] {
    border: none !important;
    background-color: transparent !important;
}
div[data-testid="stChatInput"] textarea {
    border-radius: 25px !important;
    border: 1px solid #e5e5ea !important;
    background-color: #ffffff !important;
    padding: 12px 20px !important;
}

/* Sidebar Gizleme ve Temizleme */
[data-testid="stSidebar"] { display: none; }
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. SİSTEM BELLEĞİ VE HAFIZA
# =================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =================================================================
# 3. ANA ARAYÜZ (ÜST KISIM)
# =================================================================
# Üst Panel: Roket ve İsim
st.markdown(f"""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Teknofest_logo.png" class="rocket-icon">
        <div class="brand-name">TG KAĞAN</div>
    </div>
    <div class="welcome-section">
        <div class="welcome-text">Merhaba</div>
        <div class="sub-text">Size nasıl yardımcı olabilirim?</div>
    </div>
    """, unsafe_allow_html=True)

# =================================================================
# 4. SOHBET GEÇMİŞİ VE ÖZEL MENÜ (SAĞ TIK/BASILI TUTMA SİMÜLASYONU)
# =================================================================
for i, msg in enumerate(st.session_state.messages):
    role_class = "user" if msg["role"] == "user" else "ai"
    
    # Her kullanıcı mesajı için dinamik bir "Sohbet Yönetimi" butonu (Başlık yerine geçer)
    if msg["role"] == "user":
        with st.expander(f"📌 {msg['content'][:30]}..."):
            col1, col2, col3, col4 = st.columns(4)
            if col1.button("Paylaş", key=f"sh_{i}"): st.toast("Bağlantı kopyalandı!")
            if col2.button("Adlandır", key=f"rn_{i}"): st.toast("Yeniden adlandırıldı.")
            if col3.button("Sabitle", key=f"pin_{i}"): st.toast("Sohbet sabitlendi.")
            if col4.button("Sil", key=f"del_{i}"): 
                st.session_state.messages = []
                st.rerun()

    st.markdown(f'<div class="chat-row {role_class}"><div class="bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

# =================================================================
# 5. AKILLI GİRİŞ VE YANIT (ÇİFT KUTU SORUNU ÇÖZÜLDÜ)
# =================================================================
if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mantıksal Yanıtlar
    p = prompt.lower()
    if any(x in p for x in ["selam", "merhaba"]):
        cevap = "Merhaba, sizi dinliyorum. Bugün ne üzerine çalışıyoruz?"
    elif "nasılsın" in p:
        cevap = "Sizi dinliyorum, her şey yolunda. Sizin için yapabileceğim bir şey var mı?"
    else:
        cevap = "Sizi dinliyorum. Bu konuyu detaylandırabiliriz."

    st.session_state.messages.append({"role": "assistant", "content": cevap})
    st.rerun()
