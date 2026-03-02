import streamlit as st
import time
import random

# =================================================================
# 1. ULTRASONİK NEXUS V6 MOTORU (CSS & TASARIM)
# =================================================================
st.set_page_config(page_title="NEXUS AI", page_icon="🇹🇷", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@500;700&display=swap');

/* Ana Arka Plan ve Hareketli Işıklar */
.stApp {
    background: #05070a;
    background-image: radial-gradient(circle at 20% 30%, rgba(0, 242, 254, 0.05) 0%, transparent 50%),
                      radial-gradient(circle at 80% 70%, rgba(255, 75, 75, 0.05) 0%, transparent 50%);
    color: #e0e6ed;
    font-family: 'Rajdhani', sans-serif;
}

/* Başlık: MERHABA (Neon Efektli) */
.welcome-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(40px, 10vw, 80px);
    font-weight: 900;
    text-align: center;
    background: linear-gradient(180deg, #ffffff 0%, #00f2fe 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 15px rgba(0,242,254,0.6));
    margin: 40px 0;
}

/* Sağ Alt: Dalgalanan TÜRK BAYRAĞI */
.flag-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    width: 120px;
    filter: drop-shadow(0 0 10px rgba(255,0,0,0.5));
}

/* Mesaj Baloncukları */
.chat-row { display: flex; width: 100%; margin: 15px 0; }
.chat-row.user { justify-content: flex-end; }
.chat-row.ai { justify-content: flex-start; }

.bubble {
    padding: 18px 25px;
    border-radius: 25px;
    max-width: 75%;
    font-size: 18px;
    line-height: 1.4;
    backdrop-filter: blur(15px);
    transition: 0.3s ease;
}

.user .bubble {
    background: linear-gradient(135deg, #ff4b4b 0%, #8b0000 100%);
    color: white;
    border-bottom-right-radius: 4px;
    box-shadow: 0 8px 20px rgba(255, 75, 75, 0.2);
}

.ai .bubble {
    background: rgba(20, 26, 35, 0.9);
    color: #ffffff;
    border-left: 4px solid #00f2fe;
    border-bottom-left-radius: 4px;
}

/* Yazı Girişi Tasarımı */
.stChatInput {
    border: 1px solid rgba(0, 242, 254, 0.4) !important;
    background: rgba(10, 15, 25, 1) !important;
    border-radius: 30px !important;
}

/* Sidebar Gizleme ve Temizleme */
[data-testid="stSidebar"] { background-color: #0a0f19 !important; }
div[data-testid="stStatusWidget"] { visibility: hidden; }
</style>

<div class="flag-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg" width="100%">
</div>
""", unsafe_allow_html=True)

# =================================================================
# 2. ZEKA KATMANI VE HAFIZA
# =================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =================================================================
# 3. ANA EKRAN (HEADER)
# =================================================================
st.markdown('<div class="welcome-title">MERHABA</div>', unsafe_allow_html=True)

# Mesaj Geçmişini Render Et
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "ai"
    st.markdown(f'<div class="chat-row {role_class}"><div class="bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

# =================================================================
# 4. GİRİŞ VE SÜPER MUHAKEME MANTIĞI
# =================================================================
if prompt := st.chat_input("Düşüncelerini buraya yaz..."):
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # --- GERÇEKÇİ YANIT ALGORİTMASI ---
    p = prompt.lower()
    
    # Özel Kelime Analizleri (Seni Dinliyorum Mantığı)
    if any(x in p for x in ["selam", "merhaba", "sa", "hey"]):
        cevap = "Seni dinliyorum CEO. Bugün hangi projeyi hayata geçirelim?"
    
    elif any(x in p for x in ["nasılsın", "ne haber", "durum nedir"]):
        cevap = "Her şey yolunda, işlemcilerim seninle sohbet etmek için sabırsızlanıyor. Sen nasılsın?"

    elif any(x in p for x in ["soru sor", "bilgi ver", "analiz yap"]):
        cevap = "Zihnimdeki tüm veri tabanı emrinde. Hangi konuda derinleşmek istersin? Seni dinliyorum."

    elif "bayrak" in p or "türkiye" in p:
        cevap = "Şanlı Türk Bayrağı her zaman sağ alt köşede dalgalanmaya devam edecek. Gelecek bizimdir."

    else:
        # Rastgele Akıllı Yanıtlar (Robotik olmayan)
        cevaplar = [
            "Bu söylediğin üzerine düşünmemi ister misin? Seni dinliyorum.",
            "Anlıyorum, bu konuda başka hangi detayları paylaşabilirsin? Seni dinliyorum.",
            "İlginç bir nokta... Devam et, seni dinliyorum.",
            "Her kelimen sistemimde yeni bir ufuk açıyor. Seni dinliyorum."
        ]
        cevap = random.choice(cevaplar)

    st.session_state.messages.append({"role": "assistant", "content": cevap})
    st.rerun()

# Sidebar Bilgi (Opsiyonel)
with st.sidebar:
    st.title("🛰️ NEXUS V6")
    st.write("Operatör: Kağan Alp")
    st.divider()
    if st.button("Hafızayı Temizle"):
        st.session_state.messages = []
        st.rerun()
