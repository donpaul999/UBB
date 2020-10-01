def create_student(sid, name, grade): #Non-UI
    '''
    Create a student
    params:
        sid - id
        name - string of len >= 3
        grade - int between 1 and 10
    output:
        success - return the student
        error - return None
    '''
    if len(name) < 3:
        return None
    grade = int(grade)
    if grade < 1 or grade > 10:
        return None
    return [sid, name, grade]


def get_id(student):
    return student[0];
def get_name(student):
    return student[1];
def get_grade(student):
    return student[2];



def find_student(studentList, sid):
    '''
    Find student having given id
    params:....
    output:
        Student having given idea
        None, student with given id not in list
    '''
    for s in studentList:
        if get_id(s) == sid:
            #this is the student u re looking for
            return s
    return None

def add_student(studentList, student):
    '''
    add student to list
    params:
        studentList - the list of students
        student - the student
    output:
        0 - success
        1 - Duplicate student id
    '''
    if find_student(studentList, get_id(student)) != None:
        return 1
    studentList.append(student)
    return 0

#1. Function signature
#2. Specification
#3. We can write a test for it

def readCommand():
    '''
    Read and parse the user's command
    '''
    cmd = input("command: ")
    #1. Separate command word from list of params
    #2. Identify params
    #3. Return tuple (command, list of params)
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd, [])
    command = cmd[:idx]
    params = cmd[idx:]
    params = params.split(",")
    for i in range(len(params)):
        params[i] = params[i].strip()
    return (command, params)


def add_student_ui(studentList, params):
    if len(params) != 3:
        print("Bad student parameters")
        return
    s = create_student(params[0], params[1], params[2])
    if s == None:
        print("Invalid student data")
        return
    if add_student(studentList, s) == 1:
        print("Duplicate student id!")


def start():
    studentList = []
    while True:
        #read user command
        cmdtuple = readCommand()
        cmd = cmdtuple[0]
        params = cmdtuple[1]
        if cmd == 'add':
            add_student_ui(studentList, params)
        elif cmd == 'exit':
            break;
        else:
            print("Bad command")

def test_add_student():
    slist = []
    s1 = create_student(1, "Marie", 10)
    add_student(slist, s1)
    assert get_id(slist[0]) == 1
    assert add_student(slist, s1) == 1
    assert len(slist) == 1







test_add_student()
start()
# () - function call operator
