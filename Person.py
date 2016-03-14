import datetime

class Person(object):
    def __init__(self, name):
        ''' Create a person'''
        self.name = name
        try:
            lastSpace = name.rindex(' ')
            self.lastName = name[lastSpace+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getName(self):
        return self.name
    def getLastName(self):
        return self.lastName
    def setBirthday(self, birthdate):
        self.birthday = birthdate
    def getAge(self):
        if self.birthday == None:
            raise ValueError(self.name + '\'s age has not been set.')
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        ''' sort by last name first. if same, sort by first name'''
        if self.lastName == other.lastName:
            return self.lastName < other.lastName
        return self.name < other.name
    def __str__(self):
        return self.name
                             
            
class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class G(Student):
    pass

class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        '''Assumes: student is of type Student
            Add student to the grade book'''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
    def getStudents(self):
        if self.isSorted == False:
            self.students.sort()
            self.isSorted = True

        return self.students[:]

def gradeReport(course):
    '''Assumes course is of type Grades'''
    #For every student in course.getStudents():
    for student in course.getStudents():

        sum = 0
        #For every grade in course.getGrades(student):
        for grade in course.getGrades(student):

            #Add to sum
            sum += grade

        #Compute the average
        try:
            average = float(sum) / len(course.getGrades(student))
            print str(student) + '\'s mean grade is', str(average) +'.'
        except:
            print student, 'has no grades.'

