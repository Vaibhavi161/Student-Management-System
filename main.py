from fastapi import FastAPI 
from supabase import create_client 
from dotenv import load_dotenv 
from pydantic import BaseModel 
from fastapi.middleware.cors import CORSMiddleware 
import os 
 
 
# 1. LOAD ENVIRONMENT VARIABLES 
load_dotenv() 
 
 
# 2. CREATE FASTAPI APPLICATION 
app = FastAPI() 
 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=False, 
    allow_methods=["*"], 
    allow_headers=["*"] 
) 
 
 
# 3. GET SUPABASE CREDENTIALS 
SUPABASE_URL = os.getenv("SUPABASE_URL") 
SUPABASE_KEY = os.getenv("SUPABASE_KEY") 
 
 
# 4. CONNECT TO SUPABASE 
supabase = create_client( 
    SUPABASE_URL, 
    SUPABASE_KEY 
) 


# REQUIRED: STUDENT MODEL
class Student(BaseModel):
    name: str
    course: str
    marks: int
 
 
# 5. CREATE STUDENT - POST 
@app.post("/students") 
def create_student(student: Student): 
    try: 
        response = ( 
            supabase 
            .table("students") 
            .insert(student.model_dump()) 
            .execute() 
        ) 
 
        return { 
            "message": "Student created successfully", 
            "data": response.data 
        } 
 
    except Exception as e: 
        print("CREATE ERROR:", e) 
 
        return { 
            "message": "Student creation failed", 
            "error": str(e) 
        } 
 
# ============================================================ 
# 6. GET ALL STUDENTS - GET 
# ============================================================ 
 
@app.get("/students") 
def get_all_students(): 
 
    try: 
 
        response = ( 
            supabase 
            .table("students") 
            .select("*") 
            .execute() 
        ) 
 
        if not response.data: 
            return { 
                "message": "No students found" 
            } 
 
        return { 
            "message": "Students fetched successfully", 
            "data": response.data 
        } 
 
    except Exception as e: 
 
        print("ERROR:", e) 
 
        return { 
            "message": "Failed to get students", 
            "error": str(e) 
        } 
 
 
# ============================================================ 
# 7. GET STUDENT - GET 
# ============================================================ 
 
@app.get("/students/{student_id}") 
def get_student(student_id: int): 
 
    try: 
 
        response = ( 
            supabase 
            .table("students") 
            .select("*") 
            .eq("id", student_id) 
            .execute() 
        ) 
 
        if not response.data: 
            return { 
                "message": "Student not found" 
            } 
 
        return { 
            "message": "Student found successfully", 
            "data": response.data 
        } 
 
    except Exception as e: 
 
        print("ERROR:", e) 
 
        return { 
            "message": "Failed to get student", 
            "error": str(e) 
        } 
 
 
# ============================================================ 
# 8. UPDATE STUDENT - PUT 
# ============================================================ 
 
@app.put("/students/{student_id}") 
def update_student( 
    student_id: int, 
    student: Student
): 
 
    try: 
 
        student_data = student.model_dump()

        response = ( 
            supabase 
            .table("students") 
            .update(student_data) 
            .eq("id", student_id) 
            .execute() 
        ) 
 
        if not response.data: 
            return { 
                "message": "Student not found" 
            } 
 
        return { 
            "message": "Student updated successfully", 
            "data": response.data 
        } 
 
    except Exception as e: 
 
        print("ERROR:", e) 
 
        return { 
            "message": "Student update failed", 
            "error": str(e) 
        } 
 
 
# ============================================================ 
# 9. DELETE STUDENT - DELETE 
# ============================================================ 
 
@app.delete("/students/{student_id}") 
def delete_student(student_id: int): 
 
    try: 
 
        response = ( 
            supabase 
            .table("students") 
            .delete() 
            .eq("id", student_id) 
            .execute() 
        ) 
 
        if not response.data: 
            return { 
                "message": "Student not found" 
            } 
 
        return { 
            "message": "Student deleted successfully", 
            "data": response.data 
        } 
 
    except Exception as e: 
 
        print("ERROR:", e) 
 
        return { 
            "message": "Student deletion failed", 
            "error": str(e) 
        }