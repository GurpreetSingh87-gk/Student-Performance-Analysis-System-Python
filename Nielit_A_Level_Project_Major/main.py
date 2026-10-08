# Nelit A Level Project:- Student Performance Analysis System

import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import webbrowser
import tkinter as tk
from tkinter import messagebox
from CTkTable import CTkTable
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
from datetime import datetime
import time
import math

# ================================================================================

# Load CSV Data
df = pd.read_csv(
     "student_data.csv", 
     dtype={"Student ID": str}
)

# Subject Columns
Subject_columns = [
     "Maths", 
     "Science", 
     "English", 
     "Social Science", 
     "IT"]

Mark_columns = Subject_columns + [
     "Term1",
     "Term2",
     "Term3",
     "Term4"]

df[Mark_columns] = df[Mark_columns].apply(
     pd.to_numeric,
     errors="raise"
).astype(int)

# Calculate Average Marks
df["Average_Marks"] = df[Subject_columns].mean(axis=1)

# Calculate Total Marks
df['Total_Marks(out of 500)'] = df[Subject_columns].sum(axis=1)

# Calculate Pass Percentage
PASS_MARKS = 40

df["Pass_Percentage"] = (
    df[Subject_columns]
    .ge(PASS_MARKS)
    .sum(axis=1)
    / len(Subject_columns)
    * 100
)

# Find Top Performer
top_student = df.loc[
    df["Average_Marks"].idxmax()
]

# Calculate Grade
def get_grade(marks):
     if marks >= 90:
          return "A+"
     elif marks >= 80:
          return "A"
     elif marks >= 70:
          return "B+"
     elif marks >= 60:
          return "B"
     elif marks >= 50:
          return "C"
     elif marks >= 40:
          return "D"
     else:
          return "F"

# Calculate Performance
def get_performance(marks):
     if marks >= 90:
          return "Excellent"
     elif marks >= 75:
          return "Good"
     elif marks >= 60:
          return "Average"
     elif marks >= 40:
          return "Below Average"
     else:
          return "Poor"
     
df["Grade"] = df["Average_Marks"].apply(get_grade)
df["Performance"] = df["Average_Marks"].apply(get_performance)
    
# ================================================================================

# Window
dashboard = ctk.CTk()
dashboard.title("Student Performance Analysis System")
dashboard._state_before_windows_set_titlebar_color = "zoomed"
dashboard.configure(fg_color="#eef2f7")

# Header:-
# Header Card
header = ctk.CTkFrame(
     dashboard,
     width=550,
     height=55,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
header.place(x=420, y=15)
     
# Header Title
header_title = ctk.CTkLabel(
     dashboard,
     text="Welcome to Student Performance Dashboard",
     font=("Segoe UI", 22, "bold"),
     text_color="#0f55f6",
     fg_color="#f8fafc"
)
header_title.place(x=460, y=27)

# ===============================================================================

# Date And Time:-
# -------------
 
def update_time():
     now = datetime.now()
     
     current_time = time.strftime("%I:%M %p")
     date_string = now.strftime("%B %d, %Y")
     
     time_label.configure(text=current_time)
     date_label.configure(text=date_string)

     dashboard.after(1000, update_time)
     
# Time Card     
time_card = ctk.CTkFrame(
     dashboard,
     width=110,
     height=55,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
time_card.place(x=980, y=15)

# Time Label     
time_label = ctk.CTkLabel(
     time_card, 
     text="", 
     font=("Segoe UI", 13), 
     fg_color="#f8fafc"
)
time_label.place(x=27, y=10)

# Date Card
date_card = ctk.CTkFrame(
     dashboard,
     width=160,
     height=55,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
date_card.place(x=1100, y=15)

# Date Lable
date_label = ctk.CTkLabel(
     date_card, 
     text="", 
     font=("Segoe UI", 13),
     fg_color="#f8fafc"
)
date_label.place(x=20, y=10)   

update_time()

# ================================================================================

# Sidebar Navigation:-
# ------------------

# School Image
school_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\school.png"),
     size=(50, 50)
)

# Sidebar Navigation
sidebar_nav = ctk.CTkFrame(
     dashboard,
     width=160,
     height=615,
     fg_color="#7696ff",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18,     
).place(x=15, y=15)

# School Label
school_label = ctk.CTkLabel(
     sidebar_nav,
     text="",
     image=school_img,  
     fg_color="#7696ff",  
).place(x=70, y=30)

# Line 
line_frame = ctk.CTkFrame(
     sidebar_nav,
     width=110,
     height=2,
     bg_color="#ffffff",
     border_width=0
)      
line_frame.place(x=40, y=110) 

# ===============================================================================

# Student Section:-
# --------------
students_window = None

def open_students_window():
     
     global students_window
     
     if students_window is not None and students_window.winfo_exists():
          students_window.focus()
          students_window.lift()
          return
     
     students_window = ctk.CTkToplevel(dashboard)
     students_window.title("Student Section")
     students_window.geometry("1200x700")
     students_window._state_before_windows_set_titlebar_color = "zoomed"
     students_window.configure(fg_color="#eef2f7")
     
     # Header Title Card
     head_title_card = ctk.CTkFrame(
          students_window,
          width=1200,
          height=100,
          fg_color="#295dd6",
          border_color="#dfe5eb",
     )
     head_title_card.place(x=40, y=20)
     
     # Graduation Image
     graduation_image = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-student-64.png"),
          size=(45, 45)
     )
     graduation_image_label = ctk.CTkLabel(
          head_title_card,
          text="",
          image=graduation_image
     )
     graduation_image_label.place(x=20, y=25)
          
     # Header Title
     header = ctk.CTkLabel(
          head_title_card,
          text="Student Management",
          text_color="white",
          font=("Segoe UI", 24, "bold"),
          bg_color="#295dd6"
     )
     header.place(x=90, y=25)
     
     # Paragrapg label     
     paragraph_text = ctk.CTkLabel(
          head_title_card,
          text="Manage and maintain student information.",
          font=("Segoe UI", 12),
          text_color="white",
          bg_color="#295dd6"
     )     
     paragraph_text.place(x=90, y=57)
     
     # School Image2
     school_img2 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\school.png"),
          size=(60, 60)
     )

     # School Label2
     school_label2 = ctk.CTkLabel(
          head_title_card,
          text="",
          image=school_img2
     )
     school_label2.place(x=1100, y=10)
     
     # Main Student Info Section
     student_info_card = ctk.CTkFrame(
          students_window,
          width=1200,
          height=510,
          fg_color="#ecf0f8",
          border_width=1,
          border_color="#dfe5eb",
     )
     student_info_card.place(x=40, y=120)
     
     # Info Manage Card
     info_manage_card = ctk.CTkFrame(
          student_info_card,
          width=1180,
          height=150,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )
     info_manage_card.place(x=10, y=15)
     
     # Search Title
     search_title = ctk.CTkLabel(
          info_manage_card,
          text="Search Student",
          font=("Segoe UI", 12, "bold"),
          text_color="#4b5563"
     )
     search_title.place(x=26, y=10)
     
     # Search Image
     search_img = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\search.png"),
          size=(18, 18)
     )
          
     search_var = ctk.StringVar(value="")
     
     # Search Entry Widget
     search_entry = ctk.CTkEntry(
          info_manage_card,
          placeholder_text="Search by ID or Name",
          width=330,
          height=32,
          font=("Segoe UI", 13, "bold"),
          text_color="#4b5563",
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=5,
          textvariable=search_var
     )
     search_entry.place(x=25, y=43)
       
     def search_student(*args):

          search_text = search_var.get().strip().lower()

          # Start from row 1 because row 0 is the header
          for row_index in range(1, len(table_data2)):

               if row_index % 2 == 1:
                    row_color = "#f9fafb"
               else:
                    row_color = "#ffffff"

               for column_index in range(len(table_data2[0])):

                    table.edit(
                    row=row_index,
                    column=column_index,
                    fg_color=row_color,
                    text_color="#1f2430"
               )
                    
          # If search box is empty, stop here
          if search_text == "":
               return
                    
          for row_index in range(1, len(table_data2)):
               
               student_id = str(table_data2[row_index][0]).strip().lower()
               student_name = str(table_data2[row_index][1]).strip().lower()

               # For Exact match
               if search_text == student_id or search_text == student_name:

               # Highlight ONLY this row
                    for column_index in range(len(table_data2[0])):

                         table.edit(
                              row=row_index,
                              column=column_index,
                              fg_color="#4CAF50",
                              text_color="white"
                         )
                    # Stop after finding the student
                    break
          
     search_var.trace_add("write", search_student)
          
     # Search Img Label
     search_img_label = ctk.CTkLabel(
          search_entry,
          text="",
          image=search_img
     )
     search_img_label.place(x=300, y=2)
       
     # Add Image
     add_img = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-add-48.png"),
          size=(20, 20)
     )
     
     # Add Student Fucntion 
     def open_add_student_window(refresh_student_table):
                    
          add_window = ctk.CTkToplevel()
          add_window.title("Add New Student")
          add_window.geometry("880x530")
          add_window.configure(fg_color="#eef2f7") 
          add_window.resizable(False, False)   
          
          add_window.transient()
          add_window.grab_set()
     
          # New Student Details:-  
          
          # Student ID             
          studentID = ctk.CTkLabel(
               add_window,
               text="Student ID *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563", 
          )
          studentID.place(x=20, y=18)
          studentID_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Student ID (e.g. STU101)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          studentID_Entry.place(x=140, y=18)
          
          # Student Name
          studentName = ctk.CTkLabel(
               add_window,
               text="Student Name *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563",
          )
          studentName.place(x=20, y=68)
          studentName_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Student Name",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          studentName_Entry.place(x=140, y=68)
                    
          # Class          
          class_label = ctk.CTkLabel(
               add_window,
               text="Class *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          class_label.place(x=20, y=118)
          class_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Class",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5                       
          )
          class_Entry.place(x=140, y=118)

          # Gender 
          gender_label = ctk.CTkLabel(
               add_window,
               text="Gender *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          gender_label.place(x=20, y=168)
          gender_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Gender",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          gender_Entry.place(x=140, y=168)   
                 
          # Age       
          age_label = ctk.CTkLabel(
               add_window,
               text="Age *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          age_label.place(x=450, y=18)
          age_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Age",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          age_Entry.place(x=600, y=18)      

          # Attendance Rate
          attendance_rate_label = ctk.CTkLabel(
               add_window,
               text="Attendance Rate *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          attendance_rate_label.place(x=450, y=68)
          attendance_rate_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Attendance Rate (e.g. 95%)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          attendance_rate_Entry.place(x=600, y=68)
          
          # Days Absent
          days_absent_label = ctk.CTkLabel(
               add_window,
               text="Days Absent *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          days_absent_label.place(x=450, y=118)
          days_absent_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Days Absent",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          days_absent_Entry.place(x=600, y=118)            
            
          # Maths Marks    
          maths_marks_label = ctk.CTkLabel(
               add_window,
               text="Maths Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          maths_marks_label.place(x=450, y=168)
          maths_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Maths Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          maths_Entry.place(x=600, y=168) 
                  
          # Line 
          Line_frame2 = ctk.CTkFrame(
               add_window,
               width=750,
               height=2,
               bg_color="#f2f2f2",
               border_width=1
          )      
          Line_frame2.place(x=65, y=230)
          
          # Science Marks         
          science_marks_label = ctk.CTkLabel(
               add_window,
               text="Science Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          science_marks_label.place(x=450, y=268)
          science_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Science Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          science_Entry.place(x=600, y=268)          

          # English Marks
          english_marks_label = ctk.CTkLabel(
               add_window,
               text="English Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          english_marks_label.place(x=450, y=318)
          english_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter English Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          english_Entry.place(x=600, y=318)
          
          # Social Science Marks
          sst_marks_label = ctk.CTkLabel(
               add_window,
               text="SST Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          sst_marks_label.place(x=450, y=368)
          sst_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter SST Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          sst_Entry.place(x=600, y=368)
          
          # IT Marks
          it_marks_label = ctk.CTkLabel(
               add_window,
               text="IT Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          it_marks_label.place(x=450, y=418)
          it_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter IT Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          it_Entry.place(x=600, y=418)
          
          # Term1 Marks
          term1_label = ctk.CTkLabel(
               add_window,
               text="Term1 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term1_label.place(x=20, y=268)
          term1_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Term1 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term1_Entry.place(x=140, y=268)
          
          # Term2 Marks
          term2_label = ctk.CTkLabel(
               add_window,
               text="Term2 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term2_label.place(x=20, y=318)     
          term2_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Term2 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term2_Entry.place(x=140, y=318)          
          
          # Term3 Marks
          term3_label = ctk.CTkLabel(
               add_window,
               text="Term3 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term3_label.place(x=20, y=368)          
          term3_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Term3 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term3_Entry.place(x=140, y=368)
                    
          # Term4 Marks
          term4_label = ctk.CTkLabel(
               add_window,
               text="Term4 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term4_label.place(x=20, y=418)          
          term4_Entry = ctk.CTkEntry(
               add_window,
               width=250,
               height=30,
               placeholder_text="Enter Term4 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term4_Entry.place(x=140, y=418)
          
          # Save Student Button Function          
          def save_student():

               values = {
                    "Student ID": studentID_Entry.get(),
                    "Student Name": studentName_Entry.get(),
                    "Class": class_Entry.get(),
                    "Gender": gender_Entry.get(),
                    "Age": age_Entry.get(),
                    "Attendance Rate": attendance_rate_Entry.get(),
                    "Days Absent": days_absent_Entry.get(),

                    "Maths": maths_Entry.get(),
                    "Science": science_Entry.get(),
                    "English": english_Entry.get(),
                    "Social Science": sst_Entry.get(),
                    "IT": it_Entry.get(),

                    "Term1": term1_Entry.get(),
                    "Term2": term2_Entry.get(),
                    "Term3": term3_Entry.get(),
                    "Term4": term4_Entry.get()
               }

               # Check empty fields
               if any(str(v).strip() == "" for v in values.values()):
                    messagebox.showerror("Error", "Please fill all fields.")
                    return

               # Add new row to CSV
               new_row = pd.DataFrame([values])

               new_row.to_csv(
               "student_data.csv",
               mode="a",
               header=False,
               index=False
               )

               # Add student to existing table data
               table_data2.append(values)

               # Update table
               table.update_values(table_data2)

               messagebox.showinfo("Success", "Student added successfully!")

               add_window.destroy()
               
          # Add Student Image                    
          save_btn_img = ctk.CTkImage(
               light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-add-48.png"),
               size=(20, 20)
          )
          # Add Student Button
          save_btn = ctk.CTkButton(
               add_window,
               text="Add Student",
               text_color="white",
               font=("Segoe UI", 12, "bold"),
               width=120,
               height=30,
               fg_color="#22d13c",
               bg_color="#f8fafc",
               hover_color="#22b122",
               image=save_btn_img,
               corner_radius=8,
               command=save_student
          )    
          save_btn.place(x=20, y=475) 
                                                          
     # Add button
     add_btn = ctk.CTkButton(
          info_manage_card,
          width=100,
          height=30,
          text="Add Student",
          font=("Segoe UI", 12, "bold"),
          text_color="white",
          fg_color="#22d13c",
          bg_color="#f8fafc",
          hover_color="#22b122",
          corner_radius=8,
          image=add_img,
          command=lambda: open_add_student_window(refresh_student_table)
     )
     add_btn.place(x=25, y=100)
          
     # ==========================
          
     # Update Image
     edit_img = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-edit-48.png"),
          size=(20, 20)
     )
     
     # Update Student Function
     def open_update_student_window():
                         
          update_window = ctk.CTkToplevel()
          update_window.title("Update Student")
          update_window.geometry("880x530")
          update_window.configure(fg_color="#eef2f7") 
          update_window.resizable(False, False)   
               
          update_window.transient()
          update_window.grab_set()
          
          # Update Student Details:-  
               
          # Student ID             
          studentID = ctk.CTkLabel(
                    update_window,
                    text="Student ID *",
                    font=("Segoe UI", 14, "bold"),
                    text_color="#4b5563", 
          )
          studentID.place(x=20, y=18)
          studentID_Entry = ctk.CTkEntry(
                    update_window,
                    width=250,
                    height=30,
                    placeholder_text="Enter Student ID (e.g. STU101)",
                    font=("Segoe UI", 13),
                    text_color="#4b5563",
                    fg_color="#f8fafc",
                    border_width=1,
                    border_color="#dfe5eb",
                    corner_radius=5
               )
          studentID_Entry.place(x=140, y=18)
               
          # Student Name
          studentName = ctk.CTkLabel(
               update_window,
               text="Student Name *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563",
          )
          studentName.place(x=20, y=68)
          studentName_Entry = ctk.CTkEntry(
                    update_window,
                    width=250,
                    height=30,
                    placeholder_text="Enter Student Name",
                    font=("Segoe UI", 13),
                    text_color="#4b5563",
                    fg_color="#f8fafc",
                    border_width=1,
                    border_color="#dfe5eb",
                    corner_radius=5
          )
          studentName_Entry.place(x=140, y=68)
                         
          # Class          
          class_label = ctk.CTkLabel(
               update_window,
               text="Class *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          class_label.place(x=20, y=118)
          class_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Class",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5                       
          )
          class_Entry.place(x=140, y=118)
     
          # Gender 
          gender_label = ctk.CTkLabel(
               update_window,
               text="Gender *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          gender_label.place(x=20, y=168)
          gender_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Gender",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          gender_Entry.place(x=140, y=168)   
                      
          # Age       
          age_label = ctk.CTkLabel(
               update_window,
               text="Age *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          age_label.place(x=450, y=18)
          age_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Age",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          age_Entry.place(x=600, y=18)      
     
          # Attendance Rate
          attendance_rate_label = ctk.CTkLabel(
               update_window,
               text="Attendance Rate *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          attendance_rate_label.place(x=450, y=68)
          attendance_rate_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Attendance Rate (e.g. 95%)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          attendance_rate_Entry.place(x=600, y=68)
               
          # Days Absent
          days_absent_label = ctk.CTkLabel(
               update_window,
               text="Days Absent *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          days_absent_label.place(x=450, y=118)
          days_absent_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Days Absent",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          days_absent_Entry.place(x=600, y=118)            
                 
          # Maths Marks    
          maths_marks_label = ctk.CTkLabel(
               update_window,
               text="Maths Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          maths_marks_label.place(x=450, y=168)
          maths_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Maths Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          maths_Entry.place(x=600, y=168) 
                       
          # Line 
          Line_frame2 = ctk.CTkFrame(
               update_window,
               width=750,
               height=2,
               bg_color="#f2f2f2",
               border_width=1
          )      
          Line_frame2.place(x=65, y=230)
               
          # Science Marks         
          science_marks_label = ctk.CTkLabel(
               update_window,
               text="Science Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          science_marks_label.place(x=450, y=268)
          science_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Science Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          science_Entry.place(x=600, y=268)          
     
          # English Marks
          english_marks_label = ctk.CTkLabel(
               update_window,
               text="English Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          english_marks_label.place(x=450, y=318)
          english_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter English Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          english_Entry.place(x=600, y=318)
               
          # Social Science Marks
          sst_marks_label = ctk.CTkLabel(
               update_window,
               text="SST Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          sst_marks_label.place(x=450, y=368)
          sst_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter SST Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          sst_Entry.place(x=600, y=368)
               
          # IT Marks
          it_marks_label = ctk.CTkLabel(
               update_window,
               text="IT Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"
          )
          it_marks_label.place(x=450, y=418)
          it_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter IT Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          it_Entry.place(x=600, y=418)
               
          # Term1 Marks
          term1_label = ctk.CTkLabel(
               update_window,
               text="Term1 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term1_label.place(x=20, y=268)
          term1_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Term1 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term1_Entry.place(x=140, y=268)
               
          # Term2 Marks
          term2_label = ctk.CTkLabel(
               update_window,
               text="Term2 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term2_label.place(x=20, y=318)     
          term2_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Term2 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term2_Entry.place(x=140, y=318)          
               
          # Term3 Marks
          term3_label = ctk.CTkLabel(
               update_window,
               text="Term3 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term3_label.place(x=20, y=368)          
          term3_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Term3 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term3_Entry.place(x=140, y=368)
                         
          # Term4 Marks
          term4_label = ctk.CTkLabel(
               update_window,
               text="Term4 Marks *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563"        
          )
          term4_label.place(x=20, y=418)          
          term4_Entry = ctk.CTkEntry(
               update_window,
               width=250,
               height=30,
               placeholder_text="Enter Term4 Marks (0-100)",
               font=("Segoe UI", 13),
               text_color="#4b5563",
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
          )
          term4_Entry.place(x=140, y=418)

          entries = {
               "Maths": maths_Entry,
               "Science": science_Entry,
               "English": english_Entry,
               "Social Science": sst_Entry,
               "IT": it_Entry,
               "Term1": term1_Entry,
               "Term2": term2_Entry,
               "Term3": term3_Entry,
               "Term4": term4_Entry,
          }

          # Update Student Main Function
          def update_student():

               global df

               student_id = studentID_Entry.get().strip()

               if student_id not in df["Student ID"].astype(str).values:
                    messagebox.showerror("Error", "Student ID not found!")
                    return

               index = df.index[
               df["Student ID"].astype(str) == student_id
               ][0]

               df.loc[index, "Student Name"] = studentName_Entry.get().strip()
               df.loc[index, "Class"] = class_Entry.get().strip()
               df.loc[index, "Gender"] = gender_Entry.get().strip()
               df.loc[index, "Age"] = age_Entry.get().strip()
               df.loc[index, "Attendance Rate"] = attendance_rate_Entry.get().strip()
               df.loc[index, "Days Absent"] = days_absent_Entry.get().strip()

               # Update Marks as Integer
               try:
                    for subject, entry in entries.items():
                         df.loc[index, subject] = int(float(entry.get().strip()))

               except ValueError:
                    messagebox.showerror(
                         "Invalid Marks",
                         "Please enter valid integer values for marks."
                    )
                    return
          
               df.to_csv("student_data.csv", index=False)

               refresh_student_table()

               messagebox.showinfo("Success", "Student updated successfully!")

               update_window.destroy()
          
          # Save/Update Image                    
          save_btn_img = ctk.CTkImage(
               light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-edit-48.png"),
               size=(20, 20)
          )
          # Save/Update Button
          save_btn = ctk.CTkButton(
               update_window,
               text="Update Student",
               text_color="white",
               font=("Segoe UI", 12, "bold"),
               width=123,
               height=30,
               fg_color="#4188f1",
               bg_color="#f8fafc",
               hover_color="#366ae4",
               image=save_btn_img,
               corner_radius=8,
               command=update_student
          )    
          save_btn.place(x=20, y=475)          
               
     # Update button
     edit_btn = ctk.CTkButton(
          info_manage_card,
          width=100,
          height=30,
          text="Update Student",
          font=("Segoe UI", 12, "bold"),
          text_color="white",
          fg_color="#4188f1",
          bg_color="#f8fafc",
          hover_color="#366ae4",
          corner_radius=12,
          image=edit_img,
          command=open_update_student_window
     )
     edit_btn.place(x=160, y=100)
     
     # Delete Image
     delete_img = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-delete-48.png"),
          size=(20, 20)
     )
     
     # Delete Student Function
     def open_delete_student_window():
          delete_window = ctk.CTkToplevel()
          delete_window.title("Delete Student")
          delete_window.geometry("450x200")
          delete_window.configure(fg_color="#eef2f7") 
          delete_window.resizable(False, False)   
               
          delete_window.transient()
          delete_window.grab_set() 

          # Delete Student Details:-
          
          # Student ID             
          studentID = ctk.CTkLabel(
                    delete_window,
                    text="Student ID *",
                    font=("Segoe UI", 14, "bold"),
                    text_color="#4b5563", 
          )
          studentID.place(x=20, y=18)
          studentID_Entry = ctk.CTkEntry(
                    delete_window,
                    width=250,
                    height=30,
                    placeholder_text="Enter Student ID (e.g. STU101)",
                    font=("Segoe UI", 13),
                    text_color="#4b5563",
                    fg_color="#f8fafc",
                    border_width=1,
                    border_color="#dfe5eb",
                    corner_radius=5
               )
          studentID_Entry.place(x=140, y=18)
               
          # Student Name
          studentName = ctk.CTkLabel(
               delete_window,
               text="Student Name *",
               font=("Segoe UI", 14, "bold"),
               text_color="#4b5563",
          )
          studentName.place(x=20, y=68)
          studentName_Entry = ctk.CTkEntry(
                    delete_window,
                    width=250,
                    height=30,
                    placeholder_text="Enter Student Name",
                    font=("Segoe UI", 13),
                    text_color="#4b5563",
                    fg_color="#f8fafc",
                    border_width=1,
                    border_color="#dfe5eb",
                    corner_radius=5
          )
          studentName_Entry.place(x=140, y=68)           
          
          def delete_student():

               global df

               student_id = studentID_Entry.get().strip()
               student_name = studentName_Entry.get().strip()

               if not student_id or not student_name:
                    messagebox.showerror(
                    "Error","Please enter Student ID and Student Name.")
                    return

               # Find student using BOTH ID and Name
               match = (
               (df["Student ID"].astype(str).str.strip() == student_id) &
               (df["Student Name"].astype(str).str.strip().str.lower() == student_name.lower())
               )

               if not match.any():
                    messagebox.showerror("Error", "Student ID and Student Name do not match.")
                    return

               confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {student_name}?")

               if not confirm:
                    return

               # Delete student
               df = df.loc[~match].reset_index(drop=True)

               # Save updated CSV
               df.to_csv("student_data.csv", index=False)

               # Refresh Student Table
               refresh_student_table()

               messagebox.showinfo("Success", f"{student_name} deleted successfully!")

               delete_window.destroy()     
                    
          # Delete Student Image                    
          save_btn_img = ctk.CTkImage(
               light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-delete-48.png"),
               size=(20, 20)
          )
          # Delete Student Button
          save_btn = ctk.CTkButton(
               delete_window,
               text="Delete Student",
               text_color="white",
               font=("Segoe UI", 12, "bold"),
               width=123,
               height=30,
               fg_color="#f44b4b",
               bg_color="#f8fafc",
               hover_color="#d53939",
               image=save_btn_img,
               corner_radius=8,
               command=delete_student
          )    
          save_btn.place(x=170, y=140)                    
                             
     # Delete button
     delete_btn = ctk.CTkButton(
          info_manage_card,
          width=100,
          height=30,
          text="Delete Student",
          font=("Segoe UI", 12, "bold"),
          text_color="white",
          fg_color="#f44b4b",
          bg_color="#f8fafc",
          hover_color="#d53939",
          corner_radius=12,
          image=delete_img,
          command=open_delete_student_window
     )
     delete_btn.place(x=320, y=100)
     
     # Table
     table_card2 = ctk.CTkFrame(
          student_info_card,
          width=1160,
          height=310,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18,
     )
     table_card2.place(x=20, y=180)

     # Create table data  from CSV
     table_data2 = [["Student ID",
               "Student Name",
               "Class",
               "Gender",
               "Age",
               "Attendance Rate",
               "Days Absent",
               "Maths",
               "Science",
               "English",
               "Social Science",
               "IT",
               "Total_Marks(out of 500)",
               "Term1",
               "Term2",
               "Term3",
               "Term4",
               "Average_Marks",
               "Pass_Percentage",
               "Grade",
               "Performance"]]

     for _, student in df.iterrows():
          table_data2.append([
          student["Student ID"],
          student["Student Name"],
          student["Class"],
          student["Gender"],
          student["Age"],
          f"{student['Attendance Rate']}",
          student["Days Absent"],
          student["Maths"],
          student["Science"],
          student["English"],
          student["Social Science"],
          student["IT"],
          student["Total_Marks(out of 500)"],
          student["Term1"],
          student["Term2"],
          student["Term3"],
          student["Term4"],
          f"{student['Average_Marks']}%",
          f"{student['Pass_Percentage']}%",
          student["Grade"],
          student["Performance"]
     ])
    
     # Scrollable table container for smooth vertical and horizontal scrolling
     canvas = ctk.CTkCanvas(
          table_card2,
          bg="#f8fafc",
          highlightthickness=0,
          width=1700,
          height=425,
     )
     canvas.place(x=20, y=12)

     x_scrollbar = ctk.CTkScrollbar(
          table_card2,
          orientation="horizontal",
          command=canvas.xview,
          width=12,
          height=12,
          button_color="#f8fafc",
          button_hover_color="#f8fafc",
     )
     x_scrollbar.place(x=12, y=290)

     y_scrollbar = ctk.CTkScrollbar(
          table_card2,
          orientation="vertical",
          command=canvas.yview,
          width=12,
          height=236,
          button_color="#f8fafc",
          button_hover_color="#f8fafc",
     )
     y_scrollbar.place(x=1145, y=12)

     canvas.configure(
          xscrollcommand=x_scrollbar.set, 
          yscrollcommand=y_scrollbar.set
     )

     scrollable_table = ctk.CTkFrame(
          canvas, 
          fg_color="#ffffff"
     )
     canvas_window = canvas.create_window((0, 0), window=scrollable_table, anchor="nw")

     table = CTkTable(
          master=scrollable_table,
          row=len(table_data2),
          column=len(table_data2[0]),
          values=table_data2,
          font=("Segoe UI", 12, "bold"),
          header_color="#dbeafe",
          hover_color="#bbd8fd",
          text_color="#1f2430",
          bg_color="#f8fafc",
          colors=["#f9fafb", "#ffffff"],
          width=100,
          height=30,
     )
     table.pack(fill="both", expand=True)
     search_var.trace_add("write", search_student)

     def update_scroll_region(event=None):
          canvas.configure(scrollregion=canvas.bbox("all"))
          canvas.itemconfig(canvas_window, width=max(canvas.winfo_width(), table.winfo_reqwidth() + 30))
          canvas.itemconfig(canvas_window, height=max(canvas.winfo_height(), table.winfo_reqheight() + 30))

     scrollable_table.bind("<Configure>", update_scroll_region)
     table.bind("<Configure>", update_scroll_region)
     canvas.bind("<Configure>", update_scroll_region)

     def smooth_scroll(event):
          if event.state & 0x1:  # Shift key pressed for horizontal scroll
               canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
          else:
               canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

     canvas.bind_all("<MouseWheel>", smooth_scroll)

     # Keep the table fully visible and scrollable when content changes
     update_scroll_region()
     
     # Function to recalculate for a new student
     def refresh_student_table():

          global df
          nonlocal table, table_data2
          
          # Reload CSV
    
          df = pd.read_csv(
               "student_data.csv",
               dtype={"Student ID": str}
          )
          
          # Convert marks and term marks to integers
          df[Mark_columns] = df[Mark_columns].apply(
               pd.to_numeric,
               errors="raise"
          ).astype(int)
          
          # Update Total Students
          number_stu.configure(text=str(len(df)))
          
          # Recalculate Average Marks
          df["Average_Marks"] = df[Subject_columns].mean(axis=1)

          # Recalculate Pass Percentage
          df["Pass_Percentage"] = (
               df[Subject_columns]
               .ge(PASS_MARKS)
               .sum(axis=1)
               / len(Subject_columns)
               * 100
          )

          # Recalculate Grade
          df["Grade"] = df["Average_Marks"].apply(get_grade)

          # Recalculate Performance
          df["Performance"] = df["Average_Marks"].apply(get_performance)


         # CREATE UPDATED TABLE DATA
          new_table_data = [
               [
                    "Student ID",
                    "Student Name",
                    "Class",
                    "Gender",
                    "Age",
                    "Attendance Rate",
                    "Days Absent",
                    "Maths",
                    "Science",
                    "English",
                    "Social Science",
                    "IT",
                    "Term1",
                    "Term2",
                    "Term3",
                    "Term4",
                    "Grade",
                    "Performance"
               ]
          ]

          for _, student in df.iterrows():

               new_table_data.append(
                    [
                         student["Student ID"],
                         student["Student Name"],
                         student["Class"],
                         student["Gender"],
                         student["Age"],
                         f'{student["Attendance Rate"]}%',
                         student["Days Absent"],
                         student["Maths"],
                         student["Science"],
                         student["English"],
                         student["Social Science"],
                         student["IT"],
                         student["Term1"],
                         student["Term2"],
                         student["Term3"],
                         student["Term4"],          
                         student["Grade"],
                         student["Performance"]
                    ]
               )

          # Destroy old table
          table.destroy()
          
          # Create new table
          table = CTkTable(
               master=scrollable_table,
               row=len(new_table_data),
               column=len(new_table_data[0]),
               values=new_table_data,
               font=("Segoe UI", 12, "bold"),
               header_color="#dbeafe",
               hover_color="#bbd8fd",
               text_color="#1f2430",
               bg_color="#f8fafc",
               colors=["#f9fafb", "#ffffff"],
               width=100,
               height=30
          )

          # Reconnect search
          search_var.trace_add("write", search_student)

          # Update scroll area
          update_scroll_region() 
          

# Student
sidenav_btn = ctk.CTkButton(
     sidebar_nav,
     width=110,
     height=30,
     text="Students",
     text_color="black",
     font=("Segoe UI", 15),
     hover_color="#c1bec1",
     corner_radius=18,
     fg_color="#ffffff",
     bg_color="#7696ff",
     command=open_students_window
)
sidenav_btn.place(x=40, y=150)

# ================================================================================

# Analytics Section:-
# ------------------

analytics_window = None

def open_analytics_window():
     
     global analytics_window
     
     if analytics_window is not None and analytics_window.winfo_exists():
          analytics_window.focus()
          analytics_window.lift()
          return
     
     analytics_window = ctk.CTkToplevel(dashboard)
     analytics_window.title("Analytics Section")
     analytics_window.geometry("1200x700")
     analytics_window._state_before_windows_set_titlebar_color = "zoomed"
     analytics_window.configure(fg_color="#eef2f7")
     
     # Header Title Card
     head_title_card = ctk.CTkFrame(
          analytics_window,
          width=1200,
          height=100,
          fg_color="#295dd6",
          border_color="#dfe5eb",
     )
     head_title_card.place(x=40, y=20)
     
     # Trend Image
     trend_image = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-positive-dynamic-50.png"),
          size=(45, 45)
     )
          
     trend_image_label = ctk.CTkLabel(
          head_title_card,
          text="",
          image=trend_image
     )
     trend_image_label.place(x=20, y=25)
     
     # Header Title
     header = ctk.CTkLabel(
          head_title_card,
          text="Analytics Overview",
          text_color="white",
          font=("Segoe UI", 24, "bold"),
          bg_color="#295dd6"
     )
     header.place(x=90, y=25)
     
     # Paragrapg label     
     paragraph_text = ctk.CTkLabel(
          head_title_card,
          text="Explore student performance trends and key insights.",
          font=("Segoe UI", 12),
          text_color="white",
          bg_color="#295dd6"
     )     
     paragraph_text.place(x=90, y=57)
     
     # School Image2
     school_img2 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\school.png"),
          size=(60, 60)
     )

     # School Label2
     school_label2 = ctk.CTkLabel(
          head_title_card,
          text="",
          image=school_img2
     )
     school_label2.place(x=1100, y=10)

     # Main Student Info Section
     student_info_card = ctk.CTkFrame(
          analytics_window,
          width=1200,
          height=510,
          fg_color="#ecf0f8",
          border_width=1,
          border_color="#dfe5eb",
     )
     student_info_card.place(x=40, y=120) 

     # Key Insights Card
     keyinsight_card = ctk.CTkFrame(
          student_info_card,
          width=570,
          height=250,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )
     keyinsight_card.place(x=20, y=10)
     keyinsight_title = ctk.CTkLabel(
          keyinsight_card,
          text="💡 Key Insights",
          font=("Segoe UI", 16, "bold"),
          text_color="#1f2430"
     )
     keyinsight_title.place(x=18, y=8)
     
     ctk.CTkLabel(
          keyinsight_card,
          text="✓ Mathematics has the highest class average 66.3",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=50)   

     ctk.CTkLabel(
          keyinsight_card,
          text="✓ 4 students are performing above 80%",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=80)      

     ctk.CTkLabel(
          keyinsight_card,
          text="⚠ 8 students have attendance below 75%",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=110)            

     ctk.CTkLabel(
          keyinsight_card,
          text="⚠ IT has the lowest subject average 53.8",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=140)

     ctk.CTkLabel(
          keyinsight_card,
          text="✓ George Kennedy is currently the highest-performing student.",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=170)     

     ctk.CTkLabel(
          keyinsight_card,
          text="ℹ 3 students may require additional academic support.",
          font=("Segoe UI", 15, "bold"),
          text_color="#17366d"
     ).place(x=20, y=200)      
          
     # Subject Analytics Card
     sub_anlytics_card = ctk.CTkFrame(
          student_info_card,
          width=570,
          height=250,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )    
     sub_anlytics_card.place(x=610, y=10)
     sub_anlytics_title = ctk.CTkLabel(
          sub_anlytics_card,
          text="📊 Subject Analytics",
          font=("Segoe UI", 16, "bold"),
          text_color="#1f2430"
     )
     sub_anlytics_title.place(x=18, y=8)
     
     miniheader_frame2 = ctk.CTkFrame(
               sub_anlytics_card,
               width=530,
               height=35,
               fg_color="#e7f8dc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
     )
     miniheader_frame2.place(x=20, y=40)
          
     headers = [
          "Subjects",
          "Avg Marks",
          "Strong Students",
          "Weak Students",
          "Highest",
          "Lowest"
     ]
     x_positions = [10, 110, 190, 300, 400, 470]
     
     for header, x in zip(headers, x_positions):
          ctk.CTkLabel(
               miniheader_frame2,
               text=header,
               font=("Segoe UI", 12, "bold"),
               text_color="#17366d"
          ).place(x=x, y=2)
     
     minicontent_frame2 = ctk.CTkFrame(
               sub_anlytics_card,
               width=530,
               height=170,
               fg_color="#f8fafc",
               border_width=1,
               border_color="#dfe5eb",
               corner_radius=5
     )
     minicontent_frame2.place(x=20, y=70)
     
     subjects = [
          "Maths",
          "Science",
          "English",
          "Social Science",
          "IT"
     ]
               
     for row, subject in enumerate(subjects):

          x = 20
          y = 5 + (row * 32)

          avg = df[subject].mean()
          strong = (df[subject] >= 75).sum()
          weak = (df[subject] < 40).sum()
          highest = df[subject].max()
          lowest = df[subject].min()

          values = [
               subject,
               f"{avg:.1f}",
               str(strong),
               str(weak),
               str(int(highest)),
               str(int(lowest))
          ]

          for value, x in zip(values, x_positions):

               ctk.CTkLabel(
                    minicontent_frame2,
                    text=value,
                    font=("Segoe UI", 12),
                    text_color="#17366d"
               ).place(x=x, y=y)
          
     # Performance Distribution Card
     performance_distri_card = ctk.CTkFrame(
          student_info_card,
          width=350,
          height=215,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )
     performance_distri_card.place(x=40, y=285)
     performance_distri_label = ctk.CTkLabel(
          performance_distri_card,
          text="🎯 Performance Distribution",
          font=("Segoe UI", 16, "bold"),
          text_color="#1f2430"
     )
     performance_distri_label.place(x=18, y=8)
     
     performance_counts = df["Performance"].value_counts()
     bars_color = ["#fb6464", "#fbbf24", "#e7f65c", "#61a1f4", "#3ff764"]

     performance_names = [
          "Poor",
          "Below Average",
          "Average",
          "Good",          
          "Excellent"         
     ]
     performance_values = [
          performance_counts.get("Poor", 0),
          performance_counts.get("Below Average", 0),
          performance_counts.get("Average", 0),
          performance_counts.get("Good", 0),
          performance_counts.get("Excellent", 0)
     ]

     performance_fig = Figure(figsize=(4.7, 2.4), dpi=100, facecolor="#f8fafc")
     performance_ax = performance_fig.add_subplot(111)
     performance_ax.set_facecolor("#f8fafc")
     performance_ax.barh(performance_names, performance_values, color=bars_color, height=0.55)


     # Show values at the end of bars
     for i, value in enumerate(performance_values):

          performance_ax.text(
               value + 0.05,
               i,
               str(value),
               va="center",
               fontsize=10
          )

     # Chart settings
     performance_ax.set_xlabel("Number of Students")

     performance_ax.set_xlim(0, max(performance_values) + 2)

     performance_ax.grid(axis="x", color="#e5e7eb")

     performance_ax.set_axisbelow(True)
     performance_ax.spines["top"].set_visible(False)
     performance_ax.spines["right"].set_visible(False)
     performance_ax.spines["left"].set_visible(False)
     performance_fig.tight_layout()

     performance_canvas = FigureCanvasTkAgg(performance_fig, master=performance_distri_card)
     performance_canvas.draw()
     performance_canvas.get_tk_widget().place(x=10, y=60, width=480, height=250)
          
     # High Risk Card
     high_risk_card = ctk.CTkFrame(
          student_info_card,
          width=350,
          height=215,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )
     high_risk_card.place(x=420, y=285)
     high_risk_label = ctk.CTkLabel(
          high_risk_card,
          text="⚠ High Risk Students",
          font=("Segoe UI", 16, "bold"),
          text_color="#1f2430"
     )
     high_risk_label.place(x=18, y=8)
     
     high_risk_header = ctk.CTkFrame(
          high_risk_card,
          width=310,
          height=35,
          fg_color="#fde2e2",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=5
     )
     high_risk_header.place(x=20, y=40)

     high_risk_columns = [
          ("Student", 10),
          ("Avg Marks", 130),
          ("Attendance", 225)
     ]

     for column, x in high_risk_columns:
          ctk.CTkLabel(
               high_risk_header,
               text=column,
               font=("Segoe UI", 12, "bold"),
               text_color="#7f1d1d"
          ).place(x=x, y=2)

     high_risk_content = ctk.CTkFrame(
          high_risk_card,
          width=310,
          height=130,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=5
     )
     high_risk_content.place(x=20, y=70)

     high_risk_students = df[df["Performance"] == "Poor"]

     for row, (_, student) in enumerate(high_risk_students.iterrows()):
          y = 15 + (row * 35)
          values = [
               (student["Student Name"], 10),
               (f'{student["Average_Marks"]:.1f}', 130),
               (f'{student["Attendance Rate"]}', 225)
          ]

          for value, x in values:
               ctk.CTkLabel(
                    high_risk_content,
                    text=value,
                    font=("Segoe UI", 12),
                    text_color="#17366d"
               ).place(x=x, y=y)
     
     # Top 3 Students Card
     topstudents_card = ctk.CTkFrame(
          student_info_card,
          width=350,
          height=215,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=18
     )
     topstudents_card.place(x=820, y=285)    
     topstudents_label = ctk.CTkLabel(
          topstudents_card,
          text="⭐ Top 3 Students",
          font=("Segoe UI", 16, "bold"),
          text_color="#1f2430"
     ) 
     topstudents_label.place(x=18, y=8)    
        
     miniheader_frame = ctk.CTkFrame(
          topstudents_card,
          width=310,
          height=35,
          fg_color="#dcebf8",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=5
     )
     miniheader_frame.place(x=20, y=40)
     
     # Headers
     ctk.CTkLabel(
          miniheader_frame,
          text="Rank",
          font=("Segoe UI", 12, "bold"),
          text_color="#17366d"
     ).place(x=20, y=3)

     ctk.CTkLabel(
          miniheader_frame,
          text="Name",
          font=("Segoe UI", 12, "bold"),
          text_color="#17366d"
     ).place(x=90, y=3)

     ctk.CTkLabel(
          miniheader_frame,
          text="Average Marks",
          font=("Segoe UI", 12, "bold"),
          text_color="#17366d"
     ).place(x=210, y=3)

     minicontent_frame = ctk.CTkFrame(
          topstudents_card,
          width=310,
          height=130,
          fg_color="#f8fafc",
          border_width=1,
          border_color="#dfe5eb",
          corner_radius=5
     )
     minicontent_frame.place(x=20, y=70)     
     
     df["Average_Marks"] = df[Subject_columns].mean(axis=1)
     
     rank_img1 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\quality.png"),
          size=(30, 30)
     )
     
     rank_img2 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\second-prize.png"),
          size=(30, 30)
     )
     
     rank_img3 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\third-prize.png"),
          size=(30, 30)
     )
     
     top_3 = df.nlargest(3, "Average_Marks")
     
     for i, (_, student) in enumerate(
          top_3.iterrows(),
          start=1
     ):
          y = 15 + ((i - 1) * 35)

          rank = ctk.CTkLabel(
               minicontent_frame,
               text="",
               font=("Segoe UI", 18),
               image=rank_img1
          )
          rank.place(x=20, y=15)

          rank2 = ctk.CTkLabel(
               minicontent_frame,
               text="",
               font=("Segoe UI", 18),
               image=rank_img2
          )
          rank2.place(x=20, y=52)

          rank3 = ctk.CTkLabel(
               minicontent_frame,
               text="",
               font=("Segoe UI", 18),
               image=rank_img3
          )
          rank3.place(x=20, y=90)
          
          students = ctk.CTkLabel(
               minicontent_frame,
               text=student["Student Name"],
               font=("Segoe UI", 13),
               text_color="#17366d"
          )
          students.place(x=90, y=y)

          marks = ctk.CTkLabel(
               minicontent_frame,
               text=f'{student["Average_Marks"]:.1f}',
               font=("Segoe UI", 13, "bold"),
               text_color="#17366d"
          )
          marks.place(x=230, y=y)
     
# Analytics
sidenav_btn = ctk.CTkButton(
     sidebar_nav,
     width=110,
     height=30,
     text="Analytics",
     text_color="black",
     font=("Segoe UI", 15),
     hover_color="#c1bec1",
     corner_radius=18,
     fg_color="#ffffff",
     bg_color="#7696ff",
     command=open_analytics_window
)
sidenav_btn.place(x=40, y=210)

# ================================================================================

# Prediction Section:-
# ------------------

prediction_window = None

def open_prediction_window():
     
     global prediction_window
     
     if prediction_window is not None and prediction_window.winfo_exists():
          prediction_window.focus()
          prediction_window.lift()
          return
     
     prediction_window = ctk.CTkToplevel(dashboard)
     prediction_window.title("Prediction Section")
     prediction_window.geometry("1200x700")
     prediction_window._state_before_windows_set_titlebar_color = "zoomed"
     prediction_window.configure(fg_color="#eef2f7")
     
     # Header Title Card
     head_title_card = ctk.CTkFrame(
          prediction_window,
          width=1200,
          height=100,
          fg_color="#295dd6",
          border_color="#dfe5eb",
     )
     head_title_card.place(x=40, y=20)
     
     # Trend Image
     trend_image = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\icons8-hand-62.png"),
          size=(55, 55)
     )
          
     trend_image_label = ctk.CTkLabel(
          head_title_card,
          text="",
          image=trend_image
     )
     trend_image_label.place(x=20, y=25)
     
     # Header Title
     header = ctk.CTkLabel(
          head_title_card,
          text="Prediction Analysis",
          text_color="white",
          font=("Segoe UI", 24, "bold"),
          bg_color="#295dd6"
     )
     header.place(x=90, y=25)
     
     # Paragrapg label     
     paragraph_text = ctk.CTkLabel(
          head_title_card,
          text="Predict student performance and identify at-risk students.",
          font=("Segoe UI", 12),
          text_color="white",
          bg_color="#295dd6"
     )     
     paragraph_text.place(x=90, y=57)
     
     # School Image2
     school_img2 = ctk.CTkImage(
          light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\school.png"),
          size=(60, 60)
     )

     # School Label2
     school_label2 = ctk.CTkLabel(
          head_title_card,
          text="",
          image=school_img2
     )
     school_label2.place(x=1100, y=10)

     # Main Student Info Section
     student_info_card = ctk.CTkFrame(
          prediction_window,
          width=1200,
          height=525,
          fg_color="#ecf0f8",
          border_width=1,
          border_color="#dfe5eb",
     )
     student_info_card.place(x=40, y=120)

     card_style = {
          "fg_color": "#f8fafc",
          "border_width": 1,
          "border_color": "#dfe5eb",
          "corner_radius": 16
     }

     # Enter Student Details Card
     enter_details_card = ctk.CTkFrame(
          student_info_card, width=550, height=295, **card_style
     )
     enter_details_card.place(x=10, y=5)

     ctk.CTkLabel(
          enter_details_card, text="Enter Student Details",
          font=("Segoe UI", 16, "bold"), text_color="#17366d"
     ).place(x=20, y=10)
     

     entry_style = {
          "width": 205,
          "height": 32,
          "font": ("Segoe UI", 11),
          "corner_radius": 7,
          "fg_color": "#ffffff",
          "border_width": 1,
          "border_color": "#d8e3f1"
     }
     entry_fields = [
          ("Maths", "Enter marks (0-100)", 20, 40),
          ("Science", "Enter marks (0-100)", 300, 40),
          ("English", "Enter marks (0-100)", 20, 105),
          ("Social Science", "Enter marks (0-100)", 300, 105),
          ("IT", "Enter marks (0-100)", 20, 170),
          ("Attendance Rate", "Enter percentage (0-100)", 300, 170)
     ]
     prediction_entries = {}
     for field_name, placeholder, x_position, y_position in entry_fields:
          ctk.CTkLabel(
               enter_details_card,
               text=field_name,
               font=("Segoe UI", 11, "bold"),
               text_color="#17366d"
          ).place(x=x_position, y=y_position)
          field_entry = ctk.CTkEntry(
               enter_details_card,
               placeholder_text=placeholder,
               **entry_style
          )
          field_entry.place(x=x_position, y=y_position + 30)
          prediction_entries[field_name] = field_entry

     maths_entry = prediction_entries["Maths"]
     science_entry = prediction_entries["Science"]
     english_entry = prediction_entries["English"]
     sst_entry = prediction_entries["Social Science"]
     it_entry = prediction_entries["IT"]
     attendance_entry = prediction_entries["Attendance Rate"]

     # Prediction Result Card
     predicted_results_card = ctk.CTkFrame(
          student_info_card, width=615, height=295, **card_style
     )
     predicted_results_card.place(x=575, y=5)
     
     ctk.CTkLabel(
          predicted_results_card, text="Prediction Result",
          font=("Segoe UI", 16, "bold"), text_color="#17366d"
     ).place(x=20, y=13)
     
     ctk.CTkLabel(
          predicted_results_card,
          text="Based on the entered marks, here is the predicted outcome.",
          font=("Segoe UI", 11), text_color="#617797"
     ).place(x=20, y=37)

     grade_circle = ctk.CTkFrame(
          predicted_results_card, width=110, height=110,
          fg_color="#d7fbef", corner_radius=55
     )
     grade_circle.place(x=24, y=83)
     ctk.CTkLabel(
          grade_circle, text="Expected\nGrade",
          font=("Segoe UI", 11, "bold"), text_color="#17366d",
          justify="center"
     ).place(relx=0.5, y=20, anchor="n")
     grade_value = ctk.CTkLabel(
          grade_circle, text="—", font=("Segoe UI", 29, "bold"),
          text_color="#17366d"
     )
     grade_value.place(relx=0.5, y=52, anchor="n")

     result_metrics = []
     for title, x_position, color in [
          ("Predicted Average", 155, "#17366d"),
          ("Expected Performance", 295, "#19a875"),
          ("Pass Probability", 455, "#3978ff")
     ]:
          ctk.CTkFrame(
               predicted_results_card, width=1, height=62,
               fg_color="#e3eaf3"
          ).place(x=x_position - 12, y=105)
          ctk.CTkLabel(
               predicted_results_card, text=title,
               font=("Segoe UI", 9), text_color="#617797"
          ).place(x=x_position, y=105)
          metric_value = ctk.CTkLabel(
               predicted_results_card, text="—",
               font=("Segoe UI", 17, "bold"), text_color=color
          )
          metric_value.place(x=x_position, y=130)
          result_metrics.append(metric_value)
     average_value, performance_value, pass_value = result_metrics

     insight_card = ctk.CTkFrame(
          predicted_results_card, width=575, height=72,
          fg_color="#edf5ff", corner_radius=10
     )
     insight_card.place(x=20, y=210)
     ctk.CTkLabel(
          insight_card, text="↗", width=28, height=28,
          font=("Segoe UI", 18, "bold"), text_color="#295dd6",
          fg_color="#dbeaff", corner_radius=16
     ).place(x=10, y=12)
     ctk.CTkLabel(
          insight_card, text="Prediction Insight",
          font=("Segoe UI", 14, "bold"), text_color="#17366d"
     ).place(x=58, y=9)
     insight_value = ctk.CTkLabel(
          insight_card, text="Enter student details and select Predict Performance.",
          font=("Segoe UI", 12), text_color="#17366d",
          anchor="w", justify="left", wraplength=490
     )
     insight_value.place(x=58, y=32)

     # Performance Probability Card
     probability_card = ctk.CTkFrame(
          student_info_card, width=370, height=210, **card_style
     )
     probability_card.place(x=10, y=305)
     
     ctk.CTkLabel(
          probability_card, text="Performance Probability",
          font=("Segoe UI", 15, "bold"), text_color="#17366d"
     ).place(x=20, y=10)

     probability_figure = Figure(
          figsize=(3.35, 1.72), dpi=100, facecolor="#f8fafc"
     )
     probability_axes = probability_figure.add_subplot(111)
     probability_categories = [
          "Excellent", "Good", "Average", "Needs\nImprovement"
     ]
     probability_colors = ["#49bd91", "#3978ff", "#ffb52e", "#ff626b"]
     probability_bars = probability_axes.bar(
          range(4), [0, 0, 0, 0], color=probability_colors, width=0.62
     )
     probability_texts = [
          probability_axes.text(
               bar.get_x() + bar.get_width() / 2, 1, "0%",
               ha="center", va="bottom", fontsize=10, color=color,
               fontweight="bold"
          )
          for bar, color in zip(probability_bars, probability_colors)
     ]
     probability_axes.set_ylim(0, 110)
     probability_axes.set_yticks([0, 25, 50, 75, 100])
     probability_axes.set_xticks(range(4), probability_categories)
     probability_axes.tick_params(axis="x", labelsize=9, colors="#38547e")
     probability_axes.tick_params(axis="y", labelsize=9, colors="#617797")
     probability_axes.grid(axis="y", color="#e3eaf3", linewidth=0.8)
     probability_axes.set_axisbelow(True)
     probability_axes.spines[["top", "right", "left"]].set_visible(False)
     probability_axes.spines["bottom"].set_color("#d8e3f1")
     probability_axes.set_facecolor("#f8fafc")
     probability_figure.tight_layout(pad=1.2)
     probability_chart = FigureCanvasTkAgg(
          probability_figure, master=probability_card
     )
     probability_chart.get_tk_widget().place(x=0, y=50, width=510, height=260)

     # Subject-wise Prediction Card
     subject_card = ctk.CTkFrame(
          student_info_card, width=370, height=210, **card_style
     )
     subject_card.place(x=395, y=305)
     
     ctk.CTkLabel(
          subject_card, text="Subject-wise Prediction",
          font=("Segoe UI", 15, "bold"), text_color="#17366d"
     ).place(x=20, y=10)

     subject_bars = {}
     subject_values = {}
     subject_bar_colors = {
          "Maths": "#3978ff",
          "Science": "#49bd91",
          "English": "#9854ef",
          "Social Science": "#ffb52e",
          "IT": "#11b9c4"
     }
     for index, subject in enumerate(Subject_columns):
          y_position = 35 + index * 32
          ctk.CTkLabel(
               subject_card, text=subject,
               font=("Segoe UI", 10), text_color="#17366d"
          ).place(x=17, y=y_position)
          
          subject_bar = ctk.CTkProgressBar(
               subject_card, width=270, height=9,
               progress_color=subject_bar_colors[subject],
               fg_color="#e3ebf4", corner_radius=5
          )
          subject_bar.set(0)
          subject_bar.place(x=17, y=y_position + 22)
          subject_bars[subject] = subject_bar
          subject_value = ctk.CTkLabel(
               subject_card, text="—",
               font=("Segoe UI", 10, "bold"), text_color="#17366d"
          )
          subject_value.place(x=310, y=y_position + 7)
          subject_values[subject] = subject_value

     # Risk Analysis Card
     risk_card = ctk.CTkFrame(
          student_info_card, width=410, height=210, **card_style
     )
     risk_card.place(x=780, y=305)
     
     ctk.CTkLabel(
          risk_card, text="Risk Analysis",
          font=("Segoe UI", 15, "bold"), text_color="#17366d"
     ).place(x=20, y=10)

     risk_figure = Figure(figsize=(1.55, 1.45), dpi=100, facecolor="#f8fafc")
     risk_axes = risk_figure.add_subplot(111)
     risk_axes.pie(
          [1], colors=["#e3ebf4"], startangle=90,
          wedgeprops={"width": 0.24, "edgecolor": "#f8fafc"}
     )
     risk_axes.text(
          0, 0.08, "—", ha="center", va="center",
          fontsize=15, fontweight="bold", color="#17366d"
     )
     risk_axes.text(
          0, -0.2, "At Risk", ha="center", va="center",
          fontsize=8, color="#38547e"
     )
     risk_axes.set_aspect("equal")
     risk_axes.axis("off")
     risk_figure.tight_layout(pad=0)
     risk_chart = FigureCanvasTkAgg(risk_figure, master=risk_card)
     risk_chart.get_tk_widget().place(x=10, y=48, width=185, height=160)

     risk_legend = {}
     for index, (risk_name, color) in enumerate([
          ("Low Risk", "#49bd91"),
          ("Moderate Risk", "#ffb52e"),
          ("High Risk", "#ff626b")
     ]):
          y_position = 40 + index * 28
          ctk.CTkLabel(
               risk_card, text="●", font=("Segoe UI", 13, "bold"),
               text_color=color
          ).place(x=175, y=y_position)
          ctk.CTkLabel(
               risk_card, text=risk_name, font=("Segoe UI", 11),
               text_color="#38547e"
          ).place(x=192, y=y_position)
          risk_value = ctk.CTkLabel(
               risk_card, text="—", font=("Segoe UI", 11, "bold"),
               text_color="#17366d"
          )
          risk_value.place(x=350, y=y_position)
          risk_legend[risk_name] = risk_value

     recommendation_card = ctk.CTkFrame(
          risk_card, width=380, height=65,
          fg_color="#edf5ff", corner_radius=9
     )
     recommendation_card.place(x=14, y=135)
     ctk.CTkLabel(
          recommendation_card, text="♧",
          font=("Segoe UI", 17, "bold"), text_color="#295dd6"
     ).place(x=10, y=8)
     ctk.CTkLabel(
          recommendation_card, text="Recommendation",
          font=("Segoe UI", 12, "bold"), text_color="#17366d"
     ).place(x=38, y=8)
     recommendation_value = ctk.CTkLabel(
          recommendation_card, text="A recommendation will appear after prediction.",
          font=("Segoe UI", 11), text_color="#38547e",
          anchor="w", justify="left", wraplength=325
     )
     recommendation_value.place(x=38, y=28)

     def predict_performance(maths, science, english, social_science, it, attendance):
          try:
               marks = [float(value) for value in (
                    maths, science, english, social_science, it
               )]
               attendance_rate = float(attendance)
               if (
                    any(not math.isfinite(mark) or mark < 0 or mark > 100 for mark in marks)
                    or not math.isfinite(attendance_rate)
                    or attendance_rate < 0
                    or attendance_rate > 100
               ):
                    raise ValueError
          except ValueError:
               messagebox.showerror(
                    "Invalid Input",
                    "Enter marks and attendance as numbers from 0 to 100."
               )
               return

          average = sum(marks) / len(marks)
          pass_probability = max(
               0, min(100, average + (attendance_rate - 75) * 0.33)
          )
          performance_centers = [95, 82.5, 67.5, 45]
          probability_weights = [
               math.exp(-((average - center) / 16) ** 2)
               for center in performance_centers
          ]
          probability_total = sum(probability_weights)
          performance_probabilities = [
               weight / probability_total * 100
               for weight in probability_weights
          ]
          for bar, label, probability in zip(
               probability_bars, probability_texts, performance_probabilities
          ):
               bar.set_height(probability)
               label.set_y(probability + 2)
               label.set_text(f"{probability:.0f}%")
          probability_chart.draw_idle()

          for subject, mark in zip(Subject_columns, marks):
               subject_bars[subject].set(mark / 100)
               subject_values[subject].configure(text=f"{mark:.0f}%")

          high_risk = max(
               5, min(90, (40 - average) * 1.5 + (75 - attendance_rate) * 0.6)
          )
          moderate_risk = max(
               8, min(35, 15 + (70 - average) * 0.35
                      + (80 - attendance_rate) * 0.15)
          )
          if high_risk + moderate_risk > 95:
               moderate_risk = 95 - high_risk
          low_risk = 100 - high_risk - moderate_risk
          risk_axes.clear()
          risk_axes.pie(
               [low_risk, moderate_risk, high_risk],
               colors=["#49bd91", "#ffb52e", "#ff626b"],
               startangle=90,
               counterclock=False,
               wedgeprops={"width": 0.24, "edgecolor": "#f8fafc"}
          )
          risk_axes.text(
               0, 0.08, f"{high_risk:.0f}%", ha="center", va="center",
               fontsize=15, fontweight="bold", color="#17366d"
          )
          risk_axes.text(
               0, -0.2, "At Risk", ha="center", va="center",
               fontsize=8, color="#38547e"
          )
          risk_axes.set_aspect("equal")
          risk_axes.axis("off")
          risk_chart.draw_idle()
          for risk_name, risk_amount in zip(
               ("Low Risk", "Moderate Risk", "High Risk"),
               (low_risk, moderate_risk, high_risk)
          ):
               risk_legend[risk_name].configure(text=f"{risk_amount:.0f}%")

          grade_value.configure(text=get_grade(average))
          average_value.configure(text=f"{average:.1f}%")
          performance_value.configure(text=get_performance(average))
          pass_value.configure(text=f"{pass_probability:.0f}%")

          weakest_subject = min(zip(Subject_columns, marks), key=lambda item: item[1])
          if high_risk >= 35:
               insight = (
                    f"High risk detected. Prioritize support in {weakest_subject[0]}."
               )
               recommendation = (
                    f"Arrange focused support for {weakest_subject[0]} and monitor attendance."
               )
          elif high_risk >= 18:
               insight = (
                    f"Some support may help, especially in {weakest_subject[0]}."
               )
               recommendation = (
                    f"Review progress in {weakest_subject[0]} and monitor attendance regularly."
               )
          else:
               insight = "This student is likely to perform well. Keep up the good work!"
               recommendation = (
                    f"Low risk. Continue regular monitoring; focus on {weakest_subject[0]}."
               )
          insight_value.configure(text=insight)
          recommendation_value.configure(text=recommendation)

     # Predict Performance Button
     predict_button = ctk.CTkButton(
          enter_details_card,
          width=300,
          height=36,
          text="↗   Predict Performance",
          text_color="white",
          font=("Segoe UI", 12, "bold"),
          hover_color="#295dd6",
          corner_radius=8,
          fg_color="#3978ff",
          bg_color="#f8fafc",
          command=lambda: predict_performance(
               maths_entry.get(),
               science_entry.get(),
               english_entry.get(),
               sst_entry.get(),
               it_entry.get(),
               attendance_entry.get()
          )
     )
     predict_button.place(x=110, y=245)


sidenav_btn = ctk.CTkButton(
     sidebar_nav,
     width=110,
     height=30,
     text="Prediction",
     text_color="black",
     font=("Segoe UI", 15),
     hover_color="#c1bec1",
     corner_radius=18,
     fg_color="#ffffff",
     bg_color="#7696ff",
     command=open_prediction_window
     
).place(x=40, y=270)

# ================================================================================

# Logout Function
def logout():
     dashboard.destroy()
     
     
# Logout
sidenav_btn = ctk.CTkButton(
     sidebar_nav,
     width=110,
     height=30,
     text="↗ Logout",
     text_color="black",
     font=("Segoe UI", 16),
     hover_color="#fc7690",
     corner_radius=18,
     fg_color="#ffffff",
     bg_color="#7696ff",
     command=logout
     
).place(x=40, y=580)

# ================================================================================

# Summary Card   
summary_card = ctk.CTkFrame(
     dashboard,
     width=200,
     height=70,
     fg_color="#f2f7fe",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)   
summary_card.place(x=420, y=78)

# Student Image
stu_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\graduated.png"),
     size=(32, 32)
)

# Circle Frame
avatar_frame = ctk.CTkFrame(
     summary_card,
     width=42,
     height=42,
     fg_color="#d3e6fe",
     corner_radius=60,
     border_width=0, 
)
avatar_frame.place(x=22, y=14)

# Student Image Label
stu_img_label = ctk.CTkLabel(
     avatar_frame,
     text="",
     font=("Segoe UI", 39),
     image=stu_img
).place(relx=0.5, rely=0.5, anchor="center")

# Total Students Title
total_stu = ctk.CTkLabel(
     summary_card,
     text="Total Students",
     font=("Segoe UI", 12, "bold"),
     text_color="#4b5563"
).place(x=90, y=5)

# Total Students Number
number_stu = ctk.CTkLabel(
     summary_card,
     text=str(len(df)),
     font=("Segoe UI", 16, "bold"),
     text_color="#1f2937"
)
number_stu.place(x=90, y=25)

# ================================================================================

# Average Marks Card
averagemark_card = ctk.CTkFrame(
     dashboard,
     width=200,
     height=70,
     fg_color="#ebfbee",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
averagemark_card.place(x=630, y=78)   

# Trend Image
trend_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\trend.png"),
     size=(35, 35)
)

# Trend Image Label
trend_label = ctk.CTkLabel(
     averagemark_card,
     text="",
     font=("Segoe UI", 39),
     image=trend_img
).place(x=20, y=15)     

# Average Marks Title
average_marks = ctk.CTkLabel(
     averagemark_card,
     text="Average Marks",
     font=("Segoe UI", 12, "bold"),
     text_color="#4b5563"
).place(x=90, y=5)

# Average Marks
average_marks_value = ctk.CTkLabel(
     averagemark_card,
     text="",
     font=("Segoe UI", 16, "bold"),
     text_color="#1f2937"
)
average_marks_value.place(x=90, y=25)

# ================================================================================

# Pass Percentage Card
pass_percentage_card = ctk.CTkFrame(
     dashboard,
     width=200,
     height=70,
     fg_color="#e1e5fc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
pass_percentage_card.place(x=840, y=78)   

# Pass Percentage Image
pass_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\graduation-cap.png"),
     size=(35, 35)
)

# Pass Percentage Image Label
pass_label = ctk.CTkLabel(
     pass_percentage_card,
     text="",
     font=("Segoe UI", 39),
     image=pass_img
).place(x=20, y=15)

# Pass Percentage Title
pass_percentage = ctk.CTkLabel(
     pass_percentage_card,
     text="Pass Percentage",
     font=("Segoe UI", 12, "bold"),
     text_color="#4b5563"
).place(x=90, y=5)

# Pass Percentage Value
pass_percentage_value = ctk.CTkLabel(
     pass_percentage_card,
     text="",
     font=("Segoe UI", 16, "bold"),
     text_color="#1f2937"
)
pass_percentage_value.place(x=90, y=25)

# ================================================================================

# Top Performer Card
top_performer = ctk.CTkFrame(
     dashboard,
     width=210,
     height=70,
     fg_color="#fcfdeb",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
top_performer.place(x=1050, y=78)   

# Top Performer Image
top_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\star.png"),
     size=(35, 35)
)

# Top Performer Image Label
top_label = ctk.CTkLabel(
     top_performer,
     text="",
     font=("Segoe UI", 39),
     image=top_img
)
top_label.place(x=20, y=15)

# Top Performer Title
top_performer_title = ctk.CTkLabel(
     top_performer,
     text="Top Performer",
     font=("Segoe UI", 12, "bold"),
     text_color="#4b5563"
).place(x=80, y=5)

# Top Performer Name
top_performer_name = ctk.CTkLabel(
     top_performer,
     text="",
     font=("Segoe UI", 12, "bold"),
     text_color="#1f2937"
)
top_performer_name.place(x=80, y=25)

# ================================================================================

# Function to handle student row click event
def student_clicked(data):
    print("CLICK DATA:", data)
    row_number = data["row"]

    # Ignore header row
    if row_number == 0:
        return
    print("Selected row:", row_number)

    # Get student data from DataFrame
    student = df.iloc[row_number - 1]

    print("Selected student:")
    print(student)

    # Update entire dashboard
    update_student_dashboard(student)    
    
# Table
table_card = ctk.CTkFrame(
     dashboard,
     width=840,
     height=245,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18,
)
table_card.place(x=420, y=155)

# Create table data  from CSV
table_data = [["Student ID",
               "Student Name",
               "Class",
               "Attendance Rate",
               "Days Absent",
               "Maths",
               "Science",
               "English",
               "Social Science",
               "IT",
               "Term1",
               "Term2",
               "Term3",
               "Term4",               
               "Grade",
               "Performance"]]

for _, student in df.iterrows():
    table_data.append([
          student["Student ID"],
          student["Student Name"],
          student["Class"],
          f"{student['Attendance Rate']}",
          student["Days Absent"],
          student["Maths"],
          student["Science"],
          student["English"],
          student["Social Science"],
          student["IT"],
          student["Term1"],
          student["Term2"],
          student["Term3"],
          student["Term4"],        
          student["Grade"],
          student["Performance"]
    ])
    
# Scrollable table container for smooth vertical and horizontal scrolling
canvas = ctk.CTkCanvas(
    table_card,
    bg="#f8fafc",
    highlightthickness=0,
    width=1235,
    height=345,
)
canvas.place(x=12, y=12)

x_scrollbar = ctk.CTkScrollbar(
    table_card,
    orientation="horizontal",
    command=canvas.xview,
    width=12,
    height=12,
    button_color="#f8fafc",
    button_hover_color="#f8fafc",
)
x_scrollbar.place(x=12, y=248)

y_scrollbar = ctk.CTkScrollbar(
    table_card,
    orientation="vertical",
    command=canvas.yview,
    width=12,
    height=236,
    button_color="#f8fafc",
    button_hover_color="#f8fafc",
)
y_scrollbar.place(x=888, y=12)

canvas.configure(
     xscrollcommand=x_scrollbar.set, 
     yscrollcommand=y_scrollbar.set
)

scrollable_table = ctk.CTkFrame(
     canvas, 
     fg_color="#ffffff"
)
canvas_window = canvas.create_window((0, 0), window=scrollable_table, anchor="nw")

table = CTkTable(
    master=scrollable_table,
    row=len(table_data),
    column=len(table_data[0]),
    values=table_data,
    command=student_clicked,
    font=("Segoe UI", 12, "bold"),
    header_color="#dbeafe",
    hover_color="#bbd8fd",
    text_color="#1f2430",
    bg_color="#f8fafc",
    colors=["#f9fafb", "#ffffff"],
    width=95,
    height=20,
)
table.pack(fill="both", expand=True)

def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(canvas_window, width=max(canvas.winfo_width(), table.winfo_reqwidth() + 30))
    canvas.itemconfig(canvas_window, height=max(canvas.winfo_height(), table.winfo_reqheight() + 30))

scrollable_table.bind("<Configure>", update_scroll_region)
table.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", update_scroll_region)

def smooth_scroll(event):
    if event.state & 0x1:  # Shift key pressed for horizontal scroll
        canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
    else:
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", smooth_scroll)

# Keep the table fully visible and scrollable when content changes
update_scroll_region()

# ================================================================================

# Student Information Status Cards
stu_info_card = ctk.CTkFrame(
     dashboard,
     width=220,
     height=380,
     fg_color="#E6D0FA",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
stu_info_card.place(x=190, y=15)

# Student Male Image
student_male_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\man.png"),
     size=(45, 45)
)

# Student Female Image
student_female_img = ctk.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Nielit_A_Level_Project_Major\images\woman.png"),
     size=(45, 45)
)

# Student Status Circle Frame
stu_circle_frame = ctk.CTkFrame(
     stu_info_card,
     width=70,
     height=70,
     fg_color="#dbeafe",
     corner_radius=60,
     border_width=0
)
stu_circle_frame.place(x=75, y=14)

# Student Male Image Label
stu_img_label = ctk.CTkLabel(
     stu_circle_frame,
     text="",
     font=("Segoe UI", 39),
     image=student_male_img,
)
stu_img_label.place(relx=0.5, rely=0.5, anchor="center")


# Student Name
stu_name = ctk.CTkLabel(
     stu_info_card,
     text="",
     font=("Segoe UI", 12, "bold"),
     text_color="#0f55f6"
)
stu_name.place(x=75, y=85)

# Student Class
stu_class = ctk.CTkLabel(
     stu_info_card,
     text="",
     font=("Segoe UI", 12, "bold"),
     text_color="#4b5563"
)
stu_class.place(x=82, y=110)

# Student Details Card
details_card = ctk.CTkFrame(
     stu_info_card,
     width=200,
     height=230,
     fg_color="#F1EFFC",
     corner_radius=18
)    
details_card.place(x=10, y=140)

# Student ID details
stu_id = ctk.CTkLabel(
     details_card,
     text="Student ID: ",
     font=("Segoe UI", 13),
     text_color="#1f2430"
     
)
stu_id.place(x=20, y=10)

# Line 
line_frame = ctk.CTkFrame(
     details_card,
     width=160,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)      
line_frame.place(x=20, y=45) 

# Gender
gender = ctk.CTkLabel(
     details_card,
     text="Gender: ",
     font=("Segoe UI", 13),
     text_color="#1f2430"
)
gender.place(x=20, y=50)

# Line 
line_frame = ctk.CTkFrame(
     details_card,
     width=160,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)      
line_frame.place(x=20, y=85) 

# Age
age = ctk.CTkLabel(
     details_card,
     text="Age: ",
     font=("Segoe UI", 13),
     text_color="#1f2430"
)
age.place(x=20, y=92)

# Line
line_frame = ctk.CTkFrame(
     details_card,
     width=160,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)
line_frame.place(x=20, y=128)

# Attendance Rate
attendance_rate = ctk.CTkLabel(
     details_card,
     text="Attendance Rate: ",
     font=("Segoe UI", 13),
     text_color="#1f2430"
)
attendance_rate.place(x=20, y=135)

# Line
line_frame = ctk.CTkFrame(
     details_card,
     width=160,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)
line_frame.place(x=20, y=170)

# Days Absent
days_absent = ctk.CTkLabel(
     details_card,
     text="Days Absent: ",
     font=("Segoe UI", 13),
     text_color="#1f2430"     
)
days_absent.place(x=20, y=180)

# ================================================================================

# Graphical Analysis Cards:-
# ------------------------
# Subject Wise Marks Card
subjectwise_card = ctk.CTkFrame(
     dashboard,
     width=350,
     height=220,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
subjectwise_card.place(x=190, y=410)

# Subject Wise Marks Title
subjectwise_title = ctk.CTkLabel(
    subjectwise_card,
    text="Subject Wise Marks",
    font=("Segoe UI", 18, "bold"),
    text_color="#1f2430"
)
subjectwise_title.place(x=18, y=8)

# Subject Wise Marks Bar Chart
subject_names = ["Maths", "Science", "English", "Social\nScience", "IT"]
subject_marks = [85, 88, 82, 76, 90]
subject_colors = ["#4f9ef5", "#f4a261", "#8b5cf6", "#f87171", "#fbbf24"]

subject_fig = Figure(figsize=(4.7, 2.4), dpi=100, facecolor="#f8fafc")
subject_ax = subject_fig.add_subplot(111)
subject_ax.set_facecolor("#f8fafc")
subject_ax.grid(axis='y', color="#e5e7eb", linestyle='-', linewidth=1)
subject_ax.set_axisbelow(True)
bars = subject_ax.bar(subject_names, subject_marks, color=subject_colors, width=0.7)
subject_ax.set_ylim(0, 100)
subject_ax.set_yticks([0, 20, 40, 60, 80, 100])
subject_ax.set_yticklabels(["0", "20", "40", "60", "80", "100"], fontsize=9, color="#6b7280")
subject_ax.set_xticklabels(subject_names, fontsize=9, color="#374151")
subject_ax.spines["top"].set_visible(False)
subject_ax.spines["right"].set_visible(False)
subject_ax.spines["left"].set_color("#d1d5db")
subject_ax.spines["bottom"].set_color("#d1d5db")
subject_fig.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.22)

subject_canvas = FigureCanvasTkAgg(subject_fig, master=subjectwise_card)
subject_canvas.draw()
subject_canvas.get_tk_widget().place(x=10, y=60, width=450, height=250)

# ================================================================================

# Performance Trend Card
performance_trend_card = ctk.CTkFrame(
     dashboard,
     width=350,
     height=220,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)
performance_trend_card.place(x=550, y=410)

performance_title = ctk.CTkLabel(
    performance_trend_card,
    text="Performance Trend (Term Wise)",
    font=("Segoe UI", 18, "bold"),
    text_color="#1f2430"
)
performance_title.place(x=18, y=8)

# Performance Trend Line Chart
trend_terms = ["Term 1", "Term 2", "Term 3", "Term 4"]
trend_scores = [68, 72, 78, 88]

trend_fig = Figure(figsize=(4.7, 2.4), dpi=100, facecolor="#f8fafc")
trend_ax = trend_fig.add_subplot(111)
trend_ax.set_facecolor("#f8fafc")
trend_ax.plot(trend_terms, trend_scores, color="#4f9ef5", linewidth=2.5, marker='o', markersize=5)
trend_ax.set_ylim(0, 100)
trend_ax.set_yticks([0, 20, 40, 60, 80, 100])
trend_ax.set_yticklabels(["0", "20", "40", "60", "80", "100"], fontsize=9, color="#6b7280")
trend_ax.set_xticklabels(trend_terms, fontsize=9, color="#374151")
trend_ax.grid(axis='y', color="#e5e7eb", linestyle='-', linewidth=1)
trend_ax.set_axisbelow(True)
trend_ax.spines["top"].set_visible(False)
trend_ax.spines["right"].set_visible(False)
trend_ax.spines["left"].set_color("#d1d5db")
trend_ax.spines["bottom"].set_color("#d1d5db")
trend_fig.subplots_adjust(left=0.12, right=0.98, top=0.88, bottom=0.22)

trend_canvas = FigureCanvasTkAgg(trend_fig, master=performance_trend_card)
trend_canvas.draw()
trend_canvas.get_tk_widget().place(x=10, y=50, width=450, height=250)

# ================================================================================

# Attendance Overview Card
attendance_overview_card = ctk.CTkFrame(
     dashboard,
     width=350,
     height=220,
     fg_color="#f8fafc",
     border_width=1,
     border_color="#dfe5eb",
     corner_radius=18
)    
attendance_overview_card.place(x=910, y=410)

attendance_title = ctk.CTkLabel(
    attendance_overview_card,
    text="Attendance Overview",
    font=("Segoe UI", 18, "bold"),
    text_color="#1f2430"
)
attendance_title.place(x=18, y=8)

# Attendance Overview Pie Chart
attendance_fig = Figure(figsize=(4.5, 2.5), dpi=100, facecolor="#f8fafc")
attendance_ax = attendance_fig.add_subplot(111)
attendance_ax.set_facecolor("#f8fafc")
attendance_ax.set_aspect('equal')
attendance_wedges, _ = attendance_ax.pie(
    [92.5, 7.5],
    startangle=90,
    colors=['#28b463', '#f06565'],
    wedgeprops={'width': 0.55, 'edgecolor': '#f8fafc'}
)
centre_circle = plt.Circle((0, 0), 0.45, fc='#f8fafc')
attendance_ax.add_artist(centre_circle)
attendance_ax.text(0, 0, '92.5%', ha='center', va='center', fontsize=14, fontweight='bold', color='#1f2430')
#attendance_ax.text(0, 0, '7.5%', ha='center', va='right', fontsize=14, fontweight='bold', color='#1f2430')
attendance_ax.axis('off')

legend_handles = [
    Patch(facecolor='#28b463', edgecolor='none', label='Present (92.5%)'),
    Patch(facecolor='#f06565', edgecolor='none', label='Absent (7.5%)')
]
attendance_ax.legend(
    handles=legend_handles,
    loc='center left',
    bbox_to_anchor=(1.0, 0.5),
    frameon=False,
    fontsize=10,
    labelcolor='#374151'
)
attendance_fig.subplots_adjust(left=0.03, right=0.8, top=0.92, bottom=0.08)
attendance_canvas = FigureCanvasTkAgg(attendance_fig, master=attendance_overview_card)
attendance_canvas.draw_idle()
attendance_canvas.get_tk_widget().place(x=10, y=60, width=450, height=250)

# ================================================================================

# Click Data Function:-
# -------------------
def update_student_dashboard(row):

     # Update Student Photo
     selected_gender = str(row["Gender"]).strip().lower()

     if selected_gender == "female":
          stu_img_label.configure(
          image=student_female_img
     )
     else:
          stu_img_label.configure(
          image=student_male_img
     )

     # Update Student Profile
     stu_name.configure(
          text=row["Student Name"]
     )
     stu_class.configure(
          text=f'Class: {row["Class"]}'
     )
     stu_id.configure(
          text=f'Student ID: {row["Student ID"]}'
     )
     gender.configure(
          text=f'Gender: {row["Gender"]}'
     )
     age.configure(
          text=f'Age: {row["Age"]}'
     )
     attendance_rate.configure(
          text=f'Attendance Rate: {row["Attendance Rate"]}'
     )
     days_absent.configure(
          text=f'Days Absent: {row["Days Absent"]}'
     )
    
     # Update Average Marks
     average_marks_value.configure(
          text=f'{row["Average_Marks"]:.2f}%'
     )

     # Update Pass Percentage
     pass_percentage_value.configure(
          text=f'{row["Pass_Percentage"]:.0f}%'
     )

     # Update Top Performer 
     top_student = df.loc[
          df["Average_Marks"].idxmax()
     ]

     top_performer_name.configure(
          text=top_student["Student Name"]
     )
     
     # Update Subject Bar Chart
     subject_ax.clear()

     subject_names = [
          "Maths",
          "Science",
          "English",
          "Social\nScience",
          "IT"
     ]

     subject_marks = [
          row["Maths"],
          row["Science"],
          row["English"],
          row["Social Science"],
          row["IT"]
     ]
    
     subject_ax.set_facecolor("#f8fafc")

     subject_ax.grid(
          axis="y",
          color="#e5e7eb",
          linestyle="-",
          linewidth=1
     )
     subject_ax.set_axisbelow(True)

     bars =subject_ax.bar(
          subject_names,
          subject_marks,
          color=subject_colors,
          width=0.7
     )

     for bar, mark in zip(bars, subject_marks):
          subject_ax.text(
          bar.get_x() + bar.get_width() / 2,
          bar.get_height() + 2,
          f"{mark:.0f}",
          ha="center",
          va="bottom"
     )

     # Chart settings
     subject_ax.set_ylim(0, 110)
     subject_canvas.draw_idle()
    
     # Update Performance Trend Line Chart
     trend_ax.clear()

     trend_terms = [
          "Term 1",
          "Term 2",
          "Term 3",
          "Term 4"
     ]
     trend_scores = [
          row["Term1"],
          row["Term2"],
          row["Term3"],
          row["Term4"]
     ]
    
     trend_ax.set_facecolor("#f8fafc")

     trend_ax.plot(
          trend_terms,
          trend_scores,
          color="#4f9ef5",
          linewidth=2.5,
          marker="o",
          markersize=5
     )
    
     for trend_terms, trend_scores in zip(trend_terms, trend_scores):
          trend_ax.annotate(
          f"{trend_scores:.0f}",
          xy=(trend_terms, trend_scores),
          xytext=(0, 10),
          textcoords="offset points",
          ha="center",
          va="bottom",
     )

     trend_ax.set_ylim(0, 100)
     trend_ax.set_yticks(
          [0, 20, 40, 60, 80, 100]
     )
     trend_ax.grid(
          axis="y",
          color="#e5e7eb"
     )
     trend_ax.set_axisbelow(True)
     trend_ax.spines["top"].set_visible(False)
     trend_ax.spines["right"].set_visible(False)

     trend_canvas.draw_idle()
    
     # Update Attendance Pie Chart
     attendance = float(
          str(row["Attendance Rate"]).replace("%", "")
     )
     absent = 100 - attendance
     attendance_ax.clear()
     values = [attendance, absent]

     labels = [
          f"Present ({attendance:.1f}%)",
          f"Absent ({absent:.1f}%)"
     ]
    
     wedges, texts = attendance_ax.pie(
          values,
          startangle=90,
          colors=['#28b463', '#f06565'],
          wedgeprops={
               "width": 0.55,
               "edgecolor": "white"
          }
     )
     attendance_ax.text(
          0,
          0,
          f"{attendance:.1f}%",
          ha="center",
          va="center",
          fontsize=13,
          fontweight="bold"
     )
     attendance_ax.legend(
          wedges,
          labels,
          loc="center left",
          bbox_to_anchor=(1, 0.5),
          frameon=False
     )
     attendance_ax.set_aspect("equal")
     attendance_canvas.draw()
    
dashboard.mainloop()
