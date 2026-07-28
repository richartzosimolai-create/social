from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

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

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toko Saya</title>
    <style>
        /* ===== CSS LENGKAP ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: #f5f5f5;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
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
        
        /* ALERT */
        .alert {
            padding: 15px 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            font-weight: 600;
        }
        
        .alert-success {
            background: #e8f5e9;
            color: #2e7d32;
            border-left: 5px solid #4caf50;
        }
        
        .alert-error {
            background: #ffebee;
            color: #c62828;
            border-left: 5px solid #ef5350;
        }
        
        /* GRID */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }
        
        /* CARD */
        .product-card {
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: center;
        }
        
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        
        .product-card .gambar {
            width: 100%;
            height: 200px;
            background: #f7f7f7;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
            margin-bottom: 15px;
        }
        
        .product-card h3 {
            font-size: 18px;
            color: #1a1a1a;
            margin-bottom: 5px;
        }
        
        .product-card .harga {
            font-size: 24px;
            font-weight: 700;
            color: #ee4d2d;
            margin-bottom: 15px;
        }
        
        /* FORM */
        .form-beli {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .form-beli input {
            padding: 10px 14px;
            border: 2px solid #e8e8e8;
            border-radius: 10px;
            font-size: 14px;
            outline: none;
            transition: border 0.2s;
        }
        
        .form-beli input:focus {
            border-color: #ee4d2d;
        }
        
        .form-beli input[type="number"] {
            width: 70px;
            margin: 0 auto;
            text-align: center;
        }
        
        .form-beli button {
            background: #ee4d2d;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .form-beli button:hover {
            background: #d43b1f;
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
</head>
<body>
    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <h1>🛍️ <span>Toko</span> Saya</h1>
            <div class="badge">6 Produk</div>
        </div>
        
        <!-- PESAN -->
        {% if pesan %}
            <div class="alert alert-{{ 'success' if sukses else 'error' }}">
                {{ pesan }}
            </div>
        {% endif %}
        
        <!-- PRODUK -->
        <div class="product-grid">
            {% for p in produk %}
            <div class="product-card">
                <div class="gambar">
                    {% if p.id == 1 %}👕
                    {% elif p.id == 2 %}🧥
                    {% elif p.id == 3 %}👖
                    {% elif p.id == 4 %}👟
                    {% elif p.id == 5 %}🎒
                    {% else %}⌚
                    {% endif %}
                </div>
                <h3>{{ p.nama }}</h3>
                <p class="harga">Rp{{ "{:,.0f}".format(p.harga).replace(',', '.') }}</p>
                
                <form action="/beli" method="POST" class="form-beli">
                    <input type="hidden" name="produk_id" value="{{ p.id }}">
                    <input type="text" name="nama" placeholder="Nama kamu" required>
                    <input type="number" name="jumlah" value="1" min="1" max="10">
                    <button type="submit">🛒 Beli Sekarang</button>
                </form>
            </div>
            {% endfor %}
        </div>
        
        <div class="footer">
            © 2026 Toko Saya - Tugas Sekolah
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, produk=produk, pesan=None, sukses=None)

@app.route('/beli', methods=['POST'])
def beli():
    nama = request.form.get('nama', '').strip()
    produk_id = int(request.form.get('produk_id', 0))
    jumlah = int(request.form.get('jumlah', 1))
    
    p = next((item for item in produk if item['id'] == produk_id), None)
    if not p:
        return render_template_string(HTML, produk=produk, pesan="Produk tidak ditemukan!", sukses=False)
    
    total = p['harga'] * jumlah
    
    # Kirim Telegram
    pesan_tele = f"🛍️ ORDER BARU!\n👤 Nama: {nama}\n📦 Produk: {p['nama']}\n💰 Harga: Rp{p['harga']:,}\n🔢 Jumlah: {jumlah}\n💳 Total: Rp{total:,}"
    
   {p['harga']:,}\n🔢 Jumlah: {jumlah}\n💳 Total: Rp{total:,}"
    
    try:
        url = f"https try:
        url = f"https://api.telegram.org/bot://api.telegram.org/bot{TOKEN}/sendMessage"
       {TOKEN}/sendMessage"
        requests.post(url, data={"chat_id requests.post(url, data={"chat_id": CHAT_ID, "text":": CHAT_ID, "text": pesan_tele}, timeout=10)
        return render_template_string(HTML pesan_tele}, timeout=10)
        return render_template_string(HTML, produk=produ, produk=produk, pesank, pesan=f"✅ Ter=f"✅ Terima kasih {ima kasih {nama}! Order bernama}! Order berhasil!", sukshasil!", sukses=Truees=True)
    except:
        return)
    except:
        return render_template_string render_template_string(HTML, produk=produk, pesan="❌(HTML, produk=produk, pesan="❌ Gagal kirim notif!", sukses Gagal kirim notif!", sukses=False)

if __name=False)

if __name__ == '__main__':
    app.run__ == '__main__':
    app.run(debug=True)
