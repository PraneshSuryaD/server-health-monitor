# 🚀 Server Health Monitoring 

A **FastAPI-based application** that monitors CPU, Memory, and Disk usage and displays them in a real-time dashboard using HTML, CSS, and JavaScript.

---

## ✅ Features
- Real-time server health metrics (CPU, Memory, Disk)
- Simple and clean dashboard interface
- FastAPI backend with REST API endpoint
- Easy to extend and customize

---

## 🛠 Tech Stack
- **Backend:** Python (FastAPI), Psutil
- **Frontend:** HTML, CSS, JavaScript
- **Other Tools:** Uvicorn, Git, Virtual Environment (venv)

---

## ⚡ How to Run Locally

### 1. **Clone the repository**
```bash
git clone https://github.com/PraneshSuryaD/server-health-monitor.git
cd server-health-monitor
```

### 2. **Create and activate a virtual environment**
```bash
# Create venv
python -m venv venv

# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Run the FastAPI server**
```bash
uvicorn server:app --reload
```

### 5. **Open the dashboard**
Simply open `dashboard.html` in your browser.  
It will fetch data from the FastAPI endpoint (`http://127.0.0.1:8000/status`) and display it in real time.

---

## ✅ Future Improvements
- Add user authentication
- Implement historical charts with database storage
- Dark mode UI
- Dockerize the application
- Multi-server monitoring feature

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push the branch and create a Pull Request

---

## 📜 License
This project is licensed under the **MIT License**.

---

🔥 Made with ❤️ using **FastAPI** and **JavaScript**
