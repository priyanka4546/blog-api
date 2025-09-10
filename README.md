# 🚀 FASTAPI_TUT

A modular FastAPI backend with JWT authentication, SQLite integration, and secure deployment via Vercel. Built for clarity, scalability, and future-proofing in a volatile tech landscape.

---

## 📦 Features

- 🔐 JWT-based authentication with OAuth2 and password hashing
- 🧩 Modular routing and repository pattern
- 🗃️ SQLite database with SQLAlchemy ORM
- ✅ Pydantic v2 validation and schema management
- 🌐 Secure deployment via Vercel with environment variables
- 📁 Clean project structure for maintainability

---

## 🧱 Project Structure

```
app/
├── blog/
│   ├── repository/
│   │   ├── blog.py
│   │   └── user.py
│   ├── routers/
│   │   ├── authentication.py
│   │   ├── user.py
│   │   └── blog.py
│   ├── database.py
│   ├── hashing.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   ├── token.py
├── blog.db
├── main.py
├── requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file locally (excluded from version control) or set these securely in Vercel:

```env
SQLALCHEMY_DATABASE_URL=sqlite:///./blog.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ✅ `.env` is excluded via `.gitignore`  

---

## 🧪 Local Development

```bash
# Create virtual environment
python -m venv fastapi-env
fastapi-env\Scripts\activate #Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

---

## 🚀 Deployment (Vercel)

1. Push your code to GitHub
2. Link the repo in Vercel dashboard
3. Set environment variables in Vercel:
   - `SQLALCHEMY_DATABASE_URL`
   - `SECRET_KEY`
   - `ALGORITHM`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`
4. Deploy

---



