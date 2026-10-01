import matplotlib.pyplot as plt

# Runtime input
n = int(input("Enter number of students: "))

students = []
attendance = []

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter attendance percentage: "))

    students.append(name)
    attendance.append(mark)

# Create dashboard
plt.figure(figsize=(12, 4))

# 1. Line Chart
plt.subplot(1, 3, 1)
plt.plot(students, attendance, marker="o")
plt.title("Attendance Trend")
plt.xlabel("Students")
plt.ylabel("Attendance %")
plt.xticks(rotation=45)

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(students, attendance)
plt.title("Attendance Comparison")
plt.xlabel("Students")
plt.ylabel("Attendance %")
plt.xticks(rotation=45)

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(
    attendance,
    labels=students,
    autopct="%1.1f%%"
)
plt.title("Attendance Distribution")

plt.tight_layout()

# Save dashboard
plt.savefig("attendance_dashboard.png")

# Display dashboard
plt.show()