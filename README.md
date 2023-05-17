# OOP-school_report
Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects, which are instances of classes. In OOP, classes define the attributes (data) and behaviors (methods) that objects can have. This approach promotes modular and reusable code by encapsulating related data and functions into objects.

# Project Title: School Report Generator

Project Description:
The School Report Generator is a program designed to automate the process of generating reports for schools. This project aims to streamline the report creation process, making it easier for teachers and administrators to generate comprehensive and organized reports for their schools.

# Features:

- School Information: Provide an interface to input and store essential information about the school, such as the school name, address, contact details, and any other relevant details.

- Student and Teacher Management: Allow users to manage student and teacher information, including names, ages, grades, subjects, and other relevant details. This feature enables the system to maintain an up-to-date database of students and teachers associated with the school.

- __init__.py:
-- The __init__.py file is an empty file that signifies a Python package. It is typically placed in a directory to indicate that the directory should be treated as a package by Python.
The __all__ variable, when defined in __init__.py, specifies which modules should be imported when using the from package import * syntax. It provides a list of module names that should be imported when the package is imported with a wildcard import statement.

- __main__.py:
--The __main__.py file is the entry point of a Python package or module. When executing the package or module directly, this file will be executed. In this file that will be executed when running the package or module as a standalone program.

# organizations.py:
- This file contains the School class, which is responsible for creating a basic description and generating a report about schools. It include methods such as add_student(),add_teacher() and get_report().

# users.py:
- This file defines the parent class Human and its child classes Student and Teacher.
The Human class represents common attributes and behaviors shared by both students and teachers.
The Teacher and Student class contains additional attributes and methods specific to teachers and student such as add_subject(),get_info() and set_school().
