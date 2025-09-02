"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""


import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    pass

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    pass

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    pass

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    # implement logic

    return report
