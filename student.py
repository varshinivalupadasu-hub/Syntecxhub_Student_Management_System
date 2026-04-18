class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }

    def __str__(self):
        return f"| {self.student_id:<10} | {self.name:<20} | {self.grade:<6} |"