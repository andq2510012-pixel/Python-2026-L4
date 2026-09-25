students=[]
def students_info(): 
    num_student = int(input("Number of student: "))
    for i in range(num_student):
        i_id = int(input("id: "))
        i_name = str(input("name: "))
        i_DoB = input("Date of birth: ")
        students.append({"id": i_id, "name":i_name, "DoB":i_DoB})

course=[]
marks={}
def courses():
    num_course = int(input("Number of courses: "))
    for i in range(num_course):
        s_id = int(input("id: "))
        s_name = str(input("name: "))
        course.append({"id": s_id, "name":s_name})
        marks[s_id]={}

def mark_student():
    s_id = int(input("subject ID: "))
    if s_id in marks:
        for student in students: 
            mark = float(input(f"Subject score of student {student['name']}: "))
            marks[s_id][student['id']] = mark

def student_list():
    for student in students: 
        print(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['DoB']}")

def course_list():
    for c in course:
        print(f"ID: {c['id']} | Subject: {c['name']}")

def mark_list():
    for s_id in marks:
        for st_id, mark in marks[s_id].items():
            print(f"Subject ID: {s_id} | Student ID: {st_id} | Score: {mark}")

def main():
    while True: 
        print("1. Student Info: ")
        print("2. Course Info: ")
        print("3. Mark: ")
        print("4. Student list: ")
        print("5. Course list: ")
        print("6. Mark list")

        a = int(input("Choose 1-6: "))

        if a == 1:
            students_info()
        elif a == 2:
            courses()
        elif a == 3:
            mark_student()
        elif a == 4:
            student_list()
        elif a == 5:
            course_list()
        elif a == 6:
            mark_list()
            break

if __name__ == "__main__":
    main()