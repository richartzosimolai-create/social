import streamlit as st
import requests

#Produk
produk = [
    {"id": 1, "nama": "👕 Kaos Polos Premium", "harga": 75000},
    {"id": 2, "nama": "🧥 Jaket Hoodie", "harga": 150000},
    {"id": 3, "nama": "👖 Celana Chino", "harga": 120000},
    {"id": 4, "nama": "👟 Sepatu Sneakers", "harga": 250000},
    {"id": 5, "nama": "🎒 Tas Ransel", "harga": 180000},
    {"id": 6, "nama": "⌚ Jam Tangan Sport", "harga": 200000},
]

# Token sm chat id
TOKEN = "8624888114:AAFEo-HDSx01ZAT4kFD7JzL-R49_slYh8m4"
CHAT_ID = "8920670099"

# ========== JUDUL ==========
st.set_page_config(page_title="Toko Saya", page_icon="🛍️")
st.title("🛍️ Toko Saya")
st.markdown("---")

# ========== TAMPILAN PRODUK (GRID 3 KOLOM) ==========
cols = st.columns(3)

for i, p in enumerate(produk):
    with cols[i % 3]:
        st.subheader(p["nama"])
        st.write(f"💰 **Rp{p['harga']:,}**")
        
        # Form beli per produk
        with st.form(key=f"form_{p['id']}"):
            nama = st.text_input("Nama kamu", key=f"nama_{p['id']}")
            jumlah = st.number_input("Jumlah", min_value=1, max_value=10, value=1, key=f"jml_{p['id']}")
            submit = st.form_submit_button("✅ Beli Sekarang")
            
            if submit:
                if not nama:
                    st.error("Nama harus diisi!")
                else:
                    total = p['harga'] * jumlah
                    
                    # Kirim notif Telegram
                    pesan = f"""
🛍️ ORDER BARU!
━━━━━━━━━━━━━━━━
👤 Nama: {nama}
📦 Produk: {p['nama']}
💰 Harga: Rp{p['harga']:,}
🔢 Jumlah: {jumlah}
💳 Total: Rp{total:,}
━━━━━━━━━━━━━━━━
                    """
                    
                    try:
                        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                        data = {"chat_id": CHAT_ID, "text": pesan}
                        r = requests.post(url, data=data, timeout=10)
                        
                        if r.status_code == 200:
                            st.success(f"✅ Terima kasih {nama}! Order berhasil!")
                            st.balloons()
                        else:
                            st.error("❌ Gagal kirim notif. Coba lagi!")
                    except:
                        st.error("❌ Error koneksi. Coba lagi!")
        
        st.markdown("---")
