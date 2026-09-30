# Student Grade Management System

## 1. Project Title

**Student Grade Management System**

---

## 2. Introduction

The Student Grade Management System is a Python-based console application developed to manage and analyse the academic performance of students.

In educational institutions, student marks and academic records need to be maintained properly. When these calculations are performed manually, it can take more time and may result in mistakes while calculating totals, percentages, averages, or grades.

This project provides a simple solution by allowing the user to enter student information and marks for different subjects. The program automatically calculates the total marks and percentage and assigns a grade according to the percentage obtained.

The system also provides additional features such as class analysis, updating marks, deleting student records, and finding the top-performing student.

---

## 3. Problem Statement

Managing student academic records manually can be difficult when the number of students increases. Teachers or users may have to calculate total marks, percentages, grades, and class averages separately for every student.

Manual management can lead to:

* Calculation mistakes.
* Difficulty in maintaining records.
* Repeated calculations.
* Difficulty finding the highest-performing student.
* Extra time required to update student marks.
* Difficulty analysing the overall class performance.

Therefore, there is a need for a simple computer-based system that can store student records and perform common academic calculations automatically.

The Student Grade Management System addresses this problem by providing a menu-driven Python application for managing student academic information.

---

## 4. Aim of the Project

The main aim of this project is to develop a simple Python application that can store, manage, and analyse student marks and academic performance.

The project focuses on applying basic Python programming concepts to a practical real-world problem.

---

## 5. Objectives

The major objectives of the project are:

1. To create a simple system for storing student information.
2. To store student names and registration numbers.
3. To record marks for different subjects.
4. To validate marks entered by the user.
5. To calculate the total marks automatically.
6. To calculate the student's percentage.
7. To assign grades based on percentage.
8. To calculate the average percentage of the class.
9. To update the marks of an existing student.
10. To delete student records when required.
11. To identify the top-performing student.
12. To provide a simple menu-based interface.
13. To demonstrate the use of Python dictionaries and loops.
14. To demonstrate exception handling for invalid input.

---

## 6. Scope of the Project

The project is designed for basic academic record management.

The system currently supports five subjects:

* Computer Science
* Mathematics
* Physics
* Chemistry
* English

The user can add multiple students to the system. Each student is identified using a registration number.

The system can then use the stored information to perform calculations and provide academic information.

The project is mainly intended as a beginner-level Python programming project and can be further developed into a larger student management application.

---

## 7. Functional Requirements

The system provides the following major functions.

### 7.1 Add a New Student

The user can add a new student by entering:

* Student name
* Registration number
* Marks in Computer Science
* Marks in Mathematics
* Marks in Physics
* Marks in Chemistry
* Marks in English

The marks must be between 0 and 100.

---

### 7.2 View an Existing Student

The user can search for a student using the registration number.

If the student exists, the system displays:

* Student name
* Registration number
* Total marks
* Percentage
* Grade

If the registration number is not found, the system displays an appropriate message.

---

### 7.3 Class Analysis

The class analysis option provides basic information about the stored students.

It calculates:

* Total number of students.
* Average percentage of the class.

This helps the user understand the overall academic performance of the students.

---

### 7.4 Update Student Details

The system allows the user to update the marks of an existing student.

The user enters the registration number and provides new marks for all five subjects.

The updated marks replace the previous marks stored in the system.

---

### 7.5 Delete Student

The user can delete an existing student record by entering the student's registration number.

If the registration number exists, the corresponding record is removed.

If the registration number does not exist, the system informs the user that the student was not found.

---

### 7.6 Find Top Performer

The system compares the percentages of all stored students.

It identifies the student having the highest percentage and displays:

* Student name
* Registration number
* Percentage

This feature makes it easier to identify the student with the highest academic performance.

---

### 7.7 Exit

The Exit option terminates the program.

A thank-you message is displayed before the application closes.

---

## 8. Grading Criteria

The system assigns grades according to the calculated percentage.

| Percentage | Grade |
| ---------- | ----- |
| 90% – 100% | A+    |
| 80% – 89%  | A     |
| 70% – 79%  | B     |
| 60% – 69%  | C     |
| 50% – 59%  | D     |
| Below 50%  | F     |

The percentage is calculated using the total marks obtained in the five subjects.

---

## 9. Input Validation

Input validation is included while entering student marks.

The program checks whether the entered marks are within the valid range of 0 to 100.

If the user enters a value outside this range, the program displays an error message and asks for the marks again.

The program also uses exception handling to manage invalid numerical input.

For example, if the user enters text instead of a number while entering marks, the program displays:

`Invalid input! please enter numbers only`

This prevents the program from terminating because of an invalid marks entry.

---

## 10. Data Storage

The project uses a Python dictionary named `student` to store student information.

The registration number is used as the key.

Each student record contains:

* Name
* Marks

The marks are stored in another dictionary containing the subjects and their respective marks.

A simplified representation of the data structure is:

```text
student
   |
   |-- Registration Number
           |
           |-- Name
           |
           |-- Marks
                  |
                  |-- Computer Science
                  |-- Maths
                  |-- Physics
                  |-- Chemistry
                  |-- English
```

This structure makes it possible to access student information using the registration number.

---

## 11. Technologies Used

### Programming Language

**Python**

### Python Concepts Used

The project uses several fundamental Python concepts:

* Variables
* Dictionaries
* Lists
* Loops
* `while` loop
* `for` loop
* Conditional statements
* `if-elif-else`
* User input
* Type conversion
* `sum()`
* Exception handling
* `try-except`
* Dictionary operations
* Mathematical calculations

---

## 12. Program Workflow

The general workflow of the system is:

```text
Start
  |
  v
Display Welcome Message
  |
  v
Display Menu
  |
  v
User Selects an Option
  |
  +---- Add Student
  |
  +---- View Student
  |
  +---- Class Analysis
  |
  +---- Update Student
  |
  +---- Delete Student
  |
  +---- Find Top Performer
  |
  +---- Exit
  |
  v
Perform Selected Operation
  |
  v
Display Result
  |
  v
Return to Menu
  |
  v
Exit when option 7 is selected
```

---

## 13. Algorithm

### Step 1

Start the program.

### Step 2

Create an empty dictionary to store student records.

### Step 3

Display the Student Grade Management System menu.

### Step 4

Ask the user to select an option.

### Step 5

If the user selects Add Student:

* Enter the student's name.
* Enter the registration number.
* Enter marks for five subjects.
* Validate the marks.
* Store the information in the dictionary.

### Step 6

If the user selects View Student:

* Ask for the registration number.
* Search for the student.
* Calculate total marks.
* Calculate percentage.
* Assign the appropriate grade.
* Display the result.

### Step 7

If the user selects Class Analysis:

* Count the number of students.
* Calculate each student's percentage.
* Calculate the class average.
* Display the result.

### Step 8

If the user selects Update Student:

* Ask for the registration number.
* Check whether the student exists.
* Enter new marks.
* Update the stored marks.

### Step 9

If the user selects Delete Student:

* Ask for the registration number.
* Check whether the student exists.
* Delete the record.

### Step 10

If the user selects Find Top Performer:

* Check all student records.
* Calculate each student's percentage.
* Compare the percentages.
* Store the highest percentage.
* Display the corresponding student's information.

### Step 11

If the user selects Exit, terminate the program.

### Step 12

If an invalid menu option is entered, display an error message.

---

## 14. Expected Input

The program accepts the following types of input:

```text
Student Name
Registration Number
Computer Science Marks
Maths Marks
Physics Marks
Chemistry Marks
English Marks
Menu Choice
```

Marks are expected to be numerical values between 0 and 100.

---

## 15. Expected Output

After successfully adding a student, the system displays:

```text
STUDENT ADDED SUCCESSFULLY
```

When viewing a student, the system displays information similar to:

```text
===== STUDENT GRADE =====
Name : Siddesh
Registration Number : 26BCE10178
Total : 425
Percentage : 85.0 %
Grade : A
```

The exact output depends on the information entered by the user.

---

## 16. Non-Functional Requirements

### 16.1 Simplicity

The system should be simple enough for a beginner to understand and use.

### 16.2 Usability

The menu-based interface allows users to select operations easily.

### 16.3 Accuracy

The system performs calculations automatically to reduce manual calculation errors.

### 16.4 Reliability

Input validation and exception handling help prevent invalid marks from being stored.

### 16.5 Maintainability

The code uses basic Python concepts and can be modified or extended easily.

---

## 17. Limitations

Although the system performs the required operations, it has some limitations.

1. Student records are stored only temporarily.
2. Data is lost when the program is closed.
3. The project does not use a database.
4. The application does not have a graphical user interface.
5. There is no login or authentication system.
6. The system currently supports five predefined subjects.
7. It is designed for console-based use.

---

## 18. Future Enhancements

The project can be improved in the future by adding:

* Database storage using SQLite or MySQL.
* A graphical user interface.
* Student login functionality.
* Teacher or administrator login.
* Attendance management.
* Subject-wise performance analysis.
* Report card generation.
* Exporting student records to CSV or Excel.
* Searching students by name.
* Sorting students according to percentage.
* More detailed class statistics.
* Automatic report generation.
* Support for different numbers of subjects.

These improvements could transform the basic console application into a more complete academic management system.

---

## 19. Educational Value

This project provides practical experience with fundamental Python programming.

By developing this project, the programmer can understand how programming concepts can be applied to solve a real-world problem.

The project demonstrates the use of:

* Data structures for storing information.
* Loops for repeated operations.
* Conditions for decision-making.
* Exception handling for invalid input.
* Mathematical operations for academic calculations.
* Dictionaries for structured data management.

---

## 20. Conclusion

The Student Grade Management System is a simple Python-based application created to manage student academic records.

It allows users to add, view, update, and delete student records. It also calculates total marks and percentages, assigns grades, analyses class performance, and identifies the top-performing student.

The project demonstrates how basic Python programming concepts can be combined to create a useful console-based application.

Although the current version has limitations such as temporary data storage and a console-only interface, it provides a strong foundation for developing a more advanced student management system in the future.

---

## 21. Author

**Name:** Deepanshu Kumar
**Course:** B.Tech CSE Core
**College:** VIT Bhopal University
**Programming Language:** Python
**Project Type:** Console-Based Application

---

## 22. Project Status

**Status:** Completed

 
