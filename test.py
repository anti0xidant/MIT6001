class Student(object):
    def __init__(self):
        self.grades = []

    def getGrades(self):
        for g in self.grades:
            yield g

    def addGrade(self, grade):
        self.grades.append(grade)
