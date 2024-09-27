# finding average

def calculating_percentage():
    student_marks = {
        'Krishna':[67, 68, 69],
        'Arjun':[70, 98, 63],
        'Malika':[52, 56, 60]
    }
    query_name = input('enter the name of the Student:  ').capitalize()
    marks = student_marks[query_name]
    total_marks = sum(marks)
    length = len(marks)
    r = total_marks/length
    return f"{r:.2f}"

