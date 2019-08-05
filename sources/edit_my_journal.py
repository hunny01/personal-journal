'''
***********************************************************************************************************
File Name   :   edit_my_journal.py
Description :   This Function Will Allow The User To Create New Entries In The Journal
				* User Can Create Atmost 50 Journal Entries. Once The Limit Is Exceeded
				* System Will Capture The Latest Journal Entry And Will Delete The Oldest Once
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import csv
import show_title as st
import datetime as dt
import pandas as pd

def edit_my_journal(login_user):
	#This Function Clears The Terminal Screen, And Displays A Title Bar.
	st.show_title()

	#Getting Existing DataFrame From The Journal
	personal_journal = pd.read_csv(f"Journals\\{login_user}.csv")
	
	#Converting DataFrame Into List
	final_frame = list(personal_journal.values)
	
	#Creating New Entry By Appending TimeStamp And Takikng Input From User
	new_entry = [str(dt.datetime.now()), input('Please Input Your New Journal Entry: ')]

	#Checking If Length Exceeds 50, Then Deleting Oldest Entry And Keeping New Entry
	if(len(final_frame) == 50):
		final_frame.pop(0)
	final_frame.append(new_entry)
	
	#Writing Data To File
	pd.DataFrame(final_frame).to_csv(f"Journals\\{login_user}.csv", index=False)
	print("Journal Updated !!")