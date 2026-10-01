import math
import numpy as np
import curses 

def ask(stdscr, prompt):
    stdscr.addstr(prompt)                # in câu hỏi tại vị trí con trỏ
    curses.echo()                        # bật hiện chữ khi gõ
    s = stdscr.getstr().decode()         # đọc đến Enter, bytes -> str
    curses.noecho()                      # tắt hiện chữ để menu không in ký tự lạ
    return s                             # trả chuỗi, giống input()

students=[]
def students_info(stdscr):
    stdscr.clear()
    num_student = int(ask(stdscr, "Number of student: "))
    for i in range(num_student):
        stdscr.addstr("\n")
        i_id = int(ask(stdscr, "id: "))
        i_name = str(ask(stdscr, "name: "))
        i_DoB = ask(stdscr, "Date of birth: ")
        students.append({"id": i_id, "name": i_name, "DoB": i_DoB})

course=[]
marks={}
credit={}
def courses(stdscr):
    stdscr.clear()
    num_course = int(ask(stdscr, "Number of courses: "))
    for i in range(num_course):
        stdscr.addstr("\n")
        s_id = int(ask(stdscr, ("id: ")))
        s_name = str(ask(stdscr, "name: "))
        s_credit = int(ask(stdscr, "credit: "))
        course.append({"id": s_id, "name":s_name, "credit ":s_credit})
        marks[s_id]={}
        credit[s_id]= s_credit

def mark_student(stdscr):
    stdscr.clear()
    s_id = int(ask(stdscr, "subject ID: "))
    if s_id in marks:
        for student in students:
            stdscr.addstr("\n")
            mark = math.floor(float(ask(stdscr, f"Score of {student['name']}: ")))
            marks[s_id][student['id']] = mark

def GPA(student_id):
    ID_subject_has_mark = [s for s in marks if student_id in marks[s]]
    if not ID_subject_has_mark: 
        return 0.0
    c = np.array([credit[s] for s in ID_subject_has_mark])              #credit từng môn
    m = np.array([marks[s][student_id] for s in ID_subject_has_mark])   #điểm của từng học sinh, lấy từ dictionary mark
    return np.dot(c, m)/np.sum(c)                                       #tính GPA (TB có trọng số)

def output_GPA(stdscr):
    stdscr.clear()
    sid = int(ask(stdscr, "Student ID: "))                      # hỏi ID
    stdscr.addstr(f"\nGPA: {GPA(sid):.2f}\n")                   # tính và in GPA 
    stdscr.getch()                                              # chờ bấm phím
def sort_GPA(stdscr):
    students.sort(key=lambda st: GPA(st['id']), reverse=True)   # sắp xếp students theo GPA desc
    stdscr.clear()                                              # xóa màn hình cũ
    for st in students:
        stdscr.addstr(f"{st['name']} | {GPA(st['id'])}\n")      # in tên và GPA 
    stdscr.getch()                                              # chờ bấm phím rồi mới quay lại menu


def student_list(stdscr):
    for student in students: 
        stdscr.addstr(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['DoB']}")

def course_list(stdscr):
    for c in course:
        stdscr.addstr(f"ID: {c['id']} | Subject: {c['name']}")

def mark_list(stdscr):
    for s_id in marks:
        for st_id, mark in marks[s_id].items():
            stdscr.addstr(f"Subject ID: {s_id} | Student ID: {st_id} | Score: {mark}")
    stdscr.getch()

def main(stdscr):
    stdscr.scrollok(True)
    while True: 
        stdscr.addstr("1. Student Info: \n")
        stdscr.addstr("2. Course Info: \n")
        stdscr.addstr("3. Mark: \n")
        stdscr.addstr("4. Student list: \n")
        stdscr.addstr("5. Course list: \n")
        stdscr.addstr("6. Mark list \n")
        stdscr.adđstr("7. GPA \n")
        stdscr.addstr("8. GPA list \n")

        a = int(ask(stdscr, "Choose 1-6: \n"))

        if a == 1:
            students_info(stdscr)
        elif a == 2:
            courses(stdscr)
        elif a == 3:
            mark_student(stdscr)
        elif a == 4:
            student_list(stdscr)
        elif a == 5:
            course_list(stdscr)
        elif a == 6:
            mark_list(stdscr)
        elif a == 7:
            output_GPA(stdscr)
        elif a == 8:
            sort_GPA(stdscr)

if __name__ == "__main__": # chạy menu chỉ khi chạy trực tiếp file này
    curses.wrapper(main)