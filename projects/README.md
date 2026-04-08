# 💼 AI Job Intelligence Platform

## 🚀 Overview

AI-powered backend system that collects, stores, and serves job listings through APIs.
Now includes a rule-based recommendation engine for ranking job listings.

This project simulates a real-world data pipeline:

* Scraping → Database → API → Client

---

## ⚙️ Features

### 🔍 Job Data Collection

* Web scraping using `requests` + `BeautifulSoup`
* Multi-page scraping support
* Clean extraction of:

  * Title
  * Company
  * Location
  * Link

### 🗄️ Database

* SQLite database
* Structured schema
* Duplicate prevention using `UNIQUE` constraint

### ⚡ API (FastAPI)

* `GET /jobs` → Paginated job listings
* `GET /jobs/search?keyword=` → Search by job title
* `GET /jobs/location?location=` → Filter by location

### 📄 Pagination

* Efficient data loading using:

  * `limit`
  * `offset`

---

## 🧠 Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy (basic usage)
* BeautifulSoup (scraping)
* Docker (planned)

---

## 📂 Project Structure

```
project/
│── api/
│── database/
│── scraper/
│── main.py
│── database.db
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run API

```
uvicorn main:app --reload
```

### 3. Access API

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Future Improvements

* Add filtering (salary, role)
* Add caching (Redis)
* Deploy on cloud (Render / AWS)
* Add AI features (job recommendations, RAG)

---

## 📌 Learning Goals

* Backend engineering fundamentals
* API design
* Data pipeline building
* Real-world system thinking

---
