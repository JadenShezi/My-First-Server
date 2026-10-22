from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Student(BaseModel):
    id:int
    name:str
    course:str

app = FastAPI(title="Our Demo Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

students = [{"id":1,"name": "Thabo", "course": "Networking"},
            {"id":2,"name": "Ayanda", "course": "Software Development"},
            {"id":3,"name": "Lerato", "course": "Computer Science"}]

@app.get('/')
def home():
    return {'message':'This is your home page'}

@app.get('/messages')
def message():
    return {'message':'This is your message panel'}

@app.get('/students')
def getstudents():
    return students


@app.get("/students/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message":"Student not found"}

@app.get("/search")
def search_students(course:str):
    results=[]
    for student in students:
        if student["course"].lower == course.lower():
            results.append(student)
    return results

  

@app.post("/students")
def create_student(student:Student):
    students.append(student)
    return{
        "message":"Student received successfully",
        "student":student
    }