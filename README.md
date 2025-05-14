install packages:
or
pipenv shell
pipenv install

Start the FastAPI server using Uvicorn:
uvicorn main:app --reload

Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Trigger test:
http://127.0.0.1:8000/testpublicformulrs

view result:
file:///<DIRECTORY>/publicformauiautomation/main.html

-- NEW README CONTENT --

# UI Automation Via AI Agents

This project provides an end-to-end automation testing and reporting solution for Birdeye repositories (UI-web-2.0, public-forms, etc.) using Browser-Use, FastAPI and HTML/JS frontend.

---

## 📁 Project Structure

```
publicformauiautomation/
├── main.py                # FastAPI backend (serves API and static files)
├── outputs/               # Automation result JSON files
├── publicFormScripts/     # Directory of automation scripts (based on repo)
│   ├── __init__.py
│   ├── checkin.py
│   ├── dlc.py
│   └── ... (other scripts)
└── static/                # Frontend files
    ├── main.html
    ├── script.js
```

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```sh
git clone <repo-url>
cd publicformauiautomation
```

### 2. **Set Up Python Environment**

- **With pyenv (recommended):**
  ```sh
  pyenv install 3.11.0
  pyenv local 3.11.0
  ```

- **With pipenv:**
  ```sh
  pip install pipenv
  pipenv install
  pipenv shell
  ```

### 3. **Install Dependencies**

```sh
pip install -r requirements.txt
# or, if using pipenv:
pipenv install
```

### 4. **Set Up Environment Variables**

- Copy `.env.example` to `.env` and fill in your API keys (e.g., `GOOGLE_API_KEY`).

---

## 🏁 Running the App

### **Start the FastAPI Server**

You can use the provided shell script for convenience:

```sh
pipenv run start
```

---

## 🌐 Accessing the Frontend

- Open your browser and go to:  
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

  This serves the `main.html` UI and all static assets directly from FastAPI.

---

## 🧑‍💻 Usage

- **Run Automation:**  
  Use the "Run Automation" tab to select and trigger any automation script.

- **View Results:**  
  Switch to the "Results" tab to see the latest automation results in a table.

- **API Endpoint Examples:**
  - `POST /run-dlc` — Run DLC automation
  - `POST /run-reviewus` — Run Review Us automation
  - `POST /run-checkin` — Run Checkin automation
  - `GET /getAutomationResult` — Get latest results
  - `GET /testpublicformulrs` — Run all automations and save results

- **API Docs:**  
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Development Notes

- All automation scripts must be in their respective repo directory eg. `publicFormScripts/` and `uiWebTwoPointOScripts/` 
- Static files (`main.html`, `script.js`) are served from the `/static` route.
- Results are saved in the `outputs/` directory.

---

## 📄 License

MIT