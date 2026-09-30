student={}
print("\n~-~-~-~-~- WELCOME TO STUDENT GRADE MANAGEMENT SYSTEM -~-~-~-~-~")
while True:
	
	print("we currently have the following features:-")
	print("1. Add a new Student")
	print("2. View an old Student")
	print("3. Class analysis")
	print("4. Update Student details")
	print("5. Delete Student")
	print("6. Find top performer")
	print("7. Exit")
	c=int(input("Enter the serial number of your choice: "))
	if c==1:
		n=input("Enter the name of the Student: ")
		r=input("Enter the registration number of the Student: ")
		marks={}
		subjects=["Computer science ","Maths","Physics","Chemistry","English"]
		for subject in subjects:
			while True:
				try:
					
					marks[subject]=float(input(f"Enter {subject} marks : "))
					if 0<=marks[subject]<=100:
						break
					else:
						print("Error!, Marks should be between or equal to 0 and 100")
				except ValueError:
					print("Invalid input! please enter numbers only")
			
		student[r]={
		"Name":n,
		"Marks":marks}
		
		print("STUDENT ADDED SUCCESsfully")
		
	elif c==2:
		r=input("Enter the registration number: ")
		if r in student:
			students=student[r]
			marks=students["Marks"]
			
			total=sum(marks.values())
			percentage=total/5
			
			if percentage>=90:
				grade="A+"
			elif percentage>=80:
				grade="A"
				
			elif percentage>=70:
				grade="B"
			elif percentage>=60:
				grade="C"
			
			elif percentage>=50:
				grade="D"
			
			else:
				grade="F"
				
				
			print("\n===== STUDENT GRADE =====")
			print("Name : ", students["Name"])
			print("registration number",r)
			print("Total",total)
			print("Percentage",percentage,'%')
			print("Grade",grade)
		else:
				print("STUDENT NOT FOUND ")
				print("Kindly check the registration number and try again")
	elif c==3:
			if len(student)==0:
				print("No record found")
			else:
				total_percentage=0
				for r,students in student.items():
					marks=students["Marks"]
					total=sum(marks.values())
					percentage=total/5
					
					total_percentage+=percentage
					
					average=total_percentage/len(student)
				print("Number of students = ",len(student))
				print("class Average =" ,round(average),"%")
	elif c==4:
		r=input("Enter the registration number: ")
		if r in student:
			subjects=["Computer science","Maths","Physics","Chemistry","English"]
			for subject in subjects:
				student[r]["Marks"][subject]=float(input(f"Enter new {subject} marks"))
				print("Student marks updated successfully")
		else:
			print("Student not found!")
	elif c==5:
		r=input("Enter the registration number: ")
		if r in student:
			del student[r]
			print("Student deleted successfully")
			
		else:
			print("Student not found!")
	elif c==6:
		if len(student) ==0:
			print("No record available.")
			
		else:
			
				top_r=" "
				top_name=" "
				highest_percentage=0
				
				for r, students in student.items():
					
					total=sum(students["Marks"].values())
					percentage=total/5
					
					if percentage >highest_percentage:
						highest_percentage=percentage
						top_r=r
						top_name=students["Name"]
				print("\n===== TOP PERFORMER =====")
				print("Name",top_name)
				print("Registration number ",top_r)
				print("percentage:",round(highest_percentage,2),"%")
					
	elif c==7:
					print("THANK YOU")
					break
	else:
			print("Invalid Choice")
