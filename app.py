# IMPORTS
import requests
import streamlit as st
from streamlit_float import float_init

# PAGE CONFIG
st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide")
float_init()

# SESSION STATE
defaults = {
    "halaman": "produk",
    "keranjang": [],
    "nama_pemesan": "",
    "kelas": "",
    "no_hp": "",
}

for key, value in defaults.items();
    st.session_state.setdefault(key, value)

# WHATSAPP CONFIG
FONNTE_API = "AHUP2hyJ32GrzWzBfmxa"  
ADMIN_PHONE = "81180895229"      

def kirim_wa(pesan):
    url = "https://api.fonnte.com/send"
    
    data = {
        "target": ADMIN_PHONE,
        "message": pesan,
        "countryCode": "62",
    }
    
    headers = {
        "Authorization": FONNTE_API
    }
    
    try:
        response = requests.post(
            url,
            data=data,
            headers=headers,
            timeout=10,
        )
        
        return response.ok
    
    except Exception as e:
        print(f"WhatsApp error: {e}")
        return False

def format_rupiah(nominal):
    return f"Rp{nominal:,}"

def data_lengkap(nama, kelas, hp):
    return bool(nama and kelas and hp)

def buat_detail_order(keranjang):
    return "\n".join(
        [
            f"- {item['nama']} ({format_rupiah(item['harga'])})"
            for item in keranjang
        ]
    )

def buat_pesan(nama, kelas, hp, detail, total):
    return f"""
🛍️ *PESANAN BARU!*
━━━━━━━━━━━━━━━━
👤 Nama: {nama}
🏫 Kelas: {kelas}
📱 No. HP: {hp}
━━━━━━━━━━━━━━━━
📦 *Detail Pesanan:*
{detail}
━━━━━━━━━━━━━━━━
💰 *Total: {format_rupiah(total)}*
━━━━━━━━━━━━━━━━
"""

def reset_pesanan():
    st.session_state.keranjang = []
    st.session_state.nama_pemesan = ""
    st.session_state.kelas = ""
    st.session_state.no_hp = ""

# PRODUCT DATA
produk = [
    {
        "id": 1,
        "nama": "Dubai chewy cookie strawberry",
        "harga": 67,
        "gambar": "https://i.ibb.co.com/xSTTgJ1K/dubai.jpg"
    },
    {
        "id": 2,
        "nama": "Chilis",
        "harga": 67,
        "gambar": "https://i.ibb.co.com/GvvnbcHn/Whats-App-Image-2026-08-02-at-19-03-45.jpg"
    },
    {
        "id": 3,
        "nama": "Samyang roll moza",
        "harga": 67,
        "gambar": "https://i.ibb.co.com/TBKfvx1G/Whats-App-Image-2026-08-02-at-19-03-45-1.jpg"
    },
    {
        "id": 4,
        "nama": "Scoopable cookies",
        "harga": 67,
        "gambar": "https://i.ibb.co.com/BVBH8p65/Whats-App-Image-2026-08-02-at-19-03-46.jpg"
    },
    {
        "id": 5,
        "nama": "Milo dino",
        "harga": 67,
        "gambar": "https://i.imgur.com/YgPzFFl.jpeg"
    },
    {
        "id": 6,
        "nama": "Mojito",
        "harga": 67,
        "gambar": "https://i.imgur.com/dvcbExw.jpeg"
    },
]

# CSS STYLING
:root {
    --primary: #ee4d2d;
    --primary-hover: #d43b1f;
}
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
        color: var(--primary);
    }
    .header .badge {
        background: var(--primary);
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
        animation: fadeIn 0.5s ease;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    .product-card h3 {
        font-size: 16px;
        margin: 5px 0;
        color: #1a1a1a;
    }
    .product-card .harga {
        font-size: 20px;
        font-weight: 700;
        color: var(--primary);
        margin-bottom: 10px;
    }
    .stButton > button {
        background: var(--primary);
        color: white;
        border: none;
        width: 100%;
        border-radius: 10px;
        font-weight: 600;
        padding: 8px;
        font-size: 14px;
    }
    .stButton > button:hover {
        background: var(--primary-hover) !important;
    }
    .footer {
        text-align: center;
        padding: 20px 0 10px;
        color: #999;
        font-size: 13px;
        margin-top: 30px;
        border-top: 1px solid #eee;
    }
    @media (max-width: 768px){
        .header {
            padding: 12px 15px;
        }
        .header h1 {
            font-size: 20px;
        }
        .product-card {
            padding: 12px;
        }
        .product-card h3 {
            font-size: 14px;
        }
        .product-card .harga {
            font-size: 18px;
        }
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

jumlah_produk = len(produk)
SHOP_NAME = "Social 9D"
ADD_CART_TEXT = "🛒 Tambahkan ke Keranjang"
CART_BUTTON_TEXT = "🛒 Keranjang"
DELETE_BUTTON_TEXT = "✕"
ORDER_FORM_KEY = "form_pesan"
SUBMIT_ORDER_TEXT = "✅ Kirim Pesanan"
NAME_INPUT_KEY = "input_nama"
CLASS_INPUT_KEY = "input_kelas"
PHONE_INPUT_KEY = "input_nohp"
CART_FLOAT_BOTTOM = "30px"
CART_FLOAT_RIGHT = "30px"
CART_FLOAT_WIDTH = "220px"

st.markdown(f"""
<div class="header">
    <h1>🛍️ <span>{SHOP_NAME}</span></h1>
    <div class="badge">{jumlah_produk} Produk</div>
</div>
""", unsafe_allow_html=True)

# PRODUCT PAGE
if st.session_state.halaman == "produk":
    cols = st.columns(3)

    for i, p in enumerate(produk):
        with cols[i % 3]:
            
            if p["gambar"]:
                f"""
                    <div style="width:100%; aspect-ratio:1/1; overflow:hidden; border-radius:12px; background:#f5f5f5; border:1px solid #eee;">
                    <img src="{gambar}" style="width:100%; height:100%; object-fit:cover;">
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="product-card">
                <h3>{p['nama']}</h3>
                <p class="harga">{format_rupiah(p['harga'])}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(ADD_CART_TEXT, key=f"add_{p['id']}"):
                st.session_state.keranjang.append(p.copy())
                st.rerun()

    cart_count = len(st.session_state.keranjang)
    
    button_container = st.container()

    with button_container:
        if st.button(
            f"{CART_BUTTON_TEXT} ({cart_count})",
            key="btn_keranjang",
            use_container_width=True,
        ):
            st.session_state.halaman = "keranjang"
            st.rerun()

    button_container.float(
        css=f"""
        bottom: {CARD_FLOAT_BOTTOM};
        right: {CARD_FLOAT_RIGHT};
        width: {CARD_FLOAT_WIDTH};
        """
    )

# CART PAGE
else:
    st.markdown("## 🛒 Keranjang ")
    st.markdown("---")
    
    cart_empty = len(st.session_state.keranjang) == 0
    
    if st.button("← Kembali ", key="btn_back"):
        st.session_state.halaman = "produk"
        st.rerun()
    
    st.markdown("---")
    
    if cart_empty:
        st.info("🛍️ Keranjang masih kosong")
    else:
        for idx, item in enumerate(st.session_state.keranjang):
            col1, col2, col3 = st.columns([3, 1, 0.5])
            with col1:
                st.write(f"**{item['nama']}**")
            with col2:
                st.write(format_rupiah(item["harga"]))
            with col3:
                if st.button(DELETE_BUTTON_TEXT, key=f"del_{idx}"):
                    del st.session_state.keranjang[idx]
                    st.rerun()
        
        st.markdown("---")
        
        total_harga = sum(item['harga'] for item in st.session_state.keranjang)
        
        st.markdown(f"### 💰 Total: **Rp{total_harga:,}**")
        st.markdown("---")
        
        with st.form(ORDER_FORM_KEY):
            st.markdown("### 📝 Data Pemesan")
            
            nama_pemesan = st.text_input(
                "Nama Lengkap",
            value=st.session_state.nama_pemesan,
                placeholder="Masukkan nama kamu",
                key=NAME_INPUT_KEY
            )
            kelas = st.text_input(
                "Kelas", 
                value=st.session_state.kelas,
                placeholder="Contoh: 10 IPA 1",
                key=CLASS_INPUT_KEY
            )
            no_hp = st.text_input(
                "No. HP (WA)", 
                value=st.session_state.no_hp,
                placeholder="Contoh: 08123456789",
                key=PHONE_INPUT_KEY
            )
            
            submit = st.form_submit_button(SUBMIT_ORDER_TEXT, use_container_width=True)
            
            if submit:
                if not data_lengkap(nama_pemesan, kelas, no_hp):
                    st.error("❌ Semua data harus diisi!")
                elif len(st.session_state.keranjang) == 0:
                    st.error("❌ Keranjang masih kosong!")
                else:
                    detail_order = buat_detail_order(st.session_state.keranjang)
                    pesan = buat_pesan(
                        nama_pemesan,
                        kelas,
                        no_hp,
                        detail_order,
                        total_harga
                    )
                    
                    try:
                        berhasil = kirim_wa(pesan)

                        if berhasil:
                            st.success("✅ Pesanan berhasil dikirim!")
                            st.balloons()
                        
                            reset_pesanan()
                        
                        else:
                            st.error("❌ Gagal mengirim pesan WhatsApp. Silakan coba lagi.")
                    
                    except Exception as e:
                        st.error(f"❌ Error: {e}")

st.markdown(f"""
<div class="footer">Jika ada pertanyaan bisa langsung di klik dan ngechat kita
    <a href="https://wa.me/{NO_HP}" target="_blank" style="color:#ee4d2d; text-decoration:none; font-weight:600;">
       bisa diklik
    </a>
</div>
""", unsafe_allow_html=True)
