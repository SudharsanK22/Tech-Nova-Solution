# 🚀 TechNova Solutions

## Project Overview
TechNova Solutions is a modern **full-stack web application** designed with premium UI aesthetics and a powerful **Python backend**. The project demonstrates a clean architecture with a responsive frontend and high-performance API backend.

---

# 🏗️ Architecture & Tech Stack

The project follows a **clean separation of concerns**, divided into two main directories:

- **Frontend**
- **Backend**

---

# 1️⃣ Frontend (Client-Side)

### Core Technology
- React 18 (via CDN)
- HTML5
- Vanilla JavaScript

### Styling
- Tailwind CSS (configured dynamically via CDN)
- Custom CSS for **glassmorphism effects and animations**

### Icons
- Phosphor Icons for elegant UI elements

### Key Features
- **Single Page Application (SPA)**  
  Built entirely in a single `index.html` file using React components:
  - Navbar
  - Hero
  - About
  - Services
  - Works
  - Contact
  - Footer

- **Premium Aesthetics**
  - Dark mode by default (`#0f172a`)
  - Glassmorphism effects
  - Animated gradients
  - Scroll-triggered animations

- **Dynamic Portfolio**
  - Fetches and renders projects from backend using REST API  
  - Endpoint: `/api/works`

- **Functional Contact Form**
  - Sends user inquiries asynchronously to the backend

- **Responsive Design**
  - Mobile-friendly navigation
  - Responsive grid layouts for desktop and mobile

---

# 2️⃣ Backend (Server-Side)

### Framework
- FastAPI (High-performance Python web framework)

### Database
- SQLite (`technova.db`)
- Uses Python built-in `sqlite3` module

### Data Validation
- Pydantic models
  - `Contact`
  - `Work`

### Key Features

**CORS Enabled**
- Securely accepts requests from the frontend

**Contact API**
- Endpoint: `/api/contact`
- Accepts **POST requests**
- Stores user leads in the database

**Works API**
- Endpoint: `/api/works`
- **GET** → Fetch portfolio items  
- **POST** → Add new works (for admin use)

**Database Seeding (`seed.py`)**
- Script to populate the database with demo portfolio items

---

# 📂 Project Structure
P1/
│
├── frontend/
│ └── index.html # Complete React + Tailwind frontend
│
└── backend/
├── main.py # FastAPI entry point and API routes
├── database.py # Database setup and CRUD operations
├── seed.py # Script to add dummy portfolio data
├── requirements.txt # Python dependencies
└── technova.db # SQLite database (auto generated)


---

# 🚀 How to Run the Project

## Prerequisites
- Python 3.x
- Node.js or Python (to serve frontend)

---

## Step 1: Start the Backend

Navigate to backend directory


cd P1/backend


Install dependencies


pip install -r requirements.txt


Run the API server


uvicorn main:app --reload


Backend will run at:


http://localhost:8000


---

## Step 2: Seed the Database (Optional but Recommended)

Open another terminal in backend directory


cd P1/backend


Run seed script


python seed.py


This will populate the **Works section with demo projects**.

---

## Step 3: Run the Frontend

Navigate to frontend directory


cd P1/frontend


Start a simple HTTP server


python -m http.server 8080


Open browser and go to:


http://localhost:8080


---

# 🎯 Future Enhancements

### Admin Dashboard
Build a secure **authenticated interface** to manage:
- Contact form submissions
- Portfolio projects

### Production Build
Move from CDN-based React to a modern build tool such as:

- Vite
- Next.js

for better optimization and performance.

### Database Upgrade
Migrate from **SQLite → PostgreSQL** for improved scalability in production environments.

---

# 📌 Author
TechNova Solutions Development Team
