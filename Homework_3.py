# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
# Create a Student class that has the following attributes:

# name
# last name
# age
# master (either MCSBT or MDBI)
# Make sure you parametrize all those fields in the constructor.

class Student: 
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
    
    def what_master(self): 
        if self.master == "MCSBT":
            print ("enrolled in MCBT")
        if self.master == "MDBI":
            print ("enrolled in MDBI")
        else:
            return False
    
agata = Student("Agata", "Kaczmarek", "31","MDBI")  



#%%

# Add a print_student method in the Student class that prints a line 
# like follows for the object

# Pepe García is a 55 year old student of the MCSDBI masters programme

# Create a list of all 28 Students representing all students in this class.  
# Then iterate over all of them and call print_student on each one to print 
# its description.

class Student1: 
    def __init__(self, name, last_name, age, master):
            self.name = name
            self.last_name = last_name
            self.age = age
            self.master = master 
        
    
    def print_student(self):
       for students in list_of_students:
        print(str(self.name) + "is a" + str(self.age) + "year old student of the" 
                 + str(self.master) + "masters programme")
                 
class IE: 

    students = []     
                        
    def _init_(self, name):
            self.name = name

    def add_members_list(self, list_of_students):
        self.students += list_of_students       
    
list_of_students = [Student1("Alejandro", "Meneses", "27", "MCBT"), 
                    Student1("Agata", "Kaczmarek", "31","MDBI"), 
           Student1("Anastasia", "Lasunina", "25", "MDBI"), 
           Student1("Candela", "Noya", "24", "MDBI"), 
           Student1("Daniil", "Osipov", "21", "MDBI"), 
           Student1("David", "Barrero Gonzalez", "31", "MCSBT"), 
           Student1("Edem", "Francois", "28", "MCSBT"),
           Student1("Eduardo", "Paraja", "23", "MDBI"),
                     Student1("Florian", "Diegruber", "25", "MCSBT"),
                     Student1("Hannah", "Oldorf", "23", "MCBT"),
                     Student1("Isabella", "Rosenthal", "27", "MDBI"),
                     Student1("Javier", "Fernandez", "24", "MCSBT"),
                     Student1("Lukas", "Hauser", "28","MDBI"),
                     Student1("Leila", "Tazi", "27", "MCSBT"),
                     Student1("Laura", "Kageneck", "23", "MCSBT"),
                     Student1("Monica", "Alvarenga","28", "MDBI"),
                     Student1("Natalie", "Cedeno", "26", "MDBI"),
                     Student1("Octavio", "Ramírez", "28", "MDBI"),
                     Student1("Tancredi", "Bernard", "21", "MCSBT"),
                     Student1("Yasmine", "Lyagoubi", "23", "MDBI"),
                     Student1("Arthur", "Maroquene-Froissart", "23", "MCSBT")]
    
    







