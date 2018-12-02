# Exercise 81 - Username and Password Checker
user_dict = {}
username_entry = None
cond_numb, cond_Ulet, cond_len5 = False, False, False
conditions = [cond_numb, cond_Ulet, cond_len5]

with open('users.txt', 'r') as users:
	user_dict = {user.strip('\n'): '' for user in users.readlines()}
	
while username_entry == None or username_entry in user_dict:
	username_entry = input("Enter a username: ")
	if username_entry in user_dict:
		print('Username exists')
	else:
		print('Username is fine')
		user_dict[username_entry] = ''
		break

while any(condition == False for condition in conditions):
	user_pw_entry = input('Enter a password: ')

	if not any(c.isdigit() for c in user_pw_entry):
		print("Password needs at least one number")
		cond_numb = False
	else:
		cond_numb = True
	if not any(c.isupper() for c in user_pw_entry):
		print("Password needs at least one uppercase letter")
		cond_Ulet = False
	else:
		cond_Ulet = True
	if not len(user_pw_entry) >= 5:
		print("Password needs to be at least 5 characters in length")
		cond_len5 = False
	else:
		cond_len5 = True

	conditions = [cond_numb, cond_Ulet, cond_len5]

print("Password is fine")


'''
# ALTERNATIVE SOLUTION
while True:
	usr = input("Enter username: ")
	with open('users.txt', 'r') as file:
		users = file.readlines()
		users = [i.strip('\n') for i in users]
	if usr in users:
		print('Username exists')
		continue
	else:
		print('Username is fine')
		break

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
'''