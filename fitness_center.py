import tkinter as tk
from tkinter import messagebox


# -----------------------------
# Member Class
# -----------------------------
class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type

    def display_info(self):
        return f"ID: {self.member_id} | Name: {self.name} | Membership: {self.membership_type}"


# -----------------------------
# FitnessClass Class
# -----------------------------
class FitnessClass:
    def __init__(self, class_name, instructor, schedule):
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.attendance_list = []

    def add_attendance(self, member):
        self.attendance_list.append(member)

    def display_class(self):
        return f"{self.class_name} | Instructor: {self.instructor} | Schedule: {self.schedule}"


# -----------------------------
# ManagementSystem Class
# -----------------------------
class ManagementSystem:
    def __init__(self):
        self.members = []
        self.classes = []

    def add_member(self, member):

        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                return "Duplicate ID"

        self.members.append(member)
        return "Success"

    def remove_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return "Member removed."

        return "Member not found."

    def search_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def display_members(self):

        if not self.members:
            return "No members found."

        result = ""

        for member in self.members:
            result += member.display_info() + "\n"

        return result

    def add_class(self, fitness_class):
        self.classes.append(fitness_class)

    def display_classes(self):

        if not self.classes:
            return "No classes available."

        result = ""

        for fitness_class in self.classes:
            result += fitness_class.display_class() + "\n"

        return result

    def record_attendance(self, member_id, class_name):

        member = self.search_member(member_id)

        if member is None:
            return "Member not found."

        for fitness_class in self.classes:

            if fitness_class.class_name.lower() == class_name.lower():

                fitness_class.add_attendance(member)

                return f"{member.name} added to {class_name}"

        return "Class not found."

    def display_attendance(self):

        result = ""

        for fitness_class in self.classes:

            result += f"\n{fitness_class.class_name} Attendance:\n"

            if not fitness_class.attendance_list:
                result += "No attendance recorded.\n"

            else:
                for member in fitness_class.attendance_list:
                    result += f"- {member.name}\n"

        return result


# -----------------------------
# Create System
# -----------------------------
system = ManagementSystem()


# -----------------------------
# GUI Functions
# -----------------------------
def add_member():

    try:

        member_id = int(entry_member_id.get())
        name = entry_name.get()
        membership = entry_membership.get()

        if name == "" or membership == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        member = Member(member_id, name, membership)

        result = system.add_member(member)

        if result == "Duplicate ID":
            messagebox.showerror("Error", "Member ID already exists.")

        else:
            messagebox.showinfo("Success", "Member added successfully!")

        clear_member_entries()

    except ValueError:
        messagebox.showerror("Error", "Member ID must be a number.")


def remove_member():

    try:

        member_id = int(entry_member_id.get())

        result = system.remove_member(member_id)

        messagebox.showinfo("Remove Member", result)

        clear_member_entries()

    except ValueError:
        messagebox.showerror("Error", "Enter a valid member ID.")


def search_member():

    try:

        member_id = int(entry_member_id.get())

        member = system.search_member(member_id)

        output_text.delete(1.0, tk.END)

        if member:
            output_text.insert(tk.END, member.display_info())

        else:
            output_text.insert(tk.END, "Member not found.")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid member ID.")


def view_members():

    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, system.display_members())


def add_class():

    class_name = entry_class_name.get()
    instructor = entry_instructor.get()
    schedule = entry_schedule.get()

    if class_name == "" or instructor == "" or schedule == "":
        messagebox.showerror("Error", "All class fields are required.")
        return

    fitness_class = FitnessClass(class_name, instructor, schedule)

    system.add_class(fitness_class)

    messagebox.showinfo("Success", "Class added successfully!")

    clear_class_entries()


def view_classes():

    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, system.display_classes())


def record_attendance():

    try:

        member_id = int(entry_attendance_member.get())
        class_name = entry_attendance_class.get()

        result = system.record_attendance(member_id, class_name)

        messagebox.showinfo("Attendance", result)

        clear_attendance_entries()

    except ValueError:
        messagebox.showerror("Error", "Member ID must be a number.")


def view_attendance():

    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, system.display_attendance())


def clear_output():

    output_text.delete(1.0, tk.END)


# -----------------------------
# Clear Entry Functions
# -----------------------------
def clear_member_entries():
    entry_member_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_membership.delete(0, tk.END)


def clear_class_entries():
    entry_class_name.delete(0, tk.END)
    entry_instructor.delete(0, tk.END)
    entry_schedule.delete(0, tk.END)


def clear_attendance_entries():
    entry_attendance_member.delete(0, tk.END)
    entry_attendance_class.delete(0, tk.END)


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()

window.title("Fitness Center Management System")
window.geometry("850x700")
window.configure(bg="#EAF4F4")


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    window,
    text="Fitness Center Management System",
    font=("Arial", 20, "bold"),
    bg="#EAF4F4",
    fg="#003049"
)

title_label.pack(pady=10)


# -----------------------------
# Member Frame
# -----------------------------
member_frame = tk.LabelFrame(
    window,
    text="Member Management",
    padx=10,
    pady=10,
    bg="#F1FAEE",
    font=("Arial", 12, "bold")
)

member_frame.pack(fill="x", padx=10, pady=5)

tk.Label(member_frame, text="Member ID", bg="#F1FAEE").grid(row=0, column=0)
entry_member_id = tk.Entry(member_frame)
entry_member_id.grid(row=0, column=1)

tk.Label(member_frame, text="Name", bg="#F1FAEE").grid(row=1, column=0)
entry_name = tk.Entry(member_frame)
entry_name.grid(row=1, column=1)

tk.Label(member_frame, text="Membership", bg="#F1FAEE").grid(row=2, column=0)
entry_membership = tk.Entry(member_frame)
entry_membership.grid(row=2, column=1)

tk.Button(member_frame, text="Add Member", command=add_member).grid(row=3, column=0, pady=5)

tk.Button(member_frame, text="Remove Member", command=remove_member).grid(row=3, column=1)

tk.Button(member_frame, text="Search Member", command=search_member).grid(row=4, column=0)

tk.Button(member_frame, text="View Members", command=view_members).grid(row=4, column=1)


# -----------------------------
# Class Frame
# -----------------------------
class_frame = tk.LabelFrame(
    window,
    text="Fitness Classes",
    padx=10,
    pady=10,
    bg="#F1FAEE",
    font=("Arial", 12, "bold")
)

class_frame.pack(fill="x", padx=10, pady=5)

tk.Label(class_frame, text="Class Name", bg="#F1FAEE").grid(row=0, column=0)
entry_class_name = tk.Entry(class_frame)
entry_class_name.grid(row=0, column=1)

tk.Label(class_frame, text="Instructor", bg="#F1FAEE").grid(row=1, column=0)
entry_instructor = tk.Entry(class_frame)
entry_instructor.grid(row=1, column=1)

tk.Label(class_frame, text="Schedule", bg="#F1FAEE").grid(row=2, column=0)
entry_schedule = tk.Entry(class_frame)
entry_schedule.grid(row=2, column=1)

tk.Button(class_frame, text="Add Class", command=add_class).grid(row=3, column=0, pady=5)

tk.Button(class_frame, text="View Classes", command=view_classes).grid(row=3, column=1)


# -----------------------------
# Attendance Frame
# -----------------------------
attendance_frame = tk.LabelFrame(
    window,
    text="Attendance",
    padx=10,
    pady=10,
    bg="#F1FAEE",
    font=("Arial", 12, "bold")
)

attendance_frame.pack(fill="x", padx=10, pady=5)

tk.Label(attendance_frame, text="Member ID", bg="#F1FAEE").grid(row=0, column=0)
entry_attendance_member = tk.Entry(attendance_frame)
entry_attendance_member.grid(row=0, column=1)

tk.Label(attendance_frame, text="Class Name", bg="#F1FAEE").grid(row=1, column=0)
entry_attendance_class = tk.Entry(attendance_frame)
entry_attendance_class.grid(row=1, column=1)

tk.Button(attendance_frame, text="Record Attendance", command=record_attendance).grid(row=2, column=0, pady=5)

tk.Button(attendance_frame, text="View Attendance", command=view_attendance).grid(row=2, column=1)


# -----------------------------
# Output Section
# -----------------------------
output_label = tk.Label(
    window,
    text="System Output",
    font=("Arial", 14, "bold"),
    bg="#EAF4F4"
)

output_label.pack()

output_text = tk.Text(window, height=15, width=90)
output_text.pack(pady=10)

tk.Button(window, text="Clear Output", command=clear_output).pack(pady=5)


# -----------------------------
# Run Program
# -----------------------------
window.mainloop()