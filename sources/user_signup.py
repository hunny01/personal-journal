'''
***********************************************************************************************************
File Name   :   user_signup.py
Description :   This Is The Sign-Up Page Where User Will Enter The Username And Password
				* Un-Successful Login: System Will Raise Approprate Error
				* Successful Login: System Will Redirect The User To The Welcome Page
					@ System Will Update The User Database
					@ System Will Create An Empty Journal For The New Registered User
					@ System Will Redirect The User To The Login Page
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import csv
import pandas as pd
import welcome as wlc


def user_signup():
	#This Function Will Allow The User To Login, Sign-Up Or Quit
	print('New User Registeration')

	#Taking Inputs From User For Username And Password
	login_user = input("Enter Username: ")
	login_password = input("Enter Password: ")
	confirm_password = input("Enter Password To Confirm: ")
	
	#Checking If User Is Already Registered Or Not
	my_database = pd.read_csv('UserManagement.csv')
	registered_users = my_database.values
	for i in range(len(registered_users)):
		if login_user == registered_users[i][0]:
			print('User Already Registered, Please Select A Different User Name')
			#Returning To Sign-Up Page Again, Since User Is Already Registered
			return user_signup()

	#Confirming Password
	if(login_password != confirm_password):
		print('Passwords Do Not Match, Please Enter Again')
	else:
		#Updating User Database
		new_user = [login_user, login_password]
		with open('UserManagement.csv', 'a', newline = '') as f:
			writer = csv.writer(f)
			writer.writerow(new_user)
 
		#Creating Empty Journal File In The Directory
		pd.DataFrame().to_csv(f'Journals\\{login_user}.csv')

		print('Sign Up Successfull. Your Personal Journal Has Been Created')
		return wlc.welcome(login_user)