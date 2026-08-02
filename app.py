import streamlit as st
import requests

st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide", initial_sidebar_state="collapsed")

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

if "nama_pemesan" not in st.session_state:
    st.session_state.nama_pemesan = ""
if "kelas" not in st.session_state:
    st.session_state.kelas = ""
if "no_hp" not in st.session_state:
    st.session_state.no_hp = ""

produk = [
    {"id": 1, "nama": "67", "harga": 67},
    {"id": 2, "nama": "67", "harga": 67},
    {"id": 3, "nama": "67", "harga": 67},
    {"id": 4, "nama": "67", "harga": 67},
    {"id": 5, "nama": "67", "harga": 67},
    {"id": 6, "nama": "67", "harga": 67},
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
        flex-wrap: wrap;
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

    /* Bikin grid produk tetap sejajar/konsisten di HP & laptop */
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        gap: 10px;
    }
    div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0 !important;
    }

    .product-card {
        background: white;
        border-radius: 16px;
        padding: 12px;
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
        font-size: 40px;
        margin-bottom: 8px;
    }
    .product-card h3 {
        font-size: 14px;
        margin: 5px 0;
        color: #1a1a1a;
    }
    .product-card .harga {
        font-size: 16px;
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
        font-size: 12px !important;
    }
    .stButton > button:hover {
        background: #d43b1f !important;
    }

    /* Card keranjang di halaman utama (bukan sidebar lagi) */
    .cart-box {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        padding: 20px 0 10px;
        color: #999;
        font-size: 13px;
        margin-top: 30px;
        border-top: 1px solid #eee;
    }

    /* Responsive tambahan khusus layar HP kecil */
    @media (max-width: 480px) {
        .product-card .gambar { font-size: 28px; }
        .product-card h3 { font-size: 12px; }
        .product-card .harga { font-size: 13px; }
        .stButton > button { font-size: 10px !important; padding: 6px !important; }
        .header h1 { font-size: 18px; }
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
        emoji = ["1", "2", "3", "4", "5", "6"][i]

        st.markdown(f"""
        <div class="product-card">
            <div class="gambar">{emoji}</div>
            <h3>{p['nama']}</h3>
            <p class="harga">Rp{p['harga']:,}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"🛒 Tambah", key=f"add_{p['id']}"):
            st.session_state.keranjang.append(p)
            st.rerun()

total_item = len(st.session_state.keranjang)
total_ha
