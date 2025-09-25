# 📊 Personal Finance Tracker

A simple yet powerful **web-based personal finance tracker** built with **Flask** and **Matplotlib**.  
Track income and expenses, view balances, and analyze your spending habits with interactive charts.  

---

## 🚀 Features
- Add income & expenses with categories and descriptions  
- View transaction history and current balance  
- Category-based spending summary (pie chart)  
- Data persistence with CSV (easy to migrate to SQL later)  
- Clean **Flask web interface** (Bootstrap)  
- Interactive **Matplotlib visualizations**  

---

## ⚙️ Project Structure
finance_tracker/
├── app.py              # Flask app (routes, views, charts)
├── tracker.py          # Core logic (Transaction & FinanceTracker classes)
├── templates/          # HTML templates (Jinja2 + Bootstrap)
│   ├── base.html       # Base template
│   ├── index.html      # Dashboard
│   ├── add.html        # Add transaction form
│   └── summary.html    # Summary & chart
├── static/             # Static files (charts, CSS)
│   └── chart.png       # Matplotlib chart (generated dynamically)
├── transactions.csv    # Data storage
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

### 🛠️ Tech Stack
- Backend: Flask (Python)
- Frontend: HTML, Bootstrap (via Jinja templates)
- Data Storage: CSV (easy upgrade path to SQLite/PostgreSQL)
- Visualization: Matplotlib

---

##📌 Future Improvements
- Add user authentication (login system)
- Switch storage from CSV → SQLite database
- Add line charts for balance over time
- Export reports as PDF/Excel
- Deploy live demo

---

##👩🏾‍💻 Author
- Name: Jessica O'Bonna
- LinkedIn: https://www.linkedin.com/in/jessica-obonna


