import streamlit as st
import requests

# ===== SETTING HALAMAN =====
st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide")

# ===== INISIALISASI KERANJANG =====
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

# ===== DATA PRODUK =====
produk = [
    {"id": 1, "nama": "Kaos Polos Premium", "harga": 75000},
    {"id": 2, "nama": "Jaket Hoodie", "harga": 150000},
    {"id": 3, "nama": "Celana Chino", "harga": 120000},
    {"id": 4, "nama": "Sepatu Sneakers", "harga": 250000},
    {"id": 5, "nama": "Tas Ransel", "harga": 180000},
    {"id": 6, "nama": "Jam Tangan Sport", "harga": 200000},
]

# token sm chat id
TOKEN = "8624888114:AAFEo-HDSx01ZAT4kFD7JzL-R49_slYh8m4"
CHAT_ID = "8920670099"  


st.markdown("""
<style>
    /* HEADER */
    .header {
        background: white;
        padding: 15px 25px;
        border-radius: 16px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .header h1 {
        font-size: 24px;
        color: #1a1a1a;
        margin: 0;
    }
    .header h1 span {
        color: #ee4d2d;
    }
    .header .badge {
        background: #ee4d2d;
        color: white;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 600;
    }
    
    /* CARD PRODUK */
    .product-card {
        background: white;
        border-radius: 16px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
        border: 1px solid #f0f0f0;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    .product-card .gambar {
        font-size: 50px;
        margin-bottom: 8px;
    }
    .product-card h3 {
        font-size: 16px;
        margin: 5px 0;
        color: #1a1a1a;
    }
    .product-card .harga {
        font-size: 20px;
        font-weight: 700;
        color: #ee4d2d;
        margin-bottom: 10px;
    }
    
    /* TOMBOL TAMBAH KERANJANG */
    .stButton > button {
        background: #ee4d2d !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 8px !important;
        font-size: 14px !important;
    }
    .stButton > button:hover {
        background: #d43b1f !important;
    }
    
    /* BADGE KERANJANG */
    .cart-badge {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 999;
        background: #ee4d2d;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 25px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(238, 77, 45, 0.4);
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.3s;
    }
    .cart-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 30px rgba(238, 77, 45, 0.6);
    }
    .cart-badge .count {
        background: white;
        color: #ee4d2d;
        border-radius: 50%;
        padding: 2px 10px;
        font-size: 14px;
        font-weight: 700;
    }
    
    /* SIDEBAR KERANJANG */
    .cart-sidebar {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0,0,0,0.15);
        margin-top: 20px;
        border: 1px solid #eee;
    }
    .cart-sidebar .cart-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .cart-sidebar .cart-item:last-child {
        border-bottom: none;
    }
    .cart-sidebar .total {
        font-size: 20px;
        font-weight: 700;
        color: #ee4d2d;
        text-align: right;
        padding-top: 15px;
        border-top: 2px solid #eee;
        margin-top: 10px;
    }
    
    /* FOOTER */
    .footer {
        text-align: center;
        padding: 20px 0 10px;
        color: #999;
        font-size: 13px;
        margin-top: 30px;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    <div class="header" style="margin-bottom:0; box-shadow:none; background:transparent; padding:0;">
        <h1>🛍️ <span>Toko</span> Saya</h1>
    </div>
    """, unsafe_allow_html=True)

# ===== TAMPILAN PRODUK =====
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
        
        # Tombol Tambah ke Keranjang
        if st.button(f"🛒 Tambahkan ke Keranjang", key=f"add_{p['id']}"):
            st.session_state.keranjang.append(p)
            st.session_state.show_cart = True
            st.rerun()

# ===== BADGE KERANJANG (di kanan bawah) =====
total_item = len(st.session_state.keranjang)
total_harga = sum(item['harga'] for item in st.session_state.keranjang)

# Tombol floating keranjang
cart_html = f"""
<div class="cart-badge" onclick="document.querySelector('[data-testid=\"stSidebar\"]').click()">
    🛒 Keranjang
    <span class="count">{total_item}</span>
</div>
"""
st.markdown(cart_html, unsafe_allow_html=True)

# ===== SIDEBAR KERANJANG =====
with st.sidebar:
    st.markdown("## 🛒 Keranjang Belanja")
    st.markdown("---")
    
    if len(st.session_state.keranjang) == 0:
        st.info("🛍️ Keranjang masih kosong")
    else:
        # Tampilkan isi keranjang
        for idx, item in enumerate(st.session_state.keranjang):
            col1, col2, col3 = st.columns([2, 1, 0.5])
            with col1:
                st.write(f"**{item['nama']}**")
            with col2:
                st.write(f"Rp{item['harga']:,}")
            with col3:
                if st.button("✕", key=f"del_{idx}"):
                    st.session_state.keranjang.pop(idx)
                    st.rerun()
        
        st.markdown("---")
        st.markdown(f"### 💰 Total: **Rp{total_harga:,}**")
        st.markdown("---")
        
        # ===== FORM PEMBAYARAN =====
        with st.form("form_pesan"):
            st.markdown("### 📝 Data Pemesan")
            nama_pemesan = st.text_input("Nama Lengkap", placeholder="Masukkan nama kamu")
            kelas = st.text_input("Kelas", placeholder="Contoh: 10 IPA 1")
            no_hp = st.text_input("No. HP (WA)", placeholder="Contoh: 08123456789")
            
            submit = st.form_submit_button("✅ Kirim Pesanan", use_container_width=True)
            
            if submit:
                if not nama_pemesan or not kelas or not no_hp:
                    st.error("❌ Semua data harus diisi!")
                elif len(st.session_state.keranjang) == 0:
                    st.error("❌ Keranjang masih kosong!")
                else:
                    # Buat pesanan
                    detail_order = "\n".join([f"- {item['nama']} (Rp{item['harga']:,})" for item in st.session_state.keranjang])
                    pesan = f"""
🛍️ *PESANAN BARU!*
━━━━━━━━━━━━━━━━
👤 Nama: {nama_pemesan}
🏫 Kelas: {kelas}
📱 No. HP: {no_hp}
━━━━━━━━━━━━━━━━
📦 *Detail Pesanan:*
{detail_order}
━━━━━━━━━━━━━━━━
💰 *Total: Rp{total_harga:,}*
━━━━━━━━━━━━━━━━
                    """
                    
                    # Kirim ke Telegram
                    try:
                        url_tele = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                        r = requests.post(url_tele, data={"chat_id": CHAT_ID, "text": pesan}, timeout=10)
                        
                        # Kirim ke WhatsApp (via link)
                        wa_link = f"https://api.whatsapp.com/send?phone={no_hp}&text=Halo%20{nama_pemesan}%2C%20pesanan%20Anda%20sedang%20kami%20proses.%20Total%20Rp{total_harga%3A%2C}"
                        
                        if r.status_code == 200:
                            st.success(f"✅ Pesanan berhasil dikirim!")
                            st.balloons()
                            st.markdown(f"📱 [Klik di sini untuk chat via WhatsApp]({wa_link})")
                            
                            # Kosongkan keranjang
                            st.session_state.keranjang = []
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

# ===== SCRIPT UNTUK FLOATING BUTTON =====
st.markdown("""
<script>
    // Klik otomatis tombol keranjang di sidebar
    document.querySelector('.cart-badge')?.addEventListener('click', function() {
        // Cari tombol sidebar di Streamlit
        const sidebarBtn = document.querySelector('[data-testid="stSidebar"] button');
        if (sidebarBtn) sidebarBtn.click();
    });
</script>
""", unsafe_allow_html=True)
