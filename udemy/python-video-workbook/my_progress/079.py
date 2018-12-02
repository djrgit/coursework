# Exercise 79 - Password Checker
conditions = False

while conditions == False:
	user_pw_entry = input('Enter a password: ')
	if len(user_pw_entry) >= 5 and \
	    any(c.isdigit() for c in user_pw_entry) and \
	    any(c.isupper() for c in user_pw_entry):
	    conditions = True
	else:
		print("Password is not fine")

print("Password is fine")