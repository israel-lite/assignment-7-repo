
import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }
    else:
        print(f"Student ID {student_id} already exists.")

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].append(today)
            # remove from absent if wrongly marked
            if today in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].remove(today)
        else:
            print(f"Student ID {sid} not registered.")

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].append(today)
            # remove from present if wrongly marked
            if today in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].remove(today)
        else:
            print(f"Student ID {sid} not registered.")

def get_report(**kwargs):
    """
    Generate attendance report with optional filters.
    kwargs can include:
        - only_present=True → show only students with present days
        - only_absent=True → show only students with absent days
    """
    report = {}
    for sid, data in attendance.items():
        if kwargs.get("only_present") and not data["present_days"]:
            continue
        if kwargs.get("only_absent") and not data["absent_days"]:
            continue
        report[sid] = data
    return report



register_student("S1", "Alice")
register_student("S2", "Bob")
register_student("S3", "Charlie")

mark_present(["S1", "S2"])  
mark_absent(["S3"])         

print("Full Report:", get_report())
print("Only Present:", get_report(only_present=True))
print("Only Absent:", get_report(only_absent=True))
