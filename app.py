from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>Hari Yoga</title></head>
    <body style='font-family:sans-serif;text-align:center;padding-top:60px'>
        <h1 style='color:#EA580C;font-size:32px'>Hari Yoga Training Center</h1>
        <h2 style='color:green'>✅ Yoga Bot Working Successfully!</h2>
        <p>Welcome to Hari Yoga - Your website is now LIVE</p>
        <br>
        <a href='/api/info' style='background:#EA580C;color:white;padding:10px 20px;text-decoration:none;border-radius:5px'>Check API</a>
    </body>
    </html>
    """

@app.route('/api/info')
def info():
    return jsonify({"name": "hari-yoga-bot", "status": "ok", "message": "Working"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
