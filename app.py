from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Portfolio data
portfolio_data = {
    'name': 'นางสาว พุทธิกานต์ ส้มเพชร์',
    'email': 'aputthikarnsomphet@gmail.com',
    'phone': '0834389242',
    'school': 'โรงเรียนกงไกรลาศวิทยา',
    'class': 'ม.6/2',
    'student_id': 17,
    'github': 'https://github.com/aputthikarnsomphet-coder',
    'projects': [
        {
            'id': 1,
            'title': 'Portfolio Website',
            'description': 'เว็บไซต์พอร์ตโฟลิโอส่วนตัวสำหรับแสดงผลงานและข้อมูล',
            'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript'],
            'link': '#',
            'status': 'กำลังดำเนินการ'
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    try:
        data = request.json
        # ที่นี่คุณสามารถเพิ่มการส่งอีเมลหรือบันทึกข้อมูล
        return jsonify({
            'status': 'success',
            'message': 'ขอบคุณสำหรับการติดต่อ! เราจะติดต่อคุณเร็ว ๆ นี้'
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
