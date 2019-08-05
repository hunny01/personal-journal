'''
***********************************************************************************************************
File Name   :   user_login.py
Description :   This Is The User Login Page Where User Will Enter The Username And Password
				* Successful Login - System Will Redirect The User To The Welcome Page
				* Un-Successful Login - System Will Raise Approprate Error
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import csv
import pandas as pd
import welcome as wlc

def user_login():
	#This Function Will Allow The User To Login, Sign-Up Or Quit
	valid_user = 0

	#Taking Inputs From User For Username And Password
	login_user = input("Enter Username: ")
	login_password = input("Enter Password: ")
	username_and_password = login_user + login_password

	#Reading User Database
	my_database = pd.read_csv('UserManagement.csv')
	my_database['combined_credentials'] = my_database.apply(lambda x:'%s%s' % (x[0],x[1]), axis=1)

	#Checking If User Already Exists Or Not
	for combined_credentials in my_database['combined_credentials']:
		print(username_and_password, combined_credentials)
		if username_and_password == combined_credentials:
			#Login Successful !!
			return wlc.welcome(login_user)
	
	#Invalid Login !!
	print("\n\nYour Username Or Password Is Incorrect, Please Login Again")