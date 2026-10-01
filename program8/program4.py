import matplotlib.pyplot as plt

departments = ["Computer Science", "Commerce", "Physics",
               "Mathematics", "English"]

students = [40, 30, 20, 15, 25]

plt.pie(students, labels=departments, autopct="%1.1f%%")

plt.title("Students by Department")

plt.savefig("department_students.png")