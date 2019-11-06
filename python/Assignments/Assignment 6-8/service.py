from domain import *

class Service:
    def __init__(self):
        '''
        Initialize the list of grades, of students and of disciplines
        '''
        self._students = []
        self._disciplines = []
        self._grades = []

    def addStudent(self, student):
        '''
        Appends to the list a new student
        '''
        self._students.append(student)

    def addDiscipline(self, discipline):
        '''
        Appends to the list a new discipline
        '''
        self._disciplines.append(discipline)

    def addGrade(self, grade):
        '''
        Appends to the list a new grade
        '''
        self._grades.append(grade)

    