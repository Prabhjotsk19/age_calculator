# ---------------  AGE CALCULATOR  ---------------
'''
WRITTEN  BY : Prabhjot Singh

'''

print("Age Calculator to calculate your Age as choice of your Date !!! ")

# Age of Person 
Age_of_Person = [0, 0, 0]

# DATE 0F BIRTH STORE HERE
Date_of_birth = []

# DATE ENTER BY USER STORE HERE
Date_enter_by_User = []

# Input from User about his Date of Birth
DOB = input("Enter your Date of birth in dd/mm/yyyy format: ")

# Input from User about his choice Date 
User_Entry = input("Enter Date to which you want to calculate your age in dd/mm/yyyy format: ")

# To split the DOB to store it in Date_of_birth list
Date_of_birth = DOB.split("/")

 # To split the User_Entry to store it in Date_enter_by_User list
Date_enter_by_User = User_Entry.split("/")


# To change every element of Date_of_birth from string to int data type
index1 = 0	
for i in Date_of_birth:
	Date_of_birth[index1] = int(i)
	index1 += 1


# To change every element of Date_enter_by_User from string to int data type
index2 = 0
for j in Date_enter_by_User:
	Date_enter_by_User[index2] = int(j)
	index2 += 1

# logic to calculate the age of person
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


