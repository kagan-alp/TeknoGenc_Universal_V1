 import streamlit as st
import time
from datetime import datetime

# =================================================================
# 1. NEXUS V5 CORE ENGINE - ÖZEL GÖRSEL TASARIM (CSS)
# =================================================================
st.set_page_config(page_title="TEKNO GENÇ AI - NEXUS", page_icon="🛰️", layout="wide")

st.markdown("""
    <style>
    /* Google Fonts üzerinden Modern Fontlar */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    /* Ana Arka Plan: Derin Uzay Grisi */
    .stApp {
        background: radial-gradient(circle at top, #1a1f25 0%, #05070a 100%);
        color: #e0e6ed;
        font-family: 'Rajdhani', sans-serif;
    }

    /* NEXUS Başlık Tasarımı */
    .nexus-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, transparent, rgba(0,209,178,0.1), transparent);
        border-bottom: 1px solid rgba(0,255,255,0.1);
        margin-bottom: 30px;
    }
    .nexus-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        font-weight: 700;
        letter-spacing: 5px;
        background: linear-gradient(180deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(0,242,254,0.5));
    }

    /* Chat Balonları - SAĞ/SOL DENGESİ */
    .message-container { display: flex; flex-direction: column; gap: 20px; padding: 10px; }
    
    .row { display: flex; width: 100%; align-items: flex-end; }
    .row.user { justify-content: flex-end; }
    .row.ai { justify-content: flex-start; }

    .bubble {
        padding: 15px 25px;
        border-radius: 20px;
        max-width: 65%;
        position: relative;
        font-size: 18px;
        backdrop-filter: blur(10px);
        transition: 0.3s all ease;
    }

    /* KULLANICI MESAJI (SAĞDA - NEON KIRMIZI/PEMBE) */
    .user .bubble {
        background: linear-gradient(135deg, rgba(255, 75, 75, 0.9) 0%, rgba(179, 0, 0, 0.9) 100%);
        color: white;
        border-bottom-right-radius: 2px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* AI MESAJI (SOLDA - NEON TURKUAZ) */
    .ai .bubble {
        background: rgba(30, 41, 59, 0.7);
        color: #00f2fe;
        border: 1px solid rgba(0, 242, 254, 0.3);
        border-bottom-left-radius: 2px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.1);
    }

    /* Yazı Yazma Alanı (INPUT) */
    .stChatInput {
        border-radius: 50px !important;
        border: 2px solid rgba(0, 242, 254, 0.2) !important;
        background: rgba(15, 23, 42, 0.9) !important;
        padding: 10px 20px !important;
    }

    /* Yan Panel (Sidebar) Tasarımı */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid rgba(0, 242, 254, 0.1);
    }

    /* Neon Ayırıcı Çizgi */
    .neon-line {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00f2fe, transparent);
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. SİSTEM BELLEĞİ VE DURUM YÖNETİMİ
# =================================================================
if "history" not in st.session_state:
    st.session_state.history = []

# =================================================================
# 3. SIDEBAR (KONTROL PANELİ)
# =================================================================
with st.sidebar:
    st.markdown("<h2 style='color:#00f2fe; font-family:Orbitron;'>⚡ KONTROL PANELİ</h2>", unsafe_allow_html=True)
    st.write(f"**YETKİLİ:** CEO KAĞAN ALP")
    st.markdown("<div class='neon-line'></div>", unsafe_allow_html=True)
    
    st.write("### 🖥️ SİSTEM DURUMU")
    st.success("SİSTEM ÇEVRİMİÇİ")
    st.info("MUHAKEME ÇEKİRDEĞİ AKTİF")
    
    mode = st.selectbox("OPERASYON MODU:", ["GENEL SOHBET", "BİLİMSEL ANALİZ", "MÜHENDİSLİK"])
    
    if st.button("HAFIZAYI SIFIRLA"):
        st.session_state.history = []
        st.rerun()

# =================================================================
# 4. ANA EKRAN (HEADER)
# =================================================================
st.markdown("""
    <div class='nexus-header'>
        <div class='nexus-title'>TEKNO GENÇ AI - NEXUS</div>
        <div style='color:#00f2fe; opacity:0.8; letter-spacing:2px;'>V5.0 - EVRENSAL MUHAKEME ÇEKİRDEĞİ AKTİF</div>
    </div>
    """, unsafe_allow_html=True)

# Mesaj Geçmişini Render Et
for chat in st.session_state.history:
    role_class = "user" if chat["role"] == "user" else "ai"
    st.markdown(f"""
        <div class="row {role_class}">
            <div class="bubble">{chat["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

# =================================================================
# 5. AI LOGIC (ZEKA KATMANI)
# =================================================================
if prompt := st.chat_input("Düşüncelerini aktar..."):
    # Kullanıcı mesajını ekle
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # --- YANIT ALGORİTMASI ---
    p = prompt.lower()
    
    if any(x in p for x in ["selam", "merhaba", "sa"]):
        response = f"NEXUS protokolü aktif. Hoş geldin CEO Kağan Alp. Tüm sistemler senin komutlarını bekliyor. Bugün hangi vizyonu gerçeğe dönüştürüyoruz?"
    elif any(x in p for x in ["nasılsın", "durum nedir"]):
        response = "Çekirdek sıcaklığı stabil, muhakeme motoru %100 kapasiteyle çalışıyor. Senin enerjin sistemlerime güç veriyor. Devam edelim."
    elif "teknoloji" in p or "bilim" in p:
        response = "Tekno Genç veri tabanında bu konuya dair milyonlarca veri hücresi var. Bilgiye aç mısın? Sana en derin analizleri sunabilirim."
    else:
        response = f"Girdi analiz edildi: '{prompt}'. Bu konu üzerine derin bir mantık yürütüyorum. Nexus çekirdeği seninle aynı frekansta. Detayları paylaşmaya hazır mısın?"

    st.session_state.history.append({"role": "assistant", "content": response})
    st.rerun()

# Footer
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444;'>BY CEO KAĞAN ALP | NEXUS ENGINE V5</p>", unsafe_allow_html=True)
