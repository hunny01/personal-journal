'''
***********************************************************************************************************
File Name   :   list_my_journal.py
Description :   This Function Will List All The Existing Journal Entries. This Function Will Also Display:
				* How Many Journal Entries Have Already Been Created
				* How Many Journal Entries User Can Still Create
-----------------------------------------------------------------------------------------------------------
Date							Action						 	Author
27th-JUL-2019					Created							Hunny Aggarwal
***********************************************************************************************************
'''

import csv
import show_title as st
import pandas as pd

def list_my_journal(login_user):	
	#This Function Clears The Terminal Screen, And Displays A Title Bar.
	st.show_title()

	try:
		personal_journal = pd.read_csv(f'Journals\\{login_user}.csv')
		entries_left = 50 - len(personal_journal)
		print('\nPrinting Your Journal !!')
		print('---------------------')
		listed_entries = list(personal_journal.values)
		for single_entry in listed_entries:
			print(single_entry[0] + ' - ' + single_entry[1])
		print(f'\nYour Journal Has {len(personal_journal)} Entries !!')
		print(f'Your Have {entries_left} Entries Left !!\n')
	except:
		print("Your Journal Is Empty !!\n")