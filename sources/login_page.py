'''
***********************************************************************************************************
File Name   :   login_page.py
Description :   This Function Will Display The Login Page. User Can
				* Login
				* Sign Up
				* Quit
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

def login_page():
	#This Function Will Allow The User To Login, Sign-Up Or Quit
	print("\n[1] Login")
	print("[2] Sign Up")
	print("[q] Quit")
	my_choice = input("\nWhat Would You Like To Do? ")
	return my_choice