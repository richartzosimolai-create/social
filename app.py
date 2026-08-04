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
.produk-card {
    border: 1px solid #eee;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 16px;
    text-align: center;
}
.produk-card img {
    width: 100%;
    border-radius: 10px;
    object-fit: cover;
    height: 180px;
}
.produk-nama {
    font-weight: 600;
    margin-top: 8px;
}
.produk-harga {
    color: #e63946;
    font-weight: 700;
}

/* ===== FLOATING CART BUTTON FIX ===== */
div:has(> div#floating-cart-marker) + div[data-testid="stButton"] {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    width: auto;
}
div:has(> div#floating-cart-marker) + div[data-testid="stButton"] button {
    border-radius: 50px;
    padding: 0.75em 1.5em;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    background-color: #e63946;
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
total_item = len(st.session_state.keranjang)
st.markdown(f"""
<div style="padding:10px 0;">
    <h2 style="margin-bottom:0;">🛍️ Social 9D</h2>
    <p style="color:gray;margin-top:0;">{total_item} item di keranjang</p>
</div>
""", unsafe_allow_html=True)

# ========================================
# ===== HALAMAN PRODUK =====
# ========================================
if st.session_state.halaman == "produk":
    cols = st.columns(3)
    for i, p in enumerate(produk):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="produk-card">
                <img src="{p['gambar']}" />
                <div class="produk-nama">{p['nama']}</div>
                <div class="produk-harga">Rp{p['harga']:,}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Tambahkan ke Keranjang", key=f"add_{p['id']}"):
                st.session_state.keranjang.append(p)
                st.rerun()

    # ===== FLOATING BUTTON KERANJANG (marker + button harus berurutan) =====
    st.markdown('<div id="floating-cart-marker"></div>', unsafe_allow_html=True)
    if st.button(f"🛒 Keranjang ({total_item} item)", key="btn_float_keranjang"):
        st.session_state.halaman = "keranjang"
        st.rerun()

# ========================================
# ===== HALAMAN KERANJANG =====
# ========================================
else:
    st.markdown("## Keranjang Belanja")
    st.markdown("---")

    total_harga = sum(item['harga'] for item in st.session_state.keranjang)

    if st.button("Kembali Belanja", key="btn_back"):
        st.session_state.halaman = "produk"
        st.rerun()

    st.markdown("---")

    if len(st.session_state.keranjang) == 0:
        st.info("Keranjang masih kosong. Yuk belanja dulu!")
    else:
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
                        [f"- {item['nama']} (Rp{item['harga']:,})" for item in st.session_state.keranjang]
                    )
                    pesan = f"""*PESANAN BARU - Social 9D*

Nama    : {nama_pemesan}
Kelas   : {kelas}
No. HP  : {no_hp}

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
st.markdown("""
<div style="text-align:center; padding:20px 0; color:gray;">
    Ada pertanyaan? Hubungi kami langsung via WhatsApp
</div>
""", unsafe_allow_html=True)
