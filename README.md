'''
***********************************************************************************************************
File Name   :   ReadMe.txt
Description :   This File Is A Guide On How To User Your Personal Journal Application
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
28th-JUL-2019			Created							Hunny Aggarwal
***********************************************************************************************************
'''

Personal Journal Application Is A Simple And Easy Journal Entry Notebook. This Application Runs On Terminal And Is Capable Of:
* User Management
* Personalized Journal Entry (Upto 50 Entries)

-------------------
1. User Management:
-------------------
* If The Application Is Started For The First Time:
	--System Will Automatically Create "UserManagement.csv" In "My Personal Journal" Directory
* If The Application Is Started For The Second Time Onwards:
	--System Will Read "UserManagement.csv" Present In "My Personal Journal" Directory
	--Create New Entries In This File For Every "Sign-Up" Request
* This Application Is Capable Of Creating The User Database On Its Own
* The User Credentials Are Kept In A CVS File

	---------------------
	1.1 Validation Rules:
	---------------------
	* Login: System Matches The Username And Password Entered By The User With The Credentials Stored In This File
	* Sign-Up: System Performs Two Validations At The Time Of Sign-Up:
		--System Checks If The Username Is Already Registered. If Yes, System Will Throw Error That 'User Already Registered, Please Select A Different User Name'
		--System Checks If The Entered Password With Confirm Password. If Wrong, System Will Throw Error That 'Passwords Do Not Match, Please Enter Again'
	If All The Validations Are Successful, Then Only System Will Navigate To The Welcome Page.

---------------------------------------------------------------------------
2. In Order To Use This Applicaion One Should Follow Below Mentioned Steps:
---------------------------------------------------------------------------
* Open Terminal
* Navigate To This Folder i.e., "My Personal Journal"
* Execute main.py From Terminal By Simply Typing "main.py" And Hit Enter
* User Will Be Asked To:
	[1] Login
	[2] Sign-Up
	[q] Quit

* If User Chooses To Login System Will Redirect The User To The Welcome Page Where User Will See Following Menu Options Will Be Available:
	[1] List Journal Entries
	[2] Create New Journal Entry
	[3] Logout

	------------------------------------------------------
	2.1 Following Is The Detailed Working Of The Function:
	------------------------------------------------------
	[1] List Journal Entries:
	-------------------------
	* Here User Will Be Able To List All The Journal Entries Done By Him/Her
	* Application Will Also Display How Many Journal Entries Are Done And How Many Entries Can Be Done
	
	-----------------------------
	[2] Create New Journal Entry:
	-----------------------------
	* This Option Allows The User To Create New Journal Entries
	* Every Journal Entry Is Entered By The User Is Captured Along With System Time Stamp
	* All The Journals Will Be Created In "Journals" Directory
	* Once User Has Done 50 Entries, System Will Replace The New Entry With The Oldest One
	
	-----------
	[3] Logout:
	-----------
	* Once User Selects This Option, System Will Navigate The User To The Login Page Where Again Below Options Will Be Displayed:
		[1] Login
		[2] Sign-Up
		[q] Quit
	* After This The User Can Further Select To Quit Or Can Login, Sign-Up To Continue Further
