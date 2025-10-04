will need microsoft c++ build tools download from here "https://visualstudio.microsoft.com/visual-cpp-build-tools/"
> ⚡ Navigate to project subfolder - `cd Nasa-Biology-Engine--main`
> ⚡ Navigate to subfolder Bioverse - `cd Bioverse`
> ⚡ Run `pip install -r backend/requirements.txt` before starting.

---

## 🧰 Run Server

```bash
cd backend
uvicorn app.main:app --reload
```

Visit **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** for Swagger UI 🚀

Try:

* `/search?q=plant`
* `/recommend?q=gravity`
* `/describe?q=bone`

---
