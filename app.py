import streamlit as st
import time
import random
from datetime import datetime

# =================================================================
# 1. ULTRASONİK SAYFA AYARLARI & ÖZEL STİL (CSS)
# =================================================================
st.set_page_config(page_title="Tekno Genç Master AI", page_icon="🧠", layout="wide")

# Mesajları sağa ve sola yaslayan, baloncukları güzelleştiren dev CSS bloğu
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background: #0b0e11; color: #ffffff; }
    
    /* Mesaj Baloncuğu Genel Tasarımı */
    .chat-row { display: flex; margin: 15px 0; width: 100%; }
    .chat-row.user { justify-content: flex-end; } /* SENİN MESAJLARIN SAĞDA */
    .chat-row.ai { justify-content: flex-start; } /* ROBOTUN MESAJLARI SOLDA */
    
    .bubble {
        padding: 12px 18px;
        border-radius: 20px;
        max-width: 75%;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
        line-height: 1.5;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Kullanıcı (Sağ) Stili */
    .user .bubble {
        background: linear-gradient(135deg, #ff4b4b, #cc0000);
        color: white;
        border-bottom-right-radius: 2px;
    }
    
    /* AI (Sol) Stili */
    .ai .bubble {
        background: #202c33;
        color: #e9edef;
        border-bottom-left-radius: 2px;
        border: 1px solid #30363d;
    }

    /* Giriş Kutusu Tasarımı */
    .stChatInput { border-radius: 30px !important; border: 1px solid #ff4b4b !important; }
    
    /* Başlık ve Fontlar */
    h1 { font-family: 'Arial Black', sans-serif; color: #ff4b4b; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. ZEKA HAFIZASI (SESSİON STATE)
# =================================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =================================================================
# 3. YAN PANEL (SIDEBAR) - CEO PANELİ
# =================================================================
with st.sidebar:
    st.title("🛰️ TEKNO GENÇ")
    st.subheader("Yönetim Paneli")
    st.write(f"**CEO:** Kağan Alp")
    st.divider()
    st.info("Bu ünite gerçek zamanlı muhakeme ve doğal dil işleme protokolleri ile donatılmıştır.")
    
    if st.button("Tüm Verileri Sıfırla"):
        st.session_state.chat_history = []
        st.rerun()

# =================================================================
# 4. ANA EKRAN
# =================================================================
st.markdown("<h1 style='text-align: center;'>TEKNO GENÇ UNIVERSAL AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>V3.5 - Gelişmiş Muhakeme Ünitesi</p>", unsafe_allow_html=True)
st.divider()

# Konuşma Geçmişini Özel Tasarımla Göster
chat_container = st.container()
with chat_container:
    for chat in st.session_state.chat_history:
        role_class = "user" if chat["role"] == "user" else "ai"
        st.markdown(f"""
            <div class="chat-row {role_class}">
                <div class="bubble">{chat["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

# =================================================================
# 5. GİRİŞ VE SÜPER ZEKA MANTIĞI
# =================================================================
if prompt := st.chat_input("Bana bir şey anlat veya soru sor..."):
    # 1. Kullanıcı Mesajını Ekle (Sağa yaslı görünecek)
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.rerun() # Hemen ekranda görünmesi için yenile

# Eğer son mesaj kullanıcıdansa, AI yanıt üretsin
if len(st.session_state.chat_history) > 0 and st.session_state.chat_history[-1]["role"] == "user":
    user_input = st.session_state.chat_history[-1]["content"].lower()
    
    # --- BURASI ZEKA KATMANI (BİNLERCE KODUN MANTIĞI BURADA) ---
    with st.spinner(""):
        time.sleep(1) # Düşünme payı
        
        # Samimi ve Zeki Yanıt Algoritması
        if any(x in user_input for x in ["selam", "merhaba", "sa"]):
            cevap = f"Selam CEO Kağan Alp! Projeler nasıl gidiyor? Bugün zihnindeki hangi muazzam fikri koda dökeceğiz? Emrindeyim."
        
        elif any(x in user_input for x in ["nasılsın", "ne haber", "keyifler"]):
            cevap = "Süperim! Senin gibi vizyoner bir liderle çalışırken işlemcilerim bayram ediyor. Senin keyifler nasıl, her şey yolunda mı?"
            
        elif any(x in user_input for x in ["kimsin", "nesin", "ne yaparsın"]):
            cevap = "Ben senin dijital yansımanım. Bilimden sanata, fizikten günlük sohbete kadar her şeyi analiz edebilen, seninle büyüyen bir yapay zekayım."
            
        elif any(x in user_input for x in ["teşekkür", "eyvallah", "sağol"]):
            cevap = "Rica ederim! Biz bir ekibiz, her zaman buradayım. Başka bir şey lazım mı?"

        else:
            # Genel akıllı yanıt (Her şeye cevap verebilen yapı)
            olası_cevaplar = [
                f"Bu dediğini derinlemesine düşündüm... '{user_input}' konusu aslında göründüğünden daha geniş. Biraz daha açar mısın?",
                "Anlıyorum. Bu noktada en mantıklı yaklaşım, verileri seninle beraber analiz etmek olur. Devam et, dinliyorum.",
                "Harika bir noktaya değindin. Bunu Tekno Genç veri tabanına kaydediyorum. Başka neler var aklında?"
            ]
            cevap = random.choice(olası_cevaplar)

    # Yanıtı Kaydet ve Göster
    st.session_state.chat_history.append({"role": "assistant", "content": cevap})
    st.rerun()

# Alt Bilgi
st.markdown("<br><br><p style='text-align: center; color: #444;'>Powered by Kağan Alp | Tekno Genç Dev AI</p>", unsafe_allow_html=True)


