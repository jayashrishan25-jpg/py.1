import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 40, 55, 70]

products = ["Laptop", "Mobile", "Tablet", "Watch"]
product_sales = [40, 70, 30, 20]

expenses = ["Food", "Travel", "Education", "Shopping"]
expense = [30, 20, 25, 25]

# Create dashboard
plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(products, product_sales)
plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(expense, labels=expenses, autopct="%1.1f%%")
plt.title("Expense Distribution")

# Another Line Chart
plt.subplot(2, 2, 4)
students = ["A", "B", "C", "D", "E"]
marks = [80, 70, 90, 75, 85]

plt.plot(students, marks, marker="o")
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.suptitle("DATA VISUALIZATION DASHBOARD")

plt.tight_layout()
plt.show()