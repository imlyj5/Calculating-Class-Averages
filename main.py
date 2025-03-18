def calculate_class_averages(classrooms):
    output = {}
    for topic, student in classrooms.items():
        scores = 0
        grade_count = 0
        if student == {}:
             output[topic]=0
        for grades in student.values():
             for grade in grades:
                  scores += grade
                  grade_count += 1
                  output[topic]=scores/grade_count

    return output

classrooms = {
    "Math": {},
    "Science": {
        "Alice": [80, 85, 88],
        "Bob": [78, 82, 85]
    }
}

print(calculate_class_averages(classrooms))

