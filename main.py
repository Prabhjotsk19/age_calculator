# ---------------  AGE CALCULATOR  ---------------
# By Prabhjot Singh

print("Age Calculator to calculate your Age as choice of your Date !!! ")

# Age of Person 
Age_of_Person = [0, 0, 0]

# Date of birth store here
Date_of_birth = []

# Date enter by user store here
Date_enter_by_User = []

DOB = input("Enter your Date of birth in dd/mm/yyyy format: ")
User_Entry = input("Enter Date to which you want to calculate your age in dd/mm/yyyy format: ")

# To split the DOB to store it in Date_of_birth list
Date_of_birth = DOB.split("/")

# To split the User_Entry to store it in Date_enter_by_User list
Date_enter_by_User = User_Entry.split("/")

# To change every element of Date_of_birth list from string to int
index1 = 0	
for item1 in Date_of_birth:
	Date_of_birth[index1] = int(item1)
	index1 += 1

# To change every element of Date_enter_by_User list from string to int
index2 = 0
for item2 in Date_enter_by_User:
	Date_enter_by_User[index2] = int(item2)
	index2 += 1

# Logic to calculate the age of person
if Date_enter_by_User[0] > Date_of_birth[0]:
	Age_of_Person[0] = Date_enter_by_User[0] - Date_of_birth[0]
else:
	Age_of_Person[0] = (Date_enter_by_User[0] + 30) - Date_of_birth[0]
	Date_enter_by_User[1] -= 1

if Date_enter_by_User[1] > Date_of_birth[1]:
	Age_of_Person[1] = Date_enter_by_User[1] - Date_of_birth[1]
else:
	Age_of_Person[1] = (Date_enter_by_User[1] + 12) - Date_of_birth[1]
	Date_enter_by_User[2] -= 1

Age_of_Person[2] = Date_enter_by_User[2] - Date_of_birth[2]

print(f"Age of Person is {Age_of_Person[2]} years, {Age_of_Person[1]} months and {Age_of_Person[0]} days!")
print("That's Great!")
