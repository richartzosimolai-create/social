import streamlit as st
import requests

produk = [
    {"id": 1, "nama": "👕 Kaos Polos Premium", "harga": 75000},
    {"id": 2, "nama": "🧥 Jaket Hoodie", "harga": 150000},
    {"id": 3, "nama": "👖 Celana Chino", "harga": 120000},
    {"id": 4, "nama": "👟 Sepatu Sneakers", "harga": 250000},
    {"id": 5, "nama": "🎒 Tas Ransel", "harga": 180000},
    {"id": 6, "nama": "⌚ Jam Tangan Sport", "harga": 200000},
]

# token sm chat id
TOKEN = "8624888114:AAFEo-HDSx01ZAT4kFD7JzL-R49_slYh8m4"
CHAT_ID = "8920670099"  

st.set_page_config(page_title="social 9D", page_icon="🛍️", layout="wide")

st.markdown("""
<style>
    /* HEADER */
    .header {
        background: white;
        padding: 20px 30px;
        border-radius: 16px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }
    .header h1 {
        font-size: 28px;
        color: #1a1a1a;
    }
    .header h1 span {
        color: #ee4d2d;
    }
    .header .badge {
        background: #ee4d2d;
        color: white;
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 14px;
        font-weight: 600;
    }
    
    /* CARD */
    .product-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    .product-card .gambar {
        font-size: 60px;
        margin-bottom: 10px;
    }
    .product-card .harga {
        font-size: 24px;
        font-weight: 700;
        color: #ee4d2d;
    }
    
    /* TOMBOL */
    .stButton > button {
        background: #ee4d2d !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    .stButton > button:hover {
        background: #d43b1f !important;
    }
    
    /* FOOTER */
    .footer {
        text-align: center;
        padding: 30px 0 10px;
        color: #999;
        font-size: 14px;
        margin-top: 30px;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# ===== TAMPILAN HEADER =====
st.markdown("""
<div class="header">
    <h1>🛍️ <span>Toko</span> Saya</h1>
    <div class="badge">6 Produk</div>
</div>
""", unsafe_allow_html=True)

# tampilin prduk
cols = st.columns(3)

for i, p in enumerate(produk):
    with cols[i % 3]:
        emoji = ["👕", "🧥", "👖", "👟", "🎒", "⌚"][i]
        
        st.markdown(f"""
        <div class="product-card">
            <div class="gambar">{emoji}</div>
            <h3>{p['nama']}</h3>
            <p class="harga">Rp{p['harga']:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        
        with st.form(key=f"form_{p['id']}"):
            nama = st.text_input("Nama kamu", key=f"nama_{p['id']}", placeholder="Masukkan nama")
            jumlah = st.number_input("Jumlah", min_value=1, max_value=10, value=1, key=f"jml_{p['id']}")
            submit = st.form_submit_button("🛒 Beli Sekarang")
            
            if submit:
                if not nama:
                    st.error("❌ Nama harus diisi!")
                else:
                    total = p['harga'] * jumlah
                    
                    pesan = f"🛍️ ORDER BARU!\n👤 Nama: {nama}\n📦 Produk: {p['nama']}\n💰 Harga: Rp{p['harga']:,}\n🔢 Jumlah: {jumlah}\n💳 Total: Rp{total:,}"
                    
                    try:
                        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                        r = requests.post(url, data={"chat_id": CHAT_ID, "text": pesan}, timeout=10)
                        
                        if r.status_code == 200:
                            st.success(f"✅ Terima kasih {nama}! Order berhasil!")
                            st.balloons()
                        else:
                            st.error("❌ Gagal kirim notif!")
                    except:
                        st.error("❌ Error koneksi!")

# ===== FOOTER =====
st.markdown("""
<div class="footer">
    © 2026 Toko Saya - Tugas Sekolah
</div>
""", unsafe_allow_html=True)
