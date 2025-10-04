will need microsoft c++ build tools download from here "https://visualstudio.microsoft.com/visual-cpp-build-tools/"
> ⚡ Navigate to project subfolder - `cd Nasa-Biology-Engine--main`
> ⚡ Navigate to subfolder Bioverse - `cd Bioverse`
> ⚡ Run `pip install -r backend/requirements.txt` before starting.

---

## 🧰 Run Server

```bash(for local system)
cd backend
uvicorn app.main:app --reload
```
```for network accessed server
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Visit **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** for Swagger UI 🚀 on local system

visit **[http://YOUR_IP:8000/docs] (replace YOUR_IP with your server's IP address)** for Swagger UI 🚀 on any system

Try:

* `/search?q=plant`
* `/recommend?q=gravity`
* `/describe?q=bone`

---
