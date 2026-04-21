# Student Portfolio Program

# Taking input from user
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
phone = input("Enter Phone Number: ")
cgpa = float(input("Enter CGPA: "))

# Calculate percentage (assuming CGPA out of 10)
percentage = cgpa * 9.5

# Displaying student details
print("\n--- Student Details ---")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Phone No   :", phone)
print("CGPA       :", cgpa)
print("Percentage :", percentage, "%")