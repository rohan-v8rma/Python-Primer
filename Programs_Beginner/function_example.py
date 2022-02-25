#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:49:23 2019

@author: Shreya_Verma
"""
# =============================================================================
# This is the function definition
def calculate_grade(marks):
    if (-1 < marks < 51):
        return "E"
    if (50 < marks < 61):
        return "D"
    if (60 < marks < 71):
        return "C"	
    if (70 < marks < 81):
        return "B"
    if (80 < marks < 91):    
        return "A"
    if (90 < marks < 101):
        return "A+"
    return None
# =============================================================================    

"""
A return statement returns the value and comes out of the function immediately.

If marks are in 80-91 range:
    1. if condition in lines 10, 12, 14, 16, 18 will be checked
    2. Once the line 18 condition is found to be true, "A" will be returned
    3. Line 20 onwards will not be executed. That is why we don't need elif.
    Elif makes sure that if one condition is true, other conditions are not checked
"""
    

english_marks = int (input("English marks? "))
hindi_marks = int (input("Hindi marks? "))

#Now I can reuse the logic to calculate grade for two subjects
english_grade = calculate_grade(english_marks) #This is the function call
hindi_grade = calculate_grade(hindi_marks)

"""
calculate_grade function does not return any value if marks don't satisfy 
any of the conditions so if grade is None then input was invalid
"""

if english_grade is None:
    print("Invalid input for English marks")
else:
    print("English grade:", english_grade)

if hindi_grade is None:
    print("Invalid input for Hindi marks")
else:
    print("Hindi grade:", hindi_grade)

"""
Also, we should give proper names to variables and functions
So instead of 'g' we should use 'grade'
It makes our code readable
"""