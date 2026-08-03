import streamlit as st
import requests

st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide")

# fonte wa
FONNTE_API = "AHUP2hyJ32GrzWzBfmxa"  
NO_HP_KAMU = "81180895229"      

def kirim_wa(pesan):
    url = "https://api.fonnte.com/send"
    data = {
        "target": NO_HP_KAMU,
        "message": pesan,
        "countryCode": "62",
    }
    headers = {"Authorization": FONNTE_API}
    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        return response.status_code == 200
    except:
        return False

if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

# formny
if "nama_pemesan" not in st.session_state:
    st.session_state.nama_pemesan = ""
if "kelas" not in st.session_state:
    st.session_state.kelas = ""
if "no_hp" not in st.session_state:
    st.session_state.no_hp = ""

produk = [
    {"id": 1, "nama": "Dubai Chewy cookie strawberry", "harga": 67, "gambar": "https://i.ibb.co.com/xSTTgJ1K/dubai.jpg"},
    {"id": 2, "nama": "Chilis", "harga": 67, "gambar": "https://i.ibb.co.com/GvvnbcHn/Whats-App-Image-2026-08-02-at-19-03-45.jpg"},
    {"id": 3, "nama": "Samyang roll moza", "harga": 67, "gambar": "https://i.ibb.co.com/TBKfvx1G/Whats-App-Image-2026-08-02-at-19-03-45-1.jpg"},
    {"id": 4, "nama": "Scoopable cookies", "harga": 67, "gambar": "https://i.ibb.co.com/BVBH8p65/Whats-App-Image-2026-08-02-at-19-03-46.jpg"},
    {"id": 5, "nama": "67", "harga": 67, "gambar": ""},
    {"id": 6, "nama": "67", "harga": 67, "gambar": ""},
]

st.markdown("""
<style>
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

st.markdown("""
<div class="header">
    <h1>🛍️ <span>Social 9D</span> </h1>
    <div class="badge">6 Produk</div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)

for i, p in enumerate(produk):
    with cols[i % 3]:
        
        if "gambar" in p and p["gambar"]:
            st.markdown(f"""
            <div style="width:100%; aspect-ratio:1/1; overflow:hidden; border-radius:12px; background:#f5f5f5; border:1px solid #eee;">
                <img src="{p['gambar']}" style="width:100%; height:100%; object-fit:cover;">
            </div>
            """, unsafe_allow_html=True)
        else:
            emoji = ["1", "2", "3", "4", "5", "6"][i]
            st.markdown(f'<div class="gambar">{emoji}</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="product-card">
            <h3>{p['nama']}</h3>
            <p class="harga">Rp{p['harga']:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🛒 Tambahkan ke Keranjang", key=f"add_{p['id']}"):
            st.session_state.keranjang.append(p)
            st.session_state.show_cart = True
            st.rerun()

total_item = len(st.session_state.keranjang)
total_harga = sum(item['harga'] for item in st.session_state.keranjang)

st.markdown(f"""
<div class="cart-badge">
    🛒 Keranjang
    <span class="count">{total_item}</span>
</div>
<div style="position:fixed; bottom:80px; right:30px; z-index:999; background:white; color:#666; padding:4px 12px; border-radius:20px; font-size:11px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
    👆 klik untuk mengecek keranjang
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🛒 Keranjang Belanja")
    st.markdown("---")
    
    if len(st.session_state.keranjang) == 0:
        st.info("🛍️ Keranjang masih kosong")
    else:
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
        
        with st.form("form_pesan"):
            st.markdown("### 📝 Data Pemesan")
            
            nama_pemesan = st.text_input(
                "Nama Lengkap", 
                value=st.session_state.nama_pemesan,
                placeholder="Masukkan nama kamu",
                key="input_nama"
            )
            kelas = st.text_input(
                "Kelas", 
                value=st.session_state.kelas,
                placeholder="Contoh: 10 IPA 1",
                key="input_kelas"
            )
            no_hp = st.text_input(
                "No. HP (WA)", 
                value=st.session_state.no_hp,
                placeholder="Contoh: 08123456789",
                key="input_nohp"
            )
            
            submit = st.form_submit_button("✅ Kirim Pesanan", use_container_width=True)
            
            if submit:
                if not nama_pemesan or not kelas or not no_hp:
                    st.error("❌ Semua data harus diisi!")
                elif len(st.session_state.keranjang) == 0:
                    st.error("❌ Keranjang masih kosong!")
                else:
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
                    
                    try:
                        kirim_wa(pesan)
                        
                        wa_text = f"Halo {nama_pemesan}, pesanan Anda sedang kami proses. Total Rp{total_harga:,}"
                        wa_link = f"https://api.whatsapp.com/send?phone={no_hp}&text={wa_text.replace(' ', '%20')}"
                        
                        st.success(f"✅ Pesanan berhasil dikirim!")
                        st.balloons()
                        st.markdown(f"📱 [Klik di sini untuk chat via WhatsApp]({wa_link})")
                        
                        st.session_state.keranjang = []
                        st.session_state.nama_pemesan = ""
                        st.session_state.kelas = ""
                        st.session_state.no_hp = ""
                        
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error: {e}")

st.markdown("""
<div class="footer">
    Social 9D
</div>
""", unsafe_allow_html=True)
