# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:30:17 2018

@author: user
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mydb = client.db_University
def add_Student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    unique_student = mydb.forsk_clients.find_one({"Student_Roll_no":Student_Roll_no})
    if unique_student:
        return "Client already exists"
    else:
        mydb.forsk_clients.insert(
                {
                "Student_Name" : Student_Name,
                "Student_Age" : Student_Age,
                "Student_Roll_no" : Student_Roll_no,
                "Student_Branch" : Student_Branch,
                
                })
        return "Client added successfully"

def view_student(Student_Roll_no):
    user = mydb.forsk_clients.find_one({"Student_Roll_no":Student_Roll_no})
    if user:
        student = user["Student_Name"]
        age = user["Student_Age"]
        roll_no = user["Student_Roll_no"]
        branch = user["Student_Branch"]
       
        return {"Student_Name":student,"Student_Age":age,"Student_Roll_no":roll_no,"Student_Branch":branch}
    else:
        return "Sorry, No such user exists"


student = raw_input("Enter Student name: ")
age = raw_input("Enter age : ")
roll_no = raw_input("Enter roll no: ")
branch = raw_input("Enter branch: ")

print add_Student(student,age,roll_no,branch)

user = raw_input("enter student roll_no to find")


print view_student(user)
