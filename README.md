<p align="center">
  <img src="https://raw.githubusercontent.com/HitDrama/AI-Chatbot-Flask/main/static/imgs/poster.png" alt="Poster Chatbot AI" width="880">
</p>

<h1 align="center">🤖 Chatbot AI với Gemini API - Dự án Flask Cá Nhân Hóa</h1>

---

## 🚀 Công nghệ sử dụng

- 🐍 Python (Flask)
- 🧠 Gemini 2.0 Flash API (Google Generative Language)
- 💾 MySQL + SQLAlchemy
- 🎨 Bootstrap 5 + Boxicons
- 📜 Markdown & Highlight code
- 🔁 Streaming dữ liệu real-time
- ☁️ Triển khai cục bộ & dễ dàng mở rộng

---

## ⚙️ Cách chạy dự án

```bash
# Cài đặt các thư viện cần thiết
pip install -r requirements.txt

# Khởi động dự án
python run.py
```
---
## 📂 Cấu hình trong config.py
```python
class Config:
    SECRET_KEY = 'uytrdcvg654z23456ygf'
    GOOGLE_API_KEY = 'KEY_YOU_GET_FROM_GOOGLE'
    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/chatgemini"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
```
---
## 🎬 Demo


<p align="center">
  <a href="https://drive.google.com/drive/u/5/folders/1i3of4oT7HQpjEzJ-yGH3thphVVo0adVp" target="_blank">
    <img src="https://github.com/HitDrama/AI-Chatbot-Flask/blob/main/static/imgs/home.png"
         alt="Xem Video Demo"
         width="600"
         style="border: 3px solid #58a6ff; border-radius: 12px;">
  </a>
</p>

<p align="center"><em>👉 Click vào ảnh để xem video demo trên Google Drive</em></p>

---
## 👨‍💻 Người phát triển

- Đặng Tô Nhân
