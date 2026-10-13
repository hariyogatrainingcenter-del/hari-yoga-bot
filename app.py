from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Batthari Hari - Yoga Master</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { 
                font-family: Arial; 
                text-align: center; 
                background: linear-gradient(to right, #ff9a00, #ff6a00);
                color: white;
                padding: 30px;
            }
            .card {
                background: white;
                color: #333;
                padding: 30px;
                border-radius: 20px;
                max-width: 500px;
                margin: auto;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 { color: #ff6a00; }
            .btn {
                background: #ff6a00;
                color: white;
                padding: 12px 25px;
                border: none;
                border-radius: 25px;
                font-size: 18px;
                margin-top: 20px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🧘 Batthari Hari 👑</h1>
            <h2>World Yoga Founder</h2>
            <p>Welcome to My Official Yoga Website!</p>
            <p>🔥 LIVE Successfully on Render 🔥</p>
            <p>⚡ Energy Mode: ON ⚡</p>
            <button class="btn" onclick="alert('Hari Blessing You! 🙏')">Get Blessing</button>
            <p style="margin-top:20px;">© 2026 Batthari Hari</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
