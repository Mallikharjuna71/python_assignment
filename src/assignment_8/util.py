from collections import namedtuple

def named_tuples_avg(l):
    Student = namedtuple('Student', 'ID, NAME, MARKS, CLASS')
    students = []
    for i in l:
        s = Student(ID=i[1], NAME=i[2], MARKS=i[0], CLASS=i[3])
        students.append(s)
    total = 0
    for i in students:
        total+= int(i.MARKS)
    return total/len(students)
