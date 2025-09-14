# 📘 blog_api

A modular FastAPI backend with JWT authentication, SQLite integration, and secure deployment via Render. Built for clarity, scalability, and future-proofing in a volatile tech landscape.

---

## 📦 Features

- 🔐 JWT-based authentication with OAuth2 and password hashing  
- 🧩 Modular routing and repository pattern  
- 🗃️ SQLite database with SQLAlchemy ORM  
- ✅ Pydantic v2 validation and schema management  
- 🌐 Secure deployment via Render with environment variables  
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
└── main.py
```

---

## ⚙️ Environment Variables

Create a `.env` file locally (excluded from version control) or set these securely in Render:

```env
SQLALCHEMY_DATABASE_URL=sqlite:///./blog.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
PORT=8000
```

✅ `.env` is excluded via `.gitignore`

---

## 🧪 Local Development

```bash
# Create virtual environment
python -m venv fastapi-env

# Activate environment
fastapi-env\Scripts\activate  # Windows
source fastapi-env/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
fastapi run app/main.py --host 0.0.0.0 --port 8000
```

Access Swagger UI at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🚀 Deployment (Render)

To deploy this API on [Render](https://render.com):

1. **Push your code to GitHub**

2. **Create a Web Service on Render**
   - Connect your GitHub repo
   - Set the **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - Set the **Start Command**:
     ```bash
     fastapi run app/main.py --host 0.0.0.0 --port $PORT
     ```

3. **Set Environment Variables** in the dashboard:
   - `SQLALCHEMY_DATABASE_URL`
   - `SECRET_KEY`
   - `ALGORITHM`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`
   - `PORT`

4. **Access Your API**  
   Once deployed, visit:
   ```
   https://your-app-name.onrender.com/docs
   ```

---



