import json
import os
from student import Student

DATA_FILE = "students.json"

class StudentManager:
    def __init__(self):
        self.students = {}
        self.load()

    def load(self):
        """Load students from JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for record in data:
                    s = Student(record["id"], record["name"], record["grade"])
                    self.students[s.student_id] = s
        else:
            self.save()  # Create empty file

    def save(self):
        """Persist students to JSON file."""
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students.values()], f, indent=4)

    def add_student(self, student_id, name, grade):
        """Add a new student with unique ID validation."""
        if student_id in self.students:
            print(f"❌ Error: Student with ID '{student_id}' already exists.")
            return False
        student = Student(student_id, name, grade)
        self.students[student_id] = student
        self.save()
        print(f"✅ Student '{name}' added successfully.")
        return True

    def update_student(self, student_id, name=None, grade=None):
        """Update an existing student's details."""
        if student_id not in self.students:
            print(f"❌ Error: No student found with ID '{student_id}'.")
            return False
        if name:
            self.students[student_id].name = name
        if grade:
            self.students[student_id].grade = grade
        self.save()
        print(f"✅ Student ID '{student_id}' updated successfully.")
        return True

    def delete_student(self, student_id):
        """Delete a student by ID."""
        if student_id not in self.students:
            print(f"❌ Error: No student found with ID '{student_id}'.")
            return False
        name = self.students[student_id].name
        del self.students[student_id]
        self.save()
        print(f"✅ Student '{name}' deleted successfully.")
        return True

    def list_students(self):
        """Display all students in a formatted table."""
        if not self.students:
            print("📭 No students found.")
            return
        print("\n" + "=" * 46)
        print(f"| {'ID':<10} | {'Name':<20} | {'Grade':<6} |")
        print("=" * 46)
        for student in self.students.values():
            print(student)
        print("=" * 46)
        print(f"  Total students: {len(self.students)}\n")

    def find_student(self, student_id):
        """Find and display a student by ID."""
        if student_id not in self.students:
            print(f"❌ No student found with ID '{student_id}'.")
            return None
        s = self.students[student_id]
        print("\n--- Student Found ---")
        print(f"  ID    : {s.student_id}")
        print(f"  Name  : {s.name}")
        print(f"  Grade : {s.grade}")
        print("---------------------\n")
        return s