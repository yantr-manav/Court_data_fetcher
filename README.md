# 🏛️ Court-Data Fetcher & Mini-Dashboard

A lightweight web application that allows users to fetch Indian court case metadata and latest orders/judgments using basic details like **Case Type**, **Case Number**, and **Filing Year**. Designed to simplify the search process and offer a clean dashboard interface.

---

## ⚖️ Court Targeted
**[Add Court Name]**

> Example options:
- Delhi High Court — https://delhihighcourt.nic.in/
- Any District Court (via eCourts portal) — e.g., https://districts.ecourts.gov.in/

---

## 🚀 Features

- ✅ Fetch metadata and order details for Indian court cases
- 🔎 Search using Case Type, Case Number, and Filing Year
- 📄 Display latest judgment/order in an organized dashboard
- 🧠 CAPTCHA-aware scraping mechanism (strategy explained below)
- 💾 Store case data in SQLite/PostgreSQL
- 📥 Download judgment/order PDFs (if available)
- 🔐 Secure configuration via `.env`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/court-data-fetcher.git
cd court-data-fetcher
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Environment

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

> You may need to set up the `.env` file as shown below before the first run.

---

## 🔐 Sample `.env` File

```env
# SQLite DB configuration
DATABASE_URL=sqlite:///court_data.db

# PostgreSQL Example (optional)
# DATABASE_URL=postgresql://username:password@localhost:5432/court_db
```

Make sure to **never commit your `.env`** file. Add it to `.gitignore`.

---

## 🤖 CAPTCHA Handling Strategy

CAPTCHAs on court websites can block automated access. Here's how to handle them:

### ✅ If CAPTCHA is simple (image-based):
- Use **manual intervention** by opening the page in a browser (e.g., Selenium) and solving the CAPTCHA manually once.
- Store session cookies or use the same session for repeated requests.

### ✅ If CAPTCHA is complex (dynamic or JS-based):
- Use **browser automation with Selenium** and **human-in-the-loop** solving.
- For scale, integrate a CAPTCHA-solving service like:
  - [2Captcha](https://2captcha.com/)
  - [Anti-Captcha](https://anti-captcha.com/)
- Some courts allow initial HTML scraping for metadata without hitting CAPTCHA walls. In that case, we avoid scraping PDFs or use `HEAD` requests to validate before full fetch.

---

## 🧪 Example Use Case

1. User opens the dashboard
2. Enters:
   - Case Type: `CRL.A.`
   - Case Number: `1234`
   - Year: `2023`
3. Clicks “Search”
4. App scrapes the official court site
5. Metadata is shown:
   - Petitioner, Respondent, Last Hearing Date, Status
6. If available, download the PDF of the judgment/order.

---

## 📹 Demo Video

[🔗 Add your Loom/YouTube demo link here]

---

## 🧱 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap / React (optional for dashboard)
- **Scraping**: `requests`, `BeautifulSoup4`, `Selenium` (if needed)
- **Database**: SQLite (default), PostgreSQL (optional)
- **Security**: `python-dotenv` for config, `.gitignore` for secrets

---

## 📁 Folder Structure

```
court-data-fetcher/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── scraper/
│   ├── fetcher.py
│   └── parser.py
├── database/
│   └── models.py
├── .env
├── .gitignore
└── README.md
```

---

## ✅ To-Do (Optional Enhancements)

- [ ] Add session caching to reduce redundant requests
- [ ] Build case history timeline view
- [ ] Multi-court support via dropdown
- [ ] Add notifications or alerts when order is updated
- [ ] Export dashboard data to CSV/PDF

---

## 👨‍⚖️ Legal Disclaimer

This tool is built for **educational and productivity enhancement** purposes. Ensure compliance with court website usage policies. Web scraping of court data must respect robots.txt and legal boundaries.