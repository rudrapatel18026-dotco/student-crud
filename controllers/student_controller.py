from fastapi import Response
from models.student_model import Student

students = []
id = 0


def create_student_controller(student: Student, response: Response):
    global id
    try:
        id += 1
        student.id = id
        students.append(student)
        response.status_code = 201
        return {
            "isSuccess": True,
            "message": "Student Created Successfully",
            "student": student,
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"isSuccess": False, "message": str(e)}


def get_students_id_controller(studentid: int, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                return {"isSuccess": True, "student": student}

        response.status_code = 404
        return {"isSuccess": False, "message": "Student not found"}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {"isSuccess": False, "message": str(e)}


def get_student_controller(response: Response):
    try:
        response.status_code = 200
        return {
            "isSuccess": True,
            "message": "Student Display Successfully",
            "students": students,
        }
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "message": str(e)}


def update_student_controller(
    studentid: int, updated_student: Student, response: Response
):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                student.name = updated_student.name
                student.email = updated_student.email
                student.course = updated_student.course
                student.semester = updated_student.semester
                return {
                    "isSuccess": True,
                    "message": "Student Updated Successfully",
                    "student": student,
                }

        response.status_code = 404
        return {"isSuccess": False, "message": "Student not found"}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "message": str(e)}


def delete_student_controller(studentid: int, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                students.remove(student)
                return {
                    "isSuccess": True,
                    "message": "Student Deleted Successfully",
                    "student": student,
                }

        response.status_code = 404
        return {"isSuccess": False, "message": "Student not found"}
    except Exception as e:
        response.status_code = 500
        return {"isSuccess": False, "message": str(e)}