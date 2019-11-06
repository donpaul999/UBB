from service import Service
from domain import *

class UI:
    def __init__(self, service):
        self._service = service

    def addStudent(self):
        pass

    def addDiscipline(self):
        pass

    def addGrade(self):
        pass


    def printStudents(self):
        self.print_stars()
        ok = 0
        for i in self._service._students:
            print(i)
            print("")
            ok = 1
        if ok == 0:
            print("There are no students in the list!")
        self.print_stars()

    def printDisciplines(self):
        self.print_stars()
        ok = 0
        for i in self._service._disciplines:
            print(i)
            print("")
            ok = 1
        if ok == 0:
            print("There are no disciplines in the list!")
        self.print_stars()

    def printGrades(self):
        self.print_stars()
        ok = 0
        for i in self._service._grades:
            for j in self._service._students:
                if j.studentId == i.studentId:
                    print("Student: " + j.Name, end=", ")
                    break
            for j in self._service._disciplines:
                if j.disciplineId == i.disciplineId:
                    print("Discipline: " + j.Name, end=", ")
                    break
            print("Grade: " + str(i.Value))
            print("")
            ok = 1
        if ok == 0:
            print("There are no grades in the list!")
        self.print_stars()


    def update_student(self):
        pass

    def update_discipline(self):
        pass

    def print_menu(self):
        print("1. Add a new student")
        print("2. Show the list of students")
        print("3. Update a student")
        print("4. Add a new discipline")
        print("5. Show the list of disciplines")
        print("6. Update a discipline")
        print("7. Add a new grade")
        print("8. Show the list of grades")
        print("9. Undo the last operation")
        print("10. Redo the last operation")
        print("11. Exit")

    def print_stars(self):
        print("***************************")

    def print_invalid(self):
        print("Invalid command!")

    def start(self):
        while True:
            self.print_menu()
            choice = input(">")
            if choice == "1":
                self.addStudent()
            elif choice == "2":
                self.printStudents()
            elif choice == "4":
                self.addDiscipline()
            elif choice == "5":
                self.printDisciplines()
            elif choice == "7":
                self.addGrade()
            elif choice == "8":
                self.printGrades()
            elif choice == "9":
                self.undo()
            elif choice == "10":
                self.redo()
            elif choice == "11":
                return
            elif choice == "3":
                self.update_student()
            elif choice == "6":
                self.update_discipline()
            else:
                self.print_invalid()