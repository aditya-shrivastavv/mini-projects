# This python program extracts the data which is in form of a table from any website
import pandas as pd
import openpyxl
from openpyxl.workbook import Workbook
import random as rn

link = input("paste the link 🤫:")

movies = pd.read_html(link)

# ask the user the table number. 
table_number = int(input("enter the table number 🤫:"))
table_number -= 1

# convert that table into excel file using pandas and openpyxl.
r_number = rn.randint(1,9999)
movies[table_number].to_excel(f"movies{r_number}.xlsx")