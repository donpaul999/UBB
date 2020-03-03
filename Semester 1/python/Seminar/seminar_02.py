#simple feature-driven development

#id = 114. ma,e = "Anna", grade = 10
#how can we abstract the student's representation from the program?


s = {"id":114, "name":"Anna", "grade":10} #dictionary
#s = [114, "Anna", 10] #as list

def create_student(sid = -1, sname="n/a", sgrade=None):
    return {"id":sid, "name":sname, "grade":sgrade}

def set_student_id(student, sid):
    student["id"] = sid
def set_student_name(student, sname):
    student["name"] = sname
def set_student_grade(student, sgrade):
    student["grade"] = sgrade


def get_student_id(student):
    return student["id"]
def get_student_name(student):
    return student["name"]
def get_student_grade(student):
    return student["grade"]

def show_students(students):
    print("List of students")
    for s in students:
        print("id: " + str(get_student_id(s)) + " Name: " + get_student_name(s))


def read_student():
    sid = int(input('student id='))
    sname = input('student name=')
    sgrade = int(input('student grade='))
    return create_student(sid,sname,sgrade)

def validate_student(student, studentList):
    for s in studentList:
        if get_student_id(student) == get_student_id(s):
            return "Duplicate student id!"

    name = get_student_name(student)
    if len(name) == 0:
        return "Empty name!"
    grade = get_student_grade(student)
    if grade < 1 or grade > 10:
        return "Invalid grade"
    return None

def add_student(studentList):
    #read
    #validate
    #add
    student = read_student()
    msg = validate_student(student, studentList)
    if msg is not None:
        print(msg)
    else:
        studentList.append(student)


def print_menu():
    print("1. Show students")
    print("2. Add student")
    print("3. Exit")


def init_students():
    res = []
    res.append(create_student(100,"Alice",9))
    res.append(create_student(101,"Bob",8))
    return res

def start():
    #students = []
    students = init_students()
    while True:
        print_menu()
        choice = input(">")
        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            return
        else:
            print("Invalid command")




start()




s["name"] = "Marie"
