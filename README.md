# Vue + Flask Blog

A modern, fully decoupled personal blog system powered by **Vue 3** (frontend) and **Flask** (backend).  
- Only the site owner can publish articles (via a simple `/admin` editor)  
- Visitors can browse articles in a clean interface  
- Markdown is supported for article content rendering

---

## 🗂 Project Structure

```
myBlog/
├── backend/    ← Flask backend API
├── frontend/   ← Vue 3 frontend SPA
```

---

## 🚀 Getting Started (Local)

### 🧱 1. Backend (Flask)

```bash
cd backend
python -m venv venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.\env\Scripts\Activate.ps1   # or `source venv/bin/activate` on macOS/Linux

pip install -r requirements.txt

# Initialize the database
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()

# Start the server
python run.py
```

This will start the Flask backend at:  
👉 `http://localhost:5000`

---

### 🌐 2. Frontend (Vue 3)

```bash
cd frontend
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
npm install
npm run serve
```

This will start the Vue frontend at:  
👉 `http://localhost:8080`

---

## 📖 Features

- ✅ Article browsing on `/`
- ✅ Article details on `/post/:id`
- ✅ Admin editor at `/admin` for writing posts
- ✅ Full Markdown rendering support
- ✅ API endpoints:
  - `GET /api/posts`
  - `GET /api/post/<id>`
  - `POST /api/post`

---

## 📝 Notes

- The backend currently has no authentication — only the owner should access `/admin`
- Future improvement: add token-based authentication to protect publishing
- You can deploy this project using:
  - **Flask backend** → AWS EC2 / Render / Railway
  - **Vue frontend** → AWS S3 + CloudFront / Netlify / Vercel

---

## 📷 Screenshots (optional)

_Add screenshots here later if you want to show UI previews._

---

## 👨‍💻 Author

Developed by [@ybenzou](https://github.com/ybenzou)  
MIT License.
