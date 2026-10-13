
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Batthari Hari - World's First AI Voice Battery Lab</title>
<style>
body{margin:0;font-family:Arial;background:#061a3a;color:#fff}
.top{background:#061a3a;padding:15px;text-align:center}
.gold{background:linear-gradient(90deg,#ffdd57,#c8a000);color:#000;padding:8px;font-weight:bold;border-radius:8px;margin:10px}
.grid5{display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr;gap:5px;margin:10px}
.iconbox{background:#eaf2ff;color:#0a1931;padding:8px;border-radius:10px;font-size:10px;font-weight:bold}
.pricebox{background:#0a1931;border:1px solid gold;padding:10px;border-radius:10px;margin:5px;font-size:12px}
.combo{background:#00c853;padding:12px;border-radius:10px;margin:5px;font-weight:bold}
.bottom{background:#051536;padding:20px;text-align:center;border-top:3px solid gold}
.btn{background:#ffdd57;color:#000;padding:15px 20px;display:block;margin:15px;border-radius:30px;text-decoration:none;font-weight:bold;font-size:18px}
</style></head><body>

<div class="top">
<div class="gold">⚡ WORLD'S FIRST AI Voice Battery Lab ⚡</div>
<h1 style="color:#ffdd57;font-size:34px;margin:5px">Batthari Hari</h1>
<p style="font-size:12px;color:#7fb3ff">AI • Voice • Batteries • Multilingual - Serving You in Your Native Language</p>
<div style="background:#1976d2;display:inline-block;padding:5px 15px;border-radius:20px;font-size:12px">🔋 ALL BATTERY TYPES</div>

<div class="grid5">
<div class="iconbox">🔋<br>Inverter</div>
<div class="iconbox">🚗<br>EV Battery</div>
<div class="iconbox">☀️<br>Solar</div>
<div class="iconbox">🚙<br>Auto</div>
<div class="iconbox">🏍️<br>Bike</div>
</div>

<div style="background:#fff;color:#000;padding:10px;border-radius:10px;margin:10px;text-align:left;font-size:11px">
<b>🌐 ALL WORLD LANGUAGES:</b><br>
Tamil - தமிழ் | Telugu - తెలుగు | Hindi - हिंदी | Punjabi | Malayalam | Bengali | Marathi | Chinese - 中文 | Kannada | Gujarati | Japanese
</div>

<div style="padding:10px">
<div class="pricebox"><b>Lifetime Gold Rs.99</b><br>Lifelong Access to AI Voice & Text</div>
<div class="pricebox"><b>Live 3 Hours Rs.99</b><br>3 Hours Live Voice Support</div>
<div class="combo">MEGA COMBO Rs.150 - SAVE Rs.48<br><small>Lifetime + Live 3 Hours</small></div>
<p style="font-size:10px">PayTM: 8610121365@ptyes | Bank: Harikrishnan K<br>A/C: 11073649754 IFSC: SBIN0000267</p>
</div>
</div>

<div class="bottom">
<h2 style="color:#ffdd57">Founder Hari 👑</h2>
<p style="color:#7fb3ff">Founder & CEO - Batthari Hari</p>
<p style="font-size:16px;margin:15px 0">📞 7418344556 • 8610121365</p>
<p style="font-size:13px">Leading India's first AI voice battery lab,<br>providing multilingual AI solutions pan-India.</p>
<a class="btn" href="https://wa.me/918610121365">Contact Founder - WhatsApp Now</a>
<p style="font-size:11px;color:#aaa;margin-top:20px">Trusted • 24/7 Support • Pan-India Service<br>support@battharihari.in • +91 8610121365</p>
<p style="font-size:9px;color:#666">© 2026 Batthari Hari - MSME Registered 5 Years</p>
</div>

</body></html>
    """

if __name__ == '__main__':
    app.run()
