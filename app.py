import streamlit as st
import requests

st.set_page_config(page_title="Social 9D", page_icon="🛍️", layout="wide")

# ===== CEK STATUS SIDEBAR =====
if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

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
: white;
        color: #ee4d2: white;
        color: #ee4d2: white;
        color: #ee4d2: white;
        color: #ee4d2        color: #ee4d2d;
        border-radius: 50%;
d;
        border-radius: 50%;
        padding: 2px 10px;
        font-size: d;
        border-radius: 50%;
        padding: 2px 10px;
        font-size: d;
        border-radius: 50%;
        padding: 2px 10px;
        font-size: 14pxd;
        border-radius: 50%;
        padding: 2px 10px;
        font-size: 14px;
        font        padding: 2px 10px;
        font-size: 14px;
        font-weight: 700;
   14px;
        font-weight: 700;
   14px;
        font-weight: 700;
   ;
        font-weight: 700;
    }
    .footer-weight: 700;
    }
    .footer }
    .footer {
        text-align }
    .footer {
        text-align: center;
        }
    .footer {
        text-align: center;
        {
        text-align: center;
       : center;
        padding: 20 padding: 20px 0  {
        text-align: center;
        padding: 20px 0  padding: 20px 0 10px;
        color: #999 padding: 20px 0 10px;
        color: #999;
        fontpx 0 10px;
       10px;
        color: #99910px;
        color: #999;
        font-size: 13px-size: 13px;
        margin-top color: #999;
        font-size: 13px;
        margin-top;
        font-size: 13px;
        font-size: 13px;
        margin-top: 30px: 30px;
        border-top: 30px;
        border-top;
        margin-top: 30px;
        border-top: 1px;
        margin-top: 30px;
        border-top: 1px;
        border-top: 1px: 1px solid #eee;
: 1px solid #eee;
 solid #eee;
    }
</style>
""", unsafe_allow_html=True solid #eee;
    }
</style>
""", unsafe_allow_html=True solid #eee;
    }
</style>
""", unsafe_allow_html=True    }
</style>
""", unsafe_allow_html=True)

st.markdown    }
</style>
""", unsafe_allow_html=True)

st.markdown)

st.markdown("""
<div)

st.markdown("""
<div class="header">
   )

st.markdown("""
<div class="header">
    <h1("""
<div class="header">
("""
<div class="header">
    <h1>🛍 class="header">
    <h1>🛍️ <span> <h1>🛍️ <span>🛍️ <span>Social 9D</span> </    <h1>🛍️ <span>Social 9D️ <span>Social 9D</span> </h1>
   Social 9D</span> </>Social 9D</span> </h1>
    <divh1>
    <div class="</span> </h1>
    <div class=" <div class="badge">6 Produk</divh1>
    <div class="badge">6 Produk</div>
</div>
 class="badgebadge">6 Produk</div>
</div>
badge">6 Produk</div>
</div>
""", unsafe_>
</div>
""", unsafe_""", unsafe_allow_html=True)

">6 Produk</div>
</div>
""", unsafe_allow""", unsafe_allow_html=True)

allow_html=True)

cols = stallow_html=True)

cols = st.columnscols = st.columns(3)

for_html=True)

cols = st.columnscols = st.columns(3)

for i, p in enumerate(.columns(3)

for i, p(3)

for i, p in enumerate(produk):
    i, p in enumerate(produ(3)

for i, p in enumerate(produk):
    withproduk):
    with in enumerate(produk):
    with cols[i % 3]:
        
 with cols[i % 3]:
        
       k):
    with cols[i % 3]:
        
        if "gambar cols[i % 3]:
        
        cols[i % 3]:
        
        if "gambar        if "gambar" in p if "gambar" in p" in p and if "gambar" in p and" in p and and and p["gambar"]:
            st.markdown(f p["gambar"]:
            st.markdown(f"""
            <div style p["gambar"]:
            st.markdown(f"""
            <div style p["gambar"]:
            st.markdown(f"""
            <div style p["gambar"]:
            st.markdown(f"""
            <div style="width:100"""
            <div style="width:100%; aspect-ratio:1/1="width:100%; aspect-ratio="width:100%; aspect-ratio="width:100%; aspect-ratio%; aspect-ratio:1/1; overflow:hidden; border-radius:; overflow:hidden; border-radius::1/1; overflow:hidden; border-radius:12px; background:1/1; overflow:hidden; border-radius:12px; background:1/1; overflow:hidden; border-radius:12px; background12px; background:#f5f12px; background:#f5f5f5; border:1px:#f5f5f5; border:1px solid #eee;">
                <img src:#f5f5f5; border:1px solid #eee;">
                <img src="{p[':#f5f5f5; border:1px solid #eee;">
5f5; border:1px solid #eee;">
                <img src solid #eee;">
                <img src="{p['gambar']}" stylegambar']}" style="width:100                <img src="{p['gambar']}" style="width:100="{p['gambar']}" style="width:100%; height:100="{p['gambar']}" style="width:100%; height:100="width:100%; height:100%; height:100%; object%; height:100%; object-fit:%; object-fit:cover;">
            </%; object-fit:cover;">
            </div>
            """, unsafe_allow%; object-fit:cover;">
            </div>
            """, unsafe_allow-fit:cover;">
            </div>
            """, unsafe_allowcover;">
            </div>
            """, unsafe_allow_html=True)
       div>
            """, unsafe_allow_html=True)
        else:
            em_html=True)
        else:
            em_html=True)
        else:
            emoji = ["1", "2",_html=True)
        else:
            emoji = ["1", "2", "3 else:
            emoji = ["1", "2", "3", "oji = ["1", "2", "3", "4", "5oji = ["1", "2", "3", "4", "5 "3", "4", "5", "4", "5", "4", "5", "6"", "6"][i]
", "6"][i", "6"][i]
           6"][i]
           ][i]
            st.markdown(f            st.markdown(f'<div class]
            st.markdown(f'<div class="gambar">{emoji}</div st.markdown(f'<div class="gambar">{emoji}</div st.markdown(f'<div class="gambar">{emoji}</div>','<div class="gambar">{emoji}</div>', unsafe_="gambar">{emoji}</div>', unsafe_allow_html=True)
>', unsafe_allow_html=True)
>', unsafe_allow_html=True)
 unsafe_allow_html=True)
allow_html=True)
        
        st.markdown(f"""
        <div class="        
        st.markdown(f"""
        <div class="product-card">
                   
        st.markdown(f"""
        <div class="product-card">
                   
        st.markdown(f"""
        <div class="product-card">
                   
        st.markdown(f"""
        <div class="product-card">
           product-card">
            <h3>{ <h3>{p['nama <h3>{p['nama'] <h3>{p['nama']}</h3>
            <p class <h3>{p['nama']}</h3>
            <p classp['nama']}</h3>
            <p class']}</h3>
            <p class}</h3>
            <p class="harga">Rp{p['="harga">Rp{p['h="harga">Rp{p['h="harga">Rp{p['harga']:,}</="harga">Rp{p['harga']:,}</p>
        </div>
        """, unsafe_allowharga']:,}</p>
        </div>
        """, unsafe_allowarga']:,}</p>
        </div>
        """, unsafe_allowarga']:,}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.buttonp>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"_html=True)
        
        if st.button(f"🛒 Tamb_html=True)
        
        if st.button(f"🛒_html=True)
        
        if st.button(f"🛒 Tambahkan(f"🛒 Tambahkan ke Keranjang", key=f"🛒 Tambahkan ke Keranjahkan ke Keranjang", key=f" Tambahkan ke Keranjang", key=f"add_{p[' ke Keranjang", key=f"add_{p['add_{p['ang", key=f"add_{p['add_{p['idid']}"):
            st.session_state.keranjang.append(p)
           id']}"):
            st.session_state.keranjang.append(p)
            st.session_state.showid']}"):
            st.session_state.keranjang.append(p)
            st.session_stateid']}"):
            st.session_state.keranjang.append(p)
            st.session_state.show']}"):
            st.session_state.keranjang.append(p)
            st.session_state.show st.session_state.show_cart = True_cart = True
            st.r.show_cart = True
            st.rerun()

total_cart = True
            st.rerun()

total_item = len_cart = True
            st.rerun()

total_item = len
            st.rerun()

total_item = len(st.session_state.erun()

total_item = len_item = len(st.session_state.(st.session_state.keranjang)
(st.session_state.keranjangkeranjang)
total_harga =(st.session_state.keranjang)
total_harga = sum(item['hkeranjang)
total_harga = sum(item['harga'] for itemtotal_harga = sum(item['h)
total_harga = sum(item['harga'] for item in st.session sum(item['harga'] for item in st.session_state.keranjangarga'] for item in st.session_state in st.session_state.keranjangarga'] for item in st.session_state_state.keranjang)

# =====.keranjang)

# =====)

# ===== TOMBOL.keranjang)

# =====)

# ===== TOMBOL KERAN TOMBOL KERANJANG + TEKS DIN TOMBOL KERANJANG + TEKS DINAMIS ( KERANJANG + TEKS TOMBOL KERANJANG + TEKS DINAMIS (JANG + TEKS DINAMIS (BUKA/TAMIS (BUKA/TBUKA/TUTUP) = DINAMIS (BUKA/TUTUP) =====
if stBUKA/TUTUP) =UTUP) =====
if stUTUP) =====
if st====
if st.session_state.show_c.session_state.show_cart:
    te====
if st.session_state.show_c.session_state.show_cart:
    te.session_state.show_cart:
    teart:
    teks_keranjang = "✕ Tutup kerks_keranjang = "art:
    teks_keranjang = "✕ Tutup kerks_keranjang = "✕ Tutup keranjang"
   ks_keranjang = "✕ Tutup keranjang"
   anjang"
    warna_teks✕ Tutup keranjang"
    warna_teks = "#ff444anjang"
    warna_teks warna_teks = "#ff444 warna_teks = "#ff444 = "#ff4444"
else:
    teks_keranjang =4"
else:
    teks_keranjang = "☰ B = "#ff4444"
else:
    teks_keranjang = "☰ Buka keranjang4"
else:
    teks_keranjang = "☰ B4"
else:
    teks_keranjang = "☰ B "☰ Buka keranjanguka keranjang"
    warna_teks = "#ee4"
    warna_teks = "#uka keranjang"
    warna_teks = "#ee4d2uka keranjang"
    warna_teks = "#ee4d2"
    warna_teks = "#ee4d2d"

st.markd2d"

st.markee4d2d"

st.markd"

st.markdown(f"""
<div style="position:fixed; bottom:d"

st.markdown(f"""
<div style="position:fixed; bottom:down(f"""
<div style="position:fixed; bottom:30px; rightdown(f"""
<div style="position:fixed; bottom:30px; right:30down(f"""
<div style="position:fixed; bottom:30px; right30px; right:30px;30px; right:30px; z-index:999; display:flex:30px; z-index:999px; z-index:999; display:30px; z-index:999; display:flex; align-items: z-index:999; display:flex; align-items:center; gap:; align-items:center; gap:; display:flex; align-items:center; gap:10px;">
   :flex; align-items:center; gap:10px;">
    <center; gap:10px;">
   10px;">
    <div style="10px;">
    <div style=" <div style="background:white;div style="background:white; color:{w <div style="background:white; color:{warna_teks};background:white; color:{warnabackground:white; color:{warna_teks}; padding:6px color:{warna_teks};arna_teks}; padding:6 padding:6px 14px;_teks}; padding:6px 14px; padding:6px 14px;px 14px; border-radius:20px; font-size border-radius:20px; font-size 14px; border-radius:20 border-radius:20px; font-size:13px; border-radius:20px; font-size:13px; font-weight::13px; font-weightpx; font-size:13px; font-weight:600; box-shadow: font-weight:600; box-shadow::13px; font-weight:600; box-shadow:0 2px600; box-shadow:0 2:600; box-shadow:0 20 2px 10px rgba0 2px 10px rgba(0,0 10px rgba(0,0px 10px rgbapx 10px rgba(0,0,0,0(0,0,0,0,0,0.1); cursor,0,0.1); cursor(0,0,0,0.1); cursor:pointer;".1); cursor:pointer;".1); cursor:pointer;":pointer;" 
         onclick=":pointer;" 
         onclick="document.querySelector('[data-testid=\\" 
         onclick="document.querySelector('[data 
         onclick="document.querySelector('[data 
         onclick="document.querySelector('[data-testid=\\"document.querySelector('[data-testid=\\"stSidebar\\"] button')-testid=\\"stSidebar-testid=\\"stSidebar\\"] button')?.click();">
stSidebar\\"] button')?.clickstSidebar\\"] button')?.click();">
        {te\\"] button')?.click();">
        {teks_keranj        {teks_keranj();">
        {te?.click();">
        {teks_keranjang}
    </ks_keranjang}
    </ang}
    </div>
   ang}
    </div>
   ks_keranjang}
    </div>
    <div class="cartdiv>
    <div classdiv>
    <div class="cart-badge" style="margin:0 <div class="cart-badge" style="margin:0; position:relative <div class="cart-badge" style="margin:0; position:relative-badge" style="margin:0="cart-badge" style="margin:0; position:relative; bottom:auto; position:relative; bottom:auto; right:auto; cursor:pointer; bottom:auto; right:auto; bottom:auto; right:auto; position:relative; bottom:auto; right:auto; cursor:pointer; right:auto; cursor:pointer;" 
         onclick="document.querySelector; cursor:pointer;" 
        ; cursor:pointer;" 
         onclick="document.querySelector('[data-testid=\;" 
         onclick="document.querySelector;" 
         onclick="document.querySelector('[data-testid=\\"stSidebar('[data-testid=\\"stSidebar onclick="document.querySelector('[data-testid=\\"stSidebar\\"] button')\"stSidebar\\"] button')('[data-testid=\\"stSidebar\\"] button')?.click();">
\\"] button')?.click();">
\\"] button')?.click();">
?.click();">
        🛒 Keranjang
        <span?.click();">
        🛒 Keranjang
        <span        🛒 Keranjang        🛒 Keranjang        🛒 Keranjang
        <span class="count">{ class="count">{total_item}</ class="count">{total_item}</span
        <span class="count">{total_item}</span>
    </div
        <span class="count">{total_item}</spantotal_item}</span>
    </divspan>
    </div>
    </div>
</div>
>
</div>
""", unsafe_>
    </div>
</div>
>
</div>
""", unsafe_allow_html=True)

with st.s>
</div>
""", unsafe_allow_html=True)

with st.s""", unsafe_allow_html=True)

with st.sidebar:
   allow_html=True)

with st.s""", unsafe_allow_html=True)

with st.sidebar:
   idebar:
    st.markdown("idebar:
    st.markdown(" st.markdown("## 🛒idebar:
    st.markdown("## 🛒 Keranjang st.markdown("## 🛒## 🛒 Keranjang## 🛒 Keranjang Bel Keranjang Belanja")
    Belanja")
    st.markdown Keranjang Belanja")
    Belanja")
    st.markdown("anja")
    st.markdown(" st.markdown("---")
    
("---")
    
    if len st.markdown("---")
    
    if len(st.session_state.keranj---")
    
    if len(st.session_state.keranjang) == ---")
    
    if len(st.session_state.keranjang) ==     if len(st.session_state.keranjang) == (st.session_state.keranjang) == 0:
        stang) == 0:
0:
        st.info("0:
        st.info("0:
        st.info(".info("🛍️ Keranj        st.info("🛍️ Keranj🛍️ Keranjang masih kosong🛍️ Keranjang masih kosong")
    else:
        for idx,🛍️ Keranjang masih kosongang masih kosong")
    else:
ang masih kosong")
    else:
        for idx, item in enumerate(st")
    else:
        for idx, item in enumerate(st.session_state.")
    else:
        for idx, item in enumerate(st        for idx, item in enumerate(st.session_state.keranjang):
           .session_state.keranjang):
            item in enumerate(st.session_state.keranjang):
            col1, colkeranjang):
            col1, col.session_state.keranjang):
            col1, col2, col3 col1, col2, col3 col1, col2, col3 = st.columns([2,2, col3 = st.columns([2, 1, 0.2, col3 = st.columns([2, 1, 0. = st.columns([2, 1 = st.columns([2, 1, 0.5])
            with 1, 0.5])
           5])
            with col1:
               5])
            with col1:
                st.write(f"**{, 0.5])
            with col1:
                st.write(f" col1:
                st.write(f"**{item['nama']}** with col1:
                st.write(f"**{item['nama']} st.write(f"**{item['item['nama']}****{item['nama']}**")
            with col2:
                st")
            with col2:
**")
            with col2:
               nama']}**")
            with col2:
                st.write(f"Rp{item['harga']:,}")
")
            with col2:
                st.write(f"Rp{item['h.write(f"Rp{item['harga']:,}")
            with col                st.write(f"Rp{item['harga']:,}")
            with st.write(f"Rp{item['harga']:,}")
            with col            with col3:
                if st.button("✕", key=farga']:,}")
            with col3:
                if st.button("3:
                if st.button col3:
                if st.button("✕", key=f3:
                if st.button("✕", key=f"del_{idx}"):
                    st✕", key=f"del_{idx}"):
                    st.session_state.ker("✕", key=f"del_{idx}"):
                    st"del_{idx}"):
                    st"del_{idx}"):
                    st.session_state.ker.session_state.ker.session_state.keranjang.pop(idx)
                    st.rerun()
        
        st.markdown.session_state.keranjang.pop(idx)
                    st.rerun()
        
        stanjang.pop(idx)
                    st.rerunanjang.pop(idx)
                    st.rerun()
        
        st.markdown("---")
       anjang.pop(idx)
                    st.rerun()
        
        st.markdown("---")
       ("---")
        st.markdown(f.markdown("---")
        st.markdown(f"### 💰 Total:()
        
        st.markdown("---")
        st.markdown(f"### 💰 st.markdown(f"### 💰 st.markdown(f"### 💰"### 💰 Total: **Rp **Rp{total_harga:, Total: **Rp{total_h Total: **Rp{total_harga:,}**")
        st.markdown Total: **Rp{total_harga:,}**")
        st.markdown{total_harga:,}**")
        st.markdown("---")
        
}**")
        st.markdown("arga:,}**")
        st.markdown("---")
        
        with st.form("---")
        
        with st.form("---")
        
        with st.form        with st.form("form_pesan---")
        
        with st.form("form_pesan"):
            st.mark("form_pesan"):
            st.mark("form_pesan"):
            st.markdown("### 📝 Data Pemesan("form_pesan"):
            st.mark"):
            st.markdown("###down("### 📝 Data Pemesandown("### 📝 Data Pemesan")
            
            nama_pemesan =down("### 📝 Data Pemesan")
            
            nama_pemesan = 📝 Data Pemesan")
            
")
            
            nama_pemesan =")
            
            nama_pemesan = st.text_input(
                "Nama st.text_input(
                "Nama            nama_pemesan = st.text_input(
                "Nama Leng st.text_input(
                "Nama Lengkap", 
                value=st st.text_input(
                "Nama Lengkap", 
                value=st Lengkap", 
                value=st Lengkap", 
                value=stkap", 
                value=st.session_state.nama_pemesan,
.session_state.nama_pemesan,
.session_state.nama_pemesan,
.session_state.nama_pemesan,
.session_state.nama_pemesan,
                placeholder="Masukkan nama kamu",
                placeholder="Mas                placeholder="Mas                placeholder="Masukkan nama kamu",
                key="input                placeholder="Masukkan nama kamu",
                key="input                key="input_nama"
           ukkan nama kamu",
                key="inputukkan nama kamu",
                key="input_nama"
            )
            kelas =_nama"
            )
            kelas =_nama"
            )
            kelas = )
            kelas = st.text_input(
_nama"
            )
            kelas = st.text_input(
                "Kelas", st.text_input(
                "Kelas st.text_input(
                "Kelas", 
                value st.text_input(
                "Kelas", 
                value=st.session_state                "Kelas", 
                value 
                value=st.session_state.k", 
                value=st.session_state=st.session_state.kelas,
               .kelas,
                placeholder="Contoh=st.session_state.kelas,
                placeholder="Contoh: 10elas,
                placeholder="Contoh.kelas,
                placeholder="Contoh placeholder="Contoh: 10 IPA 1",
               : 10 IPA 1",
                IPA 1",
               : 10 IPA 1",
               : 10 IPA 1",
                key="input_kelas"
            )
 key="input_kelas"
            )
            no_hp key="input_kelas"
            )
 key="input_kelas"
            )
 key="input_kelas"
            )
            no_hp = st.text_input            no_hp = st.text_input = st.text_input            no_hp = st.text_input(
                "No. HP (WA            no_hp = st.text_input(
                "No. HP (WA(
                "No. HP (WA(
                "No. HP (WA)", 
                value)", 
                value=st.session_state(
                "No. HP (WA)", 
                value=st.session_state)", 
                value=st.session_state)", 
                value=st.session_state=st.session_state.no_hp,
.no_hp,
                placeholder="Cont.no_hp,
                placeholder="Cont.no_hp,
                placeholder="Cont.no_hp,
                placeholder="Contoh: 08123456789",
                placeholder="Contoh: 081oh: 08123456789",
oh: 08123456789",
oh: 08123456789",
                key="input_nohp23456789",
                key="input_nohp"
            )
            
                key="input_nohp"
                key="input_nohp"
                key="input_nohp"
            )
            
            submit ="
            )
            
            submit = st            submit = st.form_submit_button("            )
            
            submit = st.form_submit_button("✅ Kirim Pes            )
            
            submit = st.form_submit_button("✅ Kirim Pes st.form_submit_button("✅ Kirim.form_submit_button("✅ Kirim Pesanan", use_container_width=True)
✅ Kirim Pesanan", use_container_width=True)
anan", use_container_width=True)
 Pesanan", use_container_width=Trueanan", use_container_width=True)
            
            if submit            
            if submit:
                if not            
            if submit:
                if not            
            if submit:
                if not nama_pemesan or not kelas)
            
            if submit:
                if not nama_pemesan or not kelas:
                if not nama_pemesan or not kelas or not no_h nama_pemesan or not kelas nama_pemesan or not kelas or not no_hp:
                    st or not no_hp:
                    st or not no_hp:
                    stp:
                    st.error("❌ or not no_hp:
                    st.error("❌ Semua data harus.error("❌ Semua data harus.error("❌ Semua data harus Semua data harus diisi!")
               .error("❌ Semua data harus diisi!")
                elif len(st.session diisi!")
                elif len(st.session diisi!")
                elif len(st.session_state.keranjang) ==  elif len(st.session_state.keranj diisi!")
                elif len(st.session_state.keranjang) == _state.keranjang) == _state.keranjang) == 0:
                    st.error("❌0:
                    st.error("❌ang) == 0:
                    st0:
                    st.error("❌0:
                    st.error(" Keranjang masih kosong!")
 Keranjang masih kosong!")
               .error("❌ Keranjang masih kosong!")
                else:
                    detail Keranjang masih kosong!")
                else:
                    detail_order = "\n❌ Keranjang masih kosong!")
                else:
                    detail_order = "\n                else:
                    detail_order = "\n".join([f"- { else:
                    detail_order = "\n".join([f"- {item['_order = "\n".join([f"- {item['nama']} (".join([f"- {item['nama']} (Rp{item".join([f"- {item['nama']} (Rp{item['hitem['nama']} (nama']} (Rp{itemRp{item['harga']:,})['harga']:,})" for itemarga']:,})" for item inRp{item['harga']:,})"['harga']:,})" for item in" for item in st.session_state. in st.session_state.keranjang])
 st.session_state.keranjang])
                    pesan = f"""
 for item in st.session_state.keranjang])
                    pesan = f"""
 st.session_state.keranjang])
                    pesan = f"""
keranjang])
                    pesan = f"""
🛍️ *P                    pesan = f"""
🛍️ *PESANAN BAR🛍️ *PESANAN BAR🛍️ *PES🛍️ *PESANAN BARESANAN BARU!*
━━U!*
━━━━━━━━━━U!*
━━━━━━━━━━ANAN BARU!*
━━━━━━━━━━━━━━━━
U!*
━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━
👤 Nama: {nama_p━━━━━━
━━━━━━
👤 Nama: {nama_p👤 Nama: {nama_pemesanemesan}
🏫 Kelas:👤 Nama: {nama_pemesan👤 Nama: {nama_pemesan}
🏫 Kelas: {kelasemesan}
🏫 Kelas:}
🏫 Kelas: {kelas}
📱 No. HP {kelas}
📱 No.}
🏫 Kelas: {kelas}
📱 No. HP}
📱 No. HP: { {kelas}
📱 No. HP: {no_hp}
━━: {no_hp}
━━ HP: {no_hp}
━━: {no_hp}
━━no_hp}
━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━
━━━━━━━━━━━━━━
━━━━━━━━━━━━━━
━━━━━━━━
📦 *Detail📦 *Detail Pesanan:*
📦 *Detail Pesanan:*
📦 *Detail Pesanan:*
{detail_order}
━━━━━━━━📦 *Detail Pesanan:*
 Pesanan:*
{detail{detail_order}
━━━━━━━━{detail_order}
━━━━━━━━━━━━━━━━
💰 *{detail_order}
━━━━━━━━━━━━━━━━
💰 *_order}
━━━━━━━━━━━━━━━━━━━━━━━━
💰 *Total: Rp{total_harga━━━━━━━━
💰 *Total: Rp{total_harga:,Total: Rp{total_harga:,Total: Rp{total_harga:,
💰 *Total: Rp{total_harga:,}*
━━━━:,}*
━━━━━━━━━━}*
━━━━━━━━━━━━}*
━━━━━━━━━━━━}*
━━━━━━━━━━━━━━━━━━━━━━━━
                   ━━━━━━
                    """
                    
                   ━━━━
                    """
                    
                    try:
                        kirim_wa(pesan━━━━
                    """
                    
                    try:
                        kirim━━━━
                    """
                    
                    try:
                        kirim_wa(pesan """
                    
                    try:
                        kirim try:
                        kirim)
                        
                        wa_text = f"H_wa(pesan)
                        
                        wa_text = f)
                        
                        wa_text = f"H_wa(pesan)
                        
                        wa_text = f"Halo {nama_p_wa(pesan)
                        
                        wa_text = f"Halo {nama_pemesan},alo {nama_pemesan}, pes"Halo {nama_pemesan}, pesalo {nama_pemesan}, pesemesan}, pesanan Anda sedang kami pesanan Anda sedang kami proses. Totalanan Anda sedang kami proses. Total Rpanan Anda sedang kami proses. Total Rpanan Anda sedang kami proses. Total Rp proses. Total Rp{total_harga Rp{total_harga:,}"
                        wa{total_harga:,}"
                        wa{total_harga:,}"
                        wa_link = f"https://api.w{total_harga:,}"
                        wa_link = f"https://api.w:,}"
                        wa_link = f"_link = f"https://api_link = f"https://api.whatsapp.com/send?phonehatsapp.com/send?phonehatsapp.com/send?phonehttps://api.whatsapp.com/send?phone={no_hp.whatsapp.com/send?phone={no_hp}&text={no_hp}&text={={no_hp}&text={={no_hp}&text={}&text={wa_text.replace('={wa_text.replace(' ', '%20wa_text.replace(' ', '%20')wa_text.replace(' ', '%20')wa_text.replace(' ', '%20') ', '%20')}"
                        
                        st')}"
                        
                        st.success}"
                        
                        st.success(f"✅}"
                        
                        st.success(f"✅}"
                        
                        st.success(f"✅.success(f"✅ Pesanan berhasil(f"✅ Pesanan berhasil Pesanan berhasil dikirim!")
                        st.balloons()
                        st.mark Pesanan berhasil dikirim!")
                        Pesanan berhasil dikirim!")
                        st.balloons()
                        st.mark dikirim!")
                        st.balloons dikirim!")
                        st.balloonsdown(f"📱 [K st.balloons()
                        st.markdown(f"📱 [Klikdown(f"📱 [Klik()
                        st.markdown(f"📱 [Klik di sini untuk()
                        st.markdown(f"lik di sini untuk chat di sini untuk chat via WhatsApp]( di sini untuk chat via WhatsApp]( chat via WhatsApp]({wa_link})📱 [Klik di sini untuk chat via WhatsApp]({wa_link}) via WhatsApp]({wa_link}){wa_link})")
                        
                        st{wa_link})")
                        
                        st.session_state.keranjang")
                        
                        st.session_state.keranjang = []
                        st")
                        
                        st.session_state.ker")
                        
                        st.session_state.ker.session_state.keranjang = []
 = []
                        st.session_state.n.session_state.nama_pemanjang = []
                        st.session_state.nama_pemesan = ""
                       anjang = []
                        st.session_state.nama_pemesan = ""
                                               st.session_state.nama_pemesan = ""
                        st.session_state.kama_pemesan = ""
                       esan = ""
                        st.session_state.k st.session_state.kelas = ""
 st.session_state.kelas = ""
                       elas = ""
                        st.session_state.no st.session_state.kelas = ""
                       elas = ""
                        st.session_state.no                        st.session_state.no_hp st.session_state.no_hp =_hp = ""
                        
                        st st.session_state.no_hp = ""
                        
                        st.rerun()
_hp = ""
                        
                        st = ""
                        
                        st.r ""
                        
                        st.rerun()
.rerun()
                    except Exception as                    except Exception as e:
                        st.rerun()
                    except Exception as e:
                        st.error(f"erun()
                    except Exception as e:
                        st.error(f"                    except Exception as e:
                        st.error(f"❌ Error: { e:
                        st.error(f".error(f"❌ Error: {❌ Error: {e}")

st❌ Error: {e}")

ste}")

st❌ Error: {e}")

st.markdown("""
<div class="e}")

st.markdown("".markdown("""
<div class=".markdown("""
<div class="footer">
    Social 9D
.markdown("""
<div class="footer">
    Social 9D
</div>
footer">
    Social 9D
"
<div class="footer">
    Socialfooter">
    Social 9D
</div>
""", unsafe_allow""", unsafe_allow_html=True</div>
""", unsafe_allow 9D
</div>
""", unsafe_allow_html=True)
