# 🔎 Khoj — The Search Engine

A high-performance fuzzy search engine built from scratch using **N-Gram indexing + RapidFuzz ranking**, designed to deliver fast and typo-tolerant search results over real-world datasets.

---

## 🚀 Live Demo

- 🌐 Frontend (Streamlit): _[Add your Streamlit URL here]_
- ⚙️ Backend (FastAPI): _[Add your Render URL here]_

---

## 🧠 Overview

Khoj is a **custom-built fuzzy search system** that replicates how modern search engines handle:

- Typo tolerance (`ptathao → pathao`)
- Fast candidate retrieval
- Intelligent ranking
- Real-world noisy data (Bangla + English)

Unlike simple CRUD-based apps, this project focuses on **core computer science concepts** such as:

- Information Retrieval
- String Matching Algorithms
- Ranking Systems
- Indexing Optimization

---

## ❗ Problem Statement

Traditional search systems rely on exact string matching, which fails when:

- Users make typos
- Data contains inconsistencies
- Multiple languages are present

This leads to:

- Poor user experience
- Irrelevant results
- Missed matches

---

## 💡 Solution

Khoj solves this by implementing:

1. **N-Gram Indexing**
   - Breaks text into character-level chunks
   - Enables fast candidate retrieval

2. **Fuzzy Matching (RapidFuzz)**
   - Handles typos and approximate matches

3. **Custom Ranking System**
   - Combines:
     - Text similarity
     - Prefix matching
     - Popularity (rating + reviews)

---

## ⚙️ System Architecture

```text
User Query
    ↓
N-Gram Candidate Retrieval
    ↓
Fuzzy Matching (RapidFuzz)
    ↓
Ranking Engine
    ↓
Top Results
```

---

## 🧩 Tech Stack

### Backend

- FastAPI
- Uvicorn
- Pandas
- RapidFuzz

### Frontend

- Streamlit

### Deployment

- Render (Backend)
- Streamlit Cloud (Frontend)

### Containerization

- Docker
- Docker Compose (optional)

---

## 📁 Project Structure

```text
Khoj_The_Search/
│
├── Api/                      # FastAPI backend
│   └── main.py
│
├── search_engine/            # Core search logic
│   ├── load_data.py
│   ├── ngram.py
│   ├── indexer.py
│   ├── search_candidates.py
│   ├── ranking.py
│   └── search.py
│
├── frontend/
│   └── app.py               # Streamlit UI
│
├── dataset/
│   └── khoj_restaurants.csv
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml (optional)
├── requirements.txt
└── README.md
```

---

## 🔍 Key Features

- ⚡ Fast in-memory search (10k+ records)
- 🧠 Typo-tolerant matching
- 🌍 Multi-language support (Bangla + English)
- 📊 Intelligent ranking system
- 🔌 API-based architecture
- 🐳 Dockerized backend & frontend

---

## 🧪 Example Queries

| Input        | Output        |
| ------------ | ------------- |
| `ptathao`    | Pathao        |
| `kacci bhai` | Kacchi Bhai   |
| `biriyani`   | Biryani shops |

---

## 🛠️ Local Setup

### 1. Clone repository

```bash
git clone https://github.com/your-username/Khoj-The-Search.git
cd Khoj-The-Search
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run backend

```bash
uvicorn Api.main:app --reload
```

---

### 5. Run frontend

```bash
streamlit run frontend/app.py
```

---

## 🐳 Docker Setup

### Build backend

```bash
docker build -f Dockerfile.backend -t khoj-backend .
```

### Run backend

```bash
docker run -p 8000:8000 khoj-backend
```

---

### Build frontend

```bash
docker build -f Dockerfile.frontend -t khoj-frontend .
```

### Run frontend

```bash
docker run -p 8501:8501 khoj-frontend
```

---

## 🔐 Environment Variables

Frontend uses:

```text
API_URL = <backend_url>/search
```

Examples:

- Local: `http://localhost:8000/search`
- Docker: `http://host.docker.internal:8000/search`
- Production: `https://your-app.onrender.com/search`

---

## 📈 Future Improvements

- Redis-based indexing
- Elasticsearch integration
- Query autocomplete
- Personalized ranking
- Location-aware results
- ML-based ranking model

---

## 🏢 Industry Relevance

This project demonstrates:

- Backend API design
- Search system engineering
- Real-world data handling
- Scalable architecture thinking
- Deployment & containerization

---

## 👨‍💻 Author

**Abdullah Al Maruf**
CSE, RUET

---

## 📜 License

This project is for Industrial Attachment at Pathao purposes.
