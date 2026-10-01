class User:
    def action(self):
        print("User action")
class Student(User):
    def action(self):
        print("Student can issue books")
class Teacher(User):
    def action(self):
        print("Teacher can issue reference books")
users = [Student(), Teacher()]
for user in users:
    user.action()