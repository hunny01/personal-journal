'''
***********************************************************************************************************
File Name   :   welcome.py
Description :   This Is The Welcome Page, Which Users Will See Once They Login
				System Will Greet Them With Their Name. Here User Will Be Able To:
				* Select List Journal: Which Will List All The Journal Entries
				* Create New Journal Entry: Which Will Allow The User To Create New Journal Entry
				* Logout: User Will Be Redirected To The Login Page
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import show_title as st
import list_my_journal as lmj
import edit_my_journal as emj
import user_login as ul

def welcome(login_user):
	#This Function Clears The Terminal Screen, And Displays A Title Bar.
	st.show_title()

	#This Function Will Allow The User To Login, Sign-Up Or Quit
	user_action = ''
	print(f'Welcome {login_user.title()}')
	while user_action != 'q':
		print("[1] List Journal Entries")
		print("[2] Create New Journal Entry")
		print("[3] Logout")
		user_action = input("\nWhat Would You Like To Do? ")

		st.show_title()
		if user_action == '1':
			lmj.list_my_journal(login_user)
		elif user_action == '2':
			emj.edit_my_journal(login_user)
		elif user_action == '3':
			#User Will Be Redirected To The Login Page
			print(f"Bye {login_user} !!")
			return
		else:
			print("\nWrong Choice, Please Enter Again.\n")