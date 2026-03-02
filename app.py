import streamlit as st
import time
import random
from datetime import datetime

# =================================================================
# 1. ÇEKİRDEK YAPILANDIRMA VE TASARIM
# =================================================================
st.set_page_config(page_title="Tekno Genç Master AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400&display=swap');
    
    .stApp { background: #05070a; color: #e0e0e0; font-family: 'Roboto', sans-serif; }
    .chat-bubble { border-radius: 20px; padding: 15px; margin: 10px 0; border: 1px solid #1f2937; line-height: 1.6; }
    .user-bubble { background: #111827; border-left: 5px solid #ff4b4b; }
    .ai-bubble { background: #1f2937; border-left: 5px solid #00d1b2; }
    .stChatInput { background-color: #111827 !important; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 2px; }
    .stStatus { border: none; background: transparent; }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. GELİŞMİŞ HAFIZA VE VERİ TABANI SİSTEMİ
# =================================================================
if "memory" not in st.session_state:
    st.session_state.memory = []
if "persona" not in st.session_state:
    st.session_state.persona = {
        "user_name": "CEO Kağan Alp",
        "mood": "Profesyonel & Dostane",
        "version": "V3.0 Master"
    }

# =================================================================
# 3. YAN PANEL - SİSTEM MONİTÖRÜ
# =================================================================
with st.sidebar:
    st.markdown(f"## 🛠️ SİSTEM MERKEZİ\n**Yetkili:** {st.session_state.persona['user_name']}")
    st.divider()
    st.info("💡 **Bilgi:** Bu ünite, doğal dil işleme ve derin muhakeme protokolleri kullanarak yanıt üretir.")
    
    st.write("### 🧠 Bilişsel Ayarlar")
    creativity = st.slider("Yaratıcılık Filtresi", 0.0, 1.0, 0.7)
    focus_mode = st.toggle("Bilimsel Odaklanma", value=False)
    
    if st.button("Hafıza Hücrelerini Temizle"):
        st.session_state.memory = []
        st.rerun()
    
    st.divider()
    st.caption("🇹🇷 Milli Yazılım Hamlesi | Tekno Genç AI")

# =================================================================
# 4. ANA ARAYÜZ
# =================================================================
st.title("🛰️ TEKNO GENÇ UNIVERSAL")
st.write(f"*{datetime.now().strftime('%H:%M')} - Sistem Çevrimiçi*")

# Konuşma Geçmişini Göster
for msg in st.session_state.memory:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =================================================================
# 5. DERİN DÜŞÜNCE VE YANIT MOTORU
# =================================================================
if prompt := st.chat_input("Nelerden bahsedelim?"):
    # Kullanıcıyı kaydet
    st.session_state.memory.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Sessiz Analiz (Kullanıcıyı yormayan arka plan işlemi)
        with st.spinner(""): # Sadece küçük bir yükleme işareti, yazı yok.
            time.sleep(1.2) # Muhakeme süresi simülasyonu

        # YANIT MANTIĞI (Doğal ve Zeki)
        p = prompt.lower()
        
        # Merhaba/Selam Protokolü
        if any(word in p for word in ["selam", "merhaba", "mrb", "sa"]):
            cevaplar = [
                f"Merhaba {st.session_state.persona['user_name']}! Seni tekrar görmek harika. Bugün enerjimiz yüksek, projelerimiz büyük. Nereden başlıyoruz?",
                "Selamlar! Sistemlerim seninle sohbet etmeye hazır. Zihnindeki o parlak fikirlerden birini paylaşmak ister misin?",
                "Merhaba! Ben hazırım. Bilim, teknoloji ya da sadece hayat... Ne konuşmak istersen buradayım."
            ]
            response = random.choice(cevaplar)
        
        # Günlük Sohbet / Hal Hatır
        elif any(word in p for word in ["nasılsın", "ne haber", "nasıl gidiyor"]):
            response = "Harikayım! Kodlarım tıkır tıkır çalışıyor, veri tabanım güncel ve seninle sohbet etmek işlemci hızımı artırıyor. Sen nasılsın, her şey yolunda mı?"
            
        # Bilimsel/Teknik Odak (Toggle açıksa)
        elif focus_mode or any(word in p for word in ["nedir", "nasıl", "neden", "fizik", "atom"]):
            response = f"Analizlerim şunu gösteriyor: '{prompt}' konusu üzerinde çalışmak evrensel bir mantık gerektirir. Eğer istersen bu konunun derinlerine inebilir, atomik yapısından matematiksel formülüne kadar her şeyi masaya yatırabiliriz. Hangi detaydan başlayalım?"
        
        # Genel Yanıt (Her şey için)
        else:
            response = f"Dediğini anlıyorum. '{prompt}' üzerine biraz düşününce, aslında bunun çok boyutlu bir konu olduğunu görüyorum. Benimle bu konudaki fikrini biraz daha paylaşır mısın? Seni dinliyorum."

        # Yazma Simülasyonu
        placeholder = st.empty()
        full_res = ""
        for chunk in response.split():
            full_res += chunk + " "
            time.sleep(0.07)
            placeholder.markdown(full_res + "▌")
        placeholder.markdown(full_res)

    st.session_state.memory.append({"role": "assistant", "content": full_res})

# =================================================================
# 6. SİSTEM ALT BİLGİSİ
# =================================================================
st.markdown("---")
st.caption("🚀 Bu yapay zeka ünitesi Kağan Alp tarafından geliştirilen Tekno Genç Çekirdeği üzerinde çalışmaktadır.")

