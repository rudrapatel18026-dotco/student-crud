from fastapi import APIRouter, Response
from models.student_model import Student
from controllers.student_controller import (
    create_student_controller,
    get_student_controller,
    update_student_controller,
    delete_student_controller,
    get_students_id_controller,
)

StudentRouter = APIRouter(
    prefix="/students",
    tags=["students"]
)


# Create Student
@StudentRouter.post("/poststudents")
def create_student(student: Student, response: Response):
    return create_student_controller(student, response)


# Get All Students
@StudentRouter.get("/getstudents")
def get_students(response: Response):
    return get_student_controller(response)


# Get Student by ID
@StudentRouter.get("/getstudent/{studentid}")
def get_students_id(studentid: int, response: Response):
    return get_students_id_controller(studentid, response)


# Delete Student
@StudentRouter.delete("/deletestudent/{studentid}")
def delete_student(studentid: int, response: Response):
    return delete_student_controller(studentid, response)


# Update Student
@StudentRouter.put("/updatestudent/{studentid}")
def update_student(
    studentid: int, updated_student: Student, response: Response
):
    return update_student_controller(studentid, updated_student, response)