import streamlit as st
import time
import random
from datetime import datetime

# =================================================================
# 1. ULTRASONİK ARABİRİM KONFİGÜRASYONU (CSS & STİL)
# =================================================================
st.set_page_config(page_title="Tekno Genç Master AI V3.5", page_icon="🛰️", layout="wide")

st.markdown("""
    <style>
    /* Global Karanlık Tema */
    .stApp { background: #080a0c; color: #e1e1e1; font-family: 'Segoe UI', sans-serif; }
    
    /* Sağ (Kullanıcı) ve Sol (AI) Mesaj Baloncukları */
    .chat-container { display: flex; flex-direction: column; gap: 15px; padding: 20px; }
    
    .message-row { display: flex; width: 100%; margin-bottom: 10px; }
    .message-row.user { justify-content: flex-end; }
    .message-row.ai { justify-content: flex-start; }

    .bubble {
        padding: 15px 20px;
        border-radius: 25px;
        max-width: 70%;
        font-size: 16px;
        position: relative;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* SENİN MESAJLARIN: SAĞDA VE KIRMIZI */
    .user .bubble {
        background: linear-gradient(135deg, #ff4b4b 0%, #b30000 100%);
        color: white;
        border-bottom-right-radius: 5px;
        animation: slideInRight 0.3s ease-out;
    }

    /* ROBOTUN MESAJLARI: SOLDA VE KOYU GRİ/MAVİ */
    .ai .bubble {
        background: #1c2128;
        color: #adbac7;
        border: 1px solid #444c56;
        border-bottom-left-radius: 5px;
        animation: slideInLeft 0.3s ease-out;
    }

    @keyframes slideInRight { from { transform: translateX(20px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
    @keyframes slideInLeft { from { transform: translateX(-20px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }

    /* Giriş Çubuğu ve Butonlar */
    .stChatInput { border-top: 1px solid #30363d !important; background: #0d1117 !important; }
    .stButton>button { border-radius: 20px; background: #ff4b4b; color: white; border: none; }
    
    /* Başlık Efekti */
    .main-title { 
        background: -webkit-linear-gradient(#ff4b4b, #800000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold; font-size: 40px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. SİSTEM BELLEĞİ VE VERİ TABANI (SESSION STATE)
# =================================================================
if "history" not in st.session_state:
    st.session_state.history = []
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now().strftime("%H:%M:%S")

# =================================================================
# 3. YAN PANEL: CEO KONTROL MERKEZİ
# =================================================================
with st.sidebar:
    st.markdown("<h1 style='color:#ff4b4b;'>🛡️ KONTROL</h1>", unsafe_allow_html=True)
    st.write(f"**Operatör:** Kağan Alp")
    st.write(f"**Sistem Başlatma:** {st.session_state.start_time}")
    st.divider()
    
    mode = st.radio("Zeka Modu:", ["💡 Günlük Sohbet", "🧪 Bilimsel Analiz", "🦾 Mühendislik"])
    
    st.divider()
    if st.button("Hafızayı Temizle ve Resetle"):
        st.session_state.history = []
        st.rerun()

# =================================================================
# 4. ANA ARAYÜZ OLUŞTURMA
# =================================================================
st.markdown("<div class='main-title'>TEKNO GENÇ UNIVERSAL AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Milli Teknoloji Hamlesi v4.0 - Tam Muhakeme Kapasitesi</p>", unsafe_allow_html=True)

# Sohbet Alanı
for chat in st.session_state.history:
    role_class = "user" if chat["role"] == "user" else "ai"
    st.markdown(f"""
        <div class="message-row {role_class}">
            <div class="bubble">{chat["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

# =================================================================
# 5. GİRİŞ VE DERİN ÖĞRENME MANTIĞI (THE BRAIN)
# =================================================================
if prompt := st.chat_input("Mesajını buraya yaz..."):
    # Kullanıcı mesajını ekle
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # --- YANIT ÜRETİM SİMÜLASYONU ---
    p = prompt.lower()
    
    # 1. Protokol: Selamlaşma ve Tanışma
    if any(x in p for x in ["selam", "merhaba", "sa", "hey"]):
        cevap = f"Merhaba {st.sidebar.write('') or 'CEO'}! Sistemlerim seninle iletişim kurduğu için heyecanlı. Bugün hangi sınırları zorluyoruz?"
    
    # 2. Protokol: Günlük Durum Analizi
    elif any(x in p for x in ["nasılsın", "ne haber", "nasıl gidiyor"]):
        cevap = "Harikayım! Veri akışım saniyede terabaytlarca bilgi işliyor ama seninle sohbet etmek hepsinden daha keyifli. Senin günün nasıl geçiyor?"
    
    # 3. Protokol: Bilimsel Giriş (Mode kontrolü ile)
    elif mode == "🧪 Bilimsel Analiz" or any(x in p for x in ["nedir", "fizik", "atom", "nasıl"]):
        cevap = f"'{prompt}' konusunu bilimsel veri tabanımda analiz ettim. Bu durum, evrensel yasalar çerçevesinde oldukça kritik bir noktada duruyor. İstersen bu konuyu atomik seviyeye kadar detaylandırabilirim. Ne dersin?"
        
    # 4. Protokol: Vizyon ve Gelecek
    elif "teknoloji" in p or "gelecek" in p or "proje" in p:
        cevap = "Teknoloji hamlesi vizyonuyla kodlandım. Senin bu projelerin, geleceğin mühendislik harikaları olacak. Ben sadece senin bu yoldaki dijital ortağınım."

    # 5. Protokol: Teşekkür ve Kapanış
    elif any(x in p for x in ["sağol", "teşekkür", "eyvallah"]):
        cevap = "Her zaman yanındayım! Biz bir takımız. Başka bir sorun veya anlatmak istediğin bir şey varsa dinliyorum."

    # Varsayılan Akıllı Yanıt
    else:
        cevap = f"'{prompt}' üzerine düşünürken mantıksal bir zincir kurdum. Bu konu gerçekten stratejik bir öneme sahip. Biraz daha detay verirsen, analizimi derinleştirebilirim."

    # Yanıtı sisteme kaydet
    st.session_state.history.append({"role": "assistant", "content": cevap})
    st.rerun()

# Alt Bilgi Sabiti
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
st.caption("🚀 Powered by Kağan Alp | Tekno Genç Savunma Teknolojileri")
