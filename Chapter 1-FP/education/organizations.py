from education.users import *

import csv
class School():
    def __init__(self,name,address,phone,email,num_stud,num_teachers):
        self.school_name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.list_of_stud = []
        self.list_of_teach = []
    def set_name(self):
        return f"{self.school_name}"
    def set_address(self):
        return f"{self.address}"
    def set_phone(self):
        return f"{self.phone}"
    def set_email(self):
        return f"{self.email}"
    def set_num_stud(self):
        return self.num_stud
    def set_num_teachers(self):
        return self.num_teachers
    
    def add_student(self,student):
        if student not in self.list_of_stud and student.school == self.school_name:
            return self.list_of_stud.append(student)
        
    def add_teacher(self,teacher):
        if teacher not in self.list_of_teach and teacher.school == self.school_name:
            return self.list_of_teach.append(teacher)
   

    def get_info(self):
        school_info = {"name": self.school_name,
                      "address": self.address,
                      "phone": self.phone,
                      "email": self.email,
                      "num_stud": self.num_stud,
                      "num_teachers":self.num_teachers}
        return school_info

    def get_report_01(self):
        with open('report_ktl.csv','w') as f:
            school_writer = csv.DictWriter(f, fieldnames = self.get_info().keys())
            school_writer.writeheader()
            school_writer.writerow(self.get_info())
            
            writer = csv.DictWriter(f,fieldnames=self.list_of_stud[0].get_info().keys())
            writer.writeheader()
            for row in self.list_of_stud[1:]:
                column_num = 0
                if row is not None:
                    column_num += 1
                    while column_num > self.num_stud:
                        break
            for s in self.list_of_stud:
                writer.writerow(s.get_info())

            writ = csv.DictWriter(f,fieldnames=self.list_of_teach[0].get_info().keys())
            for row in self.list_of_teach[1:]:
                column_number = 0
                if row is not None:
                    column_number += 1
                    while column_number > self.num_teachers:
                        break
            writ.writerows([m.get_info() for m in self.list_of_teach])


    def get_report_02(self):
        with open('report_nis.csv','w') as f:
            school_writer = csv.DictWriter(f, fieldnames = self.get_info().keys())
            school_writer.writeheader()
            school_writer.writerow(self.get_info())
            
            writer = csv.DictWriter(f,fieldnames=self.list_of_stud[0].get_info().keys())
            writ = csv.DictWriter(f,fieldnames=self.list_of_teach[0].get_info().keys())
            writer.writeheader()
            for row in self.list_of_stud[1:]:
                column_num = 0
                if row is not None:
                    column_num += 1
                    while column_num > self.num_stud:
                        break
            writer.writerows([s.get_info() for s in self.list_of_stud])
            for row in self.list_of_teach[1:]:
                column_number = 0
                if row is not None:
                    column_number += 1
                    while column_number > self.num_teachers:
                        break
            writ.writerows([m.get_info() for m in self.list_of_teach])

            
if __name__ == "__main__":
    print(f"The organizations module was imported successfully")
else:
    print(f"{School} contains {dir(School)} methods")