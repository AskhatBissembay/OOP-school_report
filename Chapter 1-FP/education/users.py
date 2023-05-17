class Human():
    def __init__(self,name,familyname,age,gender,nationality):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender=gender
        self.nationality=nationality
    def set_name(self):
        return f"{self.name}"
    def set_family(self):
        return f"{self.familyname}"
    def set_age(self):
        return self.age
    def set_gender(self):
        return f"{self.gender}"
    def set_nationality(self):
        return f"{self.nationality}"
    def get_info1(self):
        human_info = {"name": self.name,
                "family": self.familyname,
                "age":self.age,
                "gender":self.gender,
                "nationality":self.nationality}
        return human_info

class Student(Human):
    def __init__(self,school,subject,name,familyname,age,gender,nationality):
        super().__init__(name,familyname,age,gender,nationality)
        self.school = school
        self.subject = subject
        self.sub = []
    def add_subject(self,subject):
        if subject is not None:
            self.sub.extend(subject)
        else:
            print("This is not a subject")
        return self.sub
    def set_school(self):
        return f"{self.school}"
    def get_info(self):
        student_info = self.get_info1()
        student_info["subject"] = self.sub
        student_info["school"] = self.school
        student_info["Role"] = "Student"
        return student_info
    
class Teacher(Human):
    def __init__(self,school,subject,name,familyname,age,gender,nationality):
        super().__init__(name,familyname,age,gender,nationality)
        self.school = school
        self.subject = subject
        self.sub1 = []
    def add_subject(self,subject):
        if subject is not None:
            self.sub1.extend(subject)
        else:
            print("This is not a subject")
        return self.sub1
    def set_school(self):
        return f"{self.school}"
    def get_info(self):
        teacher_info = self.get_info1()
        teacher_info["subject"] = self.sub1
        teacher_info["school"] = self.school
        teacher_info["Role"] = "Teacher"
        return teacher_info

if __name__ == "__main__":
    print(f"The users module was imported successfully")
else:
    print(f"Human: {dir(Human)}, Student: {dir(Student)}, Teacher: {dir(Teacher)}")
