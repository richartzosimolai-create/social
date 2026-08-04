# ========================================
# ===== HALAMAN PRODUK =====
# ========================================
if st.session_state.halaman == "produk":

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
                st.rerun()

    # ===== TOMBOL KERANJANG (BENTUK BARU, FUNGSI TETAP) =====
    total_item = len(st.session_state.keranjang)

    st.markdown(f"""
    <style>
        .floating-cart {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 999;
            background: #ee4d2d;
            color: white;
            border: none;
            border-radius: 50px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 600;
            box-shadow: 0 4px 20px rgba(238, 77, 45, 0.4);
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .floating-cart:hover {{
            transform: scale(1.05);
            box-shadow: 0 6px 30px rgba(238, 77, 45, 0.6);
        }}
        .floating-cart .badge {{
            background: white;
            color: #ee4d2d;
            border-radius: 50%;
            padding: 0px 12px;
            font-size: 14px;
            font-weight: 700;
        }}
    </style>
    <div class="floating-cart" onclick="st.session_state.halaman = 'keranjang'; st.rerun();">
        🛒 Keranjang
        <span class="badge">{total_item}</span>
    </div>
    """, unsafe_allow_html=True)
