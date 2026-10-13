from flask import Flask, jsonify, render_template_string
app = Flask(__name__)
HTML = "<h1 style='text-align:center;color:#EA580C'>Hari Yoga Bot Live! 🕉️</h1><p style='text-align:center'>Bot Running ✅</p>"
@app.route('/')
def home():
    return render_template_string(HTML)
@app.route('/api/info')
def info():
    return jsonify({"bot":"hari-yoga-bot","status":"active"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
