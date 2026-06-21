import tkinter as tk
from tkinter import messagebox

def get_grade_point(marks):
    if marks >= 90:
        return 10, "O"
    elif marks >= 80:
        return 9, "A+"
    elif marks >= 70:
        return 8, "A"
    elif marks >= 60:
        return 7, "B+"
    elif marks >= 50:
        return 6, "B"
    elif marks >= 40:
        return 5, "C"
    else:
        return 0, "F"

def show_grading_system():
    grading = (
        "---- Grading System ----\n"
        "90-100 : GPA = 10 → Grade = O (Outstanding)\n"
        "80-89  : GPA = 9  → Grade = A+ (Excellent)\n"
        "70-79  : GPA = 8  → Grade = A  (Very Good)\n"
        "60-69  : GPA = 7  → Grade = B+ (Good)\n"
        "50-59  : GPA = 6  → Grade = B  (Above Average)\n"
        "40-49  : GPA = 5  → Grade = C  (Average)\n"
        "Below 40 : GPA = 0 → Grade = F (Fail)\n\n"
    )
    return grading

def calculate_cgpa():
    if not entries:
        messagebox.showwarning("Warning", "Please add at least one subject first!")
        return

    try:
        marks_list = [int(entry.get()) for entry in entries if entry.get().strip() != ""]
        if not marks_list:
            messagebox.showerror("Error", "Please enter marks for all subjects!")
            return

        gpas = []
        result = show_grading_system()
        result += "---- Results ----\n"
        for i, m in enumerate(marks_list):
            gpa, grade = get_grade_point(m)
            gpas.append(gpa)
            result += f"Subject {i+1}: Marks={m} → GPA={gpa}, Grade={grade}\n"

        cgpa = round(sum(gpas) / len(gpas), 2)
        result += f"\nOverall CGPA = {cgpa}\n"

        # Clear old result and insert new one
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers only!")

def add_subject():
    idx = len(entries) + 1
    lbl = tk.Label(root, text=f"Subject {idx} Marks:")
    lbl.grid(row=idx, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries.append(entry)

    # Keep calculate button and results below inputs
    calc_btn.grid(row=idx+1, column=0, columnspan=2, pady=10)
    result_box.grid(row=idx+2, column=0, columnspan=2, padx=10, pady=10)

root = tk.Tk()
root.title("CGPA Calculator")
root.geometry("550x550")

entries = []

add_btn = tk.Button(root, text="Add Subject", command=add_subject)
add_btn.grid(row=0, column=0, columnspan=2, pady=10)

calc_btn = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa, bg="lightblue")
calc_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Text widget for results
result_box = tk.Text(root, height=18, width=65, wrap="word", bg="lightyellow")
result_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
