from flask import Flask, render_template, jsonify
import psutil
import platform
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": memory.percent,
        "memory_used": f"{memory.used // (1024**3)}GB",
        "memory_total": f"{memory.total // (1024**3)}GB",
        "disk_percent": disk.percent,
        "disk_used": f"{disk.used // (1024**3)}GB",
        "disk_total": f"{disk.total // (1024**3)}GB",
        "platform": platform.system(),
        "python_version": platform.python_version(),
        "uptime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "hostname": platform.node()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "app": "Flask DevOps Dashboard",
        "version": "2.0",
        "timestamp": str(datetime.datetime.now())
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)