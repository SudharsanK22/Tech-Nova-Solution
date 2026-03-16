from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import add_contact, get_all_contacts, add_work, get_all_works

app = FastAPI()

# Enable CORS to allow the frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contact(BaseModel):
    name: str
    email: str

class Work(BaseModel):
    title: str
    description: str
    image_url: str = ""

@app.post("/api/contact")
async def receive_contact(contact: Contact):
    # Save to SQLite Database
    add_contact(contact.name, contact.email)
    return {"message": "Form Submitted Successfully ✅", "data": contact}

@app.get("/api/contacts")
async def fetch_contacts():
    # Admin endpoint to get all contacts
    return {"data": get_all_contacts()}

@app.post("/api/works")
async def create_work(work: Work):
    # Admin endpoint to add a new project
    add_work(work.title, work.description, work.image_url)
    return {"message": "Project Added Successfully ✅", "data": work}

@app.get("/api/works")
async def fetch_works():
    # Endpoint to display works on the frontend
    return {"data": get_all_works()}

@app.get("/api/health")
async def health_check():
    return {"status": "Backend is running flawlessly 🚀"}
