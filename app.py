import streamlit as st
import requests

st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide")

# ===== INISIALISASI =====
if "halaman" not in st.session_state:
    st.session_state.halaman = "produk"

if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

if "nama_pemesan" not in st.session_state:
    st.session_state.nama_pemesan = ""
if "kelas" not in st.session_state:
    st.session_state.kelas = ""
if "no_hp" not in st.session_state:
    st.session_state.no_hp = ""

# ===== FONNTE WA =====
FONNTE_API = "AHUP2hyJ32GrzWzBfmxa"
NO_HP = "81180895229"

def kirim_wa(pesan):
    url = "https://api.fonnte.com/send"
    data = {
        "target": NO_HP,
        "message": pesan,
        "countryCode": "62",
    }
    headers = {"Authorization": FONNTE_API}
    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        return response.status_code == 200
    except:
        return False

produk = [
    {"id": 1, "nama": "Dubai chewy cookie strawberry", "harga": 67, "gambar": "https://i.ibb.co.com/xSTTgJ1K/dubai.jpg"},
    {"id": 2, "nama": "Chilis", "harga": 67, "gambar": "https://i.ibb.co.com/GvvnbcHn/Whats-App-Image-2026-08-02-at-19-03-45.jpg"},
    {"id": 3, "nama": "Samyang roll moza", "harga": 67, "gambar": "https://i.ibb.co.com/TBKfvx1G/Whats-App-Image-2026-08-02-at-19-03-45-1.jpg"},
    {"id": 4, "nama": "Scoopable cookies", "harga": 67, "gambar": "https://i.ibb.co.com/BVBH8p65/Whats-App-Image-2026-08-02-at-19-03-46.jpg"},
    {"id": 5, "nama": "Milo dino", "harga": 67, "gambar": "https://i.imgur.com/YgPzFFl.jpeg"},
    {"id": 6, "nama": "Mojito", "harga": 67, "gambar": "https://i.imgur.com/dvcbExw.jpeg"},
]

# ===== GLOBAL CSS =====
st.markdown("""
<style>
    /* Sembunyikan default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .header {
        background: white;
        padding: 15px 25px;
        border-radius: 16px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
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
        border-radius: 0 0 16px 16px;
        padding: 12px 15px 15px 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        text-align: center;
        border: 1px solid #f0f0f0;
        border-top: none;
    }
    .product-card h3 {
        font-size: 15px;
        margin: 5px 0 4px 0;
        color: #1a1a1a;
    }
    .product-card .harga {
        font-size: 18px;
        font-weight: 700;
        color: #ee4d2d;
        margin-bottom: 0;
    }

    /* Tombol merah global */
    .stButton > button {
        background: #ee4d2d !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 8px !important;
        font-size: 14px !important;
        transition: background 0.2s !important;
    }
    .stButton > button:hover {
        background: #d43b1f !important;
        color: white !important;
    }

    /* Tombol back — override warna jadi abu */
    .back-btn .stButton > button {
        background: #f0f0f0 !important;
        color: #333 !important;
        border-radius: 10px !important;
    }
    .back-btn .stButton > button:hover {
        background: #ddd !important;
        color: #111 !important;
    }

    /* Floating cart button */
    .floating-wrap {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
    }
    .floating-wrap .stButton > button {
        background: #ee4d2d !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 12px 28px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 20px rgba(238, 77, 45, 0.45) !important;
        width: auto !important;
        min-width: 180px !important;
        border: none !important;
    }
    .floating-wrap .stButton > button:hover {
        background: #d43b1f !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 28px rgba(238, 77, 45, 0.5) !important;
    }

    .footer {
        text-align: center;
        padding: 20px 0 10px;
        color: #999;
        font-size: 13px;
        margin-top: 30px;
        border-top: 1px solid #eee;
    }

    /* Form styling */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        border: 1.5px solid #e0e0e0 !important;
        padding: 10px 14px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ee4d2d !important;
        box-shadow: 0 0 0 2px rgba(238,77,45,0.15) !important;
    }
    .stForm {
        background: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.07);
        border: 1px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
total_item = len(st.session_state.keranjang)
st.markdown(f"""
<div class="header">
    <h1>🛍️ <span>Social 9D</span></h1>
    <div class="badge">{total_item} item di keranjang</div>
</div>
""", unsafe_allow_html=True)

# ========================================
# ===== HALAMAN PRODUK =====
# ========================================
if st.session_state.halaman == "produk":

    cols = st.columns(3)

    for i, p in enumerate(produk):
        with cols[i % 3]:
            # Gambar produk
            if "gambar" in p and p["gambar"]:
                st.markdown(f"""
                <div style="width:100%; aspect-ratio:1/1; overflow:hidden;
                            border-radius:16px 16px 0 0; background:#f5f5f5;
                            border:1px solid #eee; border-bottom:none;">
                    <img src="{p['gambar']}" style="width:100%; height:100%; object-fit:cover;">
                </div>
                """, unsafe_allow_html=True)

            # Info produk
            st.markdown(f"""
            <div class="product-card">
                <h3>{p['nama']}</h3>
                <p class="harga">Rp{p['harga']:,}</p>
            </div>
            """, unsafe_allow_html=True)

            # Tombol tambah keranjang
            if st.button("Tambahkan ke Keranjang", key=f"add_{p['id']}"):
                st.session_state.keranjang.append(p)
                st.rerun()

            st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

    # ===== FLOATING BUTTON KERANJANG (STICKY) =====
st.markdown("""
<style>
    .sticky-cart {
        position: sticky;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
        background: #ee4d2d;
        color: white;
        border-radius: 50px;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: 700;
        box-shadow: 0 4px 20px rgba(238, 77, 45, 0.45);
        border: none;
        transition: background 0.2s;
    }
    .sticky-cart:hover {
        background: #d43b1f;
    }
</style>
""", unsafe_allow_html=True)

# Di tempat yang sama di dalam halaman produk, tambahkan tombol keranjang:
if st.button(f"Keranjang ({total_item} item)", key="btn_sticky_cart"):
    st.session_state.halaman = "keranjang"
    st.rerun()

# ===== TOMBOL KERANJANG =====
st.markdown(f'<button class="sticky-cart" onclick="document.querySelector(\'[data-testid="stButton"]\').click();">Keranjang ({total_item} item)</button>', unsafe_allow_html=True)


# ========================================
# ===== HALAMAN KERANJANG =====
# ========================================
else:
    st.markdown("## Keranjang Belanja")
    st.markdown("---")

    total_harga = sum(item['harga'] for item in st.session_state.keranjang)

    # Tombol kembali
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("Kembali Belanja", key="btn_back"):
        st.session_state.halaman = "produk"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    if len(st.session_state.keranjang) == 0:
        st.info("Keranjang masih kosong. Yuk belanja dulu!")
    else:
        # Daftar item keranjang
        for idx, item in enumerate(st.session_state.keranjang):
            col1, col2, col3 = st.columns([3, 1.5, 0.5])
            with col1:
                st.markdown(f"**{item['nama']}**")
            with col2:
                st.markdown(f"Rp{item['harga']:,}")
            with col3:
                if st.button("X", key=f"del_{idx}"):
                    st.session_state.keranjang.pop(idx)
                    st.rerun()

        st.markdown("---")
        st.markdown(f"### Total: **Rp{total_harga:,}**")
        st.markdown("---")

        # ===== FORM PEMESANAN =====
        with st.form("form_pesan"):
            st.markdown("### Data Pemesan")

            nama_pemesan = st.text_input(
                "Nama Lengkap",
                value=st.session_state.nama_pemesan,
                placeholder="Masukkan nama kamu",
            )
            kelas = st.text_input(
                "Kelas",
                value=st.session_state.kelas,
                placeholder="Contoh: 10 IPA 1",
            )
            no_hp = st.text_input(
                "No. HP (WA)",
                value=st.session_state.no_hp,
                placeholder="Contoh: 08123456789",
            )

            submit = st.form_submit_button("Kirim Pesanan", use_container_width=True)

            if submit:
                if not nama_pemesan or not kelas or not no_hp:
                    st.error("Semua data harus diisi!")
                elif len(st.session_state.keranjang) == 0:
                    st.error("Keranjang masih kosong!")
                else:
                    detail_order = "\n".join(
                        [f"- {item['nama']} (Rp{item['harga']:,})"
                         for item in st.session_state.keranjang]
                    )
                    pesan = f"""
*PESANAN BARU - Social 9D*
Nama   : {nama_pemesan}
Kelas  : {kelas}
No. HP : {no_hp}

*Detail Pesanan:*
{detail_order}

*Total: Rp{total_harga:,}*
                    """

                    kirim_wa(pesan)

                    wa_text = (
                        f"Halo kak, saya {nama_pemesan} dari kelas {kelas}. "
                        f"Saya sudah melakukan pesanan dengan total Rp{total_harga:,}. "
                        f"Mohon konfirmasinya ya kak!"
                    )
                    wa_link = (
                        f"https://api.whatsapp.com/send?phone=62{NO_HP}"
                        f"&text={wa_text.replace(' ', '%20')}"
                    )

                    # Simpan data ke session sebelum reset
                    st.session_state.keranjang = []
                    st.session_state.nama_pemesan = ""
                    st.session_state.kelas = ""
                    st.session_state.no_hp = ""

                    st.success("Pesanan berhasil dikirim! Terima kasih.")
                    st.balloons()
                    st.markdown(
                        f"[Klik di sini untuk konfirmasi via WhatsApp]({wa_link})",
                        unsafe_allow_html=False
                    )

# ===== FOOTER =====
st.markdown(f"""
<div class="footer">
    Ada pertanyaan? Hubungi kami langsung via
    <a href="https://wa.me/62{NO_HP}" target="_blank"
       style="color:#ee4d2d; text-decoration:none; font-weight:600;">
        WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)
