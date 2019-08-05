'''
***********************************************************************************************************
File Name   :   main.py
Description :   This Is Personal Journal Application Which Stores Journal Entries Entered By Various Users.
				* Any New User Can Register For This Application
				* Each User Has Access To His/Her Own Journal Only
				* Atmost 50 Entries Can Be Made In A Single Journal
				* New ENtries After 50th Entry Will Be Replace By An Oldest Entry
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import os
import csv
import show_title as st
import user_login as ul
import user_signup as us
import login_page as lp
import pandas as pd

# This Is A Banner Which Will Stay On Each And Every Page
st.show_title()

#Creating User Management Database If Not Already Created
try:
	my_database = pd.read_csv('UserManagement.csv')
	
	#Raising Exception In Case User Database Is Empty
	if(len(my_database) == 0):
		raise

	#Application Will Ask The User To Either Login, Sign-Up Or Quit
	choice = ''
	while choice != 'q':
		choice = lp.login_page()
		st.show_title()
		if choice == '1':
			ul.user_login()
		elif choice == '2':
			us.user_signup()
		elif choice == 'q':
			print("\nBye.")
		else:
			print("\nWrong Choice, Please Enter Again.\n")
except:
	#Creating New User Database For The First Time
	print('Creating Database File')
	my_database = pd.DataFrame().to_csv('UserManagement.csv')

	header = ['Username','Password']
	with open('UserManagement.csv', 'w', newline = '') as f:
		writer = csv.writer(f)
		writer.writerow(header)
	
	#Application Will Ask The User To Sign-Up Or Quit. No Login Option Will Be Available Since There Is No User Registered
	my_database = pd.read_csv('UserManagement.csv')
	st.show_title()
	print("\n[1] Sign Up")
	print("[q] Quit")
	choice = input("\nWhat Would You Like To Do? ")

	if choice == '1':
		us.user_signup()
	elif choice == 'q':
		print("\nBye.")
	else:
		print("\nWrong Choice, Please Enter Again.\n")